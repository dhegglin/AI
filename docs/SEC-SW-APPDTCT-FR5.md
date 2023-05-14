# Headline 
Check all signatures before loading code

(was SEC-SW-LOADCHK-FR1)

# Behavior
At least one digital signature of signed code _SHOULD_ be checked, covering every checkable element defined by the loaded file format before executing or acting on any code from that file.

# History

```yaml
-----
Deprecated_psb: SEC-SW-LOADCHK-FR1
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
    version: 1
    id: SEC-SW-APPDTCT-FR5
    issueref: ISS_SEC-SW-APPDTCT
    tags:
    - EN/PD
    - EN/PI
    - G7
    - Image Signing
    - PSB/OnPrem
