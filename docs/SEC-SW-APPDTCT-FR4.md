# Headline 
Closed code must use Cisco installers 

(was SEC-SW-INSCHK-FR8)

# Behavior
Closed code from Cisco-provided modules and packages _MUST_ always be installed using closed Cisco-provided installers.

# History

```yaml
---
Deprecated_psb: SEC-SW-INSCHK-FR8
---
impact: non-normative
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
          product [closed](#DEF_Closed) code
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 1
    id: SEC-SW-APPDTCT-FR4
    issueref: ISS_SEC-SW-APPDTCT
    tags:
    - EN/PD
    - EN/PI
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
