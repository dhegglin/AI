# Headline

Control password usage and behavior to ensure security and awareness

# Description

Password control is to ensure that the password workflow is well understood, responses are actionable, and that the behavior cannot be used as a Denial of Service vector.

SEC-PWD-CONTROL provides a catalog of password controls that support the development of secure and resilient products. These password controls are the operational, technical, and management safeguards used by information systems to maintain integrity, confidentiality, and security.

NIST 800-53 is the basis for SEC-PWD-CONTROL and is a major component of [FISMA compliance](https://digitalguardian.com/blog/what-fisma-compliance-fisma-definition-requirements-penalties-and-more).

For products that exclusively externalize password management, this requirement is not applicable. Externalizing password management is frequently done using RADIUS, TACACS+, or Single Sign-On solutions.  In this case it is the responsibility of the external password management solution to enforce SEC-PWD-CONTROL.

# Behavior

## SEC-PWD-CONTROL-FR1: Permanent Lock Out

The [agent](#DEF_Agent) _MUST NOT_ be locked out permanently on repeated login failure by default.

**Supplemental Guidance**: Locking [agents](#DEF_Agent) out and requiring administrative action could be used as a type of Denial of Service for the legitimate [agent](#DEF_Agent).

## SEC-PWD-CONTROL-FR2: Password Retry Attempts

The [agent](#DEF_Agent) _MUST_ be limited from retrying passwords per source per unit time.

**Supplemental Guidance**: Allowing unlimited retries allows brute force attempts and is also considered a type of Denial of Service. After a number of times, start refusing additional attempts until some timeout value has expired.

## SEC-PWD-CONTROL-FR3: Failed Login

The [agent](#DEF_Agent)  _MUST NOT_ be informed of username validity or password validity on failed login. The error messages should state that username or password was not found without giving specifics.

**Supplemental Guidance**: Validating the username or password discloses information to the potential attacker.

## SEC-PWD-CONTROL-FR4: Password Display

The [agent](#DEF_Agent) _MUST_ have the ability to hide the password at all times, only the \* character _MAY_ be displayed in place of the password characters. This also means that on password change, the new password _MUST_ be entered twice and compared before accepting the new password. 

There _MAY_ be an option for the [agent](#DEF_Agent) to specify that they want to show the credential.  For example, the IOS CLI allows configuring passwords in the clear as well as masked with the command "ios(config)#username test privilege 0 masked-secret".

**Supplemental Guidance**: Echoing the password back to the [agent](#DEF_Agent) discloses information to shoulder surfers.

## SEC-PWD-CONTROL-FR5: Rejected Password Changes

The [agent](#DEF_Agent) _MUST_ understand the reason(s) for rejected password changes.

The [agent](#DEF_Agent) _MUST_ receive actionable feedback in order to specify a password that conforms to the password rules. If the selected password violates more than one restriction, the [agent](#DEF_Agent) _SHOULD_ be told of ALL violated restrictions at the same time.

## SEC-PWD-CONTROL-FR6: Password Rules

The [agent](#DEF_Agent) _MUST_ conform to password rules only during password creation and subsequent password changes, rather then when they are used.

**Supplemental Guidance**: Enforcing the password rules during use may result in a failure if the password rules are changed.

## SEC-PWD-CONTROL-FR7: Password Expiration

The [agent](#DEF_Agent) _MUST_ be warned of impending password expiration.

A password expiration warning allows the [agent](#DEF_Agent) time to change the password before it expires. The [agent](#DEF_Agent) _MAY_ be actively warned by acknowledging the warning, or the [agent](#DEF_Agent) _MAY_ be passively warned by simply presenting a warning message.

## SEC-PWD-CONTROL-FR8: Reauthentication During Password Change

The [agent](#DEF_Agent) _MUST_ re-authenticate using the existing password before a password change.

When the [agent](#DEF_Agent) changes his or her own password, authentication using the old password _MUST_ be required immediately before the new one is set.

**Supplemental Guidance**: Requiring the [agent](#DEF_Agent) to authenticate at password changes prevents an unattended session from being used to change a password and get permanent control over the [agent](#DEF_Agent) account.

This requirement does not extend to the corner case in which an administrator resets the password of other [agents](#DEF_Agent).

## SEC-PWD-CONTROL-FR9: First Login

The [agent](#DEF_Agent) _MUST_ be forced to change their password on first login as well as after a password reset by the administrator.

**Supplemental Guidance**: A password that has been reset is disclosed to the [agent](#DEF_Agent) in order to log into the system. By definition this means that the password is uncontrolled.

# History

```yaml
-----
affected_psb: SEC-PWD-CONTROL
description:  Aggregated related requirements into functional requirements.
---
deprecated_psb: SEC-CRE-NOLOCK
impact: non-normative
headline: >
  [SEC-CRE-NOLOCK](#SEC-CRE-NOLOCK) migrated to SEC-PWD-CONTROL-FR1.
---
deprecated_psb: SEC-PWD-CHKCHG
impact: non-normative
headline: >
  [SEC-PWD-CHKCHG](#SEC-PWD-CHKCHG) migrated to SEC-PWD-CONTROL-FR6.
---
deprecated_psb: SEC-PWD-FAILWHY
impact: non-normative
headline: >
  [SEC-PWD-FAILWHY](#SEC-PWD-FAILWHY) migrated to SEC-PWD-CONTROL-FR5.
---
deprecated_psb: SEC-INC-USER
impact: non-normative
headline: >
  [SEC-INC-USER](#SEC-INC-USER) migrated to SEC-PWD-CONTROL-FR3.
---
deprecated_psb: SEC-PWD-EXPWARN
impact: non-normative
headline: >
  [SEC-PWD-EXPWARN](#SEC-PWD-EXPWARN) migrated to SEC-PWD-CONTROL-FR7.
---
deprecated_psb: SEC-CRE-LIMTRY-2
impact: non-normative
headline: >
  [SEC-CRE-LIMTRY-2](#SEC-CRE-LIMTRY-2) migrated to SEC-PWD-CONTROL-FR2.
---
deprecated_psb: SEC-CHG-PSWD-2
impact: non-normative
headline: >
  [SEC-CHG-PSWD-2](#SEC-CHG-PSWD-2) migrated to SEC-PWD-CONTROL-FR8.
```

# Normative References

* [NIST 800-53](https://nvd.nist.gov/800-53)

# Informative References

* RECIPE: [Password Management](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Password%20Management.aspx)
* [Credential Logging](https://wwwin-si.cisco.com/psb-requirements/#SEC-LOG-NOSENS)

# Attributes

    id: SEC-PWD-CONTROL
    version: 1
    issueref: ISS_PwControl
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
            restrict: >
              [offerings](#DEF_Offering)
    priority: 8
    phase: requirements
    tags:
        - CloudCritical
        - PSB/OnPrem
        - EN/PI
        - Cloud
        - EN/PI DT
