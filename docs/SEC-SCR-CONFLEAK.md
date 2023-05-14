# Headline

Do not expose critical data

# Description

Eliminate, encrypt, hash, or protect all [critical](#DEF_Critical) data such as [passwords](#DEF_Passphrase), [credentials](#DEF_Credential), [cryptographic secrets](#DEF_CryptographicSecret), and any  other [critical](#DEF_Critical) configuration information by default.  This includes passwords in configuration files that can be read when copied to an open directory.

Any environment that fails to protect [critical](#DEF_Critical) data exposes the [offering](#DEF_Offering) to unnecessary risk.

When using keys to encrypt [critical](#DEF_Critical) data, ensure that these keys are isolated and stored securely.

# Behavior

Eliminate, encrypt, hash, or protect all [critical](#DEF_Critical) data stored anywhere in your [offering](#DEF_Offering) even if the location isn't exposed.

## SEC-SCR-CONFLEAK-FR1:  Development Environment

The development environment _MUST_ protect against [critical](#DEF_Critical) data exposure.  This includes software repositories, file systems, build automation tools such as Jenkins, PCB designs, Gerber files, or any specification that would provide information to attackers or counterfeiters.

**Supplemental Guidance**:  Development environments are often overlooked and may be an easy attack vector.

## SEC-SCR-CONFLEAK-FR2:  Outside Controlled Space

The [offering](#DEF_Offering) _MUST_ protect [critical](#DEF_Critical) data outside of a its [controlled space](#DEF_ControlledSpace).

This includes any offering-internal storage in which the [offering](#DEF_Offering) will not reliably identify or treat the affected information according to its sensitivity such as a file, database, or other storage accessible via file managers, Web servers, backup systems, or other general-purpose storage management or access systems.

Third party software included in the [offering](#DEF_Offering) may require [critical](#DEF_Critical) data to be in their configuration files.  Access to this [critical](#DEF_Critical) data _MUST_ be limited to controlled environments.

Protection of data may be achieved using secure storage.  Cisco has a number of proprietary solutions including Trust Anchor Modules such as a TPm, ACT-2 or Aikido.  On general purpose hardware there are solutions based on vTPM which are integrated with HSM modules.  Commercial solutions include Hashicorp Vault, Conjur, and AWS Secrets Manager.

**Supplemental Guidance**: Examples of uncontrolled environment may include a full or partial copy of a device configuration file on the local or remote file system that can be viewed or edited.  Interactive displays, except for displays which exist *only* to show [critical](#DEF_Critical) data are also considered uncontrolled space.

## SEC-SCR-CONFLEAK-FR3:  Administrative Critical Data

If administrators must be able to edit and maintain plain text files with critical data, then these files _MUST_NOT_ be accessible for non-administrative users. This protection _MAY_ take the form of limited file privileges, access credentials, or other mechanism.

If you provide functions to make it easier for [administrators](#DEF_Administrator) to copy affected configuration information from one offering instance to another, then you _MUST_ provide a way to encrypt the transferred data using a key provided by the [administrator](#DEF_Administrator). Such a function _MUST_NOT_ include unencrypted affected information without specific, explicit [administrator](#DEF_Administrator) direction to do so.

## SEC-SCR-CONFLEAK-FR4:  Key Encryption Storage

The keys used for the encryption (also known as key encryption keys) are themselves [cryptographic secrets](#DEF_CryptographicSecret) and [critical](#DEF_Critical) data. Therefore any such key _MUST_NOT_ be stored unencrypted.

# Informative References

[Cisco Trustworthy Technologies](https://cisco.sharepoint.com/Sites/TrustworthyTechnologies)

[Cisco Common Security Modules](https://cisco.sharepoint.com/Sites/CommonSecurityModules)

[Cisco TAm Services](https://apps.na.collabserv.com/communities/service/html/communitystart?communityUuid=04b7660c-7ea5-446d-acb1-3eb54351ecdb)

<https://wwwin-github.cisco.com/CSDL/PSB/wiki/Where-to-store-that-key>

# History

```
-----
affected_psb: SEC-SCR-CONFLEAK-3
---
deprecated_psb: SEC-SCR-CONFLEAK-2
impact: non-normative
headline: >
    [SEC-SCR-CONFLEAK-2](#SEC-SCR-CONFLEAK-2) migrated to functional requirements.
```

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-CRY-ALWAYS
    relation: connects
    headline: >
        [SEC-CRY-ALWAYS](#SEC-CRY-ALWAYS) Encrypt all non-public data outside of the controlled space.
    ---
    source: PSB
    foreign_id: SEC-PWD-STORE
    relation: connects
    headline: >
        [SEC-PWD-STORE](#SEC-PWD-STORE) Irreversibly hash non-recoverable passwords.

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    waivable: true
    version: 3
    id: SEC-SCR-CONFLEAK
    issueref: ISS_DataMishandled
    tags:
    - EN/PD
    - Critical PSB
    - CloudCritical
    - PSB/OnPrem
    - Cloud
