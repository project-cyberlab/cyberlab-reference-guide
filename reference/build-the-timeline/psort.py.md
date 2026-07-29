<!-- generated-by: scripts/generate_pages.py -->
# psort.py

**Kit:** Kali Linux · SIFT Workstation  **Capability:** Build a super-timeline from many artifact sources  **Version:** plaso - psort version 20260512
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/psort.py.help.txt)

## Purpose

Filter, sort and output the events in a Plaso storage file.

## Synopsis

```
psort.py [-h] [--troubles] [-V] [--analysis PLUGIN_LIST]
[--process_memory_limit SIZE]
[--temporary_directory DIRECTORY] [--worker_memory_limit SIZE]
[--worker_timeout MINUTES] [--logfile FILENAME] [-d] [-q] [-u]
[--status_view TYPE] [--status_view_file PATH]
[--status_view_interval SECONDS] [--slice DATE_TIME]
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 03-timeline-analysis
psort.py --version
# from cyberlab 03-timeline-analysis
psort.py -o l2tcsv -w /tmp/timeline.csv /tmp/case.plaso
# from cyberlab 49-intrusion-timeline-case
psort.py -o l2tcsv -w super_timeline.csv timeline.plaso "date > '2024-01-10 00:00:00' AND date < '2024-01-12 00:00:00'"
```

## Options

