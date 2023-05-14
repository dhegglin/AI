# Headline 
Cryptographic Signature Verification 

(was SEC-SW-BASECRYP-FR1)

# Behavior

Before the first [mutable](#DEF_Mutable) [code](#DEF_Code) is
executed after power-up or reset of a
[bounded computer](#DEF_BoundedComputer), a
[Root of Trust for Detection](#DEF_RootOfTrustForDetection) _MUST_ check its
cryptographic signature. If the signature is missing or invalid,
the code _MUST NOT_ be executed.


# History

```yaml
-----
Deprecated_psb: SEC-SW-BASECRYP-FR1
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
          [base software](#DEF_BaseSoftware)
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 1
    id: SEC-SW-BASEDTCT-FR1
    issueref: ISS_SEC-SW-BASEDTCT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
