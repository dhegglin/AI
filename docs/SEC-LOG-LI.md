# Headline

Control Lawful Intercept feature logging.

# Description

Logging events for Lawful Intercept configuration changes, activations, deactivations, or login events are enabled and disabled by only the LIAdmin role.

# Behavior

## SEC-LOG-LI-FR1: LIAdmin Exclusive Control

Lawful Intercept information and configuration _MUST_ be exclusively controlled by the LIAdmin role.

## SEC-LOG-LI-FR2: Lawful Intercept Activity Logging

The LIAdmin role _MUST_ be able to enable or disable logging of any Lawful Intercept activites including logins, logouts, and configuration changes to logging, taps, monitors, accounts, or passwords.  Lawful Intercept activity also includes an event log recording when the offering or security administrator resets an LIAdmin account password, creates an account with the LIAdmin role or assigns the LIAdmin role to an existing account.

## SEC-LOG-LI-FR3: Remote Lawful Intercept Logging Server

The LIAdmin role _MUST_ be able to configure a remote Lawful Intercept logging server (address and port number) with encryption enabled by default see [SEC-CRY-ALWAYS](#SEC-CRY-ALWAYS).

## SEC-LOG-LI-FR4: Default Logging Behavior

The offering default logging behavior _MUST NOT_ log Lawful Intercept configuration changes/additions/deletions to taps, monitors, account logins, or LIAdmin role account password changes.

## SEC-LOG-LI-FR5: Scheduled Log Messages

The offerings _MUST_ provide scheduled log messages that record whether the Lawful Intercept feature is available. This log message _MUST NOT_ contain any information about the configuration of the Lawful Intercept feature taps, monitors, account logins, or password changes.  The schedule and destination for the LI feature available log _MUST_ only be configurable by the offering administrator, **not** by a LIAdmin role account.

**Supplemental Guidance**: In this instance, "available" means that an LIAdmin role user is configured and has successfully changed their password at first login.

## SEC-LOG-LI-FR6: LIAdmin Account Deletion and Password Reset

Offerings _MUST_ remove all remote log server configuration data if a LIAdmin role account is deleted, or if the offering administrator resets a LIAdmin role account password.

# Informative References

* RECIPE: [Incorporate Lawful Intercept](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Incorporate%20Lawful%20Intercept.aspx)

# Requirement References

    ---
    foreign_id: SEC-PWD-CONTROL
    relation: implies
    headline: |-
        Control password usage and behavior to ensure security and awareness
    source: PSB
    ---
    foreign_id: SEC-AUT-LI
    relation: connects
    headline: |-
        Control authentication and authorization for Lawful Intercept (LI) feature
    source: PSB

# History

```yaml
-----
affected_psb: SEC-LOG-LI
description:  Updated to functional requirements.

```

# Attributes

    id: SEC-LOG-LI
    version: 1
    issueref: ISS_LawfulIntercept
    category: Privacy and Data Security
    riskArea: Logging & Monitoring
    legallysensitive: true
    waivable: true
    applicability:
      - force: mandatory
        target:
          restrict: >
            offerings
    priority: 8
    phase: requirements
    tags:
      - EN/PI
      - EN/PD
      - PSB/OnPrem
      - Cloud
