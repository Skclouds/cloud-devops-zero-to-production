# Scenario 5 — Commands Explained

## Network inspection
- ip addr: displays network interfaces and addresses.
- ip route: displays routing table.
- ip link: displays interface state.
- ip route get 127.0.0.1: shows route selected for loopback.
- getent hosts localhost: resolves localhost.
- ping -c 4 127.0.0.1: sends four ICMP packets.

## Process inspection
- ps -ef: displays running processes.
- pgrep -af 'app.py|http.server': searches process command lines.

## Service inspection
- systemctl --user status: inspects user service state.
- systemctl --user start: starts a service.
- systemctl --user restart: restarts a service.
- systemctl --user cat: displays the unit configuration.
- journalctl --user -u: reads service logs.

## Port inspection
- ss -lntup: displays listening TCP/UDP sockets and processes.
- sudo ss -lntp: displays TCP listeners with process information.
- grep ':8080': filters output for port 8080.

## Application testing
- curl -i: displays HTTP response headers and body.
- curl --max-time 5: limits request duration to five seconds.
- sleep 2: waits two seconds before the next command.

## Configuration safety
- cp -a: backs up a file while preserving attributes.
- ls -lht: lists files with sizes, permissions and timestamps.
- grep -n: searches text and displays matching line numbers.
- nano: edits a text file.
- python3 -m py_compile: validates Python syntax.

## Evidence rule
Commands listed here include investigation and reference
commands. The incident report distinguishes observed findings
from corrections that have not yet been verified.
