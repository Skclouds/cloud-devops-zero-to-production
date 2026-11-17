# Scenario 01 — CPU and Memory Investigation: Command Reference

## 1. System identification

### `uname -a`

**Purpose:** Displays kernel and system information.

**Options:**
- `-a`: displays all available system information.

**Why we used it:** To identify the Linux kernel and confirm that the environment was running under WSL2.

**Interpretation:** The output included the hostname, kernel release, architecture and WSL2 kernel identification.

### `cat /etc/os-release`

**Purpose:** Displays Linux distribution identification.

**Options:**
- `cat`: prints file contents.
- `/etc/os-release`: standard operating-system identification file.

**Why we used it:** To confirm the Ubuntu version.

### `lscpu`

**Purpose:** Displays CPU architecture and processor information.

**Useful information:**
- CPU architecture
- Number of CPUs
- Threads and cores
- CPU model
- Virtualization information

**Why we used it:** To establish the CPU capacity available to the Linux environment.

## 2. CPU load and system resource inspection

### `uptime`

**Purpose:** Displays how long the system has been running, the number of logged-in users and load averages.

**Load averages:** Usually shown as three values representing the average system load over 1, 5 and 15 minutes.

**Important:** Load average is not CPU utilization percentage. It represents runnable tasks and tasks in uninterruptible sleep.

**Why we used it:** To establish a baseline and check whether system load was elevated.

### `free -h`

**Purpose:** Displays physical memory and swap usage.

**Options:**
- `-h`: human-readable sizes such as MiB and GiB.

**Important columns:**
- `total`: total memory available to the system.
- `used`: memory currently used.
- `free`: completely unused memory.
- `available`: estimated memory available for new applications without swapping.
- `buff/cache`: memory used for buffers and cache.
- `Swap`: swap capacity and usage.

**Why we used it:** To establish a memory baseline and check for memory pressure.

### `ps`

**Purpose:** Reports process information.

**Common forms:**

```bash
ps aux
ps -ef
ps -p 1234 -o pid,ppid,user,%cpu,%mem,stat,cmd
```

**Options:**
- `a`: processes associated with terminals.
- `u`: user-oriented output format.
- `x`: includes processes without a controlling terminal.
- `-e`: selects all processes.
- `-f`: full-format listing.
- `-p`: selects a specific process ID.
- `-o`: selects the output columns.

**Why we used it:** To identify processes and investigate CPU and memory consumption.

**Important observation:** A `ps` command can itself briefly show high CPU usage in a short-lived snapshot. Do not assume it is the cause of a persistent incident without repeated observations.

### `top -H`

**Purpose:** Displays live process activity, including individual threads.

**Options:**
- `-H`: displays threads rather than only process-level summaries.

**Why we used it:** To inspect CPU activity at thread level.

**Important:** `top -H` is not a disk-usage command.

Inside `top`:
- Press `P` to sort by CPU usage.
- Press `M` to sort by memory usage.
- Press `q` to quit.

### `top -p PID`

**Purpose:** Displays a selected process.

**Options:**
- `-p`: selects a process ID.

Replace `PID` with an actual numeric process ID.

Example:

```bash
top -p 1234
```

A PID is required. Running `top -p` without one is incomplete syntax.

## 3. Process investigation

### `pgrep`

**Purpose:** Searches for processes by name or pattern.

Examples:

```bash
pgrep -a python
pgrep -af cpu-burn
```

**Options:**
- `-a`: displays the command line along with the PID.
- `-f`: matches against the full command line.

**Why we used it:** To check whether the CPU stress process was still running.

**Interpretation:** No matching output means no matching process was found at that time. It does not prove that a process never ran.

## 4. Controlled CPU stress attempt

### `timeout`

**Command used:**

```bash
timeout 90s python3 ~/devops-lab/scenario-01/cpu-burn.py >/tmp/cpu-burn.log 2>&1 &
```

**Purpose:** Runs a command for a limited duration.

**Options and syntax:**
- `90s`: sets a 90-second time limit.
- `python3`: runs the Python interpreter.
- `>`: redirects standard output to a file.
- `2>&1`: redirects standard error to the same destination as standard output.
- `&`: starts the command in the background.

**Why we used it:** To generate controlled CPU activity without leaving an infinite stress process running.

**Important result:** We did not capture sufficient live process evidence during the stress window. The later timeout exit code was `124`, which indicates that `timeout` reached its time limit and terminated the command.

This attempt is not sufficient to claim that the live CPU investigation was completed.

## 5. Useful additional commands

These are reference commands for future investigations. They were not all executed during this scenario.

### `vmstat 1`

Reports CPU, memory, swap, I/O and system activity at one-second intervals.

### `free -h`

Useful for identifying memory pressure and swap usage.

### `pidstat 1`

Reports per-process resource usage when the `sysstat` package is installed.

### `watch -n 1 'free -h'`

Repeats the memory report every second.

### `journalctl -k`

Displays kernel journal messages, useful for investigating kernel-level events and possible OOM-killer activity.

### `dmesg -T`

Displays kernel ring-buffer messages with human-readable timestamps, subject to system permissions and kernel-log availability.

## 6. Troubleshooting principles

1. Establish a baseline before declaring an incident.
2. Identify the process consuming resources.
3. Observe whether the condition is persistent or temporary.
4. Correlate resource changes with deployments, traffic and application logs.
5. Do not restart or kill processes before collecting relevant evidence.
6. Distinguish CPU saturation from memory pressure.
7. Verify any remediation with fresh measurements.

