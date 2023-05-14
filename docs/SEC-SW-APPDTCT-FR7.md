# Headline 
Cisco controlled Authentication Roots

(was SEC-SW-LOADCHK-FR5)

# Behavior

You _MUST_ rely only on Cisco controlled authentication roots, whether created by Cisco or some other intended provider of the code being loaded (see also [SEC-AUT-DEFROOT](#SEC-AUT-DEFROOT)). For example, if you include software in your offering signed by a 3rd party, then ensure the signature is verified by a key from that provider. If you include code signed by Cisco, then ensure the signature can only be verified by the intended Cisco key.

# History

```yaml
-----
Deprecated_psb: SEC-SW-LOADCHK-FR5
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
          product [closed](#DEF_Closed) code
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 1
    id: SEC-SW-APPDTCT-FR7
    issueref: ISS_SEC-SW-APPDTCT
    tags:
    - EN/PD
    - EN/PI
    - G7
    - Image Signing
    - PSB/OnPrem
