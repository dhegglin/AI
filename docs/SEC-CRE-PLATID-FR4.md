# Headline
Single Source of Device Identity

(was SEC-CRE-IDFORM-FR2)

# Behavior

All device operations utilizing device identity such as licensing
implementations and device inventory _MUST_ be sourced from the device
identity certificate. This includes exposing product ID and
serial number through HMI or CLI display, or through management protocols
such as SNMP or NetConf/Restconf. It also includes feature enablement such
as performance level and number of supported interfaces.

Identity from any other source such as IDPROM or PCAMAP _MUST NOT_ be used. 

# History
```yaml
-----
created: SEC-CRE-PLATID
description:  New requirement for platform/device hardware trust requirements
-----

affected_psb: SEC-CRE-IDFORM-FR2
description:  merged into this FR 

```

# Attributes

    id: SEC-CRE-PLATID-FR4
    version: 1
    category: Boot and System Integrity
    riskArea: System Integrity
    legallysensitive: false
    waivable: true
    issueref: ISS_SEC-CRE-PLATID
    applicability:
      - force: mandatory
        target:
          restrict: >
            [turnkey modules](#DEF_TurnkeyModule)
    priority: 8
    phase: requirements
    tags:
        - EN/PD
        - G7
        - PSB/OnPrem
