# Trial #3

Collected 2026-10-27T14:31:30.303823-07:00 through 2026-10-27T21:48:10.107570-07:00 on the same Apple M1 Max machine with 64 GB of unified RAM.

**100 fresh scored cases: the same ten models × the same ten questions.** One model was loaded at a time and cases ran sequentially. A process lock prevented a second copy of this worker. Local task timeouts and inference-isolation checks remained active; hourly local progress logging required no Codex calls.

Prompts, initial CLI guides, per-question seeds, sampling/thinking budgets, 600-second / 12-request limits, grading and read-only controls match Trial #2. Both calendar-window files and the frozen redacted Frigate log are byte-identical to Trial #2. Local inventory and live Google/Home Assistant/Frigate reads use new per-case source receipts, so their contents may have changed. Native caches were retained and each model received the same idle/unload/reload/warmup procedure.

The historical grader self-test was adapted to reseal its deliberately changed trusted canary on each negative-control check. Scored-case artifact sealing and grading rules were unchanged. An initial preparation attempt stopped before any inference when the old control reused a sealed answer; it contributed no scored observation.

Fresh boundary controls passed 38 checks; grader controls passed 25. The sandboxed real-Pi integration probe passed. Final saved-evidence audit passed **910/910** checks, including all 100 native-metric and grading replays, non-overlapping scored-case lifetimes, unchanged protected files/prior results, and **zero Google mutation dispatches** across all attempts and controls.

Every completed outcome is retained; incorrect answers and completion-limit failures were not retried. Only source-change or external-inference infrastructure exclusions are eligible for the existing bounded retry policy.

## Runtime and ranking

The README summary includes Trial #3 score /10, total E2E, weighted uncached-input tok/s and output tok/s. Its combined score is out of 30 and its **All 3 trials total E2E** column sums all 30 case runtimes per model, including failures/repairs and excluding model load, warmup and grading. Both tables rank combined score descending, breaking ties by Trial #3 score and then original collection order. Each question now has T1, T2 and T3 correctness /2 and E2E links.

## Comparison with earlier trials

Against Trial #1: **76/100** full-pass outcomes and **77/100** verification outcomes agreed. Expected references changed for 31 pairs; 16 full-pass outcomes flipped among pairs with unchanged expected answers.

Against Trial #2: **78/100** full-pass outcomes and **77/100** verification outcomes agreed. Expected references changed for 11 pairs; 20 full-pass outcomes flipped among pairs with unchanged expected answers.

Matching expected answers does not prove identical source/context inputs; these remain small repeated samples on a shared laptop.

## Download and inspect

- [All Trial #3 scored records, expected/submitted answers, checks and timings](../data/daily/third10.jsonl.gz?raw=1)
- [Recorded models, tasks and settings](../metadata/trial-3-manifest.json.gz?raw=1)
- [Original native aggregate summary](../metadata/trial-3-summary.json.gz?raw=1)
- [Complete saved-evidence audit](../metadata/trial-3-audit.json.gz?raw=1)
- [Pairwise comparison details](../metadata/trial-3-comparison.json.gz?raw=1)
- [Trusted Trial #3 driver source](../code/trial-3-runner.py.gz?raw=1)
- [Exact unchanged questions and calendar windows](questions.md)

Full local provider/tool transcripts and source receipts remain in the separate private experiment folder. This compact public repository retains the full scored records and portable failure explanations without credentials or duplicated scratch data.
