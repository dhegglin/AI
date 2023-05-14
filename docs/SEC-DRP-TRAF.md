# Headline

Silently drop denied traffic

# Key Benefits

Silently dropping denied packets provides an attacker with no
information as to which device is filtering the packets or why.

# Behavior

## SEC-DRP-TRAF-FR1: Silently Drop Denied Traffic

When filtering packets, it _MUST_ be possible to drop denied traffic
without generating any reply to the sender. For example, it must be
possible to configure a router to drop IPv4 packets without returning
ICMP “administratively prohibited” messages.

# History
```yaml
-----
affected_psb: SEC- DRP-TRAF
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
    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-DRP-TRAF
    issueref: ISS_ACLDiscovery
    tags:
    - EN/PI
    - PSB/OnPrem
    - EN/PI DT
    - EN/PI DT
