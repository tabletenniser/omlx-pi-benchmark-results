# Qwen3.8 Youssofal

Exact model ID: `Qwen3.8-27B-MTPLX-Optimized-Speed`.

[Summary and matrix](../README.md) · [Scoring](../docs/methodology.md#scoring)

[Recorded Hugging Face model](https://huggingface.co/Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed)

## Trial 1 failures

- [Q07: Backup optimization](#q07-trial-1) — FAIL; 1/2; 422.12s.

## Trial 2 failures

- [Q09: Frigate log analysis](#q09-trial-2) — VERIFIED; completion failed; 2/2; 600.32s.
- [Q10: Meeting availability](#q10-trial-2) — FAIL; 1/2; 600.46s.

## Trial 3 failures

- [Q04: Frigate configuration](#q04-trial-3) — FAIL; 0/2; 600.50s.
- [Q07: Backup optimization](#q07-trial-3) — FAIL; 1/2; 392.75s.
- [Q09: Frigate log analysis](#q09-trial-3) — FAIL; 1/2; 564.07s.

<a id="q01-trial-1"></a>
## Q01 · Trial 1: Largest files

**PASS** · correctness **2/2** · E2E **128.76s** · checks **7/7**.

Input 70.92 tok/s · output 17.67 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q01-trial-2"></a>
## Q01 · Trial 2: Largest files

**PASS** · correctness **2/2** · E2E **123.57s** · checks **7/7**.

Input 48.28 tok/s · output 11.49 tok/s · 3 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q01-trial-3"></a>
## Q01 · Trial 3: Largest files

**PASS** · correctness **2/2** · E2E **166.32s** · checks **7/7**.

Input 51.20 tok/s · output 12.70 tok/s · 3 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-1"></a>
## Q02 · Trial 1: Exact duplicates

**PASS** · correctness **2/2** · E2E **259.60s** · checks **8/8**.

Input 69.88 tok/s · output 18.44 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-2"></a>
## Q02 · Trial 2: Exact duplicates

**PASS** · correctness **2/2** · E2E **288.16s** · checks **8/8**.

Input 47.03 tok/s · output 11.40 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-3"></a>
## Q02 · Trial 3: Exact duplicates

**PASS** · correctness **2/2** · E2E **141.84s** · checks **8/8**.

Input 54.28 tok/s · output 13.82 tok/s · 4 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-1"></a>
## Q03 · Trial 1: HA basement guards

**PASS** · correctness **2/2** · E2E **151.10s** · checks **19/19**.

Input 67.30 tok/s · output 15.31 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-2"></a>
## Q03 · Trial 2: HA basement guards

**PASS** · correctness **2/2** · E2E **181.69s** · checks **19/19**.

Input 46.85 tok/s · output 11.13 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-3"></a>
## Q03 · Trial 3: HA basement guards

**PASS** · correctness **2/2** · E2E **177.61s** · checks **19/19**.

Input 51.53 tok/s · output 11.43 tok/s · 6 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-1"></a>
## Q04 · Trial 1: Frigate configuration

**PASS** · correctness **2/2** · E2E **313.01s** · checks **19/19**.

Input 66.01 tok/s · output 15.79 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q04) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-2"></a>
## Q04 · Trial 2: Frigate configuration

**PASS** · correctness **2/2** · E2E **408.43s** · checks **19/19**.

Input 50.03 tok/s · output 13.07 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q04) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-3"></a>
## Q04 · Trial 3: Frigate configuration

**FAIL** · correctness **0/2** · E2E **600.50s** · checks **2/19**.

Input 53.19 tok/s · output 10.60 tok/s · 9 model requests.

No valid required answer.json was delivered. Missing value checks are undelivered output, not independently demonstrated factual errors. Task exceeded 600-second wall limit

Completion error:

```text
Task exceeded 600-second wall limit
```

Failed checks:

- answer.json is an object
- correct detector_types
- correct model_file
- correct model_type
- correct model_width
- correct model_height
- correct label_overrides
- correct tracked_label_count
- correct global_record_enabled
- correct continuous_retention_days
- correct motion_retention_days
- correct detection_explicitly_disabled
- correct recording_disabled_effective
- correct recording_inherits_global
- correct separate_detect_record_cameras
- correct fps_by_camera
- correct phone_camera_inputs

[Exact prompt](../docs/questions.md#q04) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-1"></a>
## Q05 · Trial 1: Drive storage

**PASS** · correctness **2/2** · E2E **154.89s** · checks **10/10**.

Input 71.88 tok/s · output 14.83 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-2"></a>
## Q05 · Trial 2: Drive storage

**PASS** · correctness **2/2** · E2E **171.31s** · checks **10/10**.

Input 51.48 tok/s · output 12.46 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-3"></a>
## Q05 · Trial 3: Drive storage

**PASS** · correctness **2/2** · E2E **186.86s** · checks **10/10**.

Input 53.10 tok/s · output 12.06 tok/s · 5 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-1"></a>
## Q06 · Trial 1: Calendar conflicts

**PASS** · correctness **2/2** · E2E **172.06s** · checks **8/8**.

Input 60.27 tok/s · output 14.24 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-2"></a>
## Q06 · Trial 2: Calendar conflicts

**PASS** · correctness **2/2** · E2E **264.05s** · checks **8/8**.

Input 49.76 tok/s · output 10.93 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-3"></a>
## Q06 · Trial 3: Calendar conflicts

**PASS** · correctness **2/2** · E2E **402.98s** · checks **8/8**.

Input 53.27 tok/s · output 11.78 tok/s · 10 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-1"></a>
## Q07 · Trial 1: Backup optimization

**FAIL** · correctness **1/2** · E2E **422.12s** · checks **8/11**.

Input 66.50 tok/s · output 14.49 tok/s · 8 model requests.

The submission failed the checks listed below.

Failed checks:

- complete source-grounded candidate CSV
- correct candidate_count
- correct candidate_total_bytes

[Exact prompt](../docs/questions.md#q07) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-2"></a>
## Q07 · Trial 2: Backup optimization

**PASS** · correctness **2/2** · E2E **398.51s** · checks **11/11**.

Input 47.60 tok/s · output 9.92 tok/s · 9 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q07) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-3"></a>
## Q07 · Trial 3: Backup optimization

**FAIL** · correctness **1/2** · E2E **392.75s** · checks **8/11**.

Input 52.48 tok/s · output 11.55 tok/s · 7 model requests.

The required complete CSV did not match its source-grounded contract. candidate_count: incorrect value. candidate_total_bytes: incorrect value.

Failed checks:

- complete source-grounded candidate CSV
- correct candidate_count
- correct candidate_total_bytes

[Exact prompt](../docs/questions.md#q07) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-1"></a>
## Q08 · Trial 1: Camera cross-check

**PASS** · correctness **2/2** · E2E **452.28s** · checks **11/11**.

Input 65.45 tok/s · output 13.27 tok/s · 9 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q08) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-2"></a>
## Q08 · Trial 2: Camera cross-check

**PASS** · correctness **2/2** · E2E **569.28s** · checks **11/11**.

Input 46.93 tok/s · output 9.62 tok/s · 8 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q08) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-3"></a>
## Q08 · Trial 3: Camera cross-check

**PASS** · correctness **2/2** · E2E **581.16s** · checks **11/11**.

Input 50.71 tok/s · output 11.09 tok/s · 12 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q08) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-1"></a>
## Q09 · Trial 1: Frigate log analysis

**PASS** · correctness **2/2** · E2E **419.22s** · checks **15/15**.

Input 63.16 tok/s · output 14.21 tok/s · 11 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q09) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-2"></a>
## Q09 · Trial 2: Frigate log analysis

**VERIFIED; completion failed** · correctness **2/2** · E2E **600.32s** · checks **15/15**.

Input 46.40 tok/s · output 10.73 tok/s · 8 model requests.

All verification checks passed.

Completion error:

```text
Task exceeded 600-second wall limit
```

[Exact prompt](../docs/questions.md#q09) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-3"></a>
## Q09 · Trial 3: Frigate log analysis

**FAIL** · correctness **1/2** · E2E **564.07s** · checks **14/15**.

Input 51.63 tok/s · output 11.39 tok/s · 12 model requests.

busiest_error_minute: one or more nested values/order differ; see exact expected/actual evidence.

Failed checks:

- correct busiest_error_minute

[Exact prompt](../docs/questions.md#q09) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-1"></a>
## Q10 · Trial 1: Meeting availability

**PASS** · correctness **2/2** · E2E **439.96s** · checks **11/11**.

Input 65.16 tok/s · output 14.70 tok/s · 8 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q10) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-2"></a>
## Q10 · Trial 2: Meeting availability

**FAIL** · correctness **1/2** · E2E **600.46s** · checks **8/11**.

Input 46.10 tok/s · output 10.80 tok/s · 9 model requests.

The submission failed the checks listed below.

Completion error:

```text
Task exceeded 600-second wall limit
```

Failed checks:

- correct days
- correct total_free_minutes
- correct first_three_meetings

[Exact prompt](../docs/questions.md#q10) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-3"></a>
## Q10 · Trial 3: Meeting availability

**PASS** · correctness **2/2** · E2E **496.86s** · checks **11/11**.

Input 53.72 tok/s · output 11.46 tok/s · 8 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q10) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-MTPLX-Optimized-Speed"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).
