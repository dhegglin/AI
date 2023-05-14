# Headline 
Recovery Image Updates

# Behavior
If the recovery mechanism and active critical configuration data are updatable, then the recovery mechanism, active critical configuration data, and/or [base software](#DEF_BaseSoftware) _MUST_ be updated in the same manner as [base software](#DEF_BaseSoftware) or by an authorized administrator.

**Supplemental Guidance**: For example, component 'A' has updatable recovery mechanism. Component 'A' is also unable to perform cryptography, but it is connected to a Secured CPU 'B' through a chain of trust.  That Secure CPU 'B' is able to do cryptography and verifies the cryptographic signature for Component 'A' then updates the recovery mechanism for component 'A'. Refer to [SEC-SW-BASEPROT](#SEC-SW-BASEPROT) for information on base software updates.  Refer also to [symbiont device](#DEF_SymbiontDevice).

# History

```yaml
-----
Deprecated_psb: SEC-SW-BASEREC-1
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
    version: 2
    id: SEC-SW-BASEREC-FR10
    issueref: ISS_SEC-SW-BASEREC
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
