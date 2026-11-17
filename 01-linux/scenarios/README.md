# Linux Practical Scenarios — Week 1

This directory contains hands-on Linux incident simulations and their technical documentation.

Each scenario separates:
- Incident report: what happened, investigation, root cause, recovery and verification.
- Command reference: command syntax, options, purpose and output interpretation.
- Evidence: actual terminal output and supporting configuration.

Commands that were discussed but not confirmed as executed are identified as additional reference.

## Scenario tracker

| Scenario | Topic | Practical result | Status |
|---|---|---|---|
| 01 | CPU and memory investigation | Baseline and process inspection performed; live CPU stress evidence still missing | Partially completed |
| 02 | Linux service failure | Malformed JSON diagnosed; systemd service recovered; HTTP 200 verified | Completed |
| 03 | Disk and inode exhaustion | Both block and inode exhaustion reproduced on loopback filesystems; cleanup verification pending | Partially completed |
| 04 | Permission and deployment failure | Permission failure reproduced; group-based recovery and artifact comparison verified | Completed |
| 05 | Network failure | Not started | Pending |

## Scenario directories

### 01 — CPU and memory
`scenario-01-cpu-memory-incident/`

Topics:
- CPU and memory baseline
- Load average interpretation
- Process and thread inspection
- Controlled CPU stress investigation

### 02 — Service failure
`scenario-02-service-failure/`

Topics:
- systemd user services
- JSON configuration validation
- journal investigation
- listening sockets
- HTTP health verification

### 03 — Disk and inode exhaustion
`scenario-03-disk-exhaustion/`

Topics:
- Filesystem capacity
- ext4 loopback filesystems
- Block exhaustion
- Inode exhaustion
- Filesystem cleanup and verification

### 04 — Permission failure
`scenario-04-permission-failure/`

Topics:
- Users and groups
- Ownership and permission bits
- Directory traversal and write permissions
- setgid directory inheritance
- Deployment identity and artifact verification

### 05 — Network failure
`scenario-05-network-failure/`

To be added after the practical exercise.

## Documentation standard

Every scenario should document:

1. Objective and environment
2. Incident simulation
3. Investigation commands
4. Command options and output interpretation
5. Root cause
6. Recovery steps
7. Verification evidence
8. Production relevance
9. Security and reliability considerations
10. Remaining work and lessons learned

## Evidence integrity

Do not fabricate terminal output or claim a verification step was completed without evidence.

Before committing:
- Review the incident report.
- Review the command reference.
- Check that evidence contains no secrets.
- Verify the Git working tree and staged changes.
