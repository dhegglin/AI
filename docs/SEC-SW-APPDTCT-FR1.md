# Headline 
Check all signatures before installing code 

(was SEC-SW-INSCHK-FR1, SEC-SW-INSCHK-FR2 and SEC-SW-INSCHK-FR4)

# Behavior

At least one digital signature covering every element listed in SEC-SW-SIG _MUST_ be checked. For modules created by users and third parties, this includes elements that would be required to be signed if the same module were released by Cisco. For open code, this behavior is modifiable by the customer per [SEC-SW-ADMOPEN](#SEC-SW-ADMOPEN). Code that is unsigned, invalidly signed or incompletely signed _MUST_ be rejected.

**Supplemental Guidance:** A malformed or invalid signature is one where the actual signature does not match the purported signed data and/or generating key. "Rejecting" the module means refusing to install it or otherwise act on its contents, other than to report the problem.

# History

```yaml
-----
Deprecated_psb: SEC-SW-INSCHK-FR1
---
impact: nonnormative
description: >
  Break into discrete FR's
-----
Deprecated_psb: SEC-SW-INSCHK-FR2
---
impact: nonnormative
description: >
  Break into discrete FR's
  -----
Deprecated_psb: SEC-SW-INSCHK-FR4
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
    id: SEC-SW-APPDTCT-FR1
    issueref: ISS_SEC-SW-APPDTCT
    tags:
    - EN/PD
    - EN/PI
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
