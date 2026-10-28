#!/usr/bin/env python3
"""Generate and validate the compact benchmark report using saved results only."""
import argparse
import csv
import gzip
import hashlib
import html
import json
import math
import os
import re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

NAMES = ['Ornith 6-bit', 'Ornith Vision 4-bit', 'Ruka Ornith oQ6', 'Qwen3.6 UD',
         'Qwen3.6 nvfp4', 'Qwen3.8 stock', 'Qwen3.8 Youssofal', 'Qwen3.8 Jundot', 'Muse Glimmer', 'Gemma 4']
QUESTIONS = ['Largest files', 'Exact duplicates', 'HA basement guards', 'Frigate configuration',
             'Drive storage', 'Calendar conflicts', 'Backup optimization', 'Camera cross-check',
             'Frigate log analysis', 'Meeting availability']


def load(root, name):
    path = root / name
    return json.loads(gzip.decompress(path.read_bytes()) if path.suffix == '.gz' else path.read_text())


def raw_rows(root, name):
    return [json.loads(line) for line in gzip.decompress((root / name).read_bytes()).splitlines() if line.strip()]


def trials(root):
    result = [raw_rows(root, 'data/daily/original6.jsonl.gz') + raw_rows(root, 'data/daily/added4.jsonl.gz'),
              raw_rows(root, 'data/daily/repeat10.jsonl.gz')]
    if (root / 'data/daily/third10.jsonl.gz').exists():
        result.append(raw_rows(root, 'data/daily/third10.jsonl.gz'))
    return result


def duration(seconds):
    minutes, seconds = divmod(round(seconds), 60)
    return f'{minutes}:{seconds:02d}'


def slug(value):
    return re.sub('[^a-z0-9]+', '-', value.lower()).strip('-')


def correct(row):
    return 2 if row['verified'] else int(any(c['passed'] for c in row['checks'] if c['name'].startswith(('correct ', 'complete '))))


def state(row):
    return 'PASS' if row['passed'] else 'VERIFIED; completion failed' if row['verified'] else 'FAIL'


def esc(value):
    return html.escape(str(value)).replace('|', '&#124;').replace('\n', '<br>')


def stats(rows):
    total = sum(r['e2e_s'] for r in rows)
    inp, out = sum(r['input_eval_s'] for r in rows), sum(r['output_eval_s'] for r in rows)
    return dict(score=sum(r['passed'] for r in rows), verified=sum(r['verified'] for r in rows),
                total_e2e_s=total, mean_e2e_s=total / len(rows),
                input_tokens=sum(r['computed_input_tokens'] for r in rows), input_eval_s=inp,
                output_tokens=sum(r['output_tokens'] for r in rows), output_eval_s=out,
                input_tok_s=sum(r['computed_input_tokens'] for r in rows) / inp,
                output_tok_s=sum(r['output_tokens'] for r in rows) / out)


def csv_file(path, rows):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def link(label, href):
    return f'<a href="{html.escape(href, quote=True)}">{html.escape(str(label))}</a>'


def table(rows, numeric=False):
    # GitHub preserves nowrap and provides horizontal overflow for wide tables.
    lines = ['<table>', '<thead>', '<tr>']
    lines += [f'<th nowrap scope="col">{cell}</th>' for cell in rows[0]]
    lines += ['</tr>', '</thead>', '<tbody>']
    for row in rows[1:]:
        lines.append('<tr>')
        for i, cell in enumerate(row):
            align = ' align="right"' if numeric and i else ''
            lines.append(f'<td nowrap{align}>{cell}</td>')
        lines.append('</tr>')
    return lines + ['</tbody>', '</table>']


