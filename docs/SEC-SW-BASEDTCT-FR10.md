# Headline 
PLD and MCU Detection of Compromised Critical Configuration Data

# Behavior
If a PLD or MCU contains [critical configuration data](#DEF_CriticalConfigurationData) that is stored in Nonvolatile storage, then a separate (golden) copy of the [critical configuration data](#DEF_CriticalConfigurationData) must be stored which can be used for detection of the compromise. Such a golden copy _MUST_ be write protected after manufacturing phase. 



# History

```yaml
-----
affected_psb: SEC-SW-BASEDTCT
---
impact: normative
description: >
  Added new FR

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
    id: SEC-SW-BASEDTCT-FR10
    issueref: ISS_SEC-SW-BASEDTCT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
