
# Week 1 – Linux Administration & Fundamentals

> Cloud + DevOps + MLOps Engineering Roadmap  
> Phase 1 | Week 1 | Linux Administration  
> Environment: Windows 11 + WSL2 + Ubuntu 24.04  
> Cloud Infrastructure Cost: $0

---

## 1. Learning Objectives

The objective of Week 1 was to develop practical Linux administration skills required for Cloud and DevOps engineering.

By completing this module, the learner should understand:

- Linux architecture and command-line operations.
- Linux filesystem hierarchy.
- File and directory management.
- User and group administration.
- File ownership and permissions.
- Process and service management.
- CPU, memory and disk monitoring.
- System logs and troubleshooting.
- Basic networking and connectivity.
- SSH fundamentals.

---

## 2. Training Environment

| Component | Configuration |
|---|---|
| Host OS | Windows 11 |
| Linux Environment | WSL2 |
| Linux Distribution | Ubuntu 24.04 LTS |
| Shell | Bash |
| Editor | Visual Studio Code |
| Version Control | Git |
| Python | Python 3 |
| Cloud Infrastructure | Local only |
| Cloud Cost | $0 |

---

# 3. Linux Fundamentals

## 3.1 System Information Commands

| Command | Purpose |
|---|---|
| `uname -a` | Displays kernel and system information. |
| `hostname` | Displays the system hostname. |
| `hostnamectl` | Displays or manages hostname and system information. |
| `lsb_release -a` | Displays Linux distribution information. |
| `whoami` | Displays the currently logged-in username. |
| `id` | Displays user ID, group ID and group memberships. |
| `date` | Displays the current system date and time. |
| `uptime` | Shows how long the system has been running and its load averages. |

### Practical examples

```bash
uname -a
hostname
hostnamectl
lsb_release -a
whoami
id
date
uptime
```

### Real-world application

These commands are useful when:
- Identifying the operating system of a server.
- Checking the Linux kernel version.
- Verifying which user is executing a deployment.
- Investigating system uptime and load.

---

# 4. Linux Filesystem Management

## 4.1 Navigation Commands

| Command | Purpose |
|---|---|
| `pwd` | Displays the current working directory. |
| `ls` | Lists files and directories. |
| `ls -l` | Displays detailed file information. |
| `ls -la` | Lists all files, including hidden files. |
| `ls -lh` | Displays file sizes in human-readable format. |
| `cd` | Changes the current directory. |
| `cd ..` | Moves to the parent directory. |
| `cd ~` | Moves to the current user's home directory. |

### Practical examples

```bash
pwd
ls
ls -l
ls -la
ls -lh

cd /
cd /home
cd ~
cd ..
```

## 4.2 File and Directory Management

| Command | Purpose |
|---|---|
| `mkdir` | Creates a directory. |
| `mkdir -p` | Creates nested directories, including missing parents. |
| `touch` | Creates an empty file or updates timestamps. |
| `cp` | Copies files and directories. |
| `mv` | Moves or renames files and directories. |
| `rm` | Removes files. |
| `rm -r` | Removes directories recursively. |
| `tree` | Displays directory structures in a tree format. |
| `find` | Searches for files and directories. |
| `file` | Identifies a file's type. |
| `stat` | Displays detailed file metadata. |

### Practical examples

```bash
mkdir linux-lab

mkdir -p linux-lab/{logs,config,scripts,backup}

touch linux-lab/logs/application.log

cp linux-lab/logs/application.log linux-lab/backup/

mv linux-lab/backup/application.log linux-lab/backup/app.log

find linux-lab -type f

tree linux-lab

stat linux-lab/logs
```

## 4.3 Reading and Searching Files

| Command | Purpose |
|---|---|
| `cat` | Displays file contents. |
| `less` | Reads large files interactively. |
| `head` | Displays the first lines of a file. |
| `tail` | Displays the last lines of a file. |
| `tail -f` | Continuously monitors new log entries. |
| `grep` | Searches for matching text patterns. |
| `grep -R` | Searches recursively through directories. |
| `wc` | Counts lines, words and characters. |

### Practical examples

