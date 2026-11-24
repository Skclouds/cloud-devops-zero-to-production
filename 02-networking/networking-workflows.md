
# Networking Workflows

**Week:** 02  
**Purpose:** Understand how networking components work together during real communication.

---

## 1. Opening a Website

```text
User enters https://example.com
              |
              v
       Browser checks cache
              |
              v
       DNS resolution
              |
              v
       Destination IP obtained
              |
              v
       Routing decision
              |
              v
       TCP connection established
       (SYN -> SYN-ACK -> ACK)
              |
              v
       TLS handshake
              |
              v
       HTTP request sent
              |
              v
       Web server processes request
              |
              v
       HTTP response returned
              |
              v
       Browser displays content
```

Note: HTTP/3 uses QUIC over UDP rather than the traditional TCP connection and TLS-over-TCP workflow.

---

## 2. DNS Resolution

```text
Application requests domain
          |
          v
Browser / OS cache checked
          |
          v
Recursive DNS resolver
          |
          v
Root DNS server
          |
          v
TLD DNS server
          |
          v
Authoritative DNS server
          |
          v
DNS answer returned
          |
          v
Answer cached according to TTL
```

A cached answer may allow the resolver to skip some of the lookup steps.

---

## 3. TCP 3-Way Handshake

```text
Client                         Server
  |                               |
  | -------- SYN ---------------> |
  |                               |
  | <------ SYN-ACK ------------- |
  |                               |
  | -------- ACK ---------------> |
  |                               |
  |     TCP connection ready      |
```

The handshake synchronizes sequence numbers and confirms communication in both directions.

---

## 4. Email Delivery

```text
Sender's email client
          |
          v
Outgoing mail server
          |
          v
SMTP transfer
          |
          v
DNS MX lookup
          |
          v
Recipient mail server
          |
          v
Mailbox storage
          |
          v
Recipient accesses mail
      IMAP / POP3
```

SMTP is used for sending and transferring email. IMAP and POP3 are used by clients to retrieve or access mailbox messages.

---

## 5. Hop-by-Hop Routing

```text
Source device
     |
     v
Default gateway
     |
     v
Router A
     |
     v
Router B
     |
     v
Destination network
     |
     v
Destination server
```

Each router makes a forwarding decision using its forwarding information.

The destination IP generally remains unchanged end-to-end, except where mechanisms such as NAT modify it.

At each IPv4 router hop, TTL decreases. In IPv6, the Hop Limit decreases.

---

## 6. TCP vs UDP Communication

### TCP

```text
Application
    |
    v
TCP connection
    |
    v
Reliable ordered byte stream
    |
    v
IP packet
    |
    v
Network
```

### UDP

```text
Application
    |
    v
UDP datagram
    |
    v
IP packet
    |
    v
Network
```

UDP does not establish a traditional connection and does not provide built-in delivery or ordering guarantees.

---

## 7. Routing Table and Forwarding Table

```text
Routes learned or configured
          |
          v
Routing Table (RIB)
          |
          v
Best route selection
          |
          v
Forwarding Table (FIB)
          |
          v
Packet destination lookup
          |
          v
Outgoing interface / next hop
```

The RIB supports route selection. The FIB supports efficient packet forwarding.
