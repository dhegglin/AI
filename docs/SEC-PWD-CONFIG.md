# Headline

Provide configuration options for customer password complexity policy

# Description

The purpose of password configuration is to allow the customer to configure the product password policy to align with their own corporate policy.

Many companies have their own infosec requirements that have password complexity requirements different from Cisco.

SEC-PWD-CONFIG provides a list of password configuration options that support the customer's password complexity requirements. These password configuration options are the operational, technical, and management safeguards used by infosec to maintain integrity, confidentiality, and security.

NIST 800-53 is the basis for SEC-PWD-CONFIG and is a major component of [FISMA compliance](https://digitalguardian.com/blog/what-fisma-compliance-fisma-definition-requirements-penalties-and-more).

**Note**: For products that exclusively externalize password management, this requirement is not applicable. Externalizing password management is frequently done using RADIUS, TACACS+, or Single Sign-On solutions.  In this case it is the responsibility of the external password management solution to enforce SEC-PWD-CONFIG.

# Behavior

## SEC-PWD-CONFIG-FR1: Password Generation

If an administrator on an [offering](https://cserv.cisco.com/library/glossary/CG33) has the ability to generate a password for user accounts managed by that Cisco product, the offering _MUST_ provide password generation for those user accounts.

A generated password _MUST_ be offered, but actually accepting such a password _SHOULD_ be optional.  The password generator _MUST_ display the password in clear text in order for it to be remembered by the administrator.

The password _MUST_ be be generated using a [cryptographic](https://cserv.cisco.com/library/glossary/CG1) random number generator, and _MUST_ have a quantifiable [unpredictability](https://cserv.cisco.com/library/glossary/CG114). This unpredictability _SHOULD_ be 'tunable' by [administrator](https://cserv.cisco.com/library/glossary/CG11) configuration.

## SEC-PWD-CONFIG-FR2: Password Measure

The offering _SHOULD_ provide a measure of password strength. The [offering](https://cserv.cisco.com/library/glossary/CG33) _SHOULD_ compute a guessability metric for passwords, and _SHOULD_ permit the [administrator](https://cserv.cisco.com/library/glossary/CG11) to set a minimum metric value for new user-selected passwords.

The units of this metric _SHOULD_ be logarithmic in some estimate of the effort required to guess the passwords, and _SHOULD_ loosely correspond to an intuitive concept of 'bits of entropy".

Unless the product team clearly identifies a better metric, the metric used _SHOULD_ be the 'NIST entropy' defined in NIST SP 800-63, Appendix A.

## SEC-PWD-CONFIG-FR3: Password Expiration

The offering _MUST_ provide the ability to enforce password expiration policies for all end-user, [local](https://cserv.cisco.com/library/glossary/CG97), administrative, and system account passwords.

All end-user and system account passwords expiration _MUST_ be configurable.  Configurable password duration for user accounts allows the product to be customizable based on the customer's requirements.

User access _MUST_ be disabled if a new password is not created within the configured timeframe.

## SEC-PWD-CONFIG-FR4: Password Complexity

The offering _MUST_ provide the ability to specify password complexity.

Password complexity _MUST_ include the following:

* Minimum password length, which _MUST_ be nonzero and up to the current maximum length
* Contain both upper-case and lower-case letters
* Contain at least one number (for example, 0-9)
* Contain at least one special character (for example, `!$%^&*()_+|~-={}[]:";'<>?,/`).

The requirements specified in SEC-PWD-STRENGTH _MAY_ be changed based on the customer's requirements and be customizable.

## SEC-PWD-CONFIG-FR5: Password Reuse

The offering _MUST_ provide the ability to limit old password reuse. If the [administrator](https://cserv.cisco.com/library/glossary/CG11) has enforced password expiration and password rotation policies, a password reuse time limit _MUST_ be defined.

Password reuse limitation _*MUST*_ be [administratively](https://cserv.cisco.com/library/glossary/CG11) configurable by time interval or number of changes.  The password time interval limitation *MUST* be [administratively](https://cserv.cisco.com/library/glossary/CG11) configurable between 0 and at most 365 days, with a default of 15 days and a granularity no larger than one day.  Alternatively, the password reuse limitation _MUST_ be [administratively](https://cserv.cisco.com/library/glossary/CG11) configurable between 3 and 24 passwords, with a default of 12 passwords.

Any user-selected password _MUST_ be rejected if the new password is identical to any password that was used within the time limitation, or is part of the reuse limitation as configured by the administrator.

# History

```yaml
-----
affected_psb: SEC-PWD-CONFIG
description:  Aggregated related requirements into functional requirements.
---
deprecated_psb: SEC-PWD-GENER
impact: non-normative
headline: >
  [SEC-PWD-CONFIG](#SEC-PWD-CONFIG) migrated to SEC-PWD-CONFIG-FR1.
---
deprecated_psb: SEC-PWD-MEASU (FR2)
impact: non-normative
headline: >
  [SEC-PWD-MEASU](#SEC-PWD-MEASU) migrated to SEC-PWD-CONFIG-FR2.
---
deprecated_psb: SEC-PWD-MAXLIFE
impact: non-normative
headline: >
  [SEC-PWD-MAXLIFE](#SEC-PWD-MAXLIFE) migrated to SEC-PWD-CONFIG-FR3.
---
deprecated_psb: SEC-PWD-SETMIN
impact: non-normative
headline: >
  [SEC-PWD-SETMIN](#SEC-PWD-SETMIN) migrated to SEC-PWD-CONFIG-FR4.
---
deprecated_psb: SEC-PWD-LIMOLD
impact: non-normative
headline: >
  [SEC-PWD-LIMOLD](#SEC-PWD-LIMOLD) migrated to SEC-PWD-CONFIG-FR5.
```

# Normative References

* [NIST 800-53](https://nvd.nist.gov/800-53)

# Informative References

* RECIPE: [Password Management](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Password%20Management.aspx)
* [Credential Logging](https://wwwin-si.cisco.com/psb-requirements/#SEC-LOG-NOSENS)

# Requirement References

```
---
source: PSB
foreign_id: SEC-PWD-STRENGTH
relation: connects
headline: >
    [SEC-PWD-STRENGTH](#SEC-PWD-STRENGTH) Enforce password strength requirements for all user, local, administrative, and system account passwords
```

# Attributes

    id: SEC-PWD-CONFIG
    version: 1
    issueref: ISS_WeakPws
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
            restrict: >
              [offerings](#DEF_Offering)
    priority: 7
    phase: requirements
    tags:
    - PSB/OnPrem
    - EN/PI
    - Cloud
