# Headline 
Software Debugger Attacks

(was SEC-SW-BASECONT-FR3)
# Behavior
Attacks through software debugging interfaces such as embedded
debuggers _MUST NOT_ be made able to subvert the
[base software](#DEF_BaseSoftware) itself, and _SHOULD NOT_ be
available at all in [closed](#DEF_Closed)
[base software](#DEF_BaseSoftware). Most of these debuggers are
forbidden outright; see [SEC-CSP-NOCDBG](#SEC-CSP-NOCDBG).

# History

```yaml
-----
Deprecated_psb: SEC-SW-BASECONT-FR3
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
    id: SEC-SW-BASEPROT-FR9
    issueref: ISS_SEC-SW-BASEPROT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
