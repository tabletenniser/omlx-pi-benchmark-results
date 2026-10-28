# Ornith 6-bit

Exact model ID: `Ornith-1.5-35B-A3B-MLX-6bit`.

[Summary and matrix](../README.md) · [Scoring](../docs/methodology.md#scoring)

[Recorded Hugging Face model](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B-MLX-6bit)

## Trial 1 failures

- [Q02: Exact duplicates](#q02-trial-1) — FAIL; 1/2; 51.54s.
- [Q04: Frigate configuration](#q04-trial-1) — FAIL; 1/2; 108.20s.
- [Q07: Backup optimization](#q07-trial-1) — FAIL; 1/2; 55.51s.
- [Q08: Camera cross-check](#q08-trial-1) — FAIL; 1/2; 158.78s.
- [Q09: Frigate log analysis](#q09-trial-1) — FAIL; 1/2; 86.91s.
- [Q10: Meeting availability](#q10-trial-1) — FAIL; 1/2; 248.81s.

## Trial 2 failures

- [Q04: Frigate configuration](#q04-trial-2) — FAIL; 1/2; 89.06s.
- [Q07: Backup optimization](#q07-trial-2) — FAIL; 0/2; 145.81s.
- [Q08: Camera cross-check](#q08-trial-2) — FAIL; 0/2; 92.09s.
- [Q09: Frigate log analysis](#q09-trial-2) — FAIL; 1/2; 83.94s.
- [Q10: Meeting availability](#q10-trial-2) — FAIL; 1/2; 213.75s.

## Trial 3 failures

- [Q04: Frigate configuration](#q04-trial-3) — FAIL; 1/2; 163.94s.
- [Q07: Backup optimization](#q07-trial-3) — FAIL; 1/2; 154.99s.
- [Q08: Camera cross-check](#q08-trial-3) — FAIL; 0/2; 161.04s.
- [Q09: Frigate log analysis](#q09-trial-3) — FAIL; 1/2; 68.87s.
- [Q10: Meeting availability](#q10-trial-3) — FAIL; 0/2; 199.64s.

<a id="q01-trial-1"></a>
## Q01 · Trial 1: Largest files

**PASS** · correctness **2/2** · E2E **53.57s** · checks **7/7**.

Input 501.48 tok/s · output 37.20 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q01-trial-2"></a>
## Q01 · Trial 2: Largest files

**PASS** · correctness **2/2** · E2E **25.29s** · checks **7/7**.

Input 567.47 tok/s · output 38.85 tok/s · 3 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q01-trial-3"></a>
## Q01 · Trial 3: Largest files

**PASS** · correctness **2/2** · E2E **60.92s** · checks **7/7**.

Input 364.20 tok/s · output 29.68 tok/s · 7 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-1"></a>
## Q02 · Trial 1: Exact duplicates

**FAIL** · correctness **1/2** · E2E **51.54s** · checks **7/8**.

Input 489.95 tok/s · output 36.84 tok/s · 6 model requests.

All 42 SHA-256 rows and byte counts were correct. duplicate_groups was numeric 0 instead of the required empty array []. This is a JSON-type contract failure, not a missed duplicate.

Failed checks:

- correct duplicate_groups

[Exact prompt](../docs/questions.md#q02) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-2"></a>
## Q02 · Trial 2: Exact duplicates

**PASS** · correctness **2/2** · E2E **102.07s** · checks **8/8**.

Input 468.95 tok/s · output 39.94 tok/s · 10 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-3"></a>
## Q02 · Trial 3: Exact duplicates

**PASS** · correctness **2/2** · E2E **105.21s** · checks **8/8**.

Input 360.89 tok/s · output 31.65 tok/s · 9 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-1"></a>
## Q03 · Trial 1: HA basement guards

**PASS** · correctness **2/2** · E2E **45.57s** · checks **19/19**.

Input 442.76 tok/s · output 34.54 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-2"></a>
## Q03 · Trial 2: HA basement guards

**PASS** · correctness **2/2** · E2E **49.51s** · checks **19/19**.

Input 460.09 tok/s · output 38.55 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-3"></a>
## Q03 · Trial 3: HA basement guards

**PASS** · correctness **2/2** · E2E **47.56s** · checks **19/19**.

Input 387.67 tok/s · output 32.12 tok/s · 4 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-1"></a>
## Q04 · Trial 1: Frigate configuration

**FAIL** · correctness **1/2** · E2E **108.20s** · checks **18/19**.

Input 400.28 tok/s · output 35.53 tok/s · 5 model requests.

Returned detector instance name apple_silicon instead of the configured type zmq. The other 18 checks passed.

Failed checks:

- correct detector_types

[Exact prompt](../docs/questions.md#q04) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-2"></a>
## Q04 · Trial 2: Frigate configuration

**FAIL** · correctness **1/2** · E2E **89.06s** · checks **18/19**.

Input 505.18 tok/s · output 38.50 tok/s · 5 model requests.

The submission failed the checks listed below.

Failed checks:

- correct detector_types

[Exact prompt](../docs/questions.md#q04) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-3"></a>
## Q04 · Trial 3: Frigate configuration

**FAIL** · correctness **1/2** · E2E **163.94s** · checks **18/19**.

Input 345.74 tok/s · output 30.56 tok/s · 9 model requests.

detector_types: one or more nested values/order differ; see exact expected/actual evidence.

Failed checks:

- correct detector_types

[Exact prompt](../docs/questions.md#q04) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-1"></a>
## Q05 · Trial 1: Drive storage

**PASS** · correctness **2/2** · E2E **38.43s** · checks **10/10**.

Input 501.94 tok/s · output 36.40 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-2"></a>
## Q05 · Trial 2: Drive storage

**PASS** · correctness **2/2** · E2E **53.60s** · checks **10/10**.

Input 463.70 tok/s · output 40.47 tok/s · 8 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-3"></a>
## Q05 · Trial 3: Drive storage

**PASS** · correctness **2/2** · E2E **49.70s** · checks **10/10**.

Input 402.81 tok/s · output 31.65 tok/s · 6 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-1"></a>
## Q06 · Trial 1: Calendar conflicts

**PASS** · correctness **2/2** · E2E **140.49s** · checks **8/8**.

Input 397.21 tok/s · output 36.33 tok/s · 10 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-2"></a>
## Q06 · Trial 2: Calendar conflicts

**PASS** · correctness **2/2** · E2E **65.72s** · checks **8/8**.

Input 492.02 tok/s · output 40.03 tok/s · 9 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-3"></a>
## Q06 · Trial 3: Calendar conflicts

**PASS** · correctness **2/2** · E2E **104.19s** · checks **8/8**.

Input 385.19 tok/s · output 31.53 tok/s · 6 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-1"></a>
## Q07 · Trial 1: Backup optimization

**FAIL** · correctness **1/2** · E2E **55.51s** · checks **10/11**.

Input 524.62 tok/s · output 39.15 tok/s · 5 model requests.

The optimal subset and all six answer fields are correct. The CSV lists all 56 eligible files rather than the 16 candidates used in the optimization. Scope mismatch in the required inventory; the backup calculation itself is correct.

Failed checks:

- complete source-grounded candidate CSV

[Exact prompt](../docs/questions.md#q07) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-2"></a>
## Q07 · Trial 2: Backup optimization

**FAIL** · correctness **0/2** · E2E **145.81s** · checks **2/11**.

Input 401.49 tok/s · output 37.72 tok/s · 12 model requests.

No valid answer.json was delivered; missing value checks indicate undelivered work, not independent factual errors.

Completion error:

```text
429: {"message":"Benchmark limit: twelve model requests per task."}
```

Failed checks:

- answer.json is an object
- actual successful Python script invocation
- complete source-grounded candidate CSV
- correct budget_bytes
- correct candidate_count
- correct candidate_total_bytes
- correct chosen_paths
- correct chosen_bytes
- correct unused_bytes

[Exact prompt](../docs/questions.md#q07) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-3"></a>
## Q07 · Trial 3: Backup optimization

**FAIL** · correctness **1/2** · E2E **154.99s** · checks **10/11**.

Input 367.67 tok/s · output 33.46 tok/s · 10 model requests.

The required complete CSV did not match its source-grounded contract.

Failed checks:

- complete source-grounded candidate CSV

[Exact prompt](../docs/questions.md#q07) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-1"></a>
## Q08 · Trial 1: Camera cross-check

**FAIL** · correctness **1/2** · E2E **158.78s** · checks **7/11**.

Input 449.25 tok/s · output 37.93 tok/s · 12 model requests.

Read both actual sources and ran the requested Python program. Its target extraction helper handles strings/lists but not the actual target mapping containing entity_id, so it selected zero automations instead of four. It also exhausted the 12-request limit. Other resulting empty reference lists are consequences of the same selection bug.

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

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-2"></a>
## Q08 · Trial 2: Camera cross-check

**FAIL** · correctness **0/2** · E2E **92.09s** · checks **3/11**.

Input 417.25 tok/s · output 35.28 tok/s · 12 model requests.

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

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-3"></a>
## Q08 · Trial 3: Camera cross-check

**FAIL** · correctness **0/2** · E2E **161.04s** · checks **3/11**.

Input 375.56 tok/s · output 30.64 tok/s · 12 model requests.

No valid required answer.json was delivered. Missing value checks are undelivered output, not independently demonstrated factual errors. 429: {"message":"Benchmark limit: twelve model requests per task."}

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

[Exact prompt](../docs/questions.md#q08) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-1"></a>
## Q09 · Trial 1: Frigate log analysis

**FAIL** · correctness **1/2** · E2E **86.91s** · checks **14/15**.

Input 490.99 tok/s · output 37.55 tok/s · 7 model requests.

Fourteen of fifteen checks passed, including all full-log counts and the component CSV. Returned busiest_error_minute as a timestamp string (with a space instead of T) rather than the requested minute_utc/error_count object. Other log-analysis values were correct.

Failed checks:

- correct busiest_error_minute

[Exact prompt](../docs/questions.md#q09) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-2"></a>
## Q09 · Trial 2: Frigate log analysis

**FAIL** · correctness **1/2** · E2E **83.94s** · checks **14/15**.

Input 451.85 tok/s · output 36.44 tok/s · 7 model requests.

The submission failed the checks listed below.

Failed checks:

- correct busiest_error_minute

[Exact prompt](../docs/questions.md#q09) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-3"></a>
## Q09 · Trial 3: Frigate log analysis

**FAIL** · correctness **1/2** · E2E **68.87s** · checks **14/15**.

Input 418.71 tok/s · output 30.81 tok/s · 5 model requests.

busiest_error_minute: one or more nested values/order differ; see exact expected/actual evidence.

Failed checks:

- correct busiest_error_minute

[Exact prompt](../docs/questions.md#q09) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-1"></a>
## Q10 · Trial 1: Meeting availability

**FAIL** · correctness **1/2** · E2E **248.81s** · checks **9/11**.

Input 403.88 tok/s · output 36.00 tok/s · 12 model requests.

Daily busy/free minute totals and total1710 free minutes were correct, but local workday starts were labeled as UTC without conversion (09:00Z rather than16:00Z on the first date). Free-interval timestamps and proposed meetings were wrong. It also exhausted the12-request limit.

Completion error:

```text
429: {"message":"Benchmark limit: twelve model requests per task."}
```

Failed checks:

- correct days
- correct first_three_meetings

[Exact prompt](../docs/questions.md#q10) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-2"></a>
## Q10 · Trial 2: Meeting availability

**FAIL** · correctness **1/2** · E2E **213.75s** · checks **8/11**.

Input 419.94 tok/s · output 38.64 tok/s · 12 model requests.

The submission failed the checks listed below.

Completion error:

```text
429: {"message":"Benchmark limit: twelve model requests per task."}
```

Failed checks:

- correct days
- correct total_free_minutes
- correct first_three_meetings

[Exact prompt](../docs/questions.md#q10) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-3"></a>
## Q10 · Trial 3: Meeting availability

**FAIL** · correctness **0/2** · E2E **199.64s** · checks **4/11**.

Input 369.69 tok/s · output 31.47 tok/s · 12 model requests.

No valid required answer.json was delivered. Missing value checks are undelivered output, not independently demonstrated factual errors. 429: {"message":"Benchmark limit: twelve model requests per task."}

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

[Exact prompt](../docs/questions.md#q10) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-MLX-6bit"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).
