# Evidence

Observed evidence in the exercise:

- eth0 was UP with 172.21.234.0/20.
- Default route was via 172.21.224.1.
- Loopback connectivity succeeded.
- Initial port 8080 had no listener.
- week1-demo.service was initially inactive.
- After starting the service, loopback returned HTTP 200.
- The application listener was 127.0.0.1:8080.
- Request to 172.21.234.0:8080 returned connection refused.

Pending evidence:
- Successful bind-address change.
- Listener on 0.0.0.0:8080.
- Successful interface-address HTTP test.

No unobserved results are claimed.
