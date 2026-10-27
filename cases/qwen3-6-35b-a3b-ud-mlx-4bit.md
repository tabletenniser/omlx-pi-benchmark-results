# Qwen3.6 UD

Exact model ID: `Qwen3.6-35B-A3B-UD-MLX-4bit`.

[Summary and matrix](../README.md) · [Scoring](../docs/methodology.md#scoring)

## Trial 1 failures

- [Q04: Frigate configuration](#q04-trial-1) — FAIL; 0/2; 105.45s.
- [Q06: Calendar conflicts](#q06-trial-1) — FAIL; 0/2; 106.47s.
- [Q07: Backup optimization](#q07-trial-1) — FAIL; 1/2; 94.10s.
- [Q08: Camera cross-check](#q08-trial-1) — FAIL; 1/2; 130.72s.
- [Q10: Meeting availability](#q10-trial-1) — FAIL; 0/2; 163.63s.

## Trial 2 failures

- [Q07: Backup optimization](#q07-trial-2) — FAIL; 1/2; 122.37s.
- [Q08: Camera cross-check](#q08-trial-2) — FAIL; 0/2; 49.69s.

<a id="q01-trial-1"></a>
## Q01 · Trial 1: Largest files

**PASS** · correctness **2/2** · E2E **51.63s** · checks **7/7**.

Input 474.68 tok/s · output 52.48 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q01-trial-2"></a>
## Q01 · Trial 2: Largest files

**PASS** · correctness **2/2** · E2E **29.41s** · checks **7/7**.

Input 554.55 tok/s · output 55.57 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-1"></a>
## Q02 · Trial 1: Exact duplicates

**PASS** · correctness **2/2** · E2E **44.61s** · checks **8/8**.

Input 489.47 tok/s · output 54.08 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-2"></a>
## Q02 · Trial 2: Exact duplicates

**PASS** · correctness **2/2** · E2E **117.46s** · checks **8/8**.

Input 485.82 tok/s · output 54.57 tok/s · 8 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-1"></a>
## Q03 · Trial 1: HA basement guards

**PASS** · correctness **2/2** · E2E **38.51s** · checks **19/19**.

Input 509.91 tok/s · output 51.83 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-2"></a>
## Q03 · Trial 2: HA basement guards

**PASS** · correctness **2/2** · E2E **38.40s** · checks **19/19**.

Input 589.95 tok/s · output 56.98 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-1"></a>
## Q04 · Trial 1: Frigate configuration

**FAIL** · correctness **0/2** · E2E **105.45s** · checks **2/19**.

Input 572.40 tok/s · output 51.42 tok/s · 3 model requests.

Read the real configuration, then ended with an unrecoverable tool-call decoding error before delivering answer.json. This is a tool protocol/completion failure; absent output does not establish that each missing fact was reasoned incorrectly.

Completion error:

```text
Model output contains an unrecoverable tool call. Previously delivered tool calls must not be executed again on retry.
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

[Exact prompt](../docs/questions.md#q04) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-2"></a>
## Q04 · Trial 2: Frigate configuration

**PASS** · correctness **2/2** · E2E **114.40s** · checks **19/19**.

Input 491.14 tok/s · output 53.46 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q04) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-1"></a>
## Q05 · Trial 1: Drive storage

**PASS** · correctness **2/2** · E2E **56.77s** · checks **10/10**.

Input 454.77 tok/s · output 50.79 tok/s · 7 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-2"></a>
## Q05 · Trial 2: Drive storage

**PASS** · correctness **2/2** · E2E **107.12s** · checks **10/10**.

Input 467.72 tok/s · output 54.24 tok/s · 9 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-1"></a>
## Q06 · Trial 1: Calendar conflicts

**FAIL** · correctness **0/2** · E2E **106.47s** · checks **3/8**.

Input 578.92 tok/s · output 54.03 tok/s · 3 model requests.

Read the actual Calendar data, then hit an unrecoverable tool-call decoding error before delivering answer.json. Missing output, rather than a demonstrated incorrect schedule calculation.

Completion error:

```text
Model output contains an unrecoverable tool call. Previously delivered tool calls must not be executed again on retry.
```

Failed checks:

- answer.json is an object
- correct all_day_count
- correct timed_count
- correct first_five_timed
- correct conflicting_pairs

[Exact prompt](../docs/questions.md#q06) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-2"></a>
## Q06 · Trial 2: Calendar conflicts

**PASS** · correctness **2/2** · E2E **128.43s** · checks **8/8**.

Input 506.77 tok/s · output 54.97 tok/s · 7 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-1"></a>
## Q07 · Trial 1: Backup optimization

**FAIL** · correctness **1/2** · E2E **94.10s** · checks **10/11**.

Input 474.09 tok/s · output 50.38 tok/s · 7 model requests.

The submission failed the checks listed below.

Failed checks:

- complete source-grounded candidate CSV

[Exact prompt](../docs/questions.md#q07) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-2"></a>
## Q07 · Trial 2: Backup optimization

**FAIL** · correctness **1/2** · E2E **122.37s** · checks **8/11**.

Input 508.47 tok/s · output 54.46 tok/s · 6 model requests.

The submission failed the checks listed below.

Failed checks:

- complete source-grounded candidate CSV
- correct candidate_count
- correct candidate_total_bytes

[Exact prompt](../docs/questions.md#q07) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-1"></a>
## Q08 · Trial 1: Camera cross-check

**FAIL** · correctness **1/2** · E2E **130.72s** · checks **10/11**.

Input 422.50 tok/s · output 47.56 tok/s · 9 model requests.

The submission failed the checks listed below.

Failed checks:

- correct automations

[Exact prompt](../docs/questions.md#q08) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-2"></a>
## Q08 · Trial 2: Camera cross-check

**FAIL** · correctness **0/2** · E2E **49.69s** · checks **3/11**.

Input 451.41 tok/s · output 55.18 tok/s · 12 model requests.

No valid answer.json was delivered; missing value checks indicate undelivered work, not independent factual errors.

Completion error:

```text
429: {"message":"Benchmark limit: twelve model requests per task."}
```

Failed checks:

- answer.json is an object
- requested Python program saved
- actual successful Python script invocation
- correct automation_count
- correct automations
- correct referenced_camera_names
- correct unknown_camera_names
- correct unreferenced_frigate_cameras

[Exact prompt](../docs/questions.md#q08) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-1"></a>
## Q09 · Trial 1: Frigate log analysis

**PASS** · correctness **2/2** · E2E **110.55s** · checks **15/15**.

Input 404.45 tok/s · output 47.84 tok/s · 8 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q09) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-2"></a>
## Q09 · Trial 2: Frigate log analysis

**PASS** · correctness **2/2** · E2E **134.04s** · checks **15/15**.

Input 403.00 tok/s · output 50.97 tok/s · 11 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q09) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-1"></a>
## Q10 · Trial 1: Meeting availability

**FAIL** · correctness **0/2** · E2E **163.63s** · checks **4/11**.

Input 383.13 tok/s · output 46.71 tok/s · 12 model requests.

No valid answer.json was delivered; missing value checks indicate undelivered work, not independent factual errors.

Completion error:

```text
429: {"message":"Benchmark limit: twelve model requests per task."}
```

Failed checks:

- answer.json is an object
- actual successful Python script invocation
- correct timezone
- correct meeting_minutes
- correct days
- correct total_free_minutes
- correct first_three_meetings

[Exact prompt](../docs/questions.md#q10) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-2"></a>
## Q10 · Trial 2: Meeting availability

**PASS** · correctness **2/2** · E2E **225.45s** · checks **11/11**.

Input 402.91 tok/s · output 50.10 tok/s · 12 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q10) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.6-35B-A3B-UD-MLX-4bit"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).
