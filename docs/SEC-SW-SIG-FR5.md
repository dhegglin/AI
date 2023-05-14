# Headline
Code-signing Keys

# Behavior

The keys used to sign internal development builds _MUST_ be different
from the [release keys](#DEF_ReleaseKey) used to sign code released
to customers or other users outside of Cisco.

Internal development builds _MUST_ _NOT_ be installable or executable on production
Cisco offerings without authorized modification to enable them to
execute development software.

**Supplemental Guidance:** [Cisco Consent Token](https://wiki.cisco.com/display/STOCT/Consent+Token) 
can be used to enable production offerings to execute internal development 
builds.

# History

```yaml
-----
affected_psb: SEC-SW-SIG-4
---
impact: normative
description: >
  Added "Code Signing Keys" FR5
  Added "Cisco controlled Packaging Systems" FR6
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
    id: SEC-SW-SIG-FR5
    issueref: ISS_SEC-SW-SIG
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
    - FAST
