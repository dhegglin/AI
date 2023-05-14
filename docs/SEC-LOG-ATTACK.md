# Headline

Log indications of attack or abuse

# Description

Log any suspicious events your software detects

# Behavior

## SEC-LOG-ATTACK-FR1: Input Validation Error

Any input validation error, regardless of the source of the input data, _MUST_ be logged by [default](#DEF_Default), unless limiting constraints of [SEC-LOG-LIMIT](#SEC-LOG-LIMIT) is reached.

The logged data _MUST_ include information about the way in which the input was found to be invalid. Unless the invalid data might be expected to do harm to the logging system, you _SHOULD_ include the invalid portion of the input itself.

## SEC-LOG-ATTACK-FR2: Loss of Contact

Unexpected loss of contact with any [peer](#DEF_Peer) _MUST_ be logged by [default](#DEF_Default) unless limiting constraints of [SEC-LOG-LIMIT](#SEC-LOG-LIMIT) is reached.

## SEC-LOG-ATTACK-FR3: Resource Limit

Any case of an [agent](#DEF_Agent) exceeding a quota or resource limit, regardless of what is enforcing that limit _MUST_ be logged unless limiting constraints of [SEC-LOG-LIMIT](#SEC-LOG-LIMIT) is reached.

The logged data _MUST_ name the agent and the type of resource overused.

## SEC-LOG-ATTACK-FR4: Login status

When a user logs in using an interactive user interface, the following indications _SHOULD_ be provided upon successful login.

-   The last time at which a username was successfully used for authentication, the name of the authenticating host, the name or address of the location from which the user last received service, and the type of service used. A representative message might be "User goodguy last logged in 2008-Dec-13, to foo.cisco.com, from bar.cisco.com using SSH"

-   The number of failed login attempts since the last successful login, together with the information normally given for a successful attempt, such as "User goodguy failed to log in 5 times!  Most recent failure 2008-Dec-13, to foo.cisco.com, from bar.cisco.com using HTTPS"

## SEC-LOG-ATTACK-FR5: Other Activities

Any detected activity likely to indicate fraud, abuse, or other security violations _MUST_ be logged by [default](#DEF_Default) unless limiting constraints of [SEC-LOG-LIMIT](#SEC-LOG-LIMIT) is reached.  This includes, but isn't limited to:

1.  Detected by your own code.

2.  Detected by intrusion detection systems, intrusion prevention systems, firewalls, or similar monitoring elements embedded in your offering.

You _MUST_ log events which you believe indicate *probable*, as opposed to possible, security attacks. You _SHOULD_ log events which you reasonably *suspect* to represent security attacks.

Off the shelf monitoring subsystems usually assign some sort of probability score for each logged event, and you _MAY_ rely on these scores to choose what to log.

**Supplemental Guidance:** When you log a probable attack indication, assign it a priority, or use a reporting method, that lets the logging system identify it as something that may need immediate operator attention.

# Informative References

* RECIPE: [Log Security-relevant Information](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Log%20SecurityRelevant%20Information.aspx)
* RECIPE: [Application Logging and Monitoring](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/ASLR%20in%20Linux%20Systems.aspx)
* RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)


# Requirement References
```
---
foreign_id: SEC-LOG-LIMIT
relation: connects
headline: |-
  SEC-LOG-LIMIT requires you to control the rate at which events are logged.
source: PSB
---
foreign_id: SEC-LOG-CONTENT
relation: connects
headline: |-
  SEC-LOG-CONTENT lists information to be included in all log entries.
source: PSB
```

# History

```yaml
-----
affected_psb: SEC-LOG-ATTACK-2
description:  Added FR4 to indicate feedback to user.
-----
affected_psb: SEC-LOG-ATTACK
description:  Added Recipe links.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: >
          [offerings](#DEF_Offering)
    category: Logging and Auditing
    riskArea: Logging & Monitoring
    waivable: true
    version: 2
    id: SEC-LOG-ATTACK
    issueref: ISS_Underlogging
    tags:
      - EN/PI
      - PSB/OnPrem
      - Cloud
      - FAST
