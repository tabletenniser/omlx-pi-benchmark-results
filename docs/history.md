# Earlier benchmark suites

Different prompts, model sets and protocols were used; these scores are historical and should not be merged with the daily /10 scores. Some observations are duplicated between the original suites and the normalized ten-model matrix. Downloads are lossless gzip JSONL.

| Suite | Records | Raw results | Summary |
|---|---:|---|---|
| Initial Qwen comparison | 24 | [JSONL.gz](../data/history/initial-qwen.jsonl.gz?raw=1) | [Summary](../data/history/initial-qwen-summary.json) |
| Exact word counts (original eight models) | 480 | [JSONL.gz](../data/history/word-count.jsonl.gz?raw=1) | [Summary](../data/history/word-count-summary.csv) |
| Reasoning (original eight models) | 312 | [JSONL.gz](../data/history/reasoning.jsonl.gz?raw=1) | [Summary](../data/history/reasoning-summary.csv) |
| Pi CLI Python/TypeScript/tools (original eight) | 48 | [JSONL.gz](../data/history/pi-cli.jsonl.gz?raw=1) | [Summary](../data/history/pi-cli-summary.csv) |
| Ten-model normalized word/reasoning/Pi/speed matrix | 1050 | [JSONL.gz](../data/history/ten-model-matrix.jsonl.gz?raw=1) | [Summary](../data/history/ten-model-matrix-summary.csv) |
| CLI research and local Python | 40 | [JSONL.gz](../data/history/research-python.jsonl.gz?raw=1) | [Summary](../data/history/research-python-summary.csv) |

[Exact earlier 36 trial prompts](earlier-36-prompts.md) · [Research-extension prompts](research-questions.md)

The normalized ten-model matrix has 1,050 observations: 600 word-count, 360 reasoning, 60 Pi coding/tool cases and 30 speed probes. It includes model-generated responses/reasoning and the recorded verdict/timing fields. Original per-suite records retain their richer original grading fields where available.

Two Parallel-credit research cases were blocked rather than fabricated. Raw files preserve their recorded errors/status. No new inference or cloud calls were made for this compact export.
