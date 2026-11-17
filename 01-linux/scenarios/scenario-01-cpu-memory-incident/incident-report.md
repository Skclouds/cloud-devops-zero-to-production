# Scenario 01 — CPU and Memory Investigation

## Scenario objective

Learn how to establish a Linux resource baseline and investigate CPU and memory usage using standard Linux tools.

## Environment

- Host: DESKTOP-MKUE3GK
- OS: Ubuntu 24.04.5 LTS under WSL2
- Kernel: 6.18.33.2-microsoft-standard-WSL2
- CPU: Intel Core i5-1135G7
- Linux CPUs reported: 2
- Memory reported: approximately 2.8 GiB
- Swap reported: approximately 2 GiB

These values describe the Linux environment, not necessarily the full physical capacity of the Windows host.

## Investigation performed

The following commands were used to establish the baseline:

- `uname -a`
- `cat /etc/os-release`
- `lscpu`
- `uptime`
- `free -h`
- `ps`
- `top -H`

The baseline showed low system load and available memory. A process listing briefly showed the `ps` command itself using significant CPU in the snapshot. This was not sufficient evidence of a persistent CPU-consuming application.

## CPU stress attempt

A Python CPU-burn script was created and an execution attempt was made with:

```bash
timeout 90s python3 ~/devops-lab/scenario-01/cpu-burn.py >/tmp/cpu-burn.log 2>&1 &
```

The process was not captured during its active period. A later check found no matching running process, and the timeout command returned exit code 124 after reaching its time limit.

## Findings

- The Linux environment and resource baseline were identified.
- Process and thread inspection commands were practised.
- The CPU stress attempt was made.
- Sufficient live CPU evidence was not captured to complete the stress-investigation exercise.

## Status

**Partially completed — live CPU stress investigation still requires a controlled repeat.**

## Production lessons

- High CPU usage is a symptom, not a root cause.
- Correlate CPU changes with deployments, traffic, logs and application behavior.
- For JVM applications, identify hot threads and correlate them with thread dumps and application evidence.
- High memory usage alone does not prove a memory leak.
- A high post-GC heap may indicate retained objects, caches or legitimate long-lived data; profiling and heap analysis are needed.
- Increasing RAM without identifying the cause can hide rather than solve a resource problem.

## Recovery and verification methodology

1. Capture system baseline.
2. Identify the process or thread consuming resources.
3. Correlate the event with application and deployment timelines.
4. Gather logs and application-specific diagnostics.
5. Apply the smallest safe remediation.
6. Verify CPU, memory, application health and logs.
7. Document the root cause and preventive action.

## Evidence still required

- Live CPU measurements while the stress process is running.
- Process identification during the stress window.
- Post-stress resource measurements.
- Confirmation that the stress process terminates cleanly.
