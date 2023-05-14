# Headline 
Symbiont Detection Techniques

(was SEC-SW-DETECT-FR3)

# Behavior

A [symbiont](#DEF_SymbiontDevice) device _MAY_ rely on a host to implement a [Root of Trust for Detection](#DEF_RootOfTrustForDetection) and perform detection of changes to its [base software](#DEF_BaseSoftware). If the [symbiont](#DEF_SymbiontDevice) boots independently from the host, then the integrity of the symbiont firmware _MUST_ be checked prior to executing outside of the host chain of trust for detection.  The following additional requirements apply in these cases:
* The [symbiont](#DEF_SymbiontDevice) firmware _MUST_ be protected with the same or better protections given to [base software](#DEF_BaseSoftware).
* When a corruption is detected, the host _SHOULD_ be able to immediately trigger recovery for the [symbiont](#DEF_SymbiontDevice) followed by a restart of the symbiont device.

**Supplemental Guidance**: This FR relies on FR1 and FR2 of this requirement to detect changes to the symbiont's [base software](#DEF_BaseSoftware).

# History

```yaml
-----
affected_psb: SEC-SW-DETECT-FR3
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
          [base software](#DEF_BaseSoftware)
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 1
    id: SEC-SW-BASEDTCT-FR4
    issueref: ISS_SEC-SW-BASEDTCT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - PSB/OnPrem
