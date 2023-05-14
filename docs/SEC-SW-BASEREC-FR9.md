# Headline 
Recovery Protection

# Behavior
The recovery mechanism _MUST_ be protected against unauthorized modification with the same level of protection given to [base software](#DEF_BaseSoftware). 

The [Root of Trust for Recovery](#DEF_RootOfTrustForRecovery) (or Chain of Trust for Recovery) and recovery images _SHOULD_ be protected independently from running [base software](#DEF_BaseSoftware).

**Supplemental Guidance**: These protections can be achieved with mechanisms explained in [SEC-SW-BASEPROT-FR1](#SEC-SW-BASEPROT-FR1) through FR9.

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
    id: SEC-SW-BASEREC-FR9
    issueref: ISS_SEC-SW-BASEREC
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
