# Headline

Implement DNS securely per EDCS-1000043

# Key Benefits

DNS is a critical element of the Internet infrastructure, and the
availability and correctness of DNS data have major, pervasive security
implications for essentially all TCP/IP networks and the vast majority
of widely used TCP/IP protocols. Absent DNSSEC, DNS spoofing is easy,
and DNS spoofing attacks are in wide use on the public Internet. DNS
servers can also be attacked in other ways, and can for example be used
as amplifiers for denial of service attacks. Proper DNS and DNSSEC
implementation are among the most critical security concerns in IP
networks as of the adoption of this requirement.

# Description

Everything relies on DNS data; messing up DNS causes security problems
everywhere, often very large ones. Implement DNS according to the rules.

# Behavior

## SEC-DNS-SECURE-FR1: Comply with EDCS-1000043

Comply with all security requirements (requirements with IDs beginning
with “SEC-”) in the Global DNS Modernization and Security Requirements,
EDCS-1000043. Each such requirement _MUST_ be met with on the same
basis as any PSB requirement.

# History

```yaml
-----
affected_psb: SEC-SUP-PATCH
description:  Updated to functional requirements. 

```
PSBCTR 4.0: New requirement adopted.

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-

                      DNS-awareofferings
    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-DNS-SECURE
    issueref: ISS_DNSSpoof
    tags:
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
