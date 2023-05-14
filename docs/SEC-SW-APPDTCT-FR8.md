# Headline 
Protect Signature Verification Elements 

(was SEC-SW-INSCHK-FR7)


# Behavior

Controlled space and/or good cryptography _MUST_ be used to assure that no code, authentication roots, or other material trusted for signature verification can be modified without the consent of the appropriate controlling policy entity.

**Supplemental Guidance**: [SEC-SW-BASEDTCT](#SEC-SW-BASEDTCT) applies additional rules for base software.

# History

```yaml
-----
Deprecated_psb: SEC-SW-INSCHK-FR7
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
    id: SEC-SW-APPDTCT-FR8
    issueref: ISS_SEC-SW-APPDTCT
    tags:
    - EN/PD
    - EN/PI
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
