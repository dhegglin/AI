# Headline

Let customers control open signature checks

# Key Benefits

Allowing customers to control signature verification is fundamental to
the concept of an [open](#DEF_Open) product. Without this ability,
customers would be unable to modify the standard software. However,
actually changing this configuration setting obviously has serious
security implications, and it must therefore be tightly controlled.

# Description

For [open](#DEF_Open) software, allow customers to configure
checking Cisco-generated signatures, checking third party or
customer-generated signatures, neither, or both.

# Behavior

## SEC-SW-ADMOPEN-FR2: Configure Cisco signature checks
The [administrator](#DEF_Administrator) _MUST_ be able to configure
whether signature checking is performed specifically for Cisco-generated signatures.
## SEC-SW-ADMOPEN-FR3: Configure non-Cisco signature checks
The [administrator](#DEF_Administrator) _MUST_ be able to configure
whether customer-provided or third-party signatures are checked and which trusted roots are used.
## SEC-SW-ADMOPEN-FR4: Configure signature formats
If the signature checking system supports multiple algorithms or
    signature or [certificate](#DEF_Certificate) formats, the [administrator](#DEF_Administrator) _MUST_ be able to configure which
    algorithms and formats are accepted.
## SEC-SW-ADMOPEN-FR5: Configure invalid signature behavior
The [administrator](#DEF_Administrator) _SHOULD_ be able to configure
the system to completely refuse to load or install [code](#DEF_Code)
with invalid signatures, or to load or install them with warnings or log
entries.
## SEC-SW-ADMOPEN-FR6: Default signature checking behavior
Unless customer-provided or third-party [code](#DEF_Code) is expected to
be the rule rather than the exception, by default all Cisco-generated
signatures _SHOULD_ be checked. By default[, code](#DEF_Code) with
missing or invalid Cisco signatures _SHOULD_ _NOT_ be loaded or
installed. Customer-provided or third-party signatures _SHOULD_ be
handled similarly once appropriate trust roots have been configured.
## SEC-SW-ADMOPEN-FR7: Signature checking granularity
It _SHOULD_ be possible to configure the signature checking settings independently for
different classes of [code](#DEF_Code), with the available classes
including at least [base software](#DEF_BaseSoftware), chain loaders, operating system kernels and user-space software.
## SEC-SW-ADMOPEN-FR8: Immutability of signature checking settings
On a [standalone device](#DEF_StandaloneDevice), it _SHOULD_ be
possible for the [administrator](#DEF_Administrator) to “lock” the signature checking
setting such that the Cisco-provided software will not permit it to be
changed without restoring the device to a [clean state](#DEF_CleanState)
using a procedure requiring physical access to the device hardware.
## SEC-SW-ADMOPEN-FR9: Adherence to other signature verification requirements
Subject to these limitations and exceptions, the actual signature
verification _MUST_ be done by the methods described in
[SEC‑SW‑INSCHK](#SEC-SW-INSCHK) and [SEC_SW_LOADCHK](#SEC-SW-LOADCHK).

# History
```yaml
-----
affected_psb: SEC-SW-ADMOPEN
---
impact: non-normative
description: >
  Cosmetic updates. Conformance to new PSB template.
```

## Older history (manually maintained; may be incomplete)

PSBCTR 5.0: Added

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          loaders and installers
                      processing opencode
                      which might carry digital signatures.

    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 1
    id: SEC-SW-ADMOPEN
    issueref: ISS_NotReallyOpen
    tags:
    - EN/PI
    - PSB/OnPrem
