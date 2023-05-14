# Headline 
Closed Base Software Installer 

(was SEC-SW-BASEBASE-FR5)
# Behavior
Unless being [open](#DEF_Open) is a major part of the customer value proposition, [base software](#DEF_BaseSoftware) _MUST_ be
[closed](#DEF_Closed) and all [base software](#DEF_BaseSoftware)
involved in installing it _MUST_ also be [closed](#DEF_Closed), as
well as all trust information (i.e. keys) used to verify it.

# History

```yaml
-----
Deprecated_psb: SEC-SW-BASEBASE-FR5
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
    version: 1
    id: SEC-SW-BASEPROT-FR4
    issueref: ISS_SEC-SW-BASEPROT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
