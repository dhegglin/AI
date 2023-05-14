# Headline 
Sign All Code

# Behavior

Every released version of any Cisco-branded or Cisco-provided
[code](#DEF_Code) _MUST_ be protected by one or more digital
signatures made using [good cryptography](#DEF_GoodCryptography).

You _MUST_ sign *all* data having anything to do with any code you
are distributing. Note that the definition of "[code](#DEF_Code)"
is very broad and includes things you may not think of as programs.
Data also includes static assets such as images, HTML, audio.  Libraries
that process these files may have vulnerabilities that can compromise the system.

# History

```yaml
-----
affected_psb: SEC-SW-SIG-3
---
impact: nonnormative
description: >
  Break into discrete FR's
-----
affected_psb: SEC-SW-SIG-3
---
impact: normative
description: >
  Add requirements for loadtime signature checks.
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
    version: 5
    id: SEC-SW-SIG-FR1
    issueref: ISS_SEC-SW-SIG
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
    - FAST
