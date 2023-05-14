# Headline 
Check Data Integrity 

(was SEC-SW-DETECT-FR6)


# Behavior
[Critical Configuration Data](#DEF_CriticalConfigurationData) _MUST_ be checked for corruption and alteration using one of the following methods prior to use.
* Check a digital signature or cryptographic hash. A symbiont device may rely on the host to perform this check. 
* Compare it with known-good values 

Device-specific critical configuration data such as license information _SHOULD_ be bound to the device identity [see SEC-HW-IDTRUST](#SEC-HW-IDTRUST) such that it only functions for that unique device (e.g., a valid device-specific license should be invalid on any device other than the one from which it was originally copied).

# History

```yaml
-----
affected_psb: SEC-SW-DETECT-FR6
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
    id: SEC-SW-BASEDTCT-FR7
    issueref: ISS_SEC-SW-BASEDTCT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - PSB/OnPrem
