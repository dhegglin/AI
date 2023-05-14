# Headline 
Check all subsidiary module signatures on installation

(was SEC-SW-INSCHK-FR11)

# Behavior

If a module or package being installed includes subsidiary modules or packages which are also installed for immediate use, then all of the required signature checks _MUST_ be applied to each of those subsidiary modules or packages. If the subsidiary packages are not actually installed for use but are stored for possible future installation, their signatures _SHOULD_ be checked.

# History

```yaml
-----
Deprecated_psb: SEC-SW-INSCHK-FR11
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
          product [closed](#DEF_Closed) code
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 1
    id: SEC-SW-APPDTCT-FR2
    issueref: ISS_SEC-SW-APPDTCT
    tags:
    - EN/PD
    - EN/PI
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
