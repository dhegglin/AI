# Headline 
Detection Policies

(was SEC-SW-DETECT-FR5)

# Behavior
The detection mechanism _MAY_ use policies defined by a platform administrator on what actions are taken by the [RoT for Detection](#DEF_RootOfTrustForDetection) (and/or Chain of Trust for Detection).


# History

```yaml
-----
affected_psb: SEC-SW-DETECT-FR5
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
          [base software](#DEF_BaseSoftware)
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 1
    id: SEC-SW-BASEDTCT-FR6
    issueref: ISS_SEC-SW-BASEDTCT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - PSB/OnPrem
