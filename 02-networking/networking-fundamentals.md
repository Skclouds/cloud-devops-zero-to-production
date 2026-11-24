# Networking Fundamentals

**Learning track:** Cloud + DevOps Engineering  
**Week:** 02  
**Source:** Personal networking notes and completed theory discussions

---

## 1. Home Network and Internet Connectivity

A home network connects devices such as laptops, phones, and smart TVs so they can communicate with each other and access the Internet.

Typical connectivity workflow:

1. A device connects to the router through Wi-Fi or Ethernet.
2. DHCP provides network configuration.
3. DNS resolves a domain name when required.
4. The device sends traffic to its default gateway when the destination is outside its local network.
5. The router forwards traffic toward the ISP.
6. NAT/PAT may translate private addressing to a public IPv4 address.
7. The destination server responds.

### ISP

An Internet Service Provider (ISP) provides connectivity between a customer's network and the Internet.

### Private and Public IP Addresses

- **Private IP:** Used inside private networks and not directly routed across the public Internet.
- **Public IP:** Globally routable address used for communication across the Internet.

Private IPv4 ranges:

| Range | CIDR |
|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 |

### DHCP

Dynamic Host Configuration Protocol provides network configuration to devices, commonly including:

- IP address
- Subnet mask or prefix
- Default gateway
- DNS server

### NAT and PAT

- **NAT:** Network Address Translation changes IP address information in packets.
- **PAT:** Port Address Translation also uses transport-layer ports, allowing multiple private devices to share one public IPv4 address.

### DNS

Domain Name System resolves names such as `example.com` into DNS records, including IP addresses.

DNS helps locate a destination. It does not establish the HTTP connection itself.

---

## 2. Network Types

| Network | Meaning |
|---|---|
| LAN | Local Area Network |
| MAN | Metropolitan Area Network |
| WAN | Wide Area Network |

A LAN commonly connects devices within a home, office, or building. A WAN connects networks across larger geographical areas.

---

## 3. Network Topologies

A network topology describes how network devices are arranged or connected.

### Bus

Devices share a common communication backbone.

### Star

Devices connect through a central device, commonly a switch.

### Ring

Devices form a circular connection.

### Tree

A hierarchical arrangement of network segments.

### Mesh

Devices or nodes have multiple interconnections, providing alternate paths.

---

## 4. OSI 7-Layer Model

The OSI model divides network communication into seven conceptual layers.

| Layer | Name | Main responsibility | Examples |
|---|---|---|---|
| 7 | Application | Network services for applications | HTTP, DNS, SMTP |
| 6 | Presentation | Data representation, encoding, encryption concepts | TLS is commonly associated with this function conceptually |
| 5 | Session | Establishing and managing communication sessions | Session management concepts |
| 4 | Transport | Process-to-process communication | TCP, UDP |
| 3 | Network | Logical addressing and routing | IP, ICMP |
| 2 | Data Link | Local-link delivery and framing | Ethernet, MAC |
| 1 | Physical | Transmission of bits | Cable, radio, electrical and optical signals |

The OSI model is a reference model used to understand and troubleshoot networking.

---

## 5. TCP/IP Model

The TCP/IP model describes the architecture used by Internet networking.

| TCP/IP layer | Common protocols or technologies |
|---|---|
| Application | HTTP, HTTPS, DNS, SMTP, SSH |
| Transport | TCP, UDP |
| Internet | IPv4, IPv6, ICMP |
| Network Access / Link | Ethernet, Wi-Fi |

Some learning resources use a five-layer model by separating the physical layer from the link layer.

---

## 6. Client-Server Architecture

In client-server architecture:

- A client requests a service or resource.
- A server provides the requested service or resource.

Example:

A browser requests a web page from a web server.

Client and server are roles. They do not necessarily mean separate physical machines.

---

## 7. Peer-to-Peer Architecture

In peer-to-peer (P2P) architecture, participating devices can communicate and share resources directly.

A peer may act as both a client and a server.

P2P systems may still use central or distributed services for discovery, coordination, or authentication.

---

## 8. Network Protocols

A protocol defines rules for communication between networked systems.

Examples:

| Protocol | Purpose |
|---|---|
| HTTP / HTTPS | Web communication |
| DNS | Domain-name resolution |
| DHCP | Network configuration |
| TCP | Reliable, ordered transport |
| UDP | Connectionless datagram transport |
| IP | Logical addressing and packet routing |
| ARP | IPv4 address-to-link-layer address resolution on a local network |
| ICMP | Network control and diagnostic messages |
| SSH | Secure remote access |
| SMTP | Sending and transferring email |
| IMAP | Accessing and synchronizing email |
| POP3 | Retrieving email |

Protocols operate together across networking layers.

---

## 9. HTTP

HTTP is an application-layer request-response protocol.

A client sends an HTTP request, and a server returns an HTTP response.

### Common HTTP Methods

