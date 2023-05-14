# Headline

Protect against Supplier backdoors, malware, or known vulnerabilities.

# Key Benefits

Cisco products that include third-party offerings are vulnerable to backdoors from those sources. Contracts with third parties need to include language that protect Cisco and Cisco’s customers from backdoors and other vulnerabilities. Appropriate language provides protections and strengthens trust.

# Description

Contracts need to include warrantees that cover backdoors, malware, or known vulnerabilities.  Suppliers also need to commit to informing Cisco of any vulnerabilities and fixing those issues in a timely manner.

Opensource software: Evaluate your selection with security in mind.  See “Implementation Guidance” for more ideas on evaluating opensource.

Commercial software:  Evaluate your selection with security in mind; place requirements on the product; and add support elements to the agreement.

# Behavior

## SEC-UPS-NOBACK-FR1: Warrantees

FR1 applies to vendor relationships where there is a contract present.

1. Contracts _MUST_ include a vendor’s warranty that the offering is free from backdoors, malware, critical or high severity vulnerabilities.

## SEC-UPS-NOBACK-FR2: SLAs

FR2 applies to vendor relationships where there is a contract present.

1. Contracts _MUST_ include the vendor’s obligation to inform Cisco of vulnerabilities in a timely manner.
1. Contracts _SHOULD_ include timelines and obligations to fix based on severity that allow for Cisco to meet its PSIRT policy.
1. Contracts _SHOULD_ provide time-limit for disclosure to Cisco.

## SEC-UPS-NOBACK-FR3: SDL

FR3 applies for commercial suppliers, OEM, and ODM agreements.

1. Selected suppliers _SHOULD_ show evidence of a Secure Development Lifecycle (SDL).
1. Supplier _SHOULD_ clearly document security requirements during the requirements gathering phase of the development lifecycle.
1. Supplier _SHOULD_ clearly document how the design meets the identified security requirements. One of the ways in which to meet this requirement is through a traceability matrix.

## SEC-UPS-NOBACK-FR4: Provide Requirements

FR4 applies for commercial suppliers, OEM, ODM and reseller agreements.

1. Developers _SHOULD_ provide security requirements in procurement (e.g., in RFIs and RFPs).
1. The developer _MAY_ select specific PSBs that are relevant to the offering/component being procured.  For example, pertaining to high risk, or not applicable to the function of the component.

## SEC-UPS-NOBACK-FR5: Opensource Quality

FR5 applies when opensource is in the [offering](#DEF_Offering).

1. A developer that is selecting opensource _SHOULD_ evaluate that code from a security perspective prior to selection.

# Normative References

* Value Chain Security Architecture Policy - [EDCS - 11693735](https://docs.cisco.com/share/page/dp/ws/faceted-search#searchTerm=11693735&scope=repo&sortField=Relevance)

# History

---
affected_psb: SEC-UPS-NOBACK
impact: normative
description: The requirement scope increased beyond backdoor to include other vulnerabilities.

# Attributes

    id: SEC-UPS-NOBACK
    version: 2
    issueref: ISS_UpstBackDoor
    category: Threat Surface Reduction
    riskArea: System Hardening
    legallysensitive: false
    waivable: true
    applicability:
    - force: mandatory
      target:
        restrict: >
          [offerings](#DEF_Offering)
    priority: 9
    phase: requirements
    tags:
     - EN/PD
     - EN/PI
     - PSB/OnPrem
