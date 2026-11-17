# Scenario 02 — Linux Service Failure: Command Reference

## 1. Application and configuration inspection

### `cat`

**Purpose:** Displays file contents.

Examples used in this lab:

```bash
cat config.json
cat config.json.broken
```

**Why:** To inspect the application configuration and compare the valid and malformed JSON files.

### `python3 -m json.tool`

**Purpose:** Parses and validates JSON.

```bash
python3 -m json.tool config.json
```

**Options:**
- `-m`: runs a Python module as a script.
- `json.tool`: Python's built-in JSON formatting and validation module.

**Why:** To identify malformed JSON before restarting the application.

**Interpretation:** Valid JSON is formatted and printed. Invalid JSON produces a parsing error with a line and column.

## 2. Linux systemd service management

The lab used a user-level systemd service:

`~/.config/systemd/user/week1-demo.service`

### `systemctl --user status`

**Purpose:** Displays the status of a service managed by the current user's systemd instance.

```bash
systemctl --user status week1-demo.service
```

**Options:**
- `--user`: communicates with the user's systemd manager.
- `status`: displays service state and recent log information.

**Why:** To investigate why the application service failed.

**Important:** User services are different from system-wide services. A system-wide service is generally managed without `--user`.

### `systemctl --user is-active`

**Purpose:** Checks whether a service is active.

```bash
systemctl --user is-active week1-demo.service
```

**Interpretation:**
- `active`: service is active.
- `inactive`: service is not running.
- `failed`: systemd considers the service failed.

The command's exit status can be checked with:

```bash
echo $?
```

### `systemctl --user restart`

**Purpose:** Stops and starts a service again.

```bash
systemctl --user restart week1-demo.service
```

**Why:** We used a restart after correcting the application's JSON configuration so that the application would read the corrected configuration during startup.

### `systemctl --user daemon-reload`

**Purpose:** Reloads systemd's unit-file definitions.

```bash
systemctl --user daemon-reload
```

**When required:** After creating or modifying a systemd unit file.

**Important:** Changing an application's JSON configuration does not itself require `daemon-reload`. Restart the application if it reads configuration only at startup.

## 3. Journal investigation

### `journalctl --user -u`

**Purpose:** Displays logs for a user-level systemd service.

```bash
journalctl --user -u week1-demo.service
```

**Options:**
- `--user`: accesses the user journal.
- `-u`: filters logs by a systemd unit.

Useful variations:

```bash
journalctl --user -u week1-demo.service -n 50
journalctl --user -u week1-demo.service -f
journalctl --user -u week1-demo.service --since "10 minutes ago"
```

**Additional options:**
- `-n 50`: shows the latest 50 entries.
- `-f`: follows new log entries.
- `--since`: filters by time.

**Why:** The journal exposed the Python traceback and JSON decoding failure.

**Observed error:**

`json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes`

The error pointed to line 5, column 1 of the configuration.

## 4. Network and application verification

### `ss -lntp`

**Purpose:** Displays TCP listening sockets and associated process information where permissions allow.

```bash
ss -lntp
```

**Options:**
- `-l`: listening sockets.
- `-n`: numeric addresses and ports.
- `-t`: TCP sockets.
- `-p`: process information.

To inspect port 8080:

```bash
ss -lntp | grep ':8080'
```

**Why:** To determine whether the application was listening on its configured port.

**Interpretation:** An empty result means no matching listening TCP socket was displayed. Check the full output and the actual bind address before concluding that the application is unavailable.

### `curl -i`

**Purpose:** Sends an HTTP request and displays response headers and body.

```bash
curl -i http://127.0.0.1:8080
```

**Options:**
- `-i`: includes HTTP response headers in output.

**Why:** To verify that the application responds to an HTTP request.

**Expected successful result:**
- HTTP status `200 OK`
- Application response body: `Application is healthy`

A listening socket alone does not prove that the application is functioning correctly. HTTP verification tests the application response.

## 5. Shell exit-status investigation

### `echo $?`

**Purpose:** Displays the exit status of the most recently executed command.

```bash
sudo -u deployer test -r /some/file
echo $?
```

**Interpretation:**
- `0`: command succeeded.
- Non-zero: command failed or returned a condition that was not true.

**Important:** Run `echo $?` immediately after the command you want to inspect. Another command changes the value.

## 6. Additional troubleshooting reference

These are useful related commands, not all confirmed as executed during this scenario.

### `systemctl --user cat week1-demo.service`

Displays the unit definition systemd is using.

### `systemctl --user show week1-demo.service`

Displays systemd properties for the service.

### `python3 -m py_compile app.py`

Checks Python syntax without running the application.

### `ps -ef`

Displays a full-format process listing.

### `ss -lntp`

Checks listening TCP ports and process associations.

## 7. Troubleshooting workflow

1. Check the service status.
2. Read the service journal.
3. Identify the actual failing component.
4. Inspect the application configuration.
5. Validate configuration syntax before restarting.
6. Restart the service.
7. Verify systemd status.
8. Verify the listening socket.
9. Send an HTTP request.
10. Inspect logs again.

## 8. Key distinction

A service can be:
- Failed because the application cannot start.
- Active but unable to serve correct responses.
- Active and listening on a port but unreachable from another network location.

Always verify both the service and the application behavior.
