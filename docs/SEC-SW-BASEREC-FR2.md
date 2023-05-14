# Headline 
Recovery Performance

# Behavior
The device _MUST_ either implement its own recovery functionality, or as a [symbiont](#DEF_SymbiontDevice) the device together with its host _MUST_ implement the device's recovery capability. In the symbiont relationship the host performs the cryptographic signature verification of the device’s recovery image.




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
    id: SEC-SW-BASEREC-FR2
    issueref: ISS_SEC-SW-BASEREC
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
