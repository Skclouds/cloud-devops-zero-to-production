# Scenario 02 — Linux Service Failure

## Scenario objective

Simulate a Linux application service failure caused by malformed JSON configuration, investigate the failure using systemd and journal logs, and recover the service.

## Environment

- OS: Ubuntu under WSL2
- Runtime: Python 3
- Service manager: systemd user service
- Service: `week1-demo.service`
- Application: Python HTTP server
- Bind address: `127.0.0.1`
- Port: `8080`

## Application behavior

The Python application reads `config.json`, extracts the configured port, and starts an HTTP server.

The successful application response is:

`Application is healthy`

## Incident simulation

A malformed configuration was used:

`config.json.broken`

The JSON configuration contained an invalid trailing comma after the `debug` property.

This prevented Python's JSON parser from loading the configuration.

## Investigation performed

Commands used:

```bash
systemctl --user status week1-demo.service
systemctl --user is-active week1-demo.service
journalctl --user -u week1-demo.service
ss -lntp | grep ':8080'
```

The service entered the failed state.

The journal showed:

`json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes`

The traceback identified the JSON parsing failure at line 5, column 1.

The port inspection showed that the application was not listening on port 8080.

## Root cause

The application configuration contained invalid JSON syntax.

The Python application could not parse its configuration and therefore could not start its HTTP server.

The evidence establishes the malformed configuration as the technical cause. It does not establish who introduced the change.

## Recovery performed

1. Backed up the configuration.
2. Corrected the malformed JSON.
3. Validated the corrected JSON using:

```bash
python3 -m json.tool config.json
```

4. Restarted the user service:

```bash
systemctl --user restart week1-demo.service
```

5. Checked service status.
6. Checked the listening socket.
7. Sent an HTTP request to the application.

## Verification

The recovery was verified through:

- systemd reporting the service active.
- Port 8080 listening.
- `curl -i http://127.0.0.1:8080` returning HTTP 200 OK.
- Response body showing `Application is healthy`.
- Application logs showing successful startup.

## Status

**Completed — application service recovered and HTTP response verified.**

## Production lessons

- A service failure does not automatically mean systemd itself is broken.
- Read the journal before changing service configuration.
- Validate configuration files before restarting production services.
- `systemctl status` confirms service-manager state, not complete application health.
- A listening socket is not sufficient proof of application correctness.
- Verify the actual application response after recovery.

## Prevention

- Add JSON validation to CI/CD pipelines.
- Validate configuration before deployment.
- Keep a known-good configuration backup.
- Use deployment health checks.
- Monitor service state and application-level health separately.

## Evidence

The application files are retained in this directory:

- `app.py`
- `config.json`
- `config.json.broken`

See `commands-explained.md` for command syntax, options and interpretation.
