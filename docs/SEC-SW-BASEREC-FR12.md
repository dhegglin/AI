# Headline 
Recovering Factory Defaults 
(was SEC-SW-BASEDFLT-FR2)

# Behavior

When performing recovery of a device's core software factory defaults, the Root of Trust for Recovery or Chain of Trust for Recovery MUST be able to recover to known-good factory defaults. 

Recovery of factory defaults MUST occur: 

- When corruption of core software is detected. 
- When core software is being recovered. 
- A device is required to return to a clean state. 
- An Administrator initiates recovery of base software or wants to reset the device to factory defaults. 
- If core software factory defaults are being recovered or reset to factory defaults by an Administrator. 

# History

```yaml
-----
Deprecated_psb: SEC-SW-BASEDFLT
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
          product code
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 2
    id: SEC-SW-BASEREC-FR12
    issueref: ISS_SEC-SW-BASEREC
    tags:
    - EN/PD
    - G7
    - Image Signing
    - PSB/OnPrem