```bash
cat application.log

head -n 10 application.log

tail -n 20 application.log

tail -f application.log

grep "ERROR" application.log

grep -R "PORT" ./config

wc -l application.log
```

### Real-world application

When investigating application failures, engineers commonly use `grep`, `tail`, `less` and `journalctl` to locate error messages and understand application behaviour.

---

# 5. Linux User and Group Management

## 5.1 User and Group Commands

| Command | Purpose |
|---|---|
| `whoami` | Identifies the current user. |
| `id` | Displays user and group identifiers. |
| `adduser` | Creates a user interactively on Ubuntu. |
| `useradd` | Creates a user using lower-level account management options. |
| `usermod` | Modifies an existing user account. |
| `userdel` | Deletes a user account. |
| `groupadd` | Creates a new group. |
| `groups` | Displays group memberships. |
| `passwd` | Changes a user's password. |
| `sudo` | Executes commands with elevated privileges. |

### Practical examples

```bash
sudo adduser devuser

sudo groupadd developers

sudo usermod -aG developers devuser

groups devuser

id devuser

sudo passwd devuser
```

## 5.2 Important Linux Account Files

| File | Purpose |
|---|---|
| `/etc/passwd` | Stores user account information. |
| `/etc/group` | Stores group information. |
| `/etc/shadow` | Stores protected password hashes and password aging information. |
| `/etc/sudoers` | Defines sudo permissions. |

### Commands

```bash
cat /etc/passwd

cat /etc/group

sudo cat /etc/shadow

sudo visudo
```

**Security note:** Avoid editing `/etc/sudoers` directly with an ordinary text editor. Use `visudo` to validate changes.

---

# 6. Linux File Permissions and Ownership

## 6.1 Permission Concepts

Linux provides three basic permission types:

| Permission | Symbol | Numeric Value | Meaning |
|---|---|---:|---|
| Read | r | 4 | Read file contents. |
| Write | w | 2 | Modify file contents. |
| Execute | x | 1 | Execute a file or traverse a directory. |

Permissions apply to:

- User/Owner
- Group
- Others

## 6.2 Permission Commands

| Command | Purpose |
|---|---|
| `ls -l` | Displays file permissions and ownership. |
| `chmod` | Changes file or directory permissions. |
| `chown` | Changes file ownership. |
| `chgrp` | Changes group ownership. |
| `umask` | Displays or sets default permission masks. |
| `stat` | Displays detailed permissions and metadata. |

### Practical examples

```bash
chmod 755 app.sh

chmod 644 app.conf

chmod 700 private-directory

sudo chown devuser:developers app.conf

sudo chgrp developers app.conf

umask

stat app.conf
```

### Permission reference

| Permission | Meaning |
|---|---|
| 755 | Owner: rwx, Group: r-x, Others: r-x |
| 644 | Owner: rw-, Group: r--, Others: r-- |
| 700 | Owner: rwx, Group: ---, Others: --- |
| 600 | Owner: rw-, Group: ---, Others: --- |

### Real-world application

Use Linux permissions to:
- Restrict access to application configuration files.
- Allow developers to read application logs.
- Prevent unauthorized modifications.
- Secure SSH private keys.
- Control deployment directory ownership.

---

# 7. Linux Process Management

## 7.1 Process Commands

| Command | Purpose |
|---|---|
| `ps aux` | Displays running processes and resource information. |
| `ps -ef` | Displays processes in full-format listing. |
| `top` | Provides real-time process and system monitoring. |
| `htop` | Provides an interactive process monitor. |
| `pgrep` | Searches for processes by name or attributes. |
| `pidof` | Displays process IDs for a program. |
| `kill` | Sends a signal to a process. |
| `jobs` | Displays jobs started in the current shell. |

### Practical examples

```bash
ps aux

ps -ef

top

htop

pgrep -a python3

pidof python3

jobs
```

## 7.2 Process Termination

| Command | Purpose |
|---|---|
| `kill -15 PID` | Sends SIGTERM for graceful termination. |
| `kill -9 PID` | Sends SIGKILL for forced termination. |

### Practical examples

```bash
pgrep -af app.py

kill -15 <PID>

kill -9 <PID>
```

**Important:** Replace `<PID>` with the actual process ID. Prefer graceful termination before forced termination.

