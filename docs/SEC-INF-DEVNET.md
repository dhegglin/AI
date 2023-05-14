# Headline

Separate production and non-production environments

# Description

Physically and/or logically separate production and non-production
(stage, development, test, demo, QA, etc.) environments to protect data
and assets.

# Behavior

## SEC-INF-DEVNET-FR1: Seperate environments
Production environments and non-production environments _MUST_ be
separate.

## SEC-INF-DEVNET-FR2: Restrict access to production targets
Operating in a non-production environment _MUST_NOT_ provide an
[agent](#DEF_Agent) with any access to production [target](#DEF_Target).

Among many other applications of this general rule--

1.  Systems in non-production environments _MUST_NOT_ use or possess
    [credentials](#DEF_Credential) that would work in the production
    environment.

2.  Network segmentation _MUST_NOT_ allow any network traffic between
    production and non-production networks.

3.  Production and non-production systems _MUST_NOT_ share files,
    databases, or other data stores. Reference
    [SEC-OPS-NPROD](SEC-OPS-NPROD) for information on preventing
    customer data being used in non-prod environment.

4.  Production and non-production systems _SHOULD_NOT_ be run in the
    same operating system instance (which usually means on the same
    virtual machine or on the "bare metal" of the same physical
    machine).

5.  Non-production environments _SHOULD_ be segmented and managed as
    different control zones when possible..

# Requirement References

    ---
    foreign_id: SEC-INF-FIREWALL
    relation: connects
    headline: |-
      SEC-INF-FIREWALL require
              segmenting the offering into zones and putting firewalls
              between them, and between the offering and the outside
              world. These same firewalls can of course help to separate
              the production offering from the associated development
              and staging networks.

    targets:
    - services
    source: PSB
    ---
    foreign_id: SEC-OPS-ASTMGT
    relation: connects
    headline: |-
      SEC-OPS-ASTMGT requires
              keeping inventory information that will usually be useful
              in verifying compliance with SEC-INF-DEVNET.

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
    foreign_id: A.12.5
    relation: connects
    headline: |-

              ISO 27002:2013: A.12.5 Control of operational software

    targets:
    - '12'
    source: ISO 27002:2013
    ---
    foreign_id: CLD 12.1
    relation: connects
    headline: |-

              ISO 27002:2013: 27002 for cloud services: CLD 12.1 Operational procedures and responsibilities

    targets:
    - '12'
    source: ISO 27017:2015

# History
```yaml
-----
affected_psb: SEC-INF-DEVNET
description:  Updated to functional requirements.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Cloud Offers
        class: ServiceThing
    category: Development Process
    riskArea: Data Governance & Protection
    waivable: true
    version: 3
    id: SEC-INF-DEVNET
    issueref: ISS_NetArch
    tags:
    - CloudCritical
    - Cloud
