# Headline 
Closed Base Software Authentication Root 

(was SEC-SW-BASECRYP-FR2)
# Behavior

The [authentication root](#DEF_AuthenticationRoot) used to check the
signature on [closed](#DEF_Closed) [base software](#DEF_BaseSoftware)
and [critical configuration data](#DEF_CriticalConfigurationData) _MUST_ be protected by a
[Root of Trust for Detection](#DEF_RootOfTrustForDetection).

Note that unless being [open](#DEF_Open) is a major part of the customer value proposition, the base software must be [closed](#DEF_Closed). 


# History

```yaml
-----
Deprecated_psb: SEC-SW-BASECRYP-FR2
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
    id: SEC-SW-BASEPROT-FR5
    issueref: ISS_SEC-SW-BASEPROT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
