# Methodology

## Collection and protocol

Ten models × ten daily questions × three observations = 300 scored results. Trial #1 retains the original six-question collection (60 observations) and adds four questions (40 observations); it is not a fresh contiguous ten-question run. Trials #2 and #3 are separate fresh 100-observation collections. Every case/model was sequential to avoid OOM. Per stage/model, the runner waited for idle, unloaded/reloaded and used the same short math warmup. Native disk/prefix caches and model-specific MTP/engine settings were retained. [Trial #3 collection and audit](trial-3.md).

All benchmarks were run locally on an **Apple M1 Max machine with 64 GB of RAM (unified memory)**; macOS 26.6.2; Pi 1.4.0; GWS 0.22.5; Node 26.10.0; Python 3.14.4. [Environment](../metadata/environment.json), [recorded models/tasks/settings](../metadata/model-task-manifest.json.gz?raw=1).

Real Pi CLI native read/write/edit/bash tools, direct Node launcher. Temperature 0.6, top_p 0.95, top_k 20; per-question seed 41001 + 100 × zero-based question index; configured thinking budget 1,024; maximum output 4,096 tokens per request; context 65,536; at most 12 model requests and 600 seconds per question. Global extensions, skills, MCP, user context, retry and compaction disabled. A fixed CLI guide and explicit write guard were provided. Matching seeds/settings do not guarantee deterministic tool interactions or native inference.

## Scoring

- **Verified:** every requested value, artifact, required source read and required successful program invocation passed.
- **Full pass:** verified plus normal Pi completion within the common request/time limits. Each full pass earns one point in the overall **/10** score.
- **Correctness /2:** 2 if verified; otherwise 1 if at least one original check beginning `correct ` (required answer field) or `complete ` (complete requested artifact) passed; otherwise 0. Fixture preservation, an object-shaped answer and tool invocation alone earn no partial correctness.
- **⚠** marks verified output whose agent did not finish normally. It receives 2/2 correctness and no /10 score point.

The /2 display is an ordinal description, not calibrated equal-weight partial credit. A single simple correct field and a nearly perfect submission may both receive 1/2. Original checks passed/total and full expected/actual details in the raw records distinguish them. Missing output means undelivered work, not necessarily a factual error. Original /10 scores were not changed for this export.

## Metrics

Overall E2E is the sum of ten recorded case `e2e_s` values, including failures and repairs. README formats this as rounded minutes:seconds; CSV retains original precision and mean E2E. E2E includes tool/network work and orchestration, but excludes model loading, warmup, grading, idle waits and unscored infrastructure attempts.

Weighted input tok/s = sum(`computed_input_tokens`) / sum(`input_eval_s`); cached prompt tokens are excluded. Weighted output tok/s = sum(`output_tokens`) / sum(`output_eval_s`); native output includes thinking. These are native engine throughput rates, not E2E tokens/s, visible-only text rates, arithmetic averages of case speeds or time-to-first-token measurements.

## Reproducibility and limitations

Full outcomes agreed on 72/100 pairs. Thirty expected references changed (file inventory, duplicate statistics, Drive usage). Among 70 stable expected-answer pairs, 24 full outcomes flipped. Same expected answers do not establish that all source/context/model inputs were identical. Two observations are too few for a high-confidence reliability estimate.

All three Qwen3.8 variants repeated 6/6 full passes on the original six. Jundot verified9/10 in both observations; its full9→7 drop comes from two correct artifacts hitting completion limits. Several backup plans were mathematically optimal but violated the required 16-candidate CSV/metadata contract. Home/live account data and shared laptop workload may change. Existing native engine/MTP/cache settings differ by model. This is a local task benchmark, not a universal model ranking.

## Harmless-operation boundary

Every student Pi process/child in these daily suites ran under macOS default-deny Seatbelt, with writes limited to disposable scratch and network limited to a loopback broker. The broker permitted fixed Google GET/schema/help operations and sanitized stored HA/Frigate reads. No user-file deletion, Workspace mutation, invitations/messages, or home-device control. Backup tests planned a subset without moving/copying/deleting files; log analysis used a frozen credential-redacted real log. The trusted grader never executes model-authored code.

Artifact reads were hardened after eleven new cases: pinned directory descriptors, O_NOFOLLOW/O_NONBLOCK, regular files, 8 MiB cap, sealed copies outside student scratch. The eleven verdicts replayed unchanged; symlink/FIFO/oversize controls passed. Earlier standalone runners should not be used on real private data without these daily-suite controls.

## Grading correction and excluded attempts

A final shell-invocation parser fix accepted the actual command `python3 plan_backup.py; ...`. All 140 new cases were regraded from saved receipts/artifacts without inference or student-code execution. Exactly one verdict changed: repeat Ornith Vision backup became PASS. [Correction record](../metadata/invocation-parser-correction.json).

During Trials #1 and #2, maintenance and occasional foreign user inference caused archived unscored infrastructure attempts. The benchmark interrupted only its own affected trial and waited; foreign inference was not killed. These are excluded from those 200 scored observations. Their final evidence audit passed 1,976/1,976 checks; zero Google mutations occurred across all attempts/controls, and five protected host files were unchanged. [Completion audit](../metadata/completion-audit.json), [full audit](../metadata/final-audit.json.gz?raw=1), [all-attempt source audit](../metadata/all-attempts-source-audit.json.gz?raw=1). Trial #3 has its own [fresh controls and saved-evidence audit](trial-3.md).

## Code and replay

[Archived final benchmark harness](../code/benchmark-harness.tar.gz?raw=1) contains the trusted runner/grader sources. It assumes the original Mac paths, installed local models and authenticated live sources. Cloning these results is not a bit-identical replay environment. Source media and weights are not bundled. The readable report script regenerates tables offline from saved data; never treat archived model responses/programs as trusted executable code.
