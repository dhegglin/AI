# Headline 
Open Base Software Authentication Root 

(was SEC-SW-BASECRYP-FR3)
# Behavior
[Open](#DEF_Open) [base software](#DEF_BaseSoftware) is
rare or nonexistent in Cisco products. If you do have
[open](#DEF_Open) [base software](#DEF_BaseSoftware), then it _MUST_ be possible to update the
[authentication root](#DEF_AuthenticationRoot) only with
an [administrator](#DEF_Administrator)-supplied value. Any such
update _MUST_ be done entirely by [base software](#DEF_BaseSoftware).
It _MUST NOT_ be possible for non-[base software](#DEF_BaseSoftware)
software to change the [authentication root](#DEF_AuthenticationRoot),
and the process _MUST_ require the [administrator](#DEF_Administrator)
to prove physical access to the [bounded computer](#DEF_BoundedComputer) whose
[base software](#DEF_BaseSoftware) is being updated.
# History

```yaml
-----
Deprecated_psb: SEC-SW-BASECRYP-FR3
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
    id: SEC-SW-BASEPROT-FR6
    issueref: ISS_SEC-SW-BASEPROT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
