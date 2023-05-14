# Headline 
Hardware Probing Attacks 

(was SEC-SW-BASECONT-FR2)

# Behavior

Possible attacks on [base software](#DEF_BaseSoftware) [controlled](#DEF_ControlledSpace) [execution space](#DEF_ExecutionSpace) through hardware probing such as JTAG (see [SEC-HW-NOJTAG](#SEC-HW-NOJTAG)) or DCI (Direct Connect Interface) _MUST_ be blocked or require authentication. 


# History

```yaml
-----
Deprecated_psb: SEC-SW-BASECONT-FR2
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
    id: SEC-SW-BASEPROT-FR8
    issueref: ISS_SEC-SW-BASEPROT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
