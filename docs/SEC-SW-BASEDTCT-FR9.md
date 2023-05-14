# Headline 
PLD and MCU Symbionts 

(was SEC-HW-PROGDEV-FR4)

# Behavior
If PLD and/or MCU images are being loaded by or can be updated by [base software](#DEF_BaseSoftware), then these images _MUST_ undergo integrity validation by base software and access to these images _MUST_ not be allowed by non-base software such as the OS or OS-level applications. 

**Supplemental Guidance**: For example, if a device that is managing the board's power is left unprotected, the device could be altered to not turn on the board, resulting in a DoS. The device is protected by ensuring that a write protect disallows its configuration data from being altered and by integrity-checking its configuration data to ensure that no unauthorized modifications were made.

# History

```yaml
-----
affected_psb: SEC-SW-PROGDEV-FR4
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
    id: SEC-SW-BASEDTCT-FR9
    issueref: ISS_SEC-SW-BASEDTCT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
