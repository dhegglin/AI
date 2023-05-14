# Headline
No default credentials

# Description
Default credentials are the most frequent source of PSIRT cases at Cisco.

You cannot have default passwords except for installation. Authentication must require unique credentials created by the customer or generated at random by customer request. 

[Authentication roots](#DEF_AuthenticationRoot), which include passwords, X.509 CAs, keys, server certificates, etc., provide the basis of trust in all [offerings](#DEF_Offering). These authentication roots as well as keys derived from these authentication roots can be used for authentication purposes.  For this reason it is important to only include essential authentication roots in the product.

Increasing the number of [authentication roots](#DEF_AuthenticationRoot) increases the risk of abuse and authentication bypass vulnerabilities. Provide only essential ones.

# Behavior

This requirement forbids any non-essential predefined credential (e.g. default credential) use on any instance of the [offering](#DEF_Offering), even if it's specific to that particular instance.

Non-essential [authentication roots](#DEF_AuthenticationRoot) are forbidden in the [offerings](#DEF_Offering); it is not sufficient to disable non-essential predefined [authentication roots](#DEF_AuthenticationRoot) by default.

You _MUST_NOT_ include any default credentials in your offering, with the following very limited exceptions for essential [authentication roots](#DEF_AuthenticationRoot), all of which have restrictions.

Essential authentication roots, which are permitted, are identified in the functional requirements.

## SEC-AUT-DEFROOT-FR1: DNS Root Keys

[Offerings](#DEF_Offering) _MAY_ include public DNSSEC key-signing keys for the DNS root zone and _SHOULD_ enable it by default as specified in [SEC-DNS-SECURE](#SEC-DNS-SECURE).

## SEC-AUT-DEFROOT-FR2: Certificate Authorities

[Offerings](#DEF_Offering) _MAY_ include and trust by default only approved X.509 CAs as described in [SEC-509-TRUST](#SEC-509-TRUST).

## SEC-AUT-DEFROOT-FR3: Installation Passwords

[Offerings](#DEF_Offering) in [clean states](#DEF_CleanState) *MAY* have default [credentials](#DEF_Credential) for *initial installation*.

A [standalone device](#DEF_StandaloneDevice) in a [clean state](#DEF_CleanState) _MAY_ provide for installation and configuration over the network, before normal operation begins, with an administrative protocol enabled by default, with little or no assurance of the source of the configuration information, using factory-preinstalled, predictable, default, or null [credentials](#DEF_Credential).

Converting an [offerings](#DEF_Offering) device type, model number, serial number, or MAC address is considered an installation password.

Until all installation credentials have been disabled, the [offering](#DEF_Offering) _MUST_ prevent normal operation and disable any function not [essential](#DEF_Essential) for the installation process itself.  This is meant to prevent accidents by causing noticeable failures.

Any install password _MUST_ be changed prior to using the product as detailed in [SEC-PWD-CONTROL](#SEC-PWD-CONTROL).

**Supplemental Guidance**: The requirement references the Initial Authenticator in [NIST Special Publication 800-53 IA-5](https://nvd.nist.gov/800-53/Rev4/control/IA-5).

## SEC-AUT-DEFROOT-FR4: Hardware Debug

[Offerings](#DEF_Offering) _MAY_ include authentication roots used for hardware debugging access as described in [SEC-HW-NOJTAG](#SEC-HW-NOJTAG).

**Supplemental Guidance** Read the numerous restrictions in [SEC-HW-NOJTAG](#SEC-HW-NOJTAG) before deciding that your planned default credential use is permitted by this FR.

## SEC-AUT-DEFROOT-FR5: Hardware Trust

[Offerings](#DEF_Offering) _MAY_ include and enable any [authentication root](#DEF_AuthenticationRoot) used by a Cisco intellectual property protection or anti-counterfeiting scheme, provided that any compromise of the affected authentication system would affect only the scheme in question and would not otherwise compromise any [security](#DEF_Security) system set up by a customer.

## SEC-AUT-DEFROOT-FR6: Consent Token

[Offerings](#DEF_Offering) _MAY_ included authentication roots to allow authentication and authorization via Consent Token.

**Supplemental Guidance:** Consent Token is also a form of a multi-factor authentication system that creates a common client – server infrastructure to allow special access to the product by Cisco with the concent of the customer leveraging the digital signature verification infrastructure available. A specific use case would be to allow debug access by Cisco with the consent of the customer.

# History

```yaml
-----
affected_psb: SEC-AUT-DEFROOT-2
description:  Updated to functional requirements and evidence changes.
---
deprecated_psb: SEC-AUT-DEFROOT
impact: normative
headline: >
  [SEC-AUT-DEFROOT](#SEC-AUT-DEFROOT) migrated to functional requirements.  Evidence changes.
```

# Informative References

* [Using AutoInstall to Remotely Configure Cisco Networking Devices](<http://www.cisco.com/c/en/us/td/docs/ios/fundamentals/configuration/guide/15_1s/cf_15_1s_book/cf_autoinstall.html>)

* [Cisco Consent Token](https://wiki.cisco.com/display/STOCT/Consent+Token)

* RECIPE: [Secure Unlock Client Recipe](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Secure%20Session%20Management.aspx)

* [NIST Special Publication 800-53 IA-5](https://nvd.nist.gov/800-53/Rev4/control/IA-5)

# Requirement References

```
---
source: PSB
foreign_id: SEC-CRE-NOBACK
relation: connects
headline: >
    [SEC-CRE-NOBACK](#SEC-CRE-NOBACK) Ensure suppliers aren't puttting back doors into the components you use
---
source: PSB
foreign_id: SEC-509-TRUST
relation: connects
headline: >
    [SEC-509-TRUST](#SEC-509-TRUST) Include only approved X.509 certificate authorities
---
source: PSB
foreign_id: SEC-509-CA
relation: connects
headline: >
    [SEC-509-CA](#SEC-509-CA) Use only certificates from qualified CAs
---
source: PSB
foreign_id: SEC-PWD-CONTROL
relation: connects
headline: >
    [SEC-PWD-CONTROL](#SEC-PWD-CONTROL) Control password usage and behavior to ensure security and awareness
---
source: PSB
foreign_id: SEC-HW-NOJTAG
relation: connects
headline: >
    [SEC-HW-NOJTAG](#SEC-HW-NOJTAG) Disable or authenticate hardware debug ports
---
source: PSB
foreign_id: SEC-CRE-RESET
relation: connects
headline: >
    [SEC-CRE-RESET](#SEC-CRE-RESET) Support and document credential loss recovery via clean state
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings
        class: not_HwComp
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    waivable: true
    version: 2
    id: SEC-AUT-DEFROOT
    issueref: ISS_DefaultCreds
    tags:
    - EN/PI
    - EN/PD
    - Critical PSB
    - PSB/OnPrem
    - Cloud
    - FAST
