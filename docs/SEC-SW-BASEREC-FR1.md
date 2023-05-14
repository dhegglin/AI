# Headline 
Storage of Recovery Code

# Behavior
The recovery mechanism _MUST_ be able to obtain authentic [base software](#DEF_BaseSoftware).
If that software or code is being stored locally in non-volatile memory, the [base software](#DEF_BaseSoftware) _MUST_ be protected from unathorized updates.

If that software or code is stored remotely, then the location of the image _MUST_ be configurable in the policies of the recovery mechanism.

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
    id: SEC-SW-BASEREC-FR1
    issueref: ISS_SEC-SW-BASEREC
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
