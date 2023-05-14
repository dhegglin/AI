# Headline

Service account credentials should only be known to designated essential custodian(s)

# Description

Exposure of credentials through sharing and/or inadequate protection is one of the leading causes of system compromise. There are many schemes that involve elaborate attacks, such as phishing campaigns, that attempt to trick users into sharing their passwords. The general user community tends to take a relaxed attitude with respect to protection of passwords. As a result, passwords become an easy target for attackers.

Service account credentials may need to be known by a minimum number of designated custodian(s) for operational redundancy purposes.

# Behavior

Implement security processes that restrict credential sharing between users and user groups.

Certain privileged service accounts (e.g. root and administrator accounts) require specific technical controls governing their usage
(SEC-OPS-SUDO).

## SRC-CRE-SHARE-FR1:  Restrict Sharing

Service (generic, machine, applications, etc) account credentials _MUST_ be known by a minimum number of custodian(s) based on job role, responsibility and operational requirements.

## SRC-CRE-SHARE-FR2:  Track and Reauthorize 

Service account  credentials that are shared _MUST_ be strictly tracked and every custodian(s)' "need to know" _MUST_ be re-approved periodically as noted in SEC-OPS-REVOKE.

# Informative References

[OWASP Category: Access Control](https://www.owasp.org/index.php/Category:Access_Control)

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-OPS-REVOKE
    relation: connects
    headline: |-
      SEC-OPS-REVOKE Ensures accounts are reviewed periodically to remove non-essential custodian(s).
    ---
    source: PSB
    foreign_id: SEC-OPS-SUDO
    relation: connects
    headline: |-
      SEC-OPS-SUDO Implement restricted root and sudo access.

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Cloud Offers
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    waivable: true
    version: 2
    id: SEC-CRE-SHARE
    issueref: ISS_BadPws
    tags:
    - CloudCritical
    - Cloud