### Real-world application

Process management is required when:
- An application is consuming excessive CPU.
- A deployment process becomes unresponsive.
- A background job needs investigation.
- A service is running multiple unwanted instances.

---

# 8. Linux Service Management

Linux distributions using systemd provide `systemctl` to manage system services.

## 8.1 systemctl Commands

| Command | Purpose |
|---|---|
| `systemctl status` | Displays service status. |
| `systemctl start` | Starts a service. |
| `systemctl stop` | Stops a service. |
| `systemctl restart` | Restarts a service. |
| `systemctl enable` | Enables a service at system startup. |
| `systemctl disable` | Disables startup activation. |
| `systemctl list-units` | Lists systemd units. |
| `systemctl is-active` | Checks whether a service is active. |

### Practical examples

```bash
systemctl list-units --type=service

systemctl status cron

sudo systemctl start cron

sudo systemctl stop cron

sudo systemctl restart cron

sudo systemctl enable cron

systemctl is-active cron
```

**Note:** WSL may not have systemd enabled by default. These commands depend on the WSL distribution's systemd configuration. Verify availability before attempting service management.

---

# 9. Linux Logs and Troubleshooting

## 9.1 journalctl Commands

| Command | Purpose |
|---|---|
| `journalctl` | Displays system journal logs. |
| `journalctl -u SERVICE` | Displays logs for a particular service. |
| `journalctl -xe` | Displays recent journal entries with explanatory context. |
| `journalctl -f` | Follows new journal entries. |
| `journalctl --since` | Filters logs from a specified time. |

### Practical examples

```bash
journalctl

journalctl -u cron

journalctl -xe

journalctl -f

journalctl --since "1 hour ago"
```

## 9.2 Log File Commands

```bash
ls -lh /var/log

sudo tail -f /var/log/syslog

sudo grep -i "error" /var/log/syslog
```

**Note:** Log file names and availability depend on the distribution and logging configuration. Ubuntu installations using systemd commonly provide journal logs.

### Real-world application

When a production service fails:
1. Check the service status.
2. Inspect its recent logs.
3. Identify the error.
4. Investigate the configuration.
5. Correct the underlying issue.
6. Restart and verify the service.

---

# 10. Linux Resource Monitoring

## 10.1 CPU and Memory Monitoring

| Command | Purpose |
|---|---|
| `free -h` | Displays memory and swap utilization. |
| `top` | Monitors CPU and memory usage by processes. |
| `htop` | Interactive resource monitoring. |
| `vmstat` | Reports process, memory and system activity statistics. |
| `uptime` | Displays load averages and uptime. |

### Practical examples

```bash
free -h

top

htop

vmstat 1 5

uptime
```

## 10.2 Disk Monitoring

| Command | Purpose |
|---|---|
| `df -h` | Displays filesystem capacity and utilization. |
| `du -sh DIRECTORY` | Displays total directory size. |
| `lsblk` | Lists block devices and partitions. |
| `iostat` | Reports CPU and storage I/O statistics. |

### Practical examples

```bash
df -h

du -sh ~/devops-lab

lsblk

iostat -xz 1 3
```

`iostat` requires the `sysstat` package.

```bash
sudo apt install -y sysstat
```

## 10.3 Simulating Disk Usage

```bash
mkdir -p ~/devops-lab/day-05

cd ~/devops-lab/day-05

dd if=/dev/zero of=testfile.log bs=1M count=100

du -sh .

ls -lh testfile.log

rm testfile.log
```

### Real-world application

These commands help investigate:
- High disk utilization.
- Memory pressure.
- CPU spikes.
- Excessive application log growth.
- Storage I/O bottlenecks.

---

# 11. Linux Networking Fundamentals

## 11.1 Network Commands

| Command | Purpose |
|---|---|
| `ip addr` | Displays network interfaces and IP addresses. |
| `ip route` | Displays the system routing table. |
| `hostname -I` | Displays assigned IP addresses. |
| `ping` | Tests basic IP connectivity. |
| `curl` | Makes HTTP requests and transfers data. |
| `ss` | Displays socket and connection information. |
| `netstat` | Displays network connections and statistics; legacy tool. |
| `traceroute` | Shows the network path towards a destination. |

