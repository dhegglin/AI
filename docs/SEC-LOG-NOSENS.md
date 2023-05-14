# Headline

Do not log sensitive records, passwords, credentials, crypto keys, etc.

# Description

The collection of logs is [essential](#DEF_Essential) for operations, investigations and auditing of Cisco's systems. However, collection of [sensitive personally identifiable information](#DEF_SPII), or [PII](#DEF_PII), passwords, credentials, etc. is not required for the majority of these efforts. In many cases, the collection of [sensitive](#DEF_Sensitive) information violates privacy requirements,  regulations, and laws. 

# Behavior

Ensure no [sensitive](#DEF_Sensitive) data (including [personal information](#DEF_PersonalInformation) and  [personal identifiers](#DEF_PersonalIdentifier)), passwords, keys, or similar items are entered into or stored in in log files. Collection and storage of personal information such as email IDs and IP addresses of personal devices should be limited to only when necessary and should be de-identified if possible.


For this requirement, to "log" information is to make a record of it, or to send it to any outside entity that makes a record of it, in order to create a history or partial history of activity in your [offering](#DEF_Offering) or in its environment, regardless of how long the record is retained. This includes, but is *not limited to*, records made for:

1.  Debugging or troubleshooting.

2.  Auditing or accountability.

3.  Detection of security incidents, suspicious data, or suspicious activity.

4.  Tracking of or response to active, already detected security violations.

5.  System optimization, feature prioritization, development planning, etc.

6.  Understanding or characterizing user behavior, whether for individual users or in the aggregate.

## SEC-LOG-NOSENS-FR1: Credentials

Cisco [offerings](#DEF_Offering)  _MUST_NOT_ log [credentials](#DEF_Credential), [Passwords](#DEF_Passphrase) including anything any [agent](#DEF_Agent)  tries to use as a password or other credential, successfully or unsuccessfully, regardless of whether the [credential](#DEF_Credential) is a valid one.

## SEC-LOG-NOSENS-FR2: Cryptographic Keys

 [Cryptographic secrets](#DEF_CryptographicSecret), encryption key credentials (e.g., [private](#DEF_Private) encryption keys, AllowList or BlockList rules, object permission attributes and/or settings) _MUST_NOT_ be logged.

## SEC-LOG-NOSENS-FR3: Financial Records

 [Sensitive](#DEF_Sensitive) financial records (such as [financial identifiers](#DEF_FinancialIdentifier), [credentials](#DEF_Credential), monetary information relating to actual transactions)  _MUST_NOT_ be logged.

## SEC-LOG-NOSENS-FR4: Sensitive Information

Possibly [sensitive](#DEF_Sensitive) personal or customer information such as [personal information](#DEF_PersonalInformation),  uploaded documents, or chat messages _MUST_NOT_ be logged.

**Supplemental Guidance**:  User identifiers, login names, etc are not sensitive personal information.

## SEC-LOG-NOSENS-FR5: Configuration

Cisco [offerings](#DEF_Offering)  _MUST_NOT_  log any [critical](#DEF_Critical) configuration details (e.g., database connection strings).

## SEC-LOG-NOSENS-FR6: Tracebacks

Offers _MUST_ only log tracebacks when an exception occurs and not for normal operation or expected outcomes.  Additional tracebacks _MAY_ be enabled if the logging level is set to DEBUG.

# Informative References
* RECIPE: [Log Security-relevant Information](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Log%20SecurityRelevant%20Information.aspx)
* RECIPE: [Application Logging and Monitoring](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/ASLR%20in%20Linux%20Systems.aspx)
* RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)

- [Cisco Privacy Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1106658)

See [SEC-DAT-MINIMIZE](#SEC-DAT-MINIMIZE) and [SEC-PRV-USERAUTH](#SEC-PRV-USERAUTH) for more requirements related to [personal information](#DEF_PersonalInformation) and [personal identifiers](#DEF_PersonalIdentifier) in logs.

# History

```
-----
affected_psb: SEC-LOG-NOSENS-4
description: >
  Removed FR6 as this is duplicated in SEC-LOG-CONTENT.  Renames FR7 to FR6
impact: non-normative
-----
affected_psb: SEC-LOG-NOSENS-4
description: >
  Clarified requirement for traceback in FR7
impact: normative
-----
affected_psb: SEC-LOG-NOSENS-3
description: >
  Combined requirement from SEC-SCR-NOLOG-2 since both requirements are addressing what not to log.
impact: normative
---
deprecated_psb: SEC-LOG-NOSENS-2
impact: non-normative
headline: >
[SEC-LOG-NOSENS-2](#SEC-LOG-NOSENSE-2) migrated to functional requirements
---
deprecated_psb: SEC-SCR-NOLOG-2
impact: normative
headline: >
  [SEC-SCR-NOLOG-2](#SEC-SCR-NOLOG-2) migrated to SEC-LOG-NOSENS-FR1, SEC-LOG-NOSENS-FR2 and SEC-LOG-NONSENS-FR5
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
    category: Logging and Auditing
    riskArea: Logging & Monitoring
    waivable: true
    version: 3
    id: SEC-LOG-NOSENS
    issueref: ISS_SensLogs
    tags:
    - EN/PD
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
    - Cloud
    - FAST
