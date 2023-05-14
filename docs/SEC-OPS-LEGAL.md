# Headline

Manage third party agreements properly

# Description

Third party agreements and "boilerplate" must be reviewed by counsel
annually. You must have a complete inventory of current legal
agreements. Procedures must be in place to monitor and assure Cisco and
supplier compliance.

# Behavior

## SEC-OPS-LEGAL-FR1: Maintain Third-Party Agreement

Cisco legal counsel _MUST_ review all third party agreements affecting
software, products, or services used to provide the
[offering](#DEF_Offering).

You _MUST_ maintain an inventory of such agreements, and of the
parties to each such agreement. You _MUST_ keep records of when each
agreement was last reviewed, by whom, and the results of the review.
Note: This is usually best done together with the more general
inventories required by
[SEC-INF-THIRD](#SEC-INF-THIRD)[SEC-OPS-ASTMGT](#SEC-OPS-ASTMGT).

You _MUST_ informed reviewing counsel of the jurisdictions in which
the [offering](#DEF_Offering) and the components affected by the
reviewed agreements are operated and in which their services are
offered, as well as of any identified regulatory concerns specific to
those jurisdictions.

New and updated agreements _MUST_ include current and approved
standard security language and service level agreement language. This
standard language _MUST_ be reviewed annually, and you _MUST_ keep
records of the purposes and jurisdictions for which counsel has approved
its use.

## SEC-OPS-LEGAL-FR2: Implement & Monitor Compliance Controls

Controls _MUST_ be in place to assure Cisco's compliance with each
agreement currently in effect, including but not limited to adhering to
any applicable usage limits and maintaining any required records. This
_MUST_ include complete compliance review no less often than annually.
These controls _SHOULD_ be in your standard operating procedures (see
[SEC-OPS-RDY](#SEC-OPS-RDY)).

You _MUST_ monitor supplier compliance with agreements, including but
not limited to adherence to agreed-upon service levels. Procedures for
monitoring _SHOULD_ be in your standard operating procedures (see
again [SEC-OPS-RDY](#SEC-OPS-RDY)).

You _MUST_ assign a supplier manager responsible for ensuring that all
parts of this requirement are met with respect to every agreement.

# Requirement References

    ---
    foreign_id: SEC-INF-THIRD
    relation: connects
    headline: |-
      SEC-INF-THIRD
              requires you to track the third party suppliers, product,
              and services you use. The required database is a logical
              place to keep the data you collect for
              SEC-OPS-LEGAL.

    targets:
    - services
    source: PSB
    ---
    foreign_id: C.9.3
    relation: connects
    headline: |-

              ISO 27002:2013: C.9.3 Management review

    targets:
    - C
    source: ISO 27001:2013
    ---
    foreign_id: A.15.1
    relation: connects
    headline: |-

              ISO 27002:2013: A.15.1 Information security in supplier relationships

    targets:
    - '15'
    source: ISO 27002:2013
    ---
    foreign_id: A.15.2
    relation: connects
    headline: |-

              ISO 27002:2013: A.15.2 Supplier service delivery management

    targets:
    - '15'
    source: ISO 27002:2013
    ---
    foreign_id: A.18.1.1
    relation: connects
    headline: |-

              ISO 27002:2013: A.18.1.1 Identification of applicable legislation and contractual requirements

    targets:
    - '18'
    source: ISO 27002:2013
    ---
    foreign_id: CLD 12.4.5
    relation: connects
    headline: |-

              ISO 27017:2015/27002 for cloud services: CL D 12.4.5 Montitoring of cloud services control

    targets:
    - '12'
    source: ISO 27017:2015

# History

pm4_filehist

# Attributes

    phase: requirements
    legallysensitive: true
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Cloud Offers
        class: not_DataConfidential
    category: Operational Process
    riskArea: Risk Assessment
    waivable: true
    version: 2
    id: SEC-OPS-LEGAL
    issueref: ISS_NoSecProgram
    tags: 
    - Cloud
