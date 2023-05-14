# Headline

Protection of Factory Defaults 
(was SEC-SW-BASEDFLT-FR3)

# Behavior

The device shall protect its [core software's](#DEF_CoreSoftware) factory defaults
at least as well as it protects its core software. Note that SEC-SW-BASEPROT-FR1
already mandates protection of [base software](#DEF_BaseSoftware) (a subset of core software)
factory defaults. This requirement extends the protection to all core software factory defaults.
An example would be the kernel's boot parameters. They must be protected in the
same manner as the kernel code itself.

# History

```yaml
-----
Deprecated_psb: SEC-BASEDFLT-FR3
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
    id: SEC-SW-BASEPROT-FR12
    issueref: ISS_SEC-SW-BASEPROT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
