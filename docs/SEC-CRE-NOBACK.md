# Headline

Do not permit undocumented ways of gaining access to the offering

# Description

If there's a way users don't know about to get access to the [offering](#DEF_Offering), then there is a back door. Back doors are serious technical, legal, and ethical exposures. Don't create them, and don't permit them to exist.

It is critical that all [offering](#DEF_Offering) teams be aware of their security exposures. Any function or means of access that an entity doesn't understand presents a possibility for an attack against which that entity cannot possibly defend. Providing this information is a fundamental ethical requirement.

*Back doors are usually discovered eventually, and result in enormous damage to customer trust and confidence*. The “grapevine”, the trade press, and the mainstream press are all eager to ensure that any vendor responsible for a back door feels the full effect on its reputation.  In some cases legal consequences may extend to civil and criminal liability for Cisco and/or individual employees.

Inserting [back doors](#DEF_BackDoor) in Cisco [offerings](#DEF_Offering), allowing others to insert them, or permitting known [back doors](#DEF_BackDoor) to continue to exist, is a policy violation, and may result in disciplinary action up to and including termination without prior warning.

# Behavior

[Back doors](#DEF_BackDoor) by default are not documented.  Any documented feature is not considered a backdoor; this includes features such as Lawful Intercept.

## SEC-CRE-NOBACK-FR1: Maintenance Hooks

The [offerings](#DEF_Offering) _MUST_NOT_ include [back doors](#DEF_BackDoor) for access by anyone, for any purpose, including service or support.  This includes any form of access whatsoever[, administrative](#DEF_Administrator) or otherwise, by any
person, Cisco employee or otherwise.  Service or Support access to the product _MUST_ be limited by [Cisco Consent Token](https://wiki.cisco.com/display/STOCT/Consent+Token) or a similar mechanism.

This type of [back door](#DEF_BackDoor) _MUST_ be treated as a critical security bugs, and PSIRT _MUST_ be engaged immediately upon discovering them.

## SEC-CRE-NOBACK-FR2: Non-essential Accounts

The [offering](#DEF_Offering) _MUST_NOT_ include non-essential accounts because they can be used as attack vectors. For [default](https://cserv.cisco.com/library/glossary/CG22) accounts that need to be retained, including guest accounts, severely restrict [access](https://cserv.cisco.com/library/glossary/CG71) and capabilities of these accounts.  Reset passwords from [default](https://cserv.cisco.com/library/glossary/CG22) to strong passwords.

This type of [back door](#DEF_BackDoor) _MUST_ be treated as a critical security bugs, and PSIRT _MUST_ be engaged immediately upon discovering them.

## SEC-CRE-NOBACK-FR3: Privilege Escalation

The offering _MUST_NOT_ permit any [back door](#DEF_BackDoor) that would allow a user to perform a function that would otherwise not be available. This includes functionality explicitly designed to disable or bypass any form of authentication, authorization, or access control.

An incomplete list of examples of this functionality includes:

- Allowing non[-administrative](#DEF_Administrator) users to use [administrative](#DEF_Administrator) functions.
- Giving access to services which the [offering](#DEF_Offering) is explicitly configured to protect, such as access list bypass or command authorization bypass.
- “Sniffing” or monitoring network traffic, even if restricted to traffic addressed to the [offering](#DEF_Offering).
- Bypassing any software or configuration integrity assurance system.
- Unrestricted access to internal data which the [offering](#DEF_Offering) would not ordinarily expose via its external interfaces.
- Use of the [offering](#DEF_Offering) as a relay or traffic generating system to access other systems.
- Any violation of the integrity of any [controlled space](#DEF_ControlledSpace).

This type of [back door](#DEF_BackDoor) _MUST_ be treated as a critical security bugs, and PSIRT _MUST_ be engaged immediately upon discovering them.

## SEC-CRE-NOBACK-FR4: Hidden Interfaces

The [offering](#DEF_Offering) _MUST_NOT_ permit any hidden interfaces as this is considered a [back door](#DEF_BackDoor).

An incomplete list of examples of this functionality includes:

- Undocumented commands.  Such commands are typically hidden as a hook for developers to execute specific scenarios and are not tested properly and may cause system instability.
- Undocumented API calls.  Such API calls are typically created by developers to execute specific scenarios.  Even if these APIs are authenticated, they are not tested properly and may cause system instability or date exposure.
- Disclosure of any installation-specific information that is not meant to be consumed by the non-administrative users of the [offering](#DEF_Offering).

# History

```yaml
-----
affected_psb: SEC-CRE-NOBACK-2
description:  Updated to functional requirements with evidence changes.
---
deprecated_psb: SEC-CRE-NOBACK
impact: normative
headline: >
  [SEC-CRE-NOBACK](#SEC-CRE-NOBACK) migrated to functional requirements.  Evidence changes.
---
deprecated_psb: SEC-AUT-ACCDEF
impact: normative
headline: >
  [SEC-AUT-ACCDEF](#SEC-AUT-ACCDEF) migrated requirement to FR2.
```

# Informative References

[Cisco Consent Token](https://wiki.cisco.com/display/STOCT/Consent+Token)

[Pantelegraph](https://offensive-git.cisco.com/nweigand/pantelegraph/)

[truffleHog](https://offensive-git.cisco.com/dhegglin/trufflehog)

[NIST 800-83](https://doi.org/10.6028/NIST.SP.800-83r1)

[NIST 800-12](https://doi.org/10.6028/NIST.SP.800-12r1)

RECIPE: [Hard Coded Credentials Recipe](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Hard%20Coded%20Credentials.aspx)

# Requirement References

```
---
source: PSB
foreign_id: SEC-UPS-NOBACK
relation: connects
headline: >
    [SEC-UPS-NOBACK](#SEC-UPS-NOBACK) Ensure suppliers aren't puttting back doors into the components used by the offering
---
source: PSB
foreign_id: SEC-AUT-LI
relation: connects
headline: >
    [SEC-AUT-LI](#SEC-AUT-LI) Control authentication and authorization for Lawful Intercept (LI) feature
---
source: PSB
foreign_id: SEC-ASU-TRAIN
relation: connects
headline: >
    [SEC-ASU-TRAIN](#SEC-ASU-TRAIN) Train the product team to ensure understanding
```

# Attributes

    phase: requirements
    legallysensitive: true
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    waivable: false
    version: 2
    id: SEC-CRE-NOBACK
    issueref: ISS_Backdoor
    tags:
    - EN/PD
    - EN/PI
    - Critical PSB
    - PSB/OnPrem
    - Cloud
    - FAST
