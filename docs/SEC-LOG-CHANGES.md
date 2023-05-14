# Headline

Log system and configuration changes

# Description

Log system changes regarding authorization, authentication, status, configuration, software, or time.

# Behavior

## SEC-LOG-CHANGES-FR1: Authorization

[Offerings](#DEF_Offering)  _MUST_ log changes to [authorization](#DEF_Authorization) policy.  This includes logging changes such as--

1.  Creating or deleting [principals](#DEF_Principal) (principals include usernames), groups, roles, or other names for authorization categories

2.  Modifying privileges, group assignments, associated access for groups, roles, [principals](#DEF_Principal), or other "marks of authority"

5.  Changes to permission settings or access control lists on data objects such as files, databases, or tables.

    You _MAY_ choose to omit--

    1.  Changes made by programs as part of their normal operation (for example changing the permissions on a temporary file as a routine part of passing that file off to another program).
    2.  Changes made by end users to permission settings on their own data (for example sharing a file with another user).

4. Changes to firewall filtering or network access lists. You _MAY_ omit dynamic changes made as part of a firewall's own normal operation

5. Changes to information authorizing resource consumption, such as quotas or rate limits.

Supplemental guidance: In addition to providing the standard information required for any logged event, and any information mentioned in the list above, the log _MUST_ identify any [principal](#DEF_Principal) or [target](#DEF_Target) referred to by the changed information.

## SEC-LOG-CHANGES-FR2: Authentication

[Offerings](#DEF_Offering) _MUST_ log any changes to how you [authenticate](#DEF_Authentication) information about [peers](#DEF_Peer), including the credentials they use, the types of credentials you'll accept, and the protocols and services you use for authentication.

At a minimum, log any change to any of these--

1.  [Authentication roots](#DEF_AuthenticationRoot), including--
    1.  Passwords (log the password change event; [*don't* log either the old or new password](#SEC-LOG-NOSENS))
    2.  Trusted certificate authorities
    3.  Authentication servers or information used to authenticate the servers themselves.
2.  Authentication protocols or procedures
3.  Parameters such as required credential strength, reauthentication intervals, etc.

Supplemental guidance: If the changed [authentication](#DEF_Authentication) is associated with a specific [principal](#DEF_Principal), then the logged event _MUST_ identify that [principal](#DEF_Principal).

## SEC-LOG-CHANGES-FR3: System Software

[Standalone devices](#DEF_StandaloneDevice) _MUST_ log changes to system software images and log all attempts to update the running monolithic software image or to change the image to be started at the next system boot. Log all attempted operating system reinstallations or updates that use standard installation tools. This applies to both successful and unsuccessful attempts.

Supplemental guidance: Attackers will often try to install modified software, debugging versions, old buggy versions, etc. Logging changes often makes it possible to trace these attempts. The Common Criteria require "auditing" (i.e. logging) updates. Many other standards and customer RFPs require it as well.

## SEC-LOG-CHANGES-FR4: System Time

[Offerings](#DEF_Offering) _MUST_ log changes to system time.

[Standalone devices](#DEF_StandaloneDevice)  _MUST_ log all "step" adjustments to the offering's time of day and all adjustments to real time clock speeds or skew values. This includes both manual changes and changes from NTP or other time synchronization systems.

Supplemental guidance: Correct time is important for log interpretation and log integrity; attackers may try to adjust system time to make it hard to detect or trace their activities. The Common Criteria require "auditing" (i.e. logging) time changes. Many other standards and customer RFPs require it as well.

Include the source of the changed time data. In most cases, the information required by [SEC-LOG-CONTENT](#SEC-LOG-CONTENT) will capture this, but time taken from devices like radio receivers may require more information to identify the real time source.  Also include both the new and old time and/or clock speed values.

## SEC-LOG-CHANGES-FR5: Status

[Offerings](#DEF_Offering) _MUST_ log startup, shutdown, crashes, and other status changes.  Log, by default, each of the following status changes for [agents](#DEF_Agent) like [network element](#DEF_NetworkElement), any TCP/IP service, any [listener](#DEF_Listener) created as part of the [offering](#DEF_Offering):

1.  Startup (whether initial or restart)

2.  Shutdown expected in normal operation

3.  Shutdown by [administrative](#DEF_Administer) action, identifying the [administrative](#DEF_Administer) [agent](#DEF_Agent) responsible

4.  Shutdown because of detected error, identifying the nature of the error

Log shutdowns even if they are to be followed immediately by restarts.

In addition to providing the standard information required for any logged event, and any information mentioned in the list above, the log _MUST_ identify the [agent](#DEF_Agent) whose status has changed.

Supplemental guidance: If one of the mentioned agents is part of a larger subsystem, and is *always* started and shut down together with the larger subsystem, then you _MAY_ consider a log message describing a change in the status of the larger subsystem as also covering the status change for the mentioned agent, *provided* that that message contains all of the required information when considered as a notification about the mentioned agent.

## SEC-LOG-CHANGES-FR6: Logging Configuration

[Offering](#DEF_Offering) _MUST_ log changes to logging configurations and content.  If the logging configuration can be changed without the change itself being recorded, the integrity of logs can easily be compromised.

Whenever any form of logging is in operation, log any change to the configuration of the logging service itself, or any modification or deletion of already recorded log information, via any [exposed interface](#DEF_ExposedInterface) intended for manipulating logging configuration, log data, or system configuration generally. You _SHOULD_ detect and log any change by any means whatsoever, regardless of whether it uses an [exposed interface](#DEF_ExposedInterface).

[Standalone devices](#DEF_StandaloneDevice) _MUST_ also be able log any configuration change which might affect log message delivery, such as any change to the [IP](#DEF_IP) routing tables or to [IP](#DEF_IP) filtering. Such logging _MAY_ be, but is not required to be, enabled by default.

Each change _MUST_ be logged before taking effect. Changes affecting the destinations to which log messages are directed _SHOULD_ additionally be logged to any new destinations after taking effect.

Changes to the configuration of the logging service include the following:

-   enabling or disabling logging

-   changes in logging servers or other log data destinations

-   changes to the logging protocols or to the configurations of those protocols

-   changes in system wide logging filters

-   changes to the logging severity or priority assigned to logging-related events such as loss of log data

-   changes to log retention periods

-   changes to the system's response to the exhaustion of logging resources, or changes in the sizes of logging buffers

-   deletion or modification of previously logged information

Supplemental guidance: This tends to turn up in formal evaluation criteria like Common Criteria profiles.  This requirement does not apply to changes to stored logging configuration made while the logging service itself is shut down.

# Informative References

* RECIPE: [Log Security-relevant Information](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Log%20SecurityRelevant%20Information.aspx)
* RECIPE: [Application Logging and Monitoring](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/ASLR%20in%20Linux%20Systems.aspx)
* RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)

# Normative References

* See [Security Logging Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1401894&ver=approved)

# Requirement References

    ---
    foreign_id: SEC-LOG-CONTENT
    relation: connects
    headline: |-
      SEC-LOG-CONTENT
              lists information to be included in all log entries.

    source: PSB
    ---
    foreign_id: FPT_TUD_EXT.1(AE)
    relation: implies
    headline: |-
      Be able to audit initiation of an update to
            firmware/software.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FPT_STM.1(AE)
    relation: implies
    headline: |-
      Be able to audit all changes to the time, with audit
              detail including the old and new values for the time, and the origin
              of the attempt to change the time (e.g. username, or IP address of
              an NTP server).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria

# History

```yaml
-----
affected_psb: SEC-LOG-CHANGES
description:  Aggregated related requirements into functional requirements.
---
deprecated_psb: SEC-AUT-LOGZCHG
impact: non-normative
headline: >
  [SEC-AUT-LOGZCHG](#SEC-AUT-LOGZCHG) migrated to SEC-LOG-CHANGES-FR1.
---
deprecated_psb: SEC-AUT-LOGNCHG
impact: non-normative
headline: >
  [SEC-AUT-LOGNCHG](#SEC-AUT-LOGNCHG) migrated to SEC-LOG-CHANGES-FR2.
---
deprecated_psb: SEC-SW-LOG
impact: non-normative
headline: >
  [SEC-SW-LOG](#SEC-SW-LOG) migrated to SEC-LOG-CHANGES-FR3.
---
deprecated_psb: SEC-TIM-LOG
impact: non-normative
headline: >
  [SEC-TIM-LOG](#SEC-TIM-LOG) migrated to SEC-TIM-LOG-CHANGES-FR4.
---
deprecated_psb: SEC-LOG-STATCHG
impact: non-normative
headline: >
  [SEC-LOG-STATCHG](#SEC-LOG-STATCHG) migrated to SEC-LOG-CHANGES-FR5.
---
deprecated_psb: SEC-LOG-LOGCONF
impact: non-normative
headline: >
  [SEC-LOG-LOGCONF](#SEC-LOG-LOGCONF) migrated to SEC-LOG-CHANGES-FR6.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict:
          offerings
    category: Logging and Auditing
    riskArea: Logging & Monitoring
    waivable: true
    version: 1
    id: SEC-LOG-CHANGES
    issueref: ISS_Underlogging
    tags:
    - EN/PI
    - CloudCritical
    - PSB/OnPrem
    - Cloud
    - FAST
