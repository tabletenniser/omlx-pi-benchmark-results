# Data, credentials and repository size

## Compact layout

| Path | Contents |
|---|---|
| [Summary CSV](../results/summary.csv) | Ten models; separate trial scores, total/mean E2E, tokens/evaluation seconds and weighted rates |
| [Per-question CSV](../results/per-question.csv) | 200 observations: /2 correctness, original full/verified flags, E2E, rates, check counts, errors and case/raw links |
| [All-suites summary](../results/all-suites-summary.csv) | Combined historical and daily model summaries |
| [Daily data](../data/daily) | Three lossless gzip JSONL files: original6 (60), added4 (40), repeat10 (100) |
| [Historical data](history.md) | Original earlier suites and the normalized ten-model matrix; some overlap |
| [Case pages](../cases) | Ten model pages covering all 100 paired model/question cases with failure explanations |
| [Exact questions](questions.md) | Ten prompts, CLI guides and exact calendar/scheduling windows |
| [Metadata](../metadata) | Environment, original settings/summary, notes, audits, hashes and credential review |
| [Harness source](../code/benchmark-harness.tar.gz?raw=1) | Trusted experimental runner/grader source archive |

Each raw JSONL row retains its original fields, including full `checks` with details, `answer`, `expected`, original absolute `directory`, model IDs, request/tool counters, token/evaluation times and recorded errors. The files are compressed, not reduced to success/failure summaries. Trial1 combines original6 and added4; trial2 uses repeat10. No inference was rerun.

## Read the raw data

Python standard library (no downloads or model execution):

```python
import gzip, json
with gzip.open('data/daily/repeat10.jsonl.gz', 'rt') as f:
    rows = [json.loads(line) for line in f]
case = next(r for r in rows
            if r['model'] == 'Qwen3.8-27B-oQ4e-mtp'
            and r['task'] == 'mac_backup_budget')
print(json.dumps({k: case[k] for k in ['checks', 'expected', 'answer']}, indent=2))
```

On macOS/Linux, `gzip -dc data/daily/repeat10.jsonl.gz` prints every row. Use `tar -tzf code/benchmark-harness.tar.gz` to list source files without executing anything.

`results/summary.csv` uses `trial_1_*`/`trial_2_*`. `score` is the original full-pass /10 count; `verified` disregards normal-completion failure. `total_e2e_s` sums ten cases; `mean_e2e_s` divides by ten. Token/evaluation-second fields allow independent weighted-rate calculations. `results/per-question.csv` separates `correctness_out_of_2`, `verified` and `full_pass` and gives the portable `case_report` and `raw_file` paths. Raw absolute paths are historical provenance; no such directory is required after cloning.

## What was left out

Full provider/tool transcript duplication, source receipt payload duplication, scratch folders, runtime compilation caches, credential stores, source media, model weights and the old private repository's Git history are omitted. The original large archive remains separate. Original scored records, answers, expected results, checks and metrics are retained; replaying the full source-receipt audit requires that separate archive.

This fresh repository must stay below **3,000,000 bytes** for both its committed working files and **the local checkout including `.git`**, measured after Git packing. Compression is lossless gzip with deterministic headers. Size is checked before publication. Future commits/data additions can grow history; check size again before pushing them.

## Credentials and public data

The owner explicitly authorized public filenames and logs. Local filenames, home-related configuration facts and Google answer metadata can appear in these scored records. They are not anonymized. Actual credential stores are excluded. Every exported payload, including contents of gzip/tar archives, was scanned before compression for known current oMLX/process secrets and credential-shaped literals, provider tokens, PEM private keys, URL passwords and bearer tokens. Any redaction is itemized without exposing its value.

[Publication manifest](../metadata/publication.json) lists hashes of shipped files and original/exported source hashes, plus credential-scan scope and transformations. Original artifact hash trees are not bundled because they refer to omitted caches and duplicate files. The manifest describes this compact export. Credential scanning is a targeted check; it is not anonymization of account metadata.
