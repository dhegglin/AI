# Headline 
PLD and MCU Image Authentication 

(was SEC-HW-PROGDEV-FR2)

# Behavior
PLD and MCU images _MUST_ be authenticated before execution. 

PLDs and MCUs capable of performing a cryptographic image signature check _SHOULD_ be used in the hardware design. 

If the PLD or MCU is acting as the Root of Trust, then that device itself _MUST_ be able to authenticate its own images and/or use DPA resistant image decryption. 

If the PLD or MCU is not acting as the Root of Trust, then relying on another device in a [symbiont](#DEF_SymbiontDevice) relationship to perform authentication or decryption is acceptable. 


# History

```yaml
-----
affected_psb: SEC-SW-PROGDEV-FR2
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
    id: SEC-SW-BASEDTCT-FR8
    issueref: ISS_SEC-SW-BASEDTCT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
