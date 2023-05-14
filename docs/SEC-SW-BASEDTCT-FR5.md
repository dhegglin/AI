# Headline 
Notification of Corruption

(was SEC-SW-DETECT-FR4)

# Behavior

All detected corruption _SHOULD_ be logged and reported.

# History

```yaml
-----
affected_psb: SEC-DETECT-FR4
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
          [base software](#DEF_BaseSoftware)
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 1
    id: SEC-SW-BASEDTCT-FR5
    issueref: ISS_SEC-SW-BASEDTCT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - PSB/OnPrem
