# Headline 
Protect the Base Software Installer 

(was SEC-SW-BASEBASE-FR3)
# Behavior

The [code](#DEF_Code) and critical configuration data 
needed to verify the new software _MUST_ be embedded in the
[base installer](#DEF_BaseInstaller) or protected by the
[Root of Trust for Detection](#DEF_RootOfTrustForDetection).
This includes public keys ([authentication roots](#DEF_AuthenticationRoot))
used to verify the new software or hashes used to
verify such keys if the verification keys are provided with the
updates themselves.

# History

```yaml
-----
Deprecated_psb: SEC-SW-BASEBASE-FR3
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
    id: SEC-SW-BASEPROT-FR3
    issueref: ISS_SEC-SW-BASEPROT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
