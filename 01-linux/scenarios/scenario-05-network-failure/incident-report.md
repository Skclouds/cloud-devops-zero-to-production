# Scenario 5 — Linux Network and Application Connectivity Failure

## Objective
Investigate an application that appears unavailable on TCP port 8080.

## Environment
- Ubuntu 24.04.5 LTS
- WSL2
- Network interface: eth0
- Application: Python HTTP server
- Port: 8080

## Symptoms
- Initial curl to 127.0.0.1:8080 returned connection refused.
- No application listener was present.
- systemd service was initially inactive.

## Investigation
- Verified loopback connectivity.
- Inspected IP addresses and routing.
- Checked application processes and systemd status.
- Inspected listening sockets using ss.
- Started the application service.
- Confirmed HTTP 200 on loopback after startup.
- Found the application listening on 127.0.0.1:8080.
- Request to the WSL eth0 address failed.

## Findings
The application was configured to bind to loopback only.
The service was initially inactive.
An immediate request after startup also demonstrated that
service activation does not guarantee application readiness.

## Proposed correction
For this lab, investigate changing the bind address from
127.0.0.1 to 0.0.0.0.

This change must be backed up and verified before being
considered successful.

## Status
COMPLETED



## Production lessons
- Check the process, service, listener, bind address and logs.
- Confirm the actual runtime file used by systemd.
- Back up configuration before modifying it.
- Validate syntax before restarting.
- Verify application health after restart.
- Do not expose services on all interfaces without
  reviewing firewall and security requirements.
