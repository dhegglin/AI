# Headline 
Root of Trust for Detection

(was SEC-SW-DETECT-FR1)

# Behavior
A successful attack that corrupts or subverts the security of [base software](#DEF_BaseSoftware) or active [critical configuration data](#DEF_CriticalConfigurationData) _MUST_ not be able to impair the mechanism (also known as a [Root of Trust for Detection](#DEF_RootOfTrustForDetection) or RoT) that would detect and report that attack. Therefore, the RoT Detection _SHOULD_ be kept separate from the base software and/or critical configuration data. 

Supplemental Guidance: One way to accomplish this is to keep Roots of Trust for Detection separate from other RoTs. This requires that the detection mechanism itself is not stored in the same physical space as active base software and/or active critical configuration data. This also ensures that this isn't used by attackers as a route to make unauthorized updates. 


# History

```yaml
-----
affected_psb: SEC-SW-DETECT-FR1
---
impact: nonnormative
description: >
  Break into discrete FR's
-----

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
    id: SEC-SW-BASEDTCT-FR3
    issueref: ISS_SEC-SW-BASEDTCT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - PSB/OnPrem
