# Headline

Track production assets

# Description

You _MUST_ have a complete inventory of all assets.

# Behavior

## SEC-OPS-ASTMGT-FR1: Asset Management Standard

Follow the [Cisco Asset Management Stardard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1453224) regarding business application inventory, services, hosts, and platforms which _MUST_ be registered in a S&TO-approved and S&TO-accessible System of Record.

## SEC-OPS-ASTMGT-FR2: Alternate Asset Management or System of Record Exception Approval (Condition: Optional:Offerings)

The Asset Management Standard allows for a S&TO-approved asset management solution, in which:

An inventory _MUST_ list all of the assets used to provide any Cisco
service [offering](#DEF_Offering). This inventory _MUST_ include:

* devices used directly to provide such services
* all Cisco-managed supporting infrastructure
* network devices
* virtual machine hosts
* all resources dedicated to Cisco services by "cloud" infrastructure-as-a-service providers

The inventory _MUST_ include:

1. Physical assets, including but not limited to:
    1. Computer equipment
    1. Storage devices
    1. Communications equipment, including but not limited to routing and switching equipment
    1. Power and environmental control equipment
    1. Removable media
1. Virtual machines and other
   virtual [network elements](#DEF_NetworkElement) or virtual operating
   system instances, such as containers
1. Templates, images, construction specifications, and software
   packages used to deploy new virtual machines, containers, etc
1. Software Assets: application software, system software, development
   tools, and utilities

For each asset, the inventory _MUST_ record:

* A unique identifier for the asset--If the asset is a physical object
  with a value of more than US$5000, this _MUST_ be the identifier of
  an RFID tag attached to the asset
* The type and capabilities of the asset
* The function for which the asset is used
* The names and contact information of those with policy authority
  over and/or responsibility for the asset
* The names and contact information of those responsible for
  supporting the asset and/or responding to misbehavior by the asset
* The asset's location, if it has one
* The asset's criticality, in the sense of the impact of its failure
* The general nature and sensitivity classification of any data stored
  or handled by the asset--You _MUST_ record the Cisco data protection
  classification ("Cisco Public", "Cisco Confidential", etc), _SHOULD_
  record the PSB classification ("[public](#DEF_Public)",
  "[private](#DEF_Private)", "[sensitive](#DEF_Sensitive)", and/or
  "[critical](#DEF_Critical)"), and _MAY_ also record classifications
  in other taxonomies
* Life cycle status applicable to the asset's type--For example
  whether the asset is awaiting deployment, is in active use, is
  awaiting erasure or decomissioning, is available for reuse, is
  unusable, is awaiting disposal, etc
* Whether, when, and how the asset has last been [erased](#DEF_Erase) or
  otherwise prepared for repurposing or decomissioning
* Enough information to determine whether the asset is presently in
  a [clean state](#DEF_CleanState) or is otherwise known to be free of
  non-[public](#DEF_Public) data

For each asset, the inventory _SHOULD_ record:

* The manufacturer's serial number, if any
* Any "hardwired" network addresses such as MAC addresses
* Any locally assigned identifiers such as IP addresses or DNS names
* The complete history of changes to inventory data about the asset

## SEC-OPS-ASTMGT-FR3: General (Condition: Force:Mandatory, Restrict:Enterprise)

Enterprise Service Portfolio (ESP) is Cisco enterprise asset management tool and should be used for asset registration and management. Infosec _MUST_ review any other asset management tool, which _MUST_ provide a data feed to S&TO.

# Normative References

* [Asset Management Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1453224)

# Informative References

* [ESP Dependency Mapping](https://cisco.sharepoint.com/sites/ILMOInfrastuctureCompliance/SitePages/Frequently-Asked-Questions.aspx#mapping)

* [Add an Application Dependency](https://cisco.sharepoint.com/sites/ILMOInfrastuctureCompliance/SitePages/Frequently-Asked-Questions.aspx#mapping)

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-INF-THIRD
    target: services
    relation: connects
    headline: >
        [SEC-INF-THIRD](#SEC-INF-THIRD)requires you to keep track of the
        products, services, and suppliers on which you depend. Many of the
        items tracked under SEC-OPS-ASTMGT will be individual instances of the
        generic categories tracked under SEC-INF-THIRD. It will often make
        sense to use the same system, or tightly coupled systems, to track
        both the generic information and the per-instance information.
    ---
    source: PSB
    foreign_id: SEC-OPS-RDY
    target: services
    relation: connects
    headline: >
        [SEC-DAT-ISMS](#SEC-DAT-ISMS)and[SEC-OPS-RDY](#SEC-OPS-RDY)both
        require documented policies and procedures for maintaining the
        inventory required by SEC-OPS-ASTMGT, and the required documents are
        useful in verifying compliance with SEC-OPS-ASTMGT.
    ---
    source: PSB
    foreign_id: SEC-CRY-ALWAYS
    target: services
    relation: connects
    headline: >
        [SEC-CRY-ALWAYS](#SEC-CRY-ALWAYS)requires that
        non-[public](#DEF_Public)data be kept inside controlled space. This
        affects erasure and decommissioning practices. SEC-OPS-ASTMGT requires
        tracking and recording erasure and decomissioning.
    ---
    source: PSB
    foreign_id: SEC-INF-SCAN
    target: services
    relation: connects
    headline: >
        [SEC-INF-SCAN](#SEC-INF-SCAN)requires running periodic network
        scans. The resulting reports can be used to help verify compliance
        with SEC-OPS-ASTMGT by finding devices that are missing from the
        inventories. Conversely, the inventory required by SEC-OPS-ASTMGT can
        be useful in finding devices to scan for[SEC-INF-SCAN](#SEC-INF-SCAN).
    ---
    source: ISO 27001:2013
    foreign_id: C.4.4
    target: C
    relation: connects
    headline: >
        ISO 27001:2013: C.4.4 Information security management system
    ---
    source: ISO 27002:2013
    foreign_id: A.12.5
    target: 12
    relation: connects
    headline: >
        ISO 27002:2013: A.12.5 Control of operational software
    ---
    source: ISO 27002:2013
    foreign_id: A.8.1
    target: 8
    relation: connects
    headline: >
        ISO 27002:2013: A.8.1 Responsibility for assets
    ---
    source: ISO 27002:2013
    foreign_id: A.8.2
    target: 8
    relation: connects
    headline: >
        ISO 27002:2013: A.8.2 Information classification
    ---
    source: ISO 27017:2015
    foreign_id: CLD 8.1
    target: 8
    relation: connects
    headline: >
        ISO 27017:2015/27002 for cloud services: A.8.1 Responsibility for
        assets

# Attributes

    id: SEC-OPS-ASTMGT
    version: 4
    category: Operational Process
    riskArea: Risk Assessment
    legallysensitive: false
    waivable: true
    issueref: ISS_AssetClueless
    applicability:
      - force: mandatory
        target:
          class: not_MobileApp
          restrict: >
            services
    priority: 8
    phase: requirements
    tags:
    - CloudCritical
    - Cloud
