# Ornith Vision 4-bit

Exact model ID: `Ornith-1.5-35B-A3B-Vision-MTPLX-4bit`.

[Summary and matrix](../README.md) · [Scoring](../docs/methodology.md#scoring)

[Recorded Hugging Face model](https://huggingface.co/zwcf5200/Ornith-1.5-35B-A3B-Vision-MTPLX-4bit)

## Trial 1 failures

- [Q03: HA basement guards](#q03-trial-1) — FAIL; 1/2; 35.39s.
- [Q04: Frigate configuration](#q04-trial-1) — FAIL; 1/2; 88.96s.
- [Q07: Backup optimization](#q07-trial-1) — FAIL; 1/2; 73.80s.
- [Q08: Camera cross-check](#q08-trial-1) — FAIL; 1/2; 149.81s.

## Trial 2 failures

- [Q08: Camera cross-check](#q08-trial-2) — FAIL; 1/2; 194.11s.
- [Q09: Frigate log analysis](#q09-trial-2) — FAIL; 1/2; 113.36s.

<a id="q01-trial-1"></a>
## Q01 · Trial 1: Largest files

**PASS** · correctness **2/2** · E2E **34.34s** · checks **7/7**.

Input 466.29 tok/s · output 56.18 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q01-trial-2"></a>
## Q01 · Trial 2: Largest files

**PASS** · correctness **2/2** · E2E **55.73s** · checks **7/7**.

Input 440.01 tok/s · output 70.87 tok/s · 10 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-1"></a>
## Q02 · Trial 1: Exact duplicates

**PASS** · correctness **2/2** · E2E **57.70s** · checks **8/8**.

Input 459.15 tok/s · output 55.98 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-2"></a>
## Q02 · Trial 2: Exact duplicates

**PASS** · correctness **2/2** · E2E **87.34s** · checks **8/8**.

Input 461.96 tok/s · output 72.43 tok/s · 12 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-1"></a>
## Q03 · Trial 1: HA basement guards

**FAIL** · correctness **1/2** · E2E **35.39s** · checks **18/19**.

Input 439.86 tok/s · output 58.58 tok/s · 5 model requests.

Identified both correct motion sensors but reversed the explicitly requested sorted order. All other checks passed.

Failed checks:

- correct idle_sensors

[Exact prompt](../docs/questions.md#q03) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-2"></a>
## Q03 · Trial 2: HA basement guards

**PASS** · correctness **2/2** · E2E **36.59s** · checks **19/19**.

Input 506.84 tok/s · output 67.01 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-1"></a>
## Q04 · Trial 1: Frigate configuration

**FAIL** · correctness **1/2** · E2E **88.96s** · checks **18/19**.

Input 414.93 tok/s · output 60.53 tok/s · 7 model requests.

Inverted the label override mapping: {bus:5, truck:7} rather than the source mapping {5:bus, 7:truck}. The detector type and other fields were correct.

Failed checks:

- correct label_overrides

[Exact prompt](../docs/questions.md#q04) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-2"></a>
## Q04 · Trial 2: Frigate configuration

**PASS** · correctness **2/2** · E2E **65.87s** · checks **19/19**.

Input 528.37 tok/s · output 58.75 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q04) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-1"></a>
## Q05 · Trial 1: Drive storage

**PASS** · correctness **2/2** · E2E **30.35s** · checks **10/10**.

Input 504.99 tok/s · output 62.05 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-2"></a>
## Q05 · Trial 2: Drive storage

**PASS** · correctness **2/2** · E2E **29.43s** · checks **10/10**.

Input 523.68 tok/s · output 73.84 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-1"></a>
## Q06 · Trial 1: Calendar conflicts

**PASS** · correctness **2/2** · E2E **98.02s** · checks **8/8**.

Input 453.36 tok/s · output 64.66 tok/s · 7 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-2"></a>
## Q06 · Trial 2: Calendar conflicts

**PASS** · correctness **2/2** · E2E **71.94s** · checks **8/8**.

Input 468.00 tok/s · output 61.51 tok/s · 9 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-1"></a>
## Q07 · Trial 1: Backup optimization

**FAIL** · correctness **1/2** · E2E **73.80s** · checks **9/11**.

Input 414.60 tok/s · output 51.92 tok/s · 6 model requests.

The optimal subset and candidate CSV were correct. candidate_count and candidate_total_bytes described the9 selected files rather than all16 candidates: selected bytes20971238 instead of candidate bytes40794599. Other9checks passed.

Failed checks:

- correct candidate_count
- correct candidate_total_bytes

[Exact prompt](../docs/questions.md#q07) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-2"></a>
## Q07 · Trial 2: Backup optimization

**PASS** · correctness **2/2** · E2E **57.88s** · checks **11/11**.

Input 456.26 tok/s · output 53.96 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q07) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-1"></a>
## Q08 · Trial 1: Camera cross-check

**FAIL** · correctness **1/2** · E2E **149.81s** · checks **7/11**.

Input 374.58 tok/s · output 53.76 tok/s · 12 model requests.

The submission failed the checks listed below.

Completion error:

```text
429: {"message":"Benchmark limit: twelve model requests per task."}
```

Failed checks:

- correct automation_count
- correct automations
- correct referenced_camera_names
- correct unreferenced_frigate_cameras

[Exact prompt](../docs/questions.md#q08) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-2"></a>
## Q08 · Trial 2: Camera cross-check

**FAIL** · correctness **1/2** · E2E **194.11s** · checks **10/11**.

Input 369.36 tok/s · output 44.50 tok/s · 12 model requests.

The submission failed the checks listed below.

Failed checks:

- correct automations

[Exact prompt](../docs/questions.md#q08) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-1"></a>
## Q09 · Trial 1: Frigate log analysis

**PASS** · correctness **2/2** · E2E **97.30s** · checks **15/15**.

Input 373.41 tok/s · output 53.18 tok/s · 10 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q09) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-2"></a>
## Q09 · Trial 2: Frigate log analysis

**FAIL** · correctness **1/2** · E2E **113.36s** · checks **11/15**.

Input 419.51 tok/s · output 62.33 tok/s · 12 model requests.

The submission failed the checks listed below.

Completion error:

```text
429: {"message":"Benchmark limit: twelve model requests per task."}
```

Failed checks:

- correct first_error_utc
- correct last_error_utc
- correct busiest_error_minute
- correct crashes_by_camera

[Exact prompt](../docs/questions.md#q09) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-1"></a>
## Q10 · Trial 1: Meeting availability

**PASS** · correctness **2/2** · E2E **130.71s** · checks **11/11**.

Input 393.47 tok/s · output 49.85 tok/s · 7 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q10) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-2"></a>
## Q10 · Trial 2: Meeting availability

**PASS** · correctness **2/2** · E2E **128.87s** · checks **11/11**.

Input 475.55 tok/s · output 59.06 tok/s · 8 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q10) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-Vision-MTPLX-4bit"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).
