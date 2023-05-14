# Headline 
Cryptographic Signature Verification of Base Software Updates

(was SEC-SW-BASEBASE-FR2)
# Behavior

Every [base installer](#DEF_BaseInstaller), which is a part of the
[base software](#DEF_BaseSoftware), _MUST_ internally verify
the cryptographic signatures on [base software](#DEF_BaseSoftware)
updates before installing them. Cryptographic Verification _MUST_
also be done on critical configuration data updates before installing them.

# History

```yaml
-----
Deprecated_psb: SEC-SW-BASEBASE-FR2
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
    id: SEC-SW-BASEPROT-FR2
    issueref: ISS_SEC-SW-BASEPROT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
