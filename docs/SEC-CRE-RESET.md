# Headline

Support and document offering recovery due to credential loss

# Description

The customer must be able to erase all user data and restore the [offering](#DEF_Offering) to its factory state.  This provides some security against attackers that get physical access to [offerings](#DEF_Offering) from gleaning configuration information.  In specific instances where the [offering](#DEF_Offering) is unable to erase user data during recovery due to limitations imposed by device vendors, the documentation must indicate which device(s) must be erased by the customer using instructions provided by the device vendor.

Erasing user data may also offer a convenient way of restoring the device to its factory state to be repurposed or resold.  Note that SEC-DAT-CLNSTATE lists the requirements for erasing data.

Note that restoring the [offering](#DEF_Offering) to its factory state does not require removing official Cisco images.  Cisco provided images may remain on the system as these are official images that provide no customer specific information and do not pose a security risk.

[Offering](#DEF_Offering) recovery is not a secret and should be documented publicly.

# Behavior

## SRC-CRE-RESET-FR1: Independent Recovery

The [offering](#DEF_Offering) _MUST_ provide a means for the [administrator](https://cserv.cisco.com/library/glossary/CG11) to recover control when all [administrator](https://cserv.cisco.com/library/glossary/CG11) [credentials](https://cserv.cisco.com/library/glossary/CG87) have been lost.

[Administrators](https://cserv.cisco.com/library/glossary/CG11) _MUST_ be able to recover the [offering](#DEF_Offering) without involving Cisco or any third party, and without involving any system operated or administered by Cisco or any third party.

Recovery _MUST_NOT_ depend on the [administrator](https://cserv.cisco.com/library/glossary/CG11)'s possessing any cryptographic dongles, smart cards[, passphrases](https://cserv.cisco.com/library/glossary/CG43), cryptographic keys, or other material which the [administrator](https://cserv.cisco.com/library/glossary/CG11) can't create, even if they are included with the [offering](#DEF_Offering).

## SEC-CRE-RESET-FR2: Recovery via Clean State

An [offering](#DEF_Offering) _MUST_ support restoring to a [clean state](#DEF_CleanState) as a recovery mechanism.

Entering a [clean state](#DEF_CleanState) _MUST_ be the default behavior for recovering from lost administrative credentials for any [offering](#DEF_Offering).

**Supplemental Guidance:**  As an example, deleting a VM is a valid method of recovering to a clean state.  Recovery via Clean State means that any activation key is removed from the product.

## SEC-CRE-RESET-FR3: Pre-Configure Recovery

Additional recovery behaviors, including less comprehensive configuration erasure _MAY_ be supported when configured by the [administrator](#DEF_Administrator).  Such behavior _MUST_ be made in advance as part of the active configuration process and while the [administrator](#DEF_Administrator) is still in possession of valid access [credentials](#DEF_Credential).

**Supplemental Guidance:**  As an example, recovering administrative credentials via email is valid if this is a preconfigured method of recovery and the email address was set before the credential loss.

## SEC-CRE-RESET-FR4: Document Recovery

The method for [offering](#DEF_Offering) recovery _MUST_ be fully described in the customer documentation.  Documenting the procedure reduces support calls and improves customer satisfaction.

In specific instances where the [offering](#DEF_Offering) is unable to erase user data during recovery due to limitations imposed by device vendors, the documentation _MUST_ clearly indicate which device(s) must be erased by the customer using instructions provided by the device vendor.  Examples of this may include Self-Encrypted Drives, Intel DCPMMs when security is enabled and TPMs.

# History

```yaml
-----
affected_psb: SEC-CRE-RESET
description:  Aggregated related requirements into functional requirements.
---
deprecated_psb: SEC-DOC-RESET
impact: non-normative
headline: >
  [SEC-DOC-RESET](#SEC-DOC-RESET) migrated to SEC-CRE-RESET-FR4
---
deprecated_psb: SEC-ERA-DATA-2
impact: non-normative
headline: >
  [SEC-ERA-DATA-2](#SEC-ERA-DATA-2) migrated to SEC-CRE-RESET-FR2
---
deprecated_psb: SEC-RES-LOSS-2
impact: normative
headline: >
  [SEC-RES-LOSS-2](#SEC-RES-LOSS-2) migrated to SEC-CRE-RESET-FR1, SEC-CRE-RESET-FR3
---
deprecated_psb: SEC-PHY-ACCESS
impact: normative
headline: >
  [SEC-PHY-ACCESS](#SEC-PHY-ACCESS) deprecated SEC-PHY-ACCESS as physical access is no longer required.  Most devices are managed over the console port or are virtual devices.
```

# Requirement References

```
---
source: PSB
foreign_id: SEC-DAT-CLNSTATE
relation: connects
headline: >
    [SEC-DAT-CLNSTATE](#SEC-DAT-CLNSTATE) Securely purge all physical storage to enter a clean state and protect sensitive dataEnsures credentials cannot be recovered after device is cleaned
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    waivable: true
    version: 1
    id: SEC-CRE-RESET
    issueref: ISS_ResetHow
    tags:
    - EN/PI
    - PSB/OnPrem
