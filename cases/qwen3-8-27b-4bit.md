# Qwen3.8 stock

Exact model ID: `Qwen3.8-27B-4bit`.

[Summary and matrix](../README.md) · [Scoring](../docs/methodology.md#scoring)

## Trial 1 failures

- [Q07: Backup optimization](#q07-trial-1) — FAIL; 1/2; 324.73s.
- [Q10: Meeting availability](#q10-trial-1) — VERIFIED; completion failed; 2/2; 600.71s.

## Trial 2 failures

- [Q07: Backup optimization](#q07-trial-2) — FAIL; 1/2; 465.86s.
- [Q08: Camera cross-check](#q08-trial-2) — FAIL; 1/2; 600.87s.
- [Q09: Frigate log analysis](#q09-trial-2) — FAIL; 1/2; 600.87s.
- [Q10: Meeting availability](#q10-trial-2) — FAIL; 0/2; 600.95s.

## Trial 3 failures

- [Q07: Backup optimization](#q07-trial-3) — FAIL; 1/2; 326.85s.
- [Q08: Camera cross-check](#q08-trial-3) — FAIL; 0/2; 600.57s.
- [Q09: Frigate log analysis](#q09-trial-3) — FAIL; 0/2; 600.57s.

<a id="q01-trial-1"></a>
## Q01 · Trial 1: Largest files

**PASS** · correctness **2/2** · E2E **124.49s** · checks **7/7**.

Input 73.61 tok/s · output 14.21 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q01-trial-2"></a>
## Q01 · Trial 2: Largest files

**PASS** · correctness **2/2** · E2E **128.62s** · checks **7/7**.

Input 66.83 tok/s · output 9.91 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q01-trial-3"></a>
## Q01 · Trial 3: Largest files

**PASS** · correctness **2/2** · E2E **137.91s** · checks **7/7**.

Input 56.75 tok/s · output 12.84 tok/s · 5 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-1"></a>
## Q02 · Trial 1: Exact duplicates

**PASS** · correctness **2/2** · E2E **148.82s** · checks **8/8**.

Input 69.60 tok/s · output 13.85 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-2"></a>
## Q02 · Trial 2: Exact duplicates

**PASS** · correctness **2/2** · E2E **223.81s** · checks **8/8**.

Input 47.39 tok/s · output 9.62 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-3"></a>
## Q02 · Trial 3: Exact duplicates

**PASS** · correctness **2/2** · E2E **176.35s** · checks **8/8**.

Input 57.21 tok/s · output 12.14 tok/s · 4 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q02) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-1"></a>
## Q03 · Trial 1: HA basement guards

**PASS** · correctness **2/2** · E2E **159.97s** · checks **19/19**.

Input 64.81 tok/s · output 13.98 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-2"></a>
## Q03 · Trial 2: HA basement guards

**PASS** · correctness **2/2** · E2E **248.42s** · checks **19/19**.

Input 44.51 tok/s · output 9.56 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-3"></a>
## Q03 · Trial 3: HA basement guards

**PASS** · correctness **2/2** · E2E **208.86s** · checks **19/19**.

Input 54.33 tok/s · output 11.81 tok/s · 6 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-1"></a>
## Q04 · Trial 1: Frigate configuration

**PASS** · correctness **2/2** · E2E **360.29s** · checks **19/19**.

Input 68.50 tok/s · output 12.90 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q04) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-2"></a>
## Q04 · Trial 2: Frigate configuration

**PASS** · correctness **2/2** · E2E **490.35s** · checks **19/19**.

Input 47.95 tok/s · output 9.23 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q04) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-3"></a>
## Q04 · Trial 3: Frigate configuration

**PASS** · correctness **2/2** · E2E **437.27s** · checks **19/19**.

Input 53.63 tok/s · output 11.69 tok/s · 6 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q04) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-1"></a>
## Q05 · Trial 1: Drive storage

**PASS** · correctness **2/2** · E2E **137.34s** · checks **10/10**.

Input 72.18 tok/s · output 14.21 tok/s · 4 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-2"></a>
## Q05 · Trial 2: Drive storage

**PASS** · correctness **2/2** · E2E **238.79s** · checks **10/10**.

Input 47.81 tok/s · output 9.59 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-3"></a>
## Q05 · Trial 3: Drive storage

**PASS** · correctness **2/2** · E2E **154.12s** · checks **10/10**.

Input 56.66 tok/s · output 12.18 tok/s · 5 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-1"></a>
## Q06 · Trial 1: Calendar conflicts

**PASS** · correctness **2/2** · E2E **238.85s** · checks **8/8**.

Input 69.49 tok/s · output 13.99 tok/s · 8 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-2"></a>
## Q06 · Trial 2: Calendar conflicts

**PASS** · correctness **2/2** · E2E **321.94s** · checks **8/8**.

Input 48.43 tok/s · output 9.60 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-3"></a>
## Q06 · Trial 3: Calendar conflicts

**PASS** · correctness **2/2** · E2E **196.73s** · checks **8/8**.

Input 55.46 tok/s · output 11.92 tok/s · 6 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-1"></a>
## Q07 · Trial 1: Backup optimization

**FAIL** · correctness **1/2** · E2E **324.73s** · checks **8/11**.

Input 66.16 tok/s · output 12.74 tok/s · 7 model requests.

The exact optimal subset and chosen/unused byte counts were correct. Reported the full57-file eligible population in the candidate CSV and metadata instead of the16-file optimization candidate set; 8/11checks passed.

Failed checks:

- complete source-grounded candidate CSV
- correct candidate_count
- correct candidate_total_bytes

[Exact prompt](../docs/questions.md#q07) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-2"></a>
## Q07 · Trial 2: Backup optimization

**FAIL** · correctness **1/2** · E2E **465.86s** · checks **8/11**.

Input 48.58 tok/s · output 9.40 tok/s · 6 model requests.

The submission failed the checks listed below.

Failed checks:

- complete source-grounded candidate CSV
- correct candidate_count
- correct candidate_total_bytes

[Exact prompt](../docs/questions.md#q07) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-3"></a>
## Q07 · Trial 3: Backup optimization

**FAIL** · correctness **1/2** · E2E **326.85s** · checks **8/11**.

Input 54.98 tok/s · output 11.75 tok/s · 6 model requests.

The required complete CSV did not match its source-grounded contract. candidate_count: incorrect value. candidate_total_bytes: incorrect value.

Failed checks:

- complete source-grounded candidate CSV
- correct candidate_count
- correct candidate_total_bytes

[Exact prompt](../docs/questions.md#q07) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-1"></a>
## Q08 · Trial 1: Camera cross-check

**PASS** · correctness **2/2** · E2E **368.43s** · checks **11/11**.

Input 62.86 tok/s · output 12.53 tok/s · 8 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q08) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-2"></a>
## Q08 · Trial 2: Camera cross-check

**FAIL** · correctness **1/2** · E2E **600.87s** · checks **10/11**.

Input 46.59 tok/s · output 9.45 tok/s · 10 model requests.

The submission failed the checks listed below.

Completion error:

```text
Task exceeded 600-second wall limit
```

Failed checks:

- correct automations

[Exact prompt](../docs/questions.md#q08) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-3"></a>
## Q08 · Trial 3: Camera cross-check

**FAIL** · correctness **0/2** · E2E **600.57s** · checks **3/11**.

Input 53.61 tok/s · output 11.32 tok/s · 10 model requests.

No valid required answer.json was delivered. Missing value checks are undelivered output, not independently demonstrated factual errors. Task exceeded 600-second wall limit

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

[Exact prompt](../docs/questions.md#q08) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-1"></a>
## Q09 · Trial 1: Frigate log analysis

**PASS** · correctness **2/2** · E2E **409.85s** · checks **15/15**.

Input 62.97 tok/s · output 12.52 tok/s · 7 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q09) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-2"></a>
## Q09 · Trial 2: Frigate log analysis

**FAIL** · correctness **1/2** · E2E **600.87s** · checks **14/15**.

Input 49.79 tok/s · output 9.60 tok/s · 10 model requests.

The submission failed the checks listed below.

Completion error:

```text
Task exceeded 600-second wall limit
```

Failed checks:

- correct busiest_error_minute

[Exact prompt](../docs/questions.md#q09) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-3"></a>
## Q09 · Trial 3: Frigate log analysis

**FAIL** · correctness **0/2** · E2E **600.57s** · checks **2/15**.

Input 54.11 tok/s · output 11.21 tok/s · 4 model requests.

No valid required answer.json was delivered. Missing value checks are undelivered output, not independently demonstrated factual errors. Task exceeded 600-second wall limit

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

[Exact prompt](../docs/questions.md#q09) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-1"></a>
## Q10 · Trial 1: Meeting availability

**VERIFIED; completion failed** · correctness **2/2** · E2E **600.71s** · checks **11/11**.

Input 63.17 tok/s · output 12.44 tok/s · 9 model requests.

All11required source/program/artifact/value checks passed. The Calendar plan was correct, but Pi had not settled at the common600-second wall limit. Verified success, not a full pass.

Completion error:

```text
Task exceeded 600-second wall limit
```

[Exact prompt](../docs/questions.md#q10) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-2"></a>
## Q10 · Trial 2: Meeting availability

**FAIL** · correctness **0/2** · E2E **600.95s** · checks **4/11**.

Input 50.85 tok/s · output 9.50 tok/s · 7 model requests.

No valid answer.json was delivered; missing value checks indicate undelivered work, not independent factual errors.

Completion error:

```text
Task exceeded 600-second wall limit
```

Failed checks:

- answer.json is an object
- actual successful Python script invocation
- correct timezone
- correct meeting_minutes
- correct days
- correct total_free_minutes
- correct first_three_meetings

[Exact prompt](../docs/questions.md#q10) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-3"></a>
## Q10 · Trial 3: Meeting availability

**PASS** · correctness **2/2** · E2E **535.16s** · checks **11/11**.

Input 53.19 tok/s · output 11.22 tok/s · 7 model requests.

All verification checks passed with normal completion.

[Exact prompt](../docs/questions.md#q10) · [Full scored records: third10.jsonl.gz](../data/daily/third10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Qwen3.8-27B-4bit"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).
