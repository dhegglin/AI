# Headline

Log retention periods set by regulation and policy

# Key Benefits

Logs retention is _MANDATORY_ regulatory requirement.

# Description

Retain logs for adminstrative, legal, audit, or other operational purposes.

# Behavior

Logs _MUST_ be retained for the length of time specified by either policy or regulatory requirements to support investigation of security incidents or other operational purposes.

## SEC-LOG-RET-FR1: Retention Period

Centralized log aggregator _MUST_ be configured to retain online security logs for a minimum of 3 months. The _RECOMMENDED_ minimum retention period is 1 year.

Maximum retention period is _RECOMMENDED_ to be set for a maximum of 3 years.

# Informative References

- Cisco InfoSec Policy

  - [Security Logging Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1401894)
- Cisco Policy

  - [ERIM](https://cisco.sharepoint.com/sites/ERIM) Enterprise Records and Information Management [Section ITE 12 10 - System Logs and Telemetry Data](http://zas-app-001-p.cisco.com/retweb/retention/scheddetail.asp).
  - [Disposition of Records](https://cisco.sharepoint.com/sites/ERIM/SitePages/Disposition-of-Records.aspx)
  - [Cisco Records Management Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-880241)
- ISO/27001
  - A.10.10.1 Audit Logging
- NIST Special Publication 800-53

  - AU-11 [Audit Record Retention](https://nvd.nist.gov/800-53/Rev4/control/AU-11)

# Attributes

    phase: requirements
    legallysensitive: true
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Hosted Services
    category: Logging and Auditing
    riskArea: Logging & Monitoring
    waivable: true
    version: 2
    id: SEC-LOG-RET
    issueref: ISS_LegalLogs
    tags:
    - CloudCritical
    - Cloud
