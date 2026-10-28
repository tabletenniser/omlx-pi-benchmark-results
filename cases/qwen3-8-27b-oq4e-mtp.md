# Qwen3.8 Jundot

Exact model ID: `Qwen3.8-27B-oQ4e-mtp`.

[Summary and matrix](../README.md) · [Scoring](../docs/methodology.md#scoring)

[Recorded Hugging Face model](https://huggingface.co/Jundot/Qwen3.8-27B-oQ4e-mtp)

## Trial 1 failures

- [Q07: Backup optimization](#q07-trial-1) — FAIL; 1/2; 214.95s.

## Trial 2 failures

- [Q07: Backup optimization](#q07-trial-2) — FAIL; 1/2; 309.85s.
- [Q08: Camera cross-check](#q08-trial-2) — VERIFIED; completion failed; 2/2; 559.44s.
- [Q09: Frigate log analysis](#q09-trial-2) — VERIFIED; completion failed; 2/2; 600.33s.

## Trial 3 failures

- [Q03: HA basement guards](#q03-trial-3) — FAIL; 1/2; 208.22s.

<a id="q01-trial-1"></a>
## Q01 · Trial 1: Largest files

**PASS** · correctness **2/2** · E2E **94.95s** · checks **7/7**.

Input 71.57 tok/s · output 19.26 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q01-trial-2"></a>
## Q01 · Trial 2: Largest files

**PASS** · correctness **2/2** · E2E **155.32s** · checks **7/7**.

Input 53.22 tok/s · output 14.74 tok/s · 3 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q01-trial-3"></a>
## Q01 · Trial 3: Largest files

**PASS** · correctness **2/2** · E2E **161.34s** · checks **7/7**.

Input 58.81 tok/s · output 16.57 tok/s · 3 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-1"></a>
## Q02 · Trial 1: Exact duplicates

**PASS** · correctness **2/2** · E2E **196.07s** · checks **8/8**.

Input 72.33 tok/s · output 24.23 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-2"></a>
## Q02 · Trial 2: Exact duplicates

**PASS** · correctness **2/2** · E2E **159.58s** · checks **8/8**.

Input 52.37 tok/s · output 16.36 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-3"></a>
## Q02 · Trial 3: Exact duplicates

**PASS** · correctness **2/2** · E2E **142.25s** · checks **8/8**.

Input 57.24 tok/s · output 15.59 tok/s · 4 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-1"></a>
## Q03 · Trial 1: HA basement guards

**PASS** · correctness **2/2** · E2E **98.20s** · checks **19/19**.

Input 77.55 tok/s · output 21.63 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-2"></a>
## Q03 · Trial 2: HA basement guards

**PASS** · correctness **2/2** · E2E **127.10s** · checks **19/19**.

Input 65.17 tok/s · output 18.21 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-3"></a>
## Q03 · Trial 3: HA basement guards

**FAIL** · correctness **1/2** · E2E **208.22s** · checks **18/19**.

Input 50.46 tok/s · output 18.31 tok/s · 6 model requests.

action: incorrect value.

Failed checks:

- correct action

[Exact prompt](../docs/questions.md#q03) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-1"></a>
## Q04 · Trial 1: Frigate configuration

**PASS** · correctness **2/2** · E2E **263.33s** · checks **19/19**.

Input 78.37 tok/s · output 18.99 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q04) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-2"></a>
## Q04 · Trial 2: Frigate configuration

**PASS** · correctness **2/2** · E2E **349.53s** · checks **19/19**.

Input 52.77 tok/s · output 15.02 tok/s · 8 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q04) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-3"></a>
## Q04 · Trial 3: Frigate configuration

**PASS** · correctness **2/2** · E2E **355.59s** · checks **19/19**.

Input 51.60 tok/s · output 14.86 tok/s · 7 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q04) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-1"></a>
## Q05 · Trial 1: Drive storage

**PASS** · correctness **2/2** · E2E **180.31s** · checks **10/10**.

Input 71.37 tok/s · output 17.91 tok/s · 8 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-2"></a>
## Q05 · Trial 2: Drive storage

**PASS** · correctness **2/2** · E2E **164.62s** · checks **10/10**.

Input 50.43 tok/s · output 13.60 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-3"></a>
## Q05 · Trial 3: Drive storage

**PASS** · correctness **2/2** · E2E **170.66s** · checks **10/10**.

Input 49.85 tok/s · output 13.55 tok/s · 5 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-1"></a>
## Q06 · Trial 1: Calendar conflicts

**PASS** · correctness **2/2** · E2E **141.82s** · checks **8/8**.

Input 72.13 tok/s · output 20.14 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-2"></a>
## Q06 · Trial 2: Calendar conflicts

**PASS** · correctness **2/2** · E2E **294.58s** · checks **8/8**.

Input 47.43 tok/s · output 12.49 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-3"></a>
## Q06 · Trial 3: Calendar conflicts

**PASS** · correctness **2/2** · E2E **264.63s** · checks **8/8**.

Input 48.56 tok/s · output 12.41 tok/s · 5 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-1"></a>
## Q07 · Trial 1: Backup optimization

**FAIL** · correctness **1/2** · E2E **214.95s** · checks **8/11**.

Input 75.39 tok/s · output 19.32 tok/s · 6 model requests.

The submission failed the checks listed below.

Failed checks:

- complete source-grounded candidate CSV
- correct candidate_count
- correct candidate_total_bytes

[Exact prompt](../docs/questions.md#q07) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-2"></a>
## Q07 · Trial 2: Backup optimization

**FAIL** · correctness **1/2** · E2E **309.85s** · checks **8/11**.

Input 48.71 tok/s · output 13.64 tok/s · 6 model requests.

The submission failed the checks listed below.

Failed checks:

- complete source-grounded candidate CSV
- correct candidate_count
- correct candidate_total_bytes

[Exact prompt](../docs/questions.md#q07) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-3"></a>
## Q07 · Trial 3: Backup optimization

**PASS** · correctness **2/2** · E2E **393.28s** · checks **11/11**.

Input 50.09 tok/s · output 14.75 tok/s · 9 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q07) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-1"></a>
## Q08 · Trial 1: Camera cross-check

**PASS** · correctness **2/2** · E2E **599.99s** · checks **11/11**.

Input 64.34 tok/s · output 16.10 tok/s · 12 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q08) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-2"></a>
## Q08 · Trial 2: Camera cross-check

**VERIFIED; completion failed** · correctness **2/2** · E2E **559.44s** · checks **11/11**.

Input 44.71 tok/s · output 12.99 tok/s · 12 model requests.

All verification checks passed.

Completion error:

```text
429: {"message":"Benchmark limit: twelve model requests per task."}
```

[Exact prompt](../docs/questions.md#q08) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-3"></a>
## Q08 · Trial 3: Camera cross-check

**PASS** · correctness **2/2** · E2E **515.21s** · checks **11/11**.

Input 50.48 tok/s · output 12.99 tok/s · 12 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q08) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-1"></a>
## Q09 · Trial 1: Frigate log analysis

**PASS** · correctness **2/2** · E2E **200.70s** · checks **15/15**.

Input 68.37 tok/s · output 20.22 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q09) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-2"></a>
## Q09 · Trial 2: Frigate log analysis

**VERIFIED; completion failed** · correctness **2/2** · E2E **600.33s** · checks **15/15**.

Input 48.74 tok/s · output 13.21 tok/s · 11 model requests.

All verification checks passed.

Completion error:

```text
Task exceeded 600-second wall limit
```

[Exact prompt](../docs/questions.md#q09) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-3"></a>
## Q09 · Trial 3: Frigate log analysis

**PASS** · correctness **2/2** · E2E **340.47s** · checks **15/15**.

Input 55.03 tok/s · output 15.93 tok/s · 8 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q09) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-1"></a>
## Q10 · Trial 1: Meeting availability

**PASS** · correctness **2/2** · E2E **372.15s** · checks **11/11**.

Input 68.48 tok/s · output 17.61 tok/s · 9 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q10) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-2"></a>
## Q10 · Trial 2: Meeting availability

**PASS** · correctness **2/2** · E2E **511.16s** · checks **11/11**.

Input 48.76 tok/s · output 13.74 tok/s · 9 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q10) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-3"></a>
## Q10 · Trial 3: Meeting availability

**PASS** · correctness **2/2** · E2E **345.47s** · checks **11/11**.

Input 56.24 tok/s · output 15.63 tok/s · 7 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q10) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-oQ4e-mtp"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).
