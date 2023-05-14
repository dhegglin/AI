# Headline

Filter based on layer 3 and layer 4 fields

# Key Benefits

A rich set of filtering options is necessary both for policy enforcement
and for incident response. Denial of service attack streams can
sometimes be shut down by filtering on very obscure combinations of
header fields.

# Behavior

## SEC-RTR-FILT-FR1: Filter forwarded traffic based on header fields

Each [router](#DEF_Router) _MUST_ support filtering forwarded traffic
based on the value(s) of any fixed field(s) in the outermost
[IP](#DEF_IP) header, and _SHOULD_ support filtering based on the
presence, absence, or contents of IPv4 options and of nested IPv6
headers.

## SEC-RTR-FILT-FR2: Filter forwarded TCP and UDP packets on L4 header fields

If the layer 4 protocol immediately following the outermost
[IP](#DEF_IP) header is TCP or UDP, the [router](#DEF_Router) _MUST_
also support filtering based on the value(s) of any fixed field(s) in
the TCP or UDP header, and _SHOULD_ support filtering based on the
presence, absence, or contents of TCP options.

# Normative References

Internet Protocol, RFC 791

Internet Protocol, Version 6 (IPv6) Specification, RFC 2460

User Datagram Protocol, RFC 768

Transmission Control Protocol, RFC 793

# History

```yaml
-----
affected_psb: SEC-RTR-FILT
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
          IProuters.

        class: Router
    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 2
    id: SEC-RTR-FILT
    issueref: ISS_Floods
    tags:
    - EN/PI
    - PSB/OnPrem
    - FAST
