# Networking Commands — Linux Reference

A practical Linux networking command reference for Cloud, DevOps, and MLOps engineering.

This document covers network interfaces, IP addressing, routing, neighbor discovery, ports, connectivity testing, DNS troubleshooting, HTTP diagnostics, and route tracing.

---

## 1. Network Interface Information

### Display IP addresses

```bash
ip addr
```

Displays network interfaces and their assigned IP addresses.

### Display network interfaces

```bash
ip link
```

Displays available network interfaces and their operational state.

### Display IPv4 addresses

```bash
ip -4 addr
```

Displays IPv4 addresses assigned to interfaces.

### Display IPv6 addresses

```bash
ip -6 addr
```

Displays IPv6 addresses assigned to interfaces.

### Display a specific interface

```bash
ip addr show eth0
```

Replace `eth0` with the interface name available on your system.

**DevOps use case:** Verify whether a server has the expected IP address and whether its network interface is up.

---

## 2. Routing Information

### Display the IPv4 routing table

```bash
ip route
```

Displays IPv4 routes available on the system.

### Display the IPv6 routing table

```bash
ip -6 route
```

Displays IPv6 routes.

### Display the default gateway

```bash
ip route show default
```

Shows the default route used when no more specific route matches the destination.

### Check the route toward a destination

```bash
ip route get 8.8.8.8
```

Shows the route and interface Linux would use to reach the destination.

**DevOps use case:** Investigate missing routes, incorrect gateways, and connectivity problems between servers.

---

## 3. Neighbor Discovery

### Display the neighbor table

```bash
ip neigh
```

Displays known neighboring devices on the local network.

The table commonly contains IPv4 ARP neighbor information and IPv6 Neighbor Discovery information.

### Display neighbors for a specific interface

```bash
ip neigh show dev eth0
```

Replace `eth0` with your actual interface name.

**DevOps use case:** Investigate local network communication and neighbor-resolution problems.

---

## 4. Listening Ports and Connections

### Display TCP and UDP sockets

```bash
ss -tuln
```

Options:

- `-t` — TCP sockets
- `-u` — UDP sockets
- `-l` — Listening sockets
- `-n` — Display numeric addresses and ports

### Display listening TCP ports

```bash
ss -lnt
```

### Display listening UDP ports

```bash
ss -lnu
```

### Display processes using sockets

```bash
sudo ss -tulnp
```

The `-p` option displays process information when permissions allow.

### Check a specific port

```bash
sudo ss -tulnp | grep ':8080'
```

Checks whether a process is listening on port `8080`.

**DevOps use case:** Troubleshoot applications that fail because a service is not listening on the expected port.

---

## 5. Connectivity Testing

### Test connectivity to an IP address

```bash
ping -c 4 8.8.8.8
```

Sends four ICMP echo requests.

### Test connectivity using a hostname

```bash
ping -c 4 example.com
```

Tests connectivity while also requiring hostname resolution.

### Test hostname resolution

```bash
getent hosts example.com
```

Uses the system's configured name-resolution mechanisms to resolve the hostname.

### Check the route to a destination

```bash
ip route get 8.8.8.8
```

**DevOps use case:** Determine whether a problem relates to network reachability, DNS resolution, or routing.

Note: A failed ping does not always mean the destination is unavailable. ICMP traffic may be blocked or filtered.

---

## 6. DNS Troubleshooting

### Query DNS using `nslookup`

```bash
nslookup example.com
```

Queries DNS for the hostname.

### Query DNS using `dig`

```bash
dig example.com
```

Displays DNS query results and additional information.

### Query an IPv4 address record

```bash
dig example.com A
```

### Query an IPv6 address record

```bash
dig example.com AAAA
```

### Query mail exchange records

```bash
dig example.com MX
```

### Query name servers

```bash
dig example.com NS
```

### Query a specific DNS server

```bash
dig @8.8.8.8 example.com
```

Queries the specified DNS server.

**DevOps use case:** Troubleshoot domain resolution, incorrect DNS records, and application failures caused by DNS.

Note: `dig` and `nslookup` may require installing DNS utilities on your Linux distribution.

---

## 7. HTTP and Application Connectivity

### Display HTTP response headers

```bash
curl -I https://example.com
```

Sends a request and displays response headers.

### Display detailed connection information

```bash
curl -v https://example.com
```

Displays detailed information about the request and connection.

### Download a response to the terminal

```bash
curl https://example.com
```

Displays the response body.

### Check whether a TCP port is reachable

```bash
nc -vz example.com 443
```

Attempts to establish a TCP connection to port `443`.

**DevOps use case:** Check whether a web application, API, or remote service is reachable.

Note: `curl` and `nc` may need to be installed.

---

## 8. Route Tracing

### Trace the path to a destination

```bash
tracepath example.com
```

Attempts to identify network hops toward the destination.

### Alternative command

```bash
traceroute example.com
```

Displays the path packets take toward a destination, subject to network behavior and filtering.

**DevOps use case:** Investigate network latency, routing paths, and connectivity problems between systems.

Note: These commands may require installation. Some networks block or limit traceroute responses.

---

## 9. Useful Troubleshooting Sequence

When a server or application cannot be reached, investigate systematically.

### Step 1 — Check the network interface

```bash
ip addr
```

Verify that the expected interface and IP address exist.

### Step 2 — Check the routing table

```bash
ip route
```

Verify that a suitable route and default gateway are present.

### Step 3 — Check DNS resolution

```bash
getent hosts example.com
```

Verify that the hostname resolves.

### Step 4 — Check listening ports

```bash
ss -tuln
```

Verify that the application is listening on the expected port.

### Step 5 — Check connectivity

```bash
ping -c 4 8.8.8.8
```

Test basic IP connectivity, keeping ICMP filtering in mind.

### Step 6 — Check the application response

```bash
curl -I https://example.com
```

Verify whether the application responds to an HTTP request.

---

## 10. DevOps and Cloud Engineering Relevance

These commands are useful when investigating:

- Server connectivity failures
- Incorrect IP configuration
- DNS resolution problems
- Missing or incorrect default routes
- Application ports not listening
- Firewall-related connectivity issues
- Service availability
- Network troubleshooting during deployments
- Connectivity between cloud instances
- Application and API availability

The objective is not simply to memorize commands. It is to understand **what layer or component each command helps investigate** and how to use the output to identify the root cause.

---

## 11. Practice Checklist

- [ ] Identify network interfaces and IP addresses
- [ ] Inspect IPv4 and IPv6 configuration
- [ ] Read the routing table
- [ ] Identify the default gateway
- [ ] Inspect the neighbor table
- [ ] Check listening TCP and UDP ports
- [ ] Test IP connectivity
- [ ] Verify DNS resolution
- [ ] Inspect HTTP response headers
- [ ] Trace the route toward a destination
- [ ] Follow the troubleshooting sequence for a simulated failure
