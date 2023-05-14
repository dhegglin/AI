# Headline
Wrapping Signatures

# Behavior

If the native signature does not protect all of the data and metadata
listed under "data to be protected", then you _MUST_ provide
additional signatures to complete the protection. These are "wrapping"
signatures.

Unless community practice for a [user platform](#DEF_UserPlatform)
strongly favors another signing method, wrapping signatures _MUST_ be
provided in CMS/PKCS\#7 format. Wrapping signatures _SHOULD_ be
provided by embedding each installable unit together with its signature
in a single CMS/PKCS\#7 message, but _MAY_ be provided as detached
signatures (signatures in files separate from the signed data).

Every embedded or detached CMS/PKCS\#7 signature _MUST_ be bundled
with the entire [certificate](#DEF_Certificate) chain expected to be
used to validate that signature.

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
    id: SEC-SW-SIG-FR3
    issueref: ISS_SEC-SW-SIG
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
    - FAST
