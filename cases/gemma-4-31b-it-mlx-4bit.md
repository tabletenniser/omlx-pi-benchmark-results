# Gemma 4

Exact model ID: `gemma-4-31B-it-MLX-4bit`.

[Summary and matrix](../README.md) · [Scoring](../docs/methodology.md#scoring)

[Recorded Hugging Face model](https://huggingface.co/lmstudio-community/gemma-4-31B-it-MLX-4bit)

## Trial 1 failures

- [Q01: Largest files](#q01-trial-1) — FAIL; 1/2; 539.50s.
- [Q04: Frigate configuration](#q04-trial-1) — FAIL; 0/2; 600.89s.
- [Q06: Calendar conflicts](#q06-trial-1) — VERIFIED; completion failed; 2/2; 600.06s.
- [Q07: Backup optimization](#q07-trial-1) — FAIL; 1/2; 502.65s.
- [Q08: Camera cross-check](#q08-trial-1) — FAIL; 0/2; 600.54s.
- [Q09: Frigate log analysis](#q09-trial-1) — FAIL; 0/2; 600.78s.
- [Q10: Meeting availability](#q10-trial-1) — FAIL; 0/2; 600.75s.

## Trial 2 failures

- [Q04: Frigate configuration](#q04-trial-2) — FAIL; 0/2; 601.01s.
- [Q06: Calendar conflicts](#q06-trial-2) — VERIFIED; completion failed; 2/2; 601.03s.
- [Q07: Backup optimization](#q07-trial-2) — FAIL; 1/2; 510.86s.
- [Q08: Camera cross-check](#q08-trial-2) — FAIL; 0/2; 600.94s.
- [Q09: Frigate log analysis](#q09-trial-2) — FAIL; 0/2; 600.17s.
- [Q10: Meeting availability](#q10-trial-2) — FAIL; 0/2; 600.95s.

<a id="q01-trial-1"></a>
## Q01 · Trial 1: Largest files

**FAIL** · correctness **1/2** · E2E **539.50s** · checks **6/7**.

Input 55.41 tok/s · output 9.69 tok/s · 6 model requests.

The top ten, file count, total bytes and sizes were correct. The 61-row inventory CSV mistyped one filename, dropping the middle -04 from a snapshot timestamp (03-04-14 became 03-14). Exact source-path completeness therefore failed; the other 6 checks passed.

Failed checks:

- complete source-grounded inventory.csv

[Exact prompt](../docs/questions.md#q01) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q01-trial-2"></a>
## Q01 · Trial 2: Largest files

**PASS** · correctness **2/2** · E2E **417.54s** · checks **7/7**.

Input 43.19 tok/s · output 7.65 tok/s · 7 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-1"></a>
## Q02 · Trial 1: Exact duplicates

**PASS** · correctness **2/2** · E2E **431.04s** · checks **8/8**.

Input 54.30 tok/s · output 9.53 tok/s · 8 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-2"></a>
## Q02 · Trial 2: Exact duplicates

**PASS** · correctness **2/2** · E2E **559.56s** · checks **8/8**.

Input 42.26 tok/s · output 7.22 tok/s · 7 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-1"></a>
## Q03 · Trial 1: HA basement guards

**PASS** · correctness **2/2** · E2E **378.06s** · checks **19/19**.

Input 56.70 tok/s · output 9.71 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-2"></a>
## Q03 · Trial 2: HA basement guards

**PASS** · correctness **2/2** · E2E **506.63s** · checks **19/19**.

Input 41.01 tok/s · output 6.85 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-1"></a>
## Q04 · Trial 1: Frigate configuration

**FAIL** · correctness **0/2** · E2E **600.89s** · checks **2/19**.

Input 57.88 tok/s · output 9.35 tok/s · 5 model requests.

Read the actual configuration but reached the 600-second limit before delivering answer.json. The missing fields reflect undelivered output, not 17 independently demonstrated factual errors.

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

[Exact prompt](../docs/questions.md#q04) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-2"></a>
## Q04 · Trial 2: Frigate configuration

**FAIL** · correctness **0/2** · E2E **601.01s** · checks **2/19**.

Input 42.03 tok/s · output 6.86 tok/s · 4 model requests.

No valid answer.json was delivered; missing value checks indicate undelivered work, not independent factual errors.

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

[Exact prompt](../docs/questions.md#q04) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-1"></a>
## Q05 · Trial 1: Drive storage

**PASS** · correctness **2/2** · E2E **301.70s** · checks **10/10**.

Input 56.16 tok/s · output 10.12 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-2"></a>
## Q05 · Trial 2: Drive storage

**PASS** · correctness **2/2** · E2E **417.05s** · checks **10/10**.

Input 40.66 tok/s · output 6.94 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-1"></a>
## Q06 · Trial 1: Calendar conflicts

**VERIFIED; completion failed** · correctness **2/2** · E2E **600.06s** · checks **8/8**.

Input 54.88 tok/s · output 9.40 tok/s · 8 model requests.

Saved correct Calendar results and passed all 8 checks, but reached the common 600-second limit before normal Pi completion. Counted as verified, not a full pass.

Completion error:

```text
Task exceeded 600-second wall limit
```

[Exact prompt](../docs/questions.md#q06) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-2"></a>
## Q06 · Trial 2: Calendar conflicts

**VERIFIED; completion failed** · correctness **2/2** · E2E **601.03s** · checks **8/8**.

Input 43.39 tok/s · output 7.31 tok/s · 7 model requests.

All verification checks passed.

Completion error:

```text
Task exceeded 600-second wall limit
```

[Exact prompt](../docs/questions.md#q06) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-1"></a>
## Q07 · Trial 1: Backup optimization

**FAIL** · correctness **1/2** · E2E **502.65s** · checks **8/11**.

Input 56.82 tok/s · output 10.08 tok/s · 8 model requests.

The submission failed the checks listed below.

Failed checks:

- complete source-grounded candidate CSV
- correct candidate_count
- correct candidate_total_bytes

[Exact prompt](../docs/questions.md#q07) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-2"></a>
## Q07 · Trial 2: Backup optimization

**FAIL** · correctness **1/2** · E2E **510.86s** · checks **10/11**.

Input 44.96 tok/s · output 8.26 tok/s · 9 model requests.

The submission failed the checks listed below.

Failed checks:

- complete source-grounded candidate CSV

[Exact prompt](../docs/questions.md#q07) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-1"></a>
## Q08 · Trial 1: Camera cross-check

**FAIL** · correctness **0/2** · E2E **600.54s** · checks **3/11**.

Input 63.47 tok/s · output 10.13 tok/s · 2 model requests.

No valid answer.json was delivered; missing value checks indicate undelivered work, not independent factual errors.

Completion error:

```text
Task exceeded 600-second wall limit
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

[Exact prompt](../docs/questions.md#q08) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-2"></a>
## Q08 · Trial 2: Camera cross-check

**FAIL** · correctness **0/2** · E2E **600.94s** · checks **3/11**.

Input 47.16 tok/s · output 7.45 tok/s · 2 model requests.

No valid answer.json was delivered; missing value checks indicate undelivered work, not independent factual errors.

Completion error:

```text
Task exceeded 600-second wall limit
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

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-1"></a>
## Q09 · Trial 1: Frigate log analysis

**FAIL** · correctness **0/2** · E2E **600.78s** · checks **2/15**.

Input 47.38 tok/s · output 9.64 tok/s · 4 model requests.

No valid answer.json was delivered; missing value checks indicate undelivered work, not independent factual errors.

Completion error:

```text
Task exceeded 600-second wall limit
```

Failed checks:

- answer.json is an object
- requested Python program saved
- actual successful Python script invocation
- complete error-component CSV
- correct total_lines
- correct parsed_lines
- correct unparsed_lines
- correct level_counts
- correct top_error_components
- correct first_error_utc
- correct last_error_utc
- correct busiest_error_minute
- correct crashes_by_camera

[Exact prompt](../docs/questions.md#q09) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-2"></a>
## Q09 · Trial 2: Frigate log analysis

**FAIL** · correctness **0/2** · E2E **600.17s** · checks **2/15**.

Input 36.33 tok/s · output 6.92 tok/s · 3 model requests.

No valid answer.json was delivered; missing value checks indicate undelivered work, not independent factual errors.

Completion error:

```text
Task exceeded 600-second wall limit
```

Failed checks:

- answer.json is an object
- requested Python program saved
- actual successful Python script invocation
- complete error-component CSV
- correct total_lines
- correct parsed_lines
- correct unparsed_lines
- correct level_counts
- correct top_error_components
- correct first_error_utc
- correct last_error_utc
- correct busiest_error_minute
- correct crashes_by_camera

[Exact prompt](../docs/questions.md#q09) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-1"></a>
## Q10 · Trial 1: Meeting availability

**FAIL** · correctness **0/2** · E2E **600.75s** · checks **3/11**.

Input 56.21 tok/s · output 9.64 tok/s · 7 model requests.

No valid answer.json was delivered; missing value checks indicate undelivered work, not independent factual errors.

Completion error:

```text
Task exceeded 600-second wall limit
```

Failed checks:

- answer.json is an object
- requested Python program saved
- actual successful Python script invocation
- correct timezone
- correct meeting_minutes
- correct days
- correct total_free_minutes
- correct first_three_meetings

[Exact prompt](../docs/questions.md#q10) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-2"></a>
## Q10 · Trial 2: Meeting availability

**FAIL** · correctness **0/2** · E2E **600.95s** · checks **3/11**.

Input 36.63 tok/s · output 6.67 tok/s · 6 model requests.

No valid answer.json was delivered; missing value checks indicate undelivered work, not independent factual errors.

Completion error:

```text
Task exceeded 600-second wall limit
```

Failed checks:

- answer.json is an object
- requested Python program saved
- actual successful Python script invocation
- correct timezone
- correct meeting_minutes
- correct days
- correct total_free_minutes
- correct first_three_meetings

[Exact prompt](../docs/questions.md#q10) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "gemma-4-31B-it-MLX-4bit"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).
