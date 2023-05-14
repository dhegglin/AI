# Headline 
Recovery Policies

# Behavior
The device _MUST_ use policies that are not stored as critical configuration data by the device to recover its own critical configuration data. As a solution to this, a [symbiont device](#DEF_SymbiontDevice) _MAY_ use policies that are provided by a host device.

**Supplemental Guidance**:  An Example of this in practice would to have two components capable of protecting [base software](#DEF_BaseSoftware) and have each component store the other's recovery policies in a critical configuration data store. When recovery is initiated, the two components coordinate to gather each others' policies. They could also, if capable, perform the recovery for each other taking turns as a symbiont.

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
    id: SEC-SW-BASEREC-FR8
    issueref: ISS_SEC-SW-BASEREC
    tags:
    - EN/PD
    - G7
    - Image Signing
    - PSB/OnPrem
