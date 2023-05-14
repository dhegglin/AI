# Headline 
Protection of PLD and MCU Critical Configuration Data

(was SEC-HW-PROGDEV-FR1)
# Behavior
If a Programmable Logic Device (PLD) or Microcontroller (MCU) contains [Critical Configuration Data](#DEF_CriticalConfigurationData) that must be kept confidential, then the configuration image of this device _MUST_ be encrypted using a Differential Power Analysis (DPA) resistant industry standard encryption mechanism.

**Supplemental Guidance**: Early encryption implementations offered by FPGA vendors were not resistant to DPA attacks and the private encryption key could be easily discerned. Encryption using devices without DPA resistance is NOT allowed for new designs.

**Supplemental Guidance**: If a PLD or MCU contains Critical Configuration Data that is stored in Nonvolatile storage, the following are some techniques that can be used to protect the Critical Configuration Data. 

* update data only from base software, and within the update routine implement bound checking/sanity checking 
* if data is immutable (like MAC address or serial number), simply write protect it after the manufacturing phase


# History

```yaml
-----
Deprecated_psb: SEC-HW-PROGDEV-FR1
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
    id: SEC-SW-BASEPROT-FR10
    issueref: ISS_SEC-SW-BASEPROT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
