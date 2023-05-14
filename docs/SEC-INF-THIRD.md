# Headline

Qualify and track third-party suppliers

# Description

Keep track of the third parties you're depending on, especially but not
only cloud service providers.

# Behavior

Assure that third-party products and services used with your
[offering](#DEF_Offering) and/or enterprise applications meet all applicable Cisco
security requirement.

## SEC-INF-THIRD-FR1: Third-Party Cloud Services

Third-party "cloud" services must be approved by Infosec's CASPR assessment process.

## SEC-INF-THIRD-FR2: Maintain Inventory of Third-Party Products

Maintain an inventory of commercial, non-Cisco products and services you
use to provide your [offering](#DEF_Offering), containing and/or linking
to the required data for each of the following categories:

1.  "Cloud" services at various layers, including low-level
    infrastructure such as virtual machines or hosted containers,
    higher-level infrastructure such as storage or database services,
    and specialized, application-level or value-added services.

    1.  Active and available instances

    2.  Service level agreements (see also
        [SEC-OPS-LEGAL](#SEC-OPS-LEGAL)).

    3.  Records of CASPR reviews and approvals authorizing the use of
        each service provider.

2.  Software packages and their assorted licenses:

    1.  Names, versions, and options

    2.  License agreements and terms. See also
        [SEC-OPS-LEGAL](#SEC-OPS-LEGAL).

    3.  Maintenance and/or support agreements and terms. See also
        [SEC-OPS-LEGAL](#SEC-OPS-LEGAL).

3.  Standard computing and networking hardware devices.

    1.  Model numbers and versions

    2.  Standard configurations

    3.  Maintenance and/or support agreements and terms. See also
        [SEC-OPS-LEGAL](#SEC-OPS-LEGAL).

4.  For all categories:

    1.  Information about the number of instances in use, where they are
        in use, and what they are being used for. See also
        [SEC-OPS-ASTMGT](#SEC-OPS-ASTMGT), which requires you to be able
        to identify *individual* instances.

    2.  Information about the qualification tests used and the results
        of those tests.

    3.  Information about acceptance tests used for new versions and/or
        new instances.

    4.  Supplier names and contacts.

    5.  Primary Cisco points of contact for suppliers.

    6.  Information necessary to reach and use suppliers' maintenance or
        support services.

Track software licenses and provide functions to assure that you're not
using more instances than you're licensed for.

# Informative References

[Cloud (Third Party Provider) Security Standards](https://policy.cisco.com/cppc/function/6510/)

# Normative References

[CASPR Engagement Page](https://ibpm.cisco.com/casp/app/login/vHmsc6v2hyE2aGQEUHMEvB-N17QLhSux*/!STANDARD)

# Requirement References

    ---
    foreign_id: SEC-OPS-ASTMGT
    relation: connects
    headline: |-
      SEC-OPS-ASTMGT
              requires you to keep track of the individual instances
              of the products and services whose suppliers and
              general nature you track under SEC-INF-THIRD.
              It will often make sense to use the same system,
              or tightly coupled systems,
              to track both the generic information and
              the per-instance information.

    targets:
    - services
    source: PSB
    ---
    foreign_id: SEC-OPS-LEGAL
    relation: connects
    headline: |-
      SEC-OPS-LEGAL
              requires you to keep track of contracts and to make sure
              they get proper legal review. The supplier/product database
              required by SEC-INF-THIRD is a logical place to record
              this information.

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

```yaml
-----
affected_psb: SEC-INF-THIRD
description:  Updated to functional requirements. 

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
    version: 2
    id: SEC-INF-THIRD
    issueref: ISS_NoSecProgram
    tags:
    - CloudCritical
    - Cloud
