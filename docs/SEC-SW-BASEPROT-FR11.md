# Headline 
PLD and MCU Write Protection 

(was SEC-HW-PROGDEV-FR5)

# Behavior
If it is not possible to detect unauthorized alterations of a PLD's configuration bitstream or an MCU's code through image verification or DPA-resistant encryption, then the storage medium of the bitstream or code _MUST_ be unmodifiable. This read only medium _SHOULD_ also be protected with a physical enclosure or epoxy and an anti-counterfeit label to mitigate tamper. 

**Supplemental Guidance**: Be aware that the trade-off is that the code can no longer be updated. This includes updates that are patches or fix vulnerabilities which could result in RMA's and bricked units. Be advised to weigh the advantages and disadvantages.

# History

```yaml
-----
Deprecated_psb: SEC-SW-PROGDEV-FR5
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
    id: SEC-SW-BASEPROT-FR11
    issueref: ISS_SEC-SW-BASEPROT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
