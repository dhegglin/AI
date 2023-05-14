# Headline

Filter incoming connections by source IP address

# Key Benefits

This feature allows access to the device to be restricted to known,
trusted sources and expected traffic profiles.

# Behavior

## SEC-CON-PERM-FR1: Filter On Source Address

Each [standalone device](#DEF_StandaloneDevice) _MUST_ be capable of
limiting connections to any service on the device based on source
[IP](#DEF_IP) address(es) of the connecting entities.

# History

```yaml
-----
affected_psb: SEC-CON-PERM
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
          standalone devices.

        class: ProtoTcpIp
    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-CON-PERM
    issueref: ISS_BadPeers
    tags:
    - EN/PI
    - PSB/OnPrem
