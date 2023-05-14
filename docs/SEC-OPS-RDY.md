# Headline

Document and follow security processes and procedures

# Description

Implement processes and procedures for day to day operational [security](#DEF_Security) activities.

# Behavior

Create and follow a standard operating procedure (SOP) covering operational matters related to security.

At least once per year, complete and document a tabletop exercise to demonstrate your SOP. See the [Sec Ops Playbooks](https://cisco.sharepoint.com/:f:/r/sites/CSDLCloudOfferSecurityCom/Shared%20Documents/Templates/Operations%20Playbooks?csf=1&web=1&e=1uVNUt) for more information on tabletop exercises.

Your SOP _MAY_ address any significant operational matter, and _MUST_ cover procedures for at least the following:

## SEC-OPS-RDY-FR1:  Vulnerability Management

Document Vulnerability management, including at least the following:

- Active vulnerability identification and intake of security defects from various sources
- Triage
- Remediation
- Validation of remediation

## SEC-OPS-RDY-FR2:  Incident Management

Document Incident management and response, including, but not limited to:

- Standardized responses to common and expected forms of attack, such as volume-based DoS attack or data theft using stolen credentials
- Strategies for responding to uncommon, unexpected, or ill-understood attacks
- Conditions and procedures for engaging CSIRT
- The identities of current BU security incident contacts

## SEC-OPS-RDY-FR3:  Change Management

Document Change Management process and procedures, including change tracking
and approval.

## SEC-OPS-RDY-FR4:  Configuration and Asset Management

Document Configuration and Asset Management, including:

- Configuration management and hardening
- Asset management
- Processes for approving, authorizing, and deauthorizing access, for assuring that configured access controls match the access actually authorized, and for handling and managing credentials. This _MUST_ specifically address the need for elevated controls for privileged access. See also [SEC-OPS-REVOKE](#SEC-OPS-REVOKE).

## SEC-OPS-RDY-FR5:  Data Handling and Data Protection

Document Data handling and data protection, including any procedures demanded by the documentation produced for [SEC-DAT-KNOWWHAT](#SEC-DAT-KNOWWHAT), or [SEC-ASU-TMOD-FR1](#SEC-ASU-TMOD-FR1), or by contractual or regulatory requirements.

## SEC-OPS-RDY-FR6:  Monitoring and logging

Document Monitoring and logging in support of Cisco Policy as well as contractual requirements.

## SEC-OPS-RDY-FR7:  Cryptographic key management

Document Cryptographic key management, addressing at least the generation, exchange, storage, use, and replacement of cryptographic keys.

## SEC-OPS-RDY-FR8:  Security governance

At least once per year, complete and document a tabletop exercise to
demonstrate your SOP. See the [Sec Ops Playbooks](https://cisco.sharepoint.com/sites/CSDLCloudOfferSecurityCom/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FCSDLCloudOfferSecurityCom%2FShared%20Documents%2FTemplates%2FOperations%20Playbooks&p=true&originalPath=aHR0cHM6Ly9jaXNjby5zaGFyZXBvaW50LmNvbS86Zjovcy9DU0RMQ2xvdWRPZmZlclNlY3VyaXR5Q29tL0VxcVJ0X1VMSG81QnRxU2dMZHJMNDVNQl9ZSzRYNlEtdUg3eXNhbDZfdEtiT1E_cnRpbWU9TWp4NWhaRDkxMGc) for
more information on tabletop exercises.

# Normative References

[Sec Ops Playbooks and Templates](https://cisco.sharepoint.com/sites/CSDLCloudOfferSecurityCom/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FCSDLCloudOfferSecurityCom%2FShared%20Documents%2FTemplates%2FOperations%20Playbooks&p=true&originalPath=aHR0cHM6Ly9jaXNjby5zaGFyZXBvaW50LmNvbS86Zjovcy9DU0RMQ2xvdWRPZmZlclNlY3VyaXR5Q29tL0VxcVJ0X1VMSG81QnRxU2dMZHJMNDVNQl9ZSzRYNlEtdUg3eXNhbDZfdEtiT1E_cnRpbWU9TWp4NWhaRDkxMGc)

[Cisco Information Security Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1490198&ver=approved)

# Requirement References

    ---
    foreign_id: SEC-OPS-REVOKE
    relation: connects
    headline: |-
      SEC-OPS-REVOKE puts
              specific constraints on your SEC-OPS-RDY SOP's
              response to changes in user status.

    targets:
    - services
    source: PSB
    ---
    foreign_id: A.12.1
    relation: connects
    headline: |-

              ISO 27002:2013: A.12.1 Operational procedures and responsibilities

    targets:
    - '12'
    source: ISO 27002:2013
    ---
    foreign_id: A.12.2
    relation: connects
    headline: |-

              ISO 27002:2013: A.12.2 Protection from malware

    targets:
    - '12'
    source: ISO 27002:2013
    ---
    foreign_id: A.12.3
    relation: connects
    headline: |-

              ISO 27002:2013: A.12.3 Backup

    targets:
    - '12'
    source: ISO 27002:2013
    ---
    foreign_id: A.12.4
    relation: connects
    headline: |-

              ISO 27002:2013: A.12.4 Logging and monitoring

    targets:
    - '12'
    source: ISO 27002:2013
    ---
    foreign_id: A.12.5
    relation: connects
    headline: |-

              ISO 27002:2013: A.12.5 Control of operational software

    targets:
    - '12'
    source: ISO 27002:2013
    ---
    foreign_id: A.12.6
    relation: connects
    headline: |-

              ISO 27002:2013: A.12.6 Technical vulnerability management

    targets:
    - '12'
    source: ISO 27002:2013
    ---
    foreign_id: A.12.7
    relation: connects
    headline: |-

              ISO 27002:2013: A.12.7 Information systems audit considerations

    targets:
    - '12'
    source: ISO 27002:2013

# History

```yaml
-----
affected_psb: SEC-OPS-RDY-3
description:  Updated to functional requirements and evidence changes.
---
deprecated_psb: SEC-OPS-RDY-2
impact: normative
headline: >
  [SEC-OPS-RDY](#SEC-OPS-RDY) migrated to functional requirements
```


# Attributes

    phase: requirements
    legallysensitive: true
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Cloud Offers
        class: not_MobileApp
    category: Operational Process
    riskArea: Risk Assessment
    waivable: true
    version: 3
    id: SEC-OPS-RDY
    issueref: ISS_NoSecProgram
    tags:
    - CloudCritical
    - Cloud
