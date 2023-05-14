# Headline

Configurably rate-limit IP based on layers 3 and 4

# Key Benefits

Rate limiting is an important tool for responding to flooding denial of
service attacks. Because attacks are diverse, it is important to have
flexible limiting criteria.

# Behavior

## SEC-LIM-TRAF-FR1: Can configure rate limiting for TCP, UDP, IP, and ICMP

Each [forwarding device](#DEF_ForwardingDevice) must provide
[administrator](#DEF_Administrator)-configurable rate limiting for TCP,
UDP, [IP](#DEF_IP) and ICMP traffic directed to or through the device.

## SEC-LIM-TRAF-FR2: Can base limiting on any combination of IP header fields

It must be possible to rate limit traffic based on the values of any
field or combination of fields in the outermost [IP](#DEF_IP) header.

## SEC-LIM-TRAF-FR3: Can base limiting on any L4 fields for TCP or UDP

When the transport protocol is TCP or UDP, it must further be possible
to rate limit traffic based on any field or combination of fields in the
TCP or UDP header.

# Informative References

Opportunity Description Document For Baseline IOS Security Features

Control Rate Plane Limiting, EDCS-282579

Control Plane Architecture, EDCS-281836

Alcazar Network Management Notes, EDCS-263024

# History

```yaml
-----
affected_psb: SEC-LIM-TRAF
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
          forwarding devices
    
        class: ProtoTcpIp
    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-LIM-TRAF
    issueref: ISS_Floods
    tags:
    - EN/PI
    - PSB/OnPrem
    - EN/PI DT
