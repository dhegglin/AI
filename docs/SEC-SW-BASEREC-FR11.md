# Headline 
Recovery of PLD and MCU Compromised Code

# Behavior

If a PLD or MCU contains Code that is stored in Nonvolatile storage, then following techniques can be used to recover from the compromise. 

- Maintaining Golden / Upgrade copies of code could be maintained, and Golden copy must be write protected from any updates. 
- Maintaining two copies code with alternatively updating while write protecting 2nd copy of the code during update _SHOULD_ be done, to prevent corrupting both copies. 

# History

```yaml
-----
Deprecated_psb: SEC-SW-BASEREC-1
---
impact: normative
description: >
  Added details for PLD and MCU

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
          product code
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 2
    id: SEC-SW-BASEREC-FR11
    issueref: ISS_SEC-SW-BASEREC
    tags:
    - EN/PD
    - G7
    - Image Signing
    - PSB/OnPrem
