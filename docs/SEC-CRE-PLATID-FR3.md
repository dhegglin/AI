# Headline
Platform Software Validation 

(was SEC-CRE-CHIPID-FR8)

# Behavior

Platform software _MUST_ validate the tamper-resistant chip-held
identity of the base and of all attached FRUs to ensure they are
authentic Cisco or supported third party hardware. If validation
fails, there _MUST_ be a management interface notification, and the
failing base or FRU _SHOULD_ be disabled.

# History
```yaml
-----
created: SEC-CRE-PLATID
description:  New requirement for platform/device hardware trust requirements
-----

affected_psb: SEC-CRE-CHIPID-8
description:  merged into this FR 
```

# Attributes

    id: SEC-CRE-PLATID-FR3
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