| Method | Common purpose |
|---|---|
| GET | Retrieve a resource |
| POST | Submit data or request processing |
| PUT | Replace a resource representation |
| PATCH | Partially update a resource |
| DELETE | Request removal of a resource |
| HEAD | Retrieve response headers without the response body |
| OPTIONS | Discover supported communication options |

### Common Status Codes

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 301 | Moved Permanently |
| 302 | Found / temporary redirect |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |
| 504 | Gateway Timeout |

### HTTP and HTTPS

- HTTP commonly uses TCP port 80.
- HTTPS commonly uses TCP port 443.
- HTTPS protects HTTP communication using TLS.

HTTP is stateless at the protocol level. Applications use mechanisms such as cookies and tokens to maintain state.

---

## 10. Cookies

A cookie is small data stored by a browser and sent with matching requests to a server.

Typical workflow:

1. Server sends a `Set-Cookie` header.
2. Browser stores the cookie according to its attributes.
3. Browser sends the cookie in later matching requests.

Common cookie attributes:

- `Secure`
- `HttpOnly`
- `SameSite`
- `Expires`
- `Max-Age`

A cookie may contain a session identifier. The actual session data is often stored server-side.

A cookie alone is not automatically proof of identity; its security depends on how the application uses and protects it.

---

## 11. Email Communication

Typical email workflow:

1. Sender writes an email in a mail client.
2. The client submits the message to an outgoing mail server using SMTP.
3. DNS MX records help identify the recipient's mail server.
4. Mail servers transfer the message using SMTP.
5. The recipient's server stores the message.
6. The recipient accesses the mailbox using IMAP or POP3.

### Email Protocols

| Protocol | Purpose |
|---|---|
| SMTP | Sending and transferring email |
| IMAP | Accessing and synchronizing email stored on the server |
| POP3 | Retrieving email from a server |

Common ports:

| Protocol | Port |
|---|---:|
| SMTP submission | 587 |
| SMTP over implicit TLS | 465 |
| SMTP server-to-server | 25 |
| IMAP | 143 |
| IMAPS | 993 |
| POP3 | 110 |
| POP3S | 995 |

Email security and delivery also involve TLS and DNS authentication records such as SPF, DKIM, and DMARC.

---

## 12. DNS Resolution

DNS translates domain names into DNS records.

Simplified resolution workflow:

1. Application requests a domain's address.
2. Local or browser caches are checked.
3. A recursive resolver handles the query.
4. The resolver may query root, TLD, and authoritative DNS servers.
5. The answer is returned and cached according to its TTL.

Common DNS records:

| Record | Purpose |
|---|---|
| A | IPv4 address |
| AAAA | IPv6 address |
| CNAME | Alias to another domain name |
| MX | Mail server information |
| TXT | Text information, often used for verification |
| NS | Authoritative name servers |

DNS commonly uses UDP port 53 and can also use TCP port 53.

---

## 13. TCP

TCP stands for Transmission Control Protocol.

TCP is a transport-layer protocol that provides:

- Connection-oriented communication
- Reliable delivery mechanisms
- Ordered byte-stream delivery
- Acknowledgments
- Retransmission when required
- Flow control
- Congestion control

TCP does not preserve application message or write boundaries. It provides a continuous byte stream.

### TCP Connection Identification

A TCP connection is identified by a four-tuple:

- Source IP address
- Source port
- Destination IP address
- Destination port

### TCP 3-Way Handshake

TCP establishes a connection using:

1. SYN
2. SYN-ACK
3. ACK

The handshake synchronizes initial sequence numbers and confirms that both endpoints can communicate.

### Simplified Example

```text
Client                         Server
  |                               |
  | -------- SYN, Seq=100 ------> |
  |                               |
  | <--- SYN-ACK, Seq=500, Ack=101|
  |                               |
  | -------- ACK, Ack=501 ------> |
  |                               |
  |       Connection ready        |
```

A SYN consumes one sequence number, so the acknowledgment is the next expected sequence number.

---

## 14. UDP

UDP stands for User Datagram Protocol.

UDP is connectionless and sends datagrams without establishing a traditional transport connection first.

UDP does not provide built-in guarantees of:

- Delivery
- Ordering
- Retransmission
- Duplicate suppression

UDP has an 8-byte header containing:

- Source port
- Destination port
- Length
- Checksum

Common uses include DNS, real-time communication, gaming, and transport protocols such as QUIC.

Applications can implement their own reliability mechanisms over UDP when needed.

---

## 15. Multiplexing and Demultiplexing

### Multiplexing

The transport layer accepts data from multiple applications and prepares it for transmission.

### Demultiplexing

The receiving transport layer uses protocol and addressing information, including ports, to deliver incoming data to the appropriate socket or application.

Example:

A client may communicate with a web server using destination port 443 while another application uses a different connection.

---

## 16. Checksum

A checksum is a calculated value used to help detect accidental data corruption during transmission or storage.

TCP and UDP use checksums to help detect corruption. IPv4 has a checksum for its header.

A checksum does not provide cryptographic authentication or protection against deliberate modification.

---

## 17. Networking Timers

A timer defines how long a protocol or application waits before taking an action.

