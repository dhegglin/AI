# Headline 
Malformed Signatures 

(was SEC-SW-LOADCHK-FR7)

# Behavior
When performing signature checks prior to execution, closed code that is signed with an invalid or malformed signature _MUST_ always be rejected.

**Supplemental Guidance:** "Rejecting" the file means refusing to install, load, or execute any code from it or to otherwise act on its contents, other than to report the problem in a timely manner.

# History

```yaml
-----
Deprecated_psb: SEC-SW-LOADCHK-FR7
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
    id: SEC-SW-APPDTCT-FR9
    issueref: ISS_SEC-SW-APPDTCT
    tags:
    - EN/PD
    - EN/PI
    - G7
    - Image Signing
    - PSB/OnPrem
