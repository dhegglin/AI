# Headline 
Protecting the factory default update process.

(was SEC-SW-BASEDFLT-FR1)
# Behavior
If the [critical configuration data](#DEF_CriticalConfigurationData) factory defaults are updatable, then the updates _MUST_ be authenticated. 

**Supplemental Guidance:** Refer to SEC-SW-BASEPROT for information on [base software](#DEF_BaseSoftware) updates. 

# History

```yaml
-----
Deprecated_psb: SEC-SW-BASEDFLT-FR1
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
    id: SEC-SW-BASEPROT-FR13
    issueref: ISS_SEC-SW-BASEPROT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