def render(root):
    manifest = load(root, 'metadata/model-task-manifest.json.gz')
    tasks = manifest['tasks']
    datasets = trials(root)
    trial_count = len(datasets)
    mappings = [{(r['model'], r['task']): r for r in rows} for rows in datasets]
    notes = load(root, 'metadata/case-notes.json.gz')
    if (root / 'metadata/trial-3-case-notes.json.gz').exists():
        notes.update(load(root, 'metadata/trial-3-case-notes.json.gz'))
    old_notes = load(root, 'metadata/original-failure-notes.json.gz')
    labels = dict(zip((m['id'] for m in manifest['models']), NAMES))
    scores = {m['id']: [sum(r['passed'] for r in rows if r['model'] == m['id']) for rows in datasets] for m in manifest['models']}
    models = sorted(manifest['models'], key=lambda m: (-sum(scores[m['id']]), -scores[m['id']][-1]))
    summary, all_cases = [], []
    overall = [['Model', f'Combined<br>score /{10 * trial_count}', f'All {trial_count} trials<br>total E2E (m:ss)'] + [f'Trial #{trial}<br>{label}' for trial in range(1, trial_count + 1) for label in ('score /10', 'total E2E (m:ss)', 'input tok/s', 'output tok/s')]]
    matrix = [['Model'] + [link(f'Q{i:02d}', f'docs/questions.md#q{i:02d}') for i in range(1, 11)]]
    for model in models:
        mid, name = model['id'], labels[model['id']]
        path = f'cases/{slug(mid)}.md'
        records = [[mapping[mid, t['id']] for t in tasks] for mapping in mappings]
        summaries = [stats(rows) for rows in records]
        combined = sum(s['score'] for s in summaries)
        combined_time = sum(s['total_e2e_s'] for s in summaries)
        summary.append({'model': mid, 'display_name': name, 'combined_score': combined, 'combined_total_e2e_s': combined_time, **{f'trial_{i}_{k}': v for i, s in enumerate(summaries, 1) for k, v in s.items()}})
        row_cells = [link(name, path), f'{combined}/{10 * trial_count}', duration(combined_time)]
        for trial, s in enumerate(summaries, 1):
            row_cells += [link(f'{s["score"]}/10', f'{path}#trial-{trial}-failures'), duration(s['total_e2e_s']), f'{s["input_tok_s"]:.2f}', f'{s["output_tok_s"]:.2f}']
        overall.append(row_cells)
        page = [f'# {name}', '', f'Exact model ID: `{mid}`.', '', '[Summary and matrix](../README.md) · [Scoring](../docs/methodology.md#scoring)', '']
        hub = model.get('display_name', '')
        if '/' in hub and not hub.startswith('/'):
            page += [f'[Recorded Hugging Face model](https://huggingface.co/{quote(hub, safe="/._-")})', '']
        for trial, mapping in enumerate(mappings, 1):
            page += [f'## Trial {trial} failures', '']
            failures = [(i, mapping[mid, t['id']]) for i, t in enumerate(tasks, 1) if not mapping[mid, t['id']]['passed']]
            page += [f'- [Q{i:02d}: {QUESTIONS[i - 1]}](#q{i:02d}-trial-{trial}) — {state(r)}; {correct(r)}/2; {r["e2e_s"]:.2f}s.' for i, r in failures] or ['All ten questions passed.']
            page += ['']
        matrix_cells = [link(name, path)]
        for i, task in enumerate(tasks, 1):
            parts = []
            for trial, mapping in enumerate(mappings, 1):
                r = mapping[mid, task['id']]
                tag = f'q{i:02d}-trial-{trial}'
                mark = ' ⚠' if r['verified'] and not r['passed'] else ''
                parts.append(f'T{trial}: ' + link(f'{correct(r)}/2{mark} · {r["e2e_s"]:.2f}s', f'{path}#{tag}'))
                fullfile = 'third10' if trial == 3 else 'repeat10' if trial == 2 else 'original6' if i <= 6 else 'added4'
                stage = 'third' if trial == 3 else 'repeat' if trial == 2 else 'added' if i > 6 else 'original6'
                reason = notes.get(f'{stage}/{mid}/{task["id"]}') if stage != 'original6' else old_notes.get(mid + '/' + task['id'])
                if not reason:
                    reason = ('All verification checks passed.' if r['verified'] else
                              'No valid answer.json was delivered; missing value checks indicate undelivered work, not independent factual errors.' if not any(c['name'] == 'answer.json is an object' and c['passed'] for c in r['checks']) else
                              'The submission failed the checks listed below.')
                page += [f'<a id="{tag}"></a>', f'## Q{i:02d} · Trial {trial}: {QUESTIONS[i - 1]}', '',
                         f'**{state(r)}** · correctness **{correct(r)}/2** · E2E **{r["e2e_s"]:.2f}s** · checks **{r["checks_passed"]}/{r["checks_total"]}**.', '',
                         f'Input {r["input_tps"]:.2f} tok/s · output {r["output_tps"]:.2f} tok/s · {r["model_requests"]} model requests.', '', str(reason), '']
                if r['error']:
                    page += ['Completion error:', '', '```text', r['error'], '```', '']
                failed = [c for c in r['checks'] if not c['passed']]
                if failed:
                    page += ['Failed checks:', ''] + ['- ' + c['name'] for c in failed] + ['']
                page += [f'[Exact prompt](../docs/questions.md#q{i:02d}) · [Full scored records: {fullfile}.jsonl.gz](../data/daily/{fullfile}.jsonl.gz?raw=1)', '',
                         f'In that JSONL file, select `model == "{mid}"` and `task == "{task["id"]}"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).', '']
                all_cases.append(dict(model=mid,question=f'Q{i:02d}',task=task['id'],trial=trial,correctness_out_of_2=correct(r),verified=r['verified'],full_pass=r['passed'],
                                      e2e_s=r['e2e_s'],input_tok_s=r['input_tps'],output_tok_s=r['output_tps'],checks_passed=r['checks_passed'],checks_total=r['checks_total'],
                                      error=r['error'],case_report=path + '#' + tag,raw_file=f'data/daily/{fullfile}.jsonl.gz'))
            matrix_cells.append('<br>'.join(parts))
        matrix.append(matrix_cells)
        (root / path).write_text('\n'.join(page))
    csv_file(root / 'results/summary.csv', summary)
    csv_file(root / 'results/per-question.csv', all_cases)
    readme = ['# Pi CLI + oMLX: local model benchmark results', '',
              f'**Ten models × ten daily tasks × {trial_count} trials = {100 * trial_count} scored observations.** Public, compact results repository. No credentials or model weights. Earlier benchmark results are included as compressed downloads.', '',
              'All benchmarks were run locally on an **Apple M1 Max machine with 64 GB of RAM (unified memory)**. macOS 26.6.2, Pi 1.4.0, GWS 0.22.5. Collected October 26–27, 2026 (America/Los_Angeles). All models/questions ran sequentially.', '',
              '## Model summary', '',
              f'Both tables are sorted by **combined score across all {trial_count} trials, out of {10 * trial_count}**, highest first. Ties use Trial #{trial_count} score descending, then collection order. Trial #1 retains the original six questions plus four additions. Subsequent trials are fresh runs of all ten. Scores require all task checks and normal completion within **600 seconds / 12 model requests**. Score links open each trial’s failures.', '',
              f'**All {trial_count} trials total E2E** sums all {10 * trial_count} case runtimes per model. Each trial’s **total E2E** sums its ten cases. Both include failures and repairs and exclude model load/warmup/grading. Rates are weighted native engine measurements: input excludes cached tokens; output includes thinking.', '',
              '*Scroll horizontally within each table to see all columns.*', ''] + table(overall, numeric=True) + ['',
              '[Summary CSV](results/summary.csv) · [Methodology](docs/methodology.md)', '', '## Question correctness and runtime', '',
              f'Each cell shows all {trial_count} trials separately: **correctness /2 · E2E seconds**. **2/2** = all verification checks passed; **1/2** = at least one required content check passed; **0/2** = none. **⚠** = verified correct but completion failed, earning no /10 point. These are descriptive categories, not equal-weight partial-credit grades. Every entry links to the case explanation and full raw records.', ''] + table(matrix) + ['',
              f'[All {100 * trial_count} per-question results CSV](results/per-question.csv) · [Exact questions and CLI guides](docs/questions.md)', '',
              '## Interpretation', '',
              '- Between Trials #1 and #2, full-pass outcomes matched on **72/100** pairs; those results are **not fully reproducible** at the per-question completion level.',
              '- Thirty expected references changed (file inventory, duplicates, Drive storage). Among 70 pairs with unchanged expected answers, **24 full-pass outcomes flipped**. Matching expected answers does not prove identical source/context inputs.',
              '- In Trials #1 and #2, all three Qwen3.8 variants repeated **6/6 full passes** on the original six questions. Jundot verified **9/10** in both, but two correct Trial #2 artifacts hit completion limits, reducing its full score from **9 to 7**.',
              '- Several mathematically optimal backup plans failed the candidate inventory/metadata requirements. See case explanations before interpreting these as optimization failures.',
              '- These are small repeated samples. Existing model-specific MTP/engine/cache settings and shared laptop workload limit generalization.', '',
              '## Data and documentation', '',
              '- [Data layout, raw-data commands, and the size limit](docs/data.md)',
              '- [Methodology, scoring, timing, safety controls, and corrections](docs/methodology.md)',
              '- [Earlier benchmark suites and downloads](docs/history.md)',
              '- [Exact prompts, CLI guides, and both calendar windows](docs/questions.md)',
              '- [Environment](metadata/environment.json), [completion audit](metadata/completion-audit.json), [reproducibility summary](metadata/reproducibility-summary.json)',
              '- [Credential review and artifact hashes](metadata/publication.json)', '',
              'The owner authorized public release of filenames and logs. Scored records retain local filenames and account/home-related answer metadata. Credentials and credential stores are excluded. Full duplicated tool/provider transcripts, scratch directories, runtime caches, source media, and model weights are omitted to keep this new repository below **3,000,000 bytes including local Git history**. Original scored result records remain available as lossless gzip downloads.', '',
              '## Regenerate or validate offline', '', '```sh', 'python3 scripts/report.py --render', 'python3 scripts/report.py --validate', '```', '',
              'These use Python’s standard library, saved files only, no inference/network calls, and no model-authored program execution. The archived benchmark harness is machine-specific experimental code. No license is assigned to personal data, third-party models, or model outputs by this repository.', '']
    (root / 'README.md').write_text('\n'.join(readme))
    if trial_count == 3:
        readme_path = root / 'README.md'
        content = readme_path.read_text().replace('- [Data layout, raw-data commands, and the size limit]',
            '- [Trial #3 collection, audit, and comparison](docs/trial-3.md)\n- [Data layout, raw-data commands, and the size limit]')
        readme_path.write_text(content)
    return summary, all_cases


