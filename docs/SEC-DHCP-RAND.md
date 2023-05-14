# Headline

Randomize DHCP xid fields

# Key Benefits

An attacker who knows or suspects that a DHCP client is requesting
configuration information may spoof DHCP responses in an attempt to
misconfigure the client, possibly taking complete control of it. This
can be done [remotely](#DEF_Remote) if XIDs can be guessed.  (A
[local](#DEF_Local) attacker can see the requests directly and could
"race" the server with responses, so this consideration is not a
defense against a local attacker.)

# Behavior

## SEC-DHCP-RAND-FR1: Randomize XID Field

The “xid” field in each generated DHCP request _MUST_ be
[cryptographically unpredictable](#DEF_CryptographicUnpredictability). A
DHCP client _MUST_NOT_ use the same sequence of “xid”s at each
restart, and each request's “xid” field _MUST_ be independent of the
“xid” field in any other request.  An exception to this requirement is
for retransmissions of a client request which may elect to increment
the XID.  Since the attack model relies on predictable XIDs, an
incremented XID from an unpredictable XID is still unpredictable
within the scope of the single client's retry period for all intents
and purposes.

“xid”s _SHOULD_ be generated using a cryptographic-grade pseudorandom
number generator.

## SEC-DHCP-RAND-FR2: Drop Responses With Incorrect XIDs

DHCP responses with incorrect “xid” fields _MUST_NOT_ be processed.

# History
```yaml
-----
affected_psb: SEC-DHCP-RAND
description:  Updated to functional requirements. 

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-

                      DHCP clients using DHCP attributes other
                      than IP
                      address and netmask

    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-DHCP-RAND
    issueref: ISS_DHCPSpoof
    tags:
    - EN/PI
    - PSB/OnPrem
    - FAST
