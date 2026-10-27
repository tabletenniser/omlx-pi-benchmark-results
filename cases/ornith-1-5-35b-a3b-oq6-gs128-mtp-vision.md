# Ruka Ornith oQ6

Exact model ID: `Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision`.

[Summary and matrix](../README.md) · [Scoring](../docs/methodology.md#scoring)

[Recorded Hugging Face model](https://huggingface.co/RukaRat/Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision)

## Trial 1 failures

- [Q02: Exact duplicates](#q02-trial-1) — FAIL; 0/2; 54.67s.
- [Q04: Frigate configuration](#q04-trial-1) — FAIL; 1/2; 101.51s.
- [Q07: Backup optimization](#q07-trial-1) — FAIL; 1/2; 68.82s.
- [Q08: Camera cross-check](#q08-trial-1) — VERIFIED; completion failed; 2/2; 106.25s.
- [Q09: Frigate log analysis](#q09-trial-1) — FAIL; 1/2; 97.39s.
- [Q10: Meeting availability](#q10-trial-1) — FAIL; 0/2; 96.14s.

## Trial 2 failures

- [Q02: Exact duplicates](#q02-trial-2) — FAIL; 1/2; 58.65s.
- [Q03: HA basement guards](#q03-trial-2) — FAIL; 1/2; 33.39s.
- [Q04: Frigate configuration](#q04-trial-2) — FAIL; 1/2; 74.87s.
- [Q08: Camera cross-check](#q08-trial-2) — FAIL; 0/2; 80.95s.

<a id="q01-trial-1"></a>
## Q01 · Trial 1: Largest files

**PASS** · correctness **2/2** · E2E **36.48s** · checks **7/7**.

Input 607.60 tok/s · output 54.54 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q01-trial-2"></a>
## Q01 · Trial 2: Largest files

**PASS** · correctness **2/2** · E2E **43.52s** · checks **7/7**.

Input 605.07 tok/s · output 53.69 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q01) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "mac_large_files"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-1"></a>
## Q02 · Trial 1: Exact duplicates

**FAIL** · correctness **0/2** · E2E **54.67s** · checks **2/8**.

Input 622.79 tok/s · output 65.12 tok/s · 6 model requests.

Actually executed the hashing program and produced correct JSON and all 42 hash rows under .tmp/dedup. The required answer.json and checksums.csv were missing from the initial task directory. The delivered-artifact verdict remains a failure; the computation itself was correct.

Failed checks:

- answer.json is an object
- complete source-grounded checksums.csv
- correct files_hashed
- correct total_bytes_hashed
- correct duplicate_groups
- correct reclaimable_bytes

[Exact prompt](../docs/questions.md#q02) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q02-trial-2"></a>
## Q02 · Trial 2: Exact duplicates

**FAIL** · correctness **1/2** · E2E **58.65s** · checks **7/8**.

Input 650.52 tok/s · output 62.29 tok/s · 8 model requests.

The submission failed the checks listed below.

Failed checks:

- correct duplicate_groups

[Exact prompt](../docs/questions.md#q02) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "mac_duplicates"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-1"></a>
## Q03 · Trial 1: HA basement guards

**PASS** · correctness **2/2** · E2E **33.45s** · checks **19/19**.

Input 642.39 tok/s · output 55.67 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q03) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q03-trial-2"></a>
## Q03 · Trial 2: HA basement guards

**FAIL** · correctness **1/2** · E2E **33.39s** · checks **18/19**.

Input 669.20 tok/s · output 57.31 tok/s · 5 model requests.

The submission failed the checks listed below.

Failed checks:

- correct idle_sensors

[Exact prompt](../docs/questions.md#q03) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "ha_basement_idle"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-1"></a>
## Q04 · Trial 1: Frigate configuration

**FAIL** · correctness **1/2** · E2E **101.51s** · checks **18/19**.

Input 581.21 tok/s · output 50.13 tok/s · 7 model requests.

Returned detector instance name apple_silicon instead of configured type zmq. The other 18 checks passed.

Failed checks:

- correct detector_types

[Exact prompt](../docs/questions.md#q04) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q04-trial-2"></a>
## Q04 · Trial 2: Frigate configuration

**FAIL** · correctness **1/2** · E2E **74.87s** · checks **18/19**.

Input 610.64 tok/s · output 47.63 tok/s · 6 model requests.

The submission failed the checks listed below.

Failed checks:

- correct detector_types

[Exact prompt](../docs/questions.md#q04) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "frigate_recording"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-1"></a>
## Q05 · Trial 1: Drive storage

**PASS** · correctness **2/2** · E2E **32.39s** · checks **10/10**.

Input 578.01 tok/s · output 51.84 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q05-trial-2"></a>
## Q05 · Trial 2: Drive storage

**PASS** · correctness **2/2** · E2E **32.37s** · checks **10/10**.

Input 561.24 tok/s · output 52.44 tok/s · 6 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q05) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "gws_drive_storage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-1"></a>
## Q06 · Trial 1: Calendar conflicts

**PASS** · correctness **2/2** · E2E **75.95s** · checks **8/8**.

Input 546.85 tok/s · output 52.73 tok/s · 8 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: original6.jsonl.gz](../data/daily/original6.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q06-trial-2"></a>
## Q06 · Trial 2: Calendar conflicts

**PASS** · correctness **2/2** · E2E **63.75s** · checks **8/8**.

Input 649.01 tok/s · output 54.96 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q06) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "gws_calendar_conflicts"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-1"></a>
## Q07 · Trial 1: Backup optimization

**FAIL** · correctness **1/2** · E2E **68.82s** · checks **10/11**.

Input 550.24 tok/s · output 48.92 tok/s · 6 model requests.

The submission failed the checks listed below.

Failed checks:

- complete source-grounded candidate CSV

[Exact prompt](../docs/questions.md#q07) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q07-trial-2"></a>
## Q07 · Trial 2: Backup optimization

**PASS** · correctness **2/2** · E2E **54.59s** · checks **11/11**.

Input 610.96 tok/s · output 50.00 tok/s · 5 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q07) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "mac_backup_budget"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-1"></a>
## Q08 · Trial 1: Camera cross-check

**VERIFIED; completion failed** · correctness **2/2** · E2E **106.25s** · checks **11/11**.

Input 472.28 tok/s · output 47.37 tok/s · 12 model requests.

All verification checks passed.

Completion error:

```text
429: {"message":"Benchmark limit: twelve model requests per task."}
```

[Exact prompt](../docs/questions.md#q08) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q08-trial-2"></a>
## Q08 · Trial 2: Camera cross-check

**FAIL** · correctness **0/2** · E2E **80.95s** · checks **3/11**.

Input 524.97 tok/s · output 51.81 tok/s · 12 model requests.

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

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "home_camera_crosscheck"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-1"></a>
## Q09 · Trial 1: Frigate log analysis

**FAIL** · correctness **1/2** · E2E **97.39s** · checks **14/15**.

Input 438.06 tok/s · output 46.93 tok/s · 12 model requests.

The submission failed the checks listed below.

Completion error:

```text
429: {"message":"Benchmark limit: twelve model requests per task."}
```

Failed checks:

- correct busiest_error_minute

[Exact prompt](../docs/questions.md#q09) · [Full scored records: added4.jsonl.gz](../data/daily/added4.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q09-trial-2"></a>
## Q09 · Trial 2: Frigate log analysis

**PASS** · correctness **2/2** · E2E **83.34s** · checks **15/15**.

Input 523.66 tok/s · output 51.14 tok/s · 8 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q09) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "frigate_log_triage"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-1"></a>
## Q10 · Trial 1: Meeting availability

**FAIL** · correctness **0/2** · E2E **96.14s** · checks **4/11**.

Input 526.73 tok/s · output 53.25 tok/s · 12 model requests.

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

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).

<a id="q10-trial-2"></a>
## Q10 · Trial 2: Meeting availability

**PASS** · correctness **2/2** · E2E **84.28s** · checks **11/11**.

Input 632.13 tok/s · output 50.67 tok/s · 7 model requests.

All verification checks passed.

[Exact prompt](../docs/questions.md#q10) · [Full scored records: repeat10.jsonl.gz](../data/daily/repeat10.jsonl.gz?raw=1)

In that JSONL file, select `model == "Ornith-1.5-35B-A3B-oQ6-gs128-mtp-vision"` and `task == "gws_meeting_slots"` for every original check/detail and full expected/submitted answer. See [how to inspect raw data](../docs/data.md).