### Practical examples

```bash
ip addr

ip route

hostname -I

ping -c 4 8.8.8.8

curl -I https://example.com

ss -tulpn

traceroute google.com
```

## 11.2 DNS Troubleshooting

| Command | Purpose |
|---|---|
| `nslookup` | Queries DNS records. |
| `dig` | Provides detailed DNS query information. |

### Practical examples

```bash
nslookup google.com

dig google.com

dig google.com A

dig google.com MX
```

## 11.3 Port Investigation

```bash
ss -ltnp

ss -tulpn
```

These commands help identify listening ports, TCP/UDP sockets and associated processes where permissions allow.

### Real-world application

Networking commands are useful when:
- An application is not reachable.
- DNS resolution fails.
- A port is already in use.
- A service is listening on the wrong interface.
- Network routing needs investigation.

---

# 12. Python HTTP Server – Practical Exercise

A lightweight Python HTTP server was used to understand local application networking.

## Create a web directory

```bash
mkdir -p ~/devops-lab/day-06

cd ~/devops-lab/day-06

echo "Hello from my Linux server" > index.html
```

## Start the HTTP server

```bash
python3 -m http.server 8000
```

## Verify connectivity

Open another terminal:

```bash
curl http://localhost:8000
```

## Verify the listening port

```bash
ss -ltnp | grep 8000
```

Stop the server using:

```text
Ctrl + C
```

### What this exercise demonstrates

- Starting a local application.
- Understanding listening ports.
- Testing HTTP connectivity.
- Inspecting network sockets.
- Diagnosing basic application accessibility.

---

# 13. Linux Administration Troubleshooting Scenarios

| Scenario | Commands to investigate |
|---|---|
| Application is not running | `ps`, `systemctl`, `journalctl` |
| High CPU utilization | `top`, `ps`, `uptime` |
| High memory utilization | `free`, `top`, `vmstat` |
| Disk utilization is high | `df`, `du`, `lsblk` |
| Permission denied | `ls -l`, `stat`, `chmod`, `chown` |
| Application port is unavailable | `ss`, `curl`, `lsof` |
| DNS resolution failure | `dig`, `nslookup` |
| Service fails to start | `systemctl`, `journalctl` |
| Missing configuration file | `find`, `ls`, `stat` |
| HTTP server is inaccessible | `curl`, `ss`, `ip route` |

---

# 14. Key Linux Administration Concepts

| Concept | Explanation |
|---|---|
| Kernel | Core component managing system hardware and resources. |
| Shell | Command interpreter used to interact with the operating system. |
| Terminal | Interface for entering and displaying commands. |
| Process | An executing instance of a program. |
| PID | Unique process identifier. |
| Daemon | Background service process. |
| systemd | Linux system and service manager. |
| Filesystem | Structure for storing and organizing data. |
| Root user | Superuser with administrative privileges. |
| SSH | Secure remote access protocol. |
| DNS | Resolves domain names to network addresses. |
| TCP | Connection-oriented transport protocol. |
| UDP | Connectionless transport protocol. |
| Port | Logical endpoint used for network communication. |

---

# 15. Week 1 Practical Deliverables

- [x] WSL2 and Ubuntu environment configured.
- [x] Linux package installation.
- [x] Git repository initialization.
- [x] Linux filesystem exercises.
- [x] User and group administration.
- [x] File permissions and ownership.
- [x] Process management.
- [x] Service management.
- [x] System monitoring.
- [x] Networking fundamentals.
- [x] Local HTTP server exercise.
- [ ] Week 1 independent practical assessment.
- [ ] Production troubleshooting examination.

---

# 16. Learning Outcome

Week 1 establishes the Linux administration foundation required for subsequent Cloud, DevOps and MLOps modules.

The next module focuses on Docker and containerization, including image creation, container networking, volumes, Docker Compose, multi-stage builds and container troubleshooting.

---

**Training Roadmap:** Cloud + DevOps + MLOps Engineer  
**Learning Approach:** Concepts + Hands-on + Troubleshooting + Assessment  
**Infrastructure Policy:** Strict $0 cloud infrastructure cost.
