# Headline 
Write-Protect Base Software 

(was SEC-SW-BASEBASE-FR1)
# Behavior

Non-[base software](#DEF_BaseSoftware) _MUST NOT_ be able to overwrite,
corrupt, or otherwise prevent the execution of all usable copies
of any [stage](#DEF_Stage) of [base software](#DEF_BaseSoftware)
or [critical configuration data](#DEF_CriticalConfigurationData) (including factory defaults).

# History

```yaml
-----
Deprecated_psb: SEC-SW-BASEBASE-FR1
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
    id: SEC-SW-BASEPROT-FR1
    issueref: ISS_SEC-SW-BASEPROT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
