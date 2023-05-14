# Headline

Support all security requirements over IPv6

# Key Benefits

It has always been the intent of the PSB to require basic security
functions to be available over IPv6. This is called out here for
clarity, for emphasis, and to give teams a requirement ID against which
to track compliance.

If any important security protocol is unavailable over IPv6 in any
significant number of widely deployed devices, customers will be forced
to choose between IPv6 transition and basic security. We cannot force
them to make this choice. In order to provide security functionality
over IPv6, devices must implement IPv6 itself.

Cisco has made repeated public commitments, from the CEO level, to
implement IPv6 in all products. Some of these commitments have directly
emphasized that there are to be no exceptions to this rule. Cisco has
also made numerous private commitments to a variety of customers and
other interested parties. Since Cisco is already fully committed to IPv6
implementation, compliance with this requirement represents no new
demand on resources.

# Description

Every function and protocol required for IPv4 is also required for IPv6.

# Behavior

## SEC-IP-IPv6-FR1: All IPv4 PSBs required for IPv6 (unless IPv4-specific)

Except for requirements which explicitly say they address only IPv4 or
and requirements concerned with elements of IPv4 which do not exist in
IPv6, every PSB requirement applies to IPv6 (and TCPv6, UDPv6, ICMPv6,
DHCPv6, etc) as well as to IPv4.

As particular examples of this very general rule:

1. Required protocols (NTP, SYSLOG, SSH, IPsec, etc) _MUST_ be
   implemented over IPv6 as well as over IPv4, and all required
   functionality must be provided over IPv6.

   IPv6 itself _MUST_ be implemented in any [offering](#DEF_Offering)
   which is required to implement any particular [IP](#DEF_IP)-based
   protocol. This implies that nearly all Cisco
   [offerings](#DEF_Offering) _MUST_ provide IPv6 stacks.
   Furthermore, those IPv6 stacks _MUST_ themselves comply with all
   applicable requirements. This requirement is not contingent on the
   presence of IPv6; it demands IPv6.

1. Filtering, logging, and robustness requirements apply to IPv6 as
   well as to IPv4.

1. Requirements on the implementation of various protocols apply to the
   IPv6 versions of those protocols as well as to the IPv4 versions.

# History

```yaml
-----
affected_psb: SEC-IP-IPv6
description:  Updated to functional requirements. 

```

## Older history (manually maintained; may be incomplete)

PSBCTR 4.0: Added as an explicit requirement.

PSBCTR 5.0: Further clarified that all products are required to
implement IPv6. Added more justification.

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings
    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-IP-IPv6
    issueref: ISS_MissingV6
    tags:
    - EN/PI
    - PSB/OnPrem
