# Headline

Revoke unnecessary access

# Description

Immediately disable all user [access](#DEF_Access) which ceases to be
justified by a business need.

# Behavior

## SEC-OPS-REVOKE-FR1: Review & Modify Access

Whenever a user's status or responsibilities change in a way that might
affect any of the criteria you use to decide what system
[access](#DEF_Access) to grant to users, you _MUST_ promptly review
and adjust that user's privileges and permissions, deleting the account
entirely if appropriate.

Processes and controls for this _MUST_ be part of your standard
operating procedures (see [SEC-OPS-RDY](#SEC-OPS-RDY)).

This applies to all user access, including for employees, contractors,
customers, business partners, and others... and for users who move from
one of these categories to another.

## SEC-OPS-REVOKE-FR1: Periodic Review of Preivilleged Accounts

In addition to on-demand adjustments, you _MUST_ periodically review
[access](#DEF_Access) to [targets](#DEF_Target)[critical](#DEF_Critical)
to overall system security, and all specially privileged or
[administrative](#DEF_Administer) access. Reviews _MUST_ be conducted
by someone with the authority to decide on access permissions, and
records of reviews _MUST_ be maintained.

# Requirement References

    ---
    foreign_id: SEC-OPS-RDY
    relation: connects
    headline: |-
      SEC-OPS-RDY
              requires developing a standard operating procedure
              addressing many concerns. SEC-OPS-REVOKE
              provides detail on one of those concerns.

    targets:
    - services
    source: PSB

# History

pm4_filehist

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Cloud Offers
        class: not_MobileApp
    category: Operational Process
    riskArea: Risk Assessment
    waivable: true
    version: 2
    id: SEC-OPS-REVOKE
    issueref: ISS_NoSecPolicy
    tags:
    - CloudCritical
    - Cloud
