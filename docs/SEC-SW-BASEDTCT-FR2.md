# Headline 
Time-of-Check--Time-of-Use

(was SEC-SW-BASECRYP-FR4)

# Behavior
[Time-of-Check/Time-of-Use (ToC/ToU)](#DEF_ToCToU) is an attack where changes in code occur between the time of checking code integrity and the time of using the code. 

If the CPU architecture plus the first-stage bootloader is not resistant to a ToC/ToU attack by design, then a ToC/ToU-resistant signature checking mechanism _MUST_ be used where available.



# History

```yaml
-----
affected_psb: SEC-SW-BASECRYP-FR4
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
    id: SEC-SW-BASEDTCT-FR2
    issueref: ISS_SEC-SW-BASEDTCT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
