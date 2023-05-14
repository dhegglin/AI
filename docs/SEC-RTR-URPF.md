# Headline

Support unicast RPF

# Key Benefits

uRPF mitigates attacks based on [IP](#DEF_IP) address spoofing,
including amplified denial of service attacks.

# Behavior

## SEC-RTR-URPF-FR1: Strict and loose required by all IP routers

Strict unicast RPF and loose unicast RPF _MUST_ be supported by all
[IP](#DEF_IP)[routers](#DEF_Router).

# Informative References

Opportunity Description Document For Baseline IOS Security Features

RFC 2267, Network Ingress Filtering: Defeating Denial of Service Attacks
that employ [IP](#DEF_IP) Source Address Spoofing

# Normative References

RFC 3704, Ingress Filtering for Multihomed Networks

# History

```yaml
-----
affected_psb: SEC-RTR-UPRF
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

    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-RTR-URPF
    issueref: ISS_L3Spoof
    tags:
    - EN/PI
    - PSB/OnPrem
    - FAST
