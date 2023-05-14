# Headline 
Recovering Critical Configuration Data

# Behavior
When recovering the critical configuration data, the recovery mechanism _MUST_ recover at least its [factory defaults](#DEF_FactoryDefault). However, the system _SHOULD_ recover to the last known-good critical configuration data. This can be done with the help of a [rollback mechanism](#DEF_Rollback).

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
    priority: 10
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
    id: SEC-SW-BASEREC-FR6
    issueref: ISS_SEC-SW-BASEREC
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
