# Headline
Physical Integration

(was SEC-CRE-CHIPID-FR3)


# Behavior
The chip _MUST_ be physically integrated into the [turnkey module](#DEF_TurnkeyModule) by soldering or crimping to a critical system component, such as a mainboard, such that it cannot easily be removed without rendering the credential storage chip (and possibly the turnkey module) unusable. 


# History
```yaml
-----
created: SEC-CRE-PLATID
description:  New requirement for platform/device hardware trust requirements
-----

affected_psb: SEC-CRE-CHIPID-3
description:  merged into this FR 

```

# Attributes

    id: SEC-CRE-PLATID-FR2
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
    priority: 10
    phase: requirements
    tags:
        - EN/PD
        - G7
        - PSB/OnPrem
        - Critical PSB