All 59 options parsed from the captured help text; 4 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | Show this help message and exit. |  |
| `--help` | — | Show this help message and exit. |  |
| `--troubles` | — | Show troubleshooting information. |  |
| `-V` | — | Show the version information. |  |
| `--version` | — | Show the version information. |  |
| `--analysis` | PLUGIN_LIST | A comma separated list of analysis plugin names to be loaded or "--analysis list" to see a list of available plugins. | Run analysis plugins (tagging, sessionizing) over events. |
| `--process_memory_limit` | SIZE | Maximum amount of memory (data segment) a process is allowed to allocate in bytes, where 0 represents no limit. The default limit is 4294967296 (4 GiB). This applies to both the main (foreman) process |  |
| `--process-memory-limit` | SIZE | Maximum amount of memory (data segment) a process is allowed to allocate in bytes, where 0 represents no limit. The default limit is 4294967296 (4 GiB). This applies to both the main (foreman) process |  |
| `--temporary_directory` | DIRECTORY | Path to the directory that should be used to store temporary files created during processing. |  |
| `--temporary-directory` | DIRECTORY | Path to the directory that should be used to store temporary files created during processing. |  |
| `--worker_memory_limit` | SIZE | Maximum amount of memory (data segment and shared memory) a worker process is allowed to consume in bytes, where 0 represents no limit. The default limit is 2147483648 (2 GiB). If a worker process exc |  |
| `--worker-memory-limit` | SIZE | Maximum amount of memory (data segment and shared memory) a worker process is allowed to consume in bytes, where 0 represents no limit. The default limit is 2147483648 (2 GiB). If a worker process exc |  |
| `--worker_timeout` | MINUTES | Number of minutes before a worker process that is not providing status updates is considered inactive. The default timeout is 15.0 minutes. If a worker process exceeds this timeout it is killed by the |  |
| `--worker-timeout` | MINUTES | Number of minutes before a worker process that is not providing status updates is considered inactive. The default timeout is 15.0 minutes. If a worker process exceeds this timeout it is killed by the |  |
| `--logfile` | FILENAME | Path of the file in which to store log messages, by default this file will be named: "psort- YYYYMMDDThhmmss.log.gz". Note that the file will be gzip compressed if the extension is ".gz". |  |
| `--log_file` | FILENAME | Path of the file in which to store log messages, by default this file will be named: "psort- YYYYMMDDThhmmss.log.gz". Note that the file will be gzip compressed if the extension is ".gz". |  |
| `--log-file` | FILENAME | Path of the file in which to store log messages, by default this file will be named: "psort- YYYYMMDDThhmmss.log.gz". Note that the file will be gzip compressed if the extension is ".gz". |  |
| `-d` | — | Enable debug output. |  |
| `--debug` | — | Enable debug output. |  |
| `-q` | — | Disable informational output. | Quiet, for scripted runs. |
| `--quiet` | — | Disable informational output. |  |
| `-u` | — | Enable unattended mode and do not ask the user for additional input when needed, but terminate with an error instead. |  |
| `--unattended` | — | Enable unattended mode and do not ask the user for additional input when needed, but terminate with an error instead. |  |
| `--status_view` | TYPE | The processing status view mode: "file", "linear", "none" or "window". |  |
| `--status-view` | TYPE | The processing status view mode: "file", "linear", "none" or "window". |  |
| `--status_view_file` | PATH | The name of the status view file. |  |
| `--status-view-file` | PATH | The name of the status view file. |  |
| `--status_view_interval` | SECONDS | Number of seconds to update the status view. |  |
| `--status-view-interval` | SECONDS | Number of seconds to update the status view. |  |
| `--slice` | DATE_TIME | Date and time to create a time slice around. This parameter, if defined, will display all events that happened X minutes before and after the defined date, where X is controlled by the --slice_size op |  |
| `--slice_size` | SLICE_SIZE | Defines the slice size. In the case of a regular time slice it defines the number of minutes the slice size should be. In the case of the --slicer it determines the number of events before and after a |  |
| `--slice-size` | SLICE_SIZE | Defines the slice size. In the case of a regular time slice it defines the number of minutes the slice size should be. In the case of the --slicer it determines the number of events before and after a |  |
| `--slicer` | — | Create a time slice around every filter match. This parameter, if defined will save all X events before and after a filter match has been made. X is defined by the --slice_size parameter. |  |
| `--data` | PATH | Path to a directory containing the data files. |  |
| `-a` | — | By default the psort removes duplicate entries from the output. This parameter changes that behavior so all events are included. |  |
| `--include_all` | — | By default the psort removes duplicate entries from the output. This parameter changes that behavior so all events are included. |  |
| `--include-all` | — | By default the psort removes duplicate entries from the output. This parameter changes that behavior so all events are included. |  |
| `--language` | LANGUAGE_TAG | The preferred language, which is used for extracting and formatting Windows EventLog message strings. Use " --language list" to see a list of supported language tags. The en-US (LCID 0x0409) language  |  |
| `--additional_fields` | ADDITIONAL_FIELDS | Defines additional fields to be included in the output besides the default fields. Multiple additional field names can be defined as a list of comma separated values. Output formats that support addit |  |
| `--additional-fields` | ADDITIONAL_FIELDS | Defines additional fields to be included in the output besides the default fields. Multiple additional field names can be defined as a list of comma separated values. Output formats that support addit |  |
| `--custom_fields` | CUSTOM_FIELDS | Defines custom fields to be included in the output besides the default fields. A custom field is defined as "name:value". Multiple custom field names can be defined as list of comma separated values.  |  |
| `--custom-fields` | CUSTOM_FIELDS | Defines custom fields to be included in the output besides the default fields. A custom field is defined as "name:value". Multiple custom field names can be defined as list of comma separated values.  |  |
| `--custom_formatter_definitions` | PATH | Path to a file containing custom event formatter definitions, which is a .yaml file. Custom event formatter definitions can be used to customize event messages and override the built-in event formatte |  |
| `--custom-formatter-definitions` | PATH | Path to a file containing custom event formatter definitions, which is a .yaml file. Custom event formatter definitions can be used to customize event messages and override the built-in event formatte |  |
| `--dynamic_time` | — | Indicate that the output should use dynamic time. Output formats that support dynamic time are: dynamic |  |
| `--dynamic-time` | — | Indicate that the output should use dynamic time. Output formats that support dynamic time are: dynamic |  |
| `--output_time_zone` | TIME_ZONE | time zone of date and time values written to the output, if supported by the output format. Use "list" to see a list of available time zones. Output formats that support an output time zone are: dynam |  |
| `--output-time-zone` | TIME_ZONE | time zone of date and time values written to the output, if supported by the output format. Use "list" to see a list of available time zones. Output formats that support an output time zone are: dynam |  |
| `-o` | FORMAT | The output format. Use "-o list" to see a list of available output formats. | Output format — `l2tcsv`, `dynamic`, `json`, or a timeline tool. |
| `--output_format` | FORMAT | The output format. Use "-o list" to see a list of available output formats. |  |
| `--output-format` | FORMAT | The output format. Use "-o list" to see a list of available output formats. |  |
| `-w` | OUTPUT_FILE | Output filename. | Write output to a file rather than stdout. |
| `--write` | OUTPUT_FILE | Output filename. |  |
| `--fields` | FIELDS | Defines which fields should be included in the output. |  |
| `--profilers` | PROFILERS_LIST | List of profilers to use by the tool. This is a comma separated list where each entry is the name of a profiler. Use "--profilers list" to list the available profilers. |  |
| `--profiling_directory` | DIRECTORY | Path to the directory that should be used to store the profiling sample files. By default the sample files are stored in the current working directory. |  |
| `--profiling-directory` | DIRECTORY | Path to the directory that should be used to store the profiling sample files. By default the sample files are stored in the current working directory. |  |
| `--profiling_sample_rate` | SAMPLE_RATE | Profiling sample rate (defaults to a sample every 1000 files). |  |
| `--profiling-sample-rate` | SAMPLE_RATE | Profiling sample rate (defaults to a sample every 1000 files). |  |

## Gotchas

- The date filter is a positional argument, not a flag. Filtering to the incident window is what makes a multi-million-event timeline usable.
- Output ordering follows the storage file, so always sort or filter explicitly rather than assuming chronology.

## See also

`log2timeline.py`, `pinfo.py`