Examples:

- TCP retransmission timer
- TCP keepalive timer
- TCP TIME-WAIT timer
- DNS cache TTL
- Application request timeout

A timeout does not always prove that the remote server failed. The response may simply be delayed or lost.

Retries should be designed carefully, especially for operations such as payments that could be processed more than once.

---

## 18. Hop-by-Hop Routing

Hop-by-hop routing means that each router forwards a packet toward its destination using its own forwarding decision.

A router generally:

1. Reads the destination IP address.
2. Looks up the destination in its forwarding information.
3. Selects an outgoing interface and next hop.
4. Forwards the packet.

At each router hop, the IPv4 TTL or IPv6 Hop Limit decreases.

The destination IP usually remains the same end-to-end, except when mechanisms such as NAT modify it.

---

## 19. Routing Table and Forwarding Table

### Routing Table — RIB

Routing Information Base:

- Stores routing information and candidate routes.
- Receives information from connected, static, and dynamic routes.
- Helps select preferred routes.

### Forwarding Table — FIB

Forwarding Information Base:

- Contains selected forwarding routes.
- Is optimized for packet forwarding.
- Helps the router quickly select an outgoing interface and next hop.

The RIB is associated with route selection; the FIB is used by the forwarding process.

---

## 20. Internet Protocol

Internet Protocol (IP) is a network-layer protocol that provides logical addressing and packet routing across interconnected networks.

IP does not itself guarantee delivery, ordering, or retransmission.

The two major IP versions are:

- IPv4
- IPv6

---

## 21. IPv4

IPv4 stands for Internet Protocol Version 4.

IPv4 uses 32-bit addresses, written as four decimal octets.

Example:

```text
192.168.1.10
```

Each octet contains 8 bits and ranges from 0 to 255.

IPv4 has a theoretical address space of 2^32 addresses.

### IPv4 Header Fields

Important fields include:

- Source address
- Destination address
- TTL
- Protocol
- Header checksum

### Public and Private IPv4

Private IPv4 ranges are used inside private networks. Public IPv4 addresses are globally routable, subject to routing and policy.

NAT is commonly used to provide Internet access to devices using private IPv4 addresses.

---

## 22. IPv4 Address Classes

Traditional classful addressing divides IPv4 addresses into Classes A, B, C, D, and E.

| Class | First octet | Default mask | Traditional purpose |
|---|---|---|---|
| A | 1–126 for ordinary unicast | 255.0.0.0 (/8) | Large networks |
| B | 128–191 | 255.255.0.0 (/16) | Medium networks |
| C | 192–223 | 255.255.255.0 (/24) | Smaller networks |
| D | 224–239 | Not applicable | Multicast |
| E | 240–255 | Not applicable | Reserved / experimental |

The 127.0.0.0/8 range is reserved for loopback.

Classful addressing is historical. Modern networks use CIDR.

---

## 23. CIDR

CIDR stands for Classless Inter-Domain Routing.

CIDR represents the network prefix using slash notation.

Examples:

```text
192.168.1.0/24
192.168.1.0/26
192.168.1.0/28
```

The prefix length specifies how many bits belong to the network portion.

CIDR is essential for:

- Cloud VPC and subnet design
- Route configuration
- IP address planning
- Firewall rules
- Kubernetes networking

---

## 24. IPv6

IPv6 stands for Internet Protocol Version 6.

IPv6 uses 128-bit addresses written in hexadecimal, separated by colons.

Example:

```text
2001:db8::1
```

IPv6 provides a vastly larger address space than IPv4.

### IPv6 Address Types

- Global Unicast
- Link-Local
- Unique Local
- Loopback: `::1`
- Unspecified: `::`

IPv6 supports address configuration through SLAAC, DHCPv6, and static configuration.

IPv6 does not use broadcast. It uses multicast and anycast addressing.

IPv6 uses Neighbor Discovery through ICMPv6 rather than ARP.

---

## 25. Practical Linux Networking Commands

These commands are reference commands. They should be executed and their actual outputs recorded in a separate practical lab.

### Display network interfaces and addresses

```bash
ip addr
```

### Display routing table

```bash
ip route
```

### Display IPv6 routes

```bash
ip -6 route
```

### Display listening TCP sockets

```bash
ss -tlnp
```

### Display listening UDP sockets

```bash
ss -ulnp
```

### Test connectivity

```bash
ping 8.8.8.8
```

### Trace network hops

```bash
traceroute example.com
```

Alternative:

```bash
tracepath example.com
```

### Resolve a domain

```bash
nslookup example.com
```

---

## 26. Week 2 Summary

By completing this theory section, the learner has studied:

- Network architecture and topologies
- OSI and TCP/IP models
- Common network protocols
- HTTP and email workflows
- DNS resolution
- TCP and UDP
- Transport-layer concepts
- Routing and forwarding
- IPv4, CIDR, and IPv6
- Basic Linux networking commands

**Next:** Perform practical networking investigations in the local Linux/WSL environment and document verified outputs.
