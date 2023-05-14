# Headline 
Recovery Log 

# Behavior
If the recovery mechanism is capable of logging recovery events, then recovery mechanism _MUST_ do so. In addition, the recovery mechanism _SHOULD_ be able to report recovery events.

**Supplemental Guidance**: It is also acceptable that the recovery mechanism requests approval from a user or system administrator before performing recovery. This is also applicable to the case where corruption is detected automatically and settings for [base software](#DEF_BaseSoftware) would be recovered.



# History

```yaml
-----
Deprecated_psb: SEC-SW-BASEREC-1
---
impact: nonnormative
description: >
  Break into discrete FR's

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        class: 
        restrict: |-
          product code
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 2
    id: SEC-SW-BASEREC-FR5
    issueref: ISS_SEC-SW-BASEREC
    tags:
    - EN/PD
    - G7
    - Image Signing
    - PSB/OnPrem
