# Headline

Maintain forwarding during flooding attack

# Key Benefits

Failure to maintain service creates obvious targets for attackers.

# Behavior

## SEC-FOR-ATTCK-FR1: Forward During Flooding

During and after any of the [reference floods](#DEF_ReferenceFlood), the
[forwarding device](#DEF_ForwardingDevice) _MUST_ maintain forwarding
of traffic sent through the [forwarding device](#DEF_ForwardingDevice)
on any path not sharing interfaces with the [reference
flood](#DEF_ReferenceFlood)'s traffic, at no less than 50 percent of the
device’s expected throughput.

# History
```yaml
-----
affected_psb: SEC-FOR-ATTCK
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
          forwarding devices.
    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-FOR-ATTCK
    issueref: ISS_Floods
    tags:
    - EN/PD
    - EN/PI
    - PSB/OnPrem