def validate(root):
    manifest = load(root, 'metadata/model-task-manifest.json.gz')
    originals = load(root, 'metadata/original-summary.json.gz')
    summary = list(csv.DictReader((root / 'results/summary.csv').open()))
    per = list(csv.DictReader((root / 'results/per-question.csv').open()))
    datasets = trials(root)
    trial_count = len(datasets)
    assert len(summary) == 10 and len(per) == 100 * trial_count
    raw = {}
    for trial, dataset in enumerate(datasets, 1):
        assert len(dataset) == 100
        for r in dataset:
            raw[r['model'], r['task'], trial] = r
    assert len(raw) == 100 * trial_count
    for row in per:
        r = raw[row['model'], row['task'], int(row['trial'])]
        assert float(row['e2e_s']) == r['e2e_s']
        assert int(row['correctness_out_of_2']) == correct(r)
        assert row['verified'] == str(r['verified']) and row['full_pass'] == str(r['passed'])
        for field in ['checks_passed', 'checks_total']:
            assert int(row[field]) == r[field]
        for published, original in [('input_tok_s', 'input_tps'), ('output_tok_s', 'output_tps')]:
            assert float(row[published]) == r[original]
    old = {r['model']: r for r in originals}
    for s in summary:
        for trial in range(1, trial_count + 1):
            subset = [r for (mid, _, tr), r in raw.items() if mid == s['model'] and tr == trial]
            expected = stats(subset)
            for field, value in expected.items():
                assert math.isclose(float(s[f'trial_{trial}_{field}']), value, rel_tol=1e-10)
            if trial < 3:
                prefix = 'expanded10' if trial == 1 else 'repeat10'
                reference = old[s['model']]
                assert expected['score'] == reference[prefix + '_full']
                assert math.isclose(expected['input_tok_s'], reference[prefix + '_input_tps'], rel_tol=1e-10)
                assert math.isclose(expected['output_tok_s'], reference[prefix + '_output_tps'], rel_tol=1e-10)
            else:
                reference = next(r for r in load(root, 'metadata/trial-3-summary.json.gz') if r['model'] == s['model'])
                assert reference['attempted'] == 10 and reference['full'] == expected['score']
                for field, key in [('input_tok_s', 'input_tps'), ('output_tok_s', 'output_tps'), ('total_e2e_s', 'total_e2e_s')]:
                    assert math.isclose(expected[field], reference[key], rel_tol=1e-10)
        assert int(s['combined_score']) == sum(int(s[f'trial_{trial}_score']) for trial in range(1, trial_count + 1))
        assert math.isclose(float(s['combined_total_e2e_s']), sum(float(s[f'trial_{trial}_total_e2e_s']) for trial in range(1, trial_count + 1)), rel_tol=1e-10)
    if trial_count == 3:
        audit = load(root, 'metadata/trial-3-audit.json.gz')
        assert audit['passed'] and audit['scored_trials'] == 100 and not audit['failed_checks']
        assert audit['google_mutation_dispatches'] == 0
    rank = lambda r: (-int(r['combined_score']), -int(r[f'trial_{trial_count}_score']))
    assert summary == sorted(summary, key=rank)
    links = 0
    for p in [root / 'README.md', *sorted((root / 'docs').glob('*.md')), *sorted((root / 'cases').glob('*.md'))]:
        content = p.read_text()
        hrefs = re.findall(r'\[[^\]\n]*\]\(([^)]+)\)', content) + re.findall(r'href="([^"]+)"', content)
        for href in hrefs:
            url = urlsplit(html.unescape(href))
            if url.scheme or url.netloc:
                continue
            target = (p.parent / unquote(url.path)).resolve() if url.path else p
            assert target.is_relative_to(root) and target.exists(), (p, href)
            if url.fragment and target.suffix == '.md':
                text = target.read_text()
                ids = set(re.findall(r'<a id="([^"]+)"', text))
                ids.update(re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in re.findall(r'^#{1,6}\s+(.+)$', text, re.M))
                assert unquote(url.fragment) in ids, (p, href)
            links += 1
    for item in load(root, 'metadata/publication.json')['files']:
        raw_bytes = (root / item['path']).read_bytes()
        assert hashlib.sha256(raw_bytes).hexdigest() == item['sha256'], item['path']
    for p in root.rglob('*'):
        assert not p.is_symlink()
    print(json.dumps({'status': 'PASS', 'models': 10, 'trials': trial_count, 'scored_observations': 100 * trial_count, 'portable_links': links,
                      'scores_and_weighted_metrics_match_originals': True, 'model_runs': 0}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--render', action='store_true')
    parser.add_argument('--validate', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    if args.render:
        render(root)
    if args.validate:
        validate(root)
