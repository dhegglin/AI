# Headline

Avoid Open Redirects

# Description

Allow redirects only to preconfigured AllowListed target URLs.
Users may associate [trust](#DEF_Trust) with a legitimate site. If the
site allows redirects openly, users may not be able to tell from a link
which site they will be redirected to, leading to users applying undue
[trust](#DEF_Trust) to arbitrary sites.

# Behavior

The required behavior at the HTTP servers are given in the below feature requirements.

## SEC-WEB-NOREDIR-FR1:

Redirects _SHOULD_ only be done to targets that are deemed to be safe
by AllowListing all allowed target URLs.

## SEC-WEB-NOREDIR-FR2:

When a user supplied URL is used to Forward or Redirect, then Input validation on user supplied URL _MUST_ be done as recommended in [SEC-VAL-INURL](https://wwwin-si.cisco.com/psb-requirements#SEC-VAL-INURL-2)

# Normative References

- [OWASP Unvalidated Forwards and Redirects Cheat Sheet](https://www.owasp.org/index.php/Unvalidated_Redirects_and_Forwards_Cheat_Sheet)

# History

 ---
    id: SEC-WEB_NOREDIR
    version: 1
    affected_psb: SEC-WEB-NOREDIR
    impact: non-normative
    headline: |-
      [SEC-WEB-NOREDIR]
    description: |-
      Updated content in new PSB format with FR
      Added mandatory Input Validation for user supplied URL, as provided in SEC-VAL-INURL

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 9
    applicability:
    - force: mandatory
      target:
        restrict: Web Applications and Services
    category: Web Security
    riskArea: Application & Interface Security
    waivable: true
    version: 1
    id: SEC-WEB-NOREDIR
    issueref: ISS_HTTPRedirect
    tags:
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
