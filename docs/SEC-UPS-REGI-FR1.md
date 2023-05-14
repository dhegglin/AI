
# Headline
Register Third Party Software

# Behavior

1.  All included [third-party software](#DEF_ThirdPartySoftware) _MUST_ be registered in the [Third Party Software Compliance and Risk Management (TPSCRM)](https://tpscompliance.cisco.com/). This enables Cisco to perform a company-level organized response (Legal, Security, etc).
Development organizations _MAY_ use an alternative Third Party Software registration solution that is accessible to PSIRT and Cisco Legal teams, provided the arrangement is clearly documented and is formally approved in advance by the Security and Trust Organization.
1.  Offer teams _MUST_ review their TPS inventory for correctness and accuracy, and manually add third party components and update component versions that were not identified by the automated scans.  
**Supplemental Guidance** Teams using TPSCRM can do this via the [TPCRM registry in the Corona tool](https://corona.cisco.com/)
1.  Offer teams _MUST_ remove from their TPS inventory all components that have been removed from the offer.
1.  Offer teams _MUST_ produce a Software Bill of Materials (SBOM) in SPDX format that meets the baseline component data field requirements of Executive Order 14028 (for details see [Designing US Executive Order 14028-compliant SBOMs](https://cisco.sharepoint.com/:w:/s/sbom/ERXMhSMobtJEmp3uTBzPOysBtcSYpG-OLkyHyJut25WDmQ).  )
**Supplemental Guidance** Teams using TPSCRM can do this via the [TPS Compliance tool](https://tpscompliance.cisco.com).  
1.  Offer teams _SHOULD_ remove components that are no longer being used or accessed (such as when one crypto library is replaced by a different library) from their codebase.

# History

```yaml
-----
affected_psb: SEC-UPS-REGI-3
impact:  normative
description:  Added requirement for SBOM, clarified language.

-----
affected_psb: SEC-UPS-REGI-3
impact:  non-normative
description:  Changed to discrete FR's

-----
affected_psb: SEC-UPS-REGI-3
impact:  non-normative
description:  Updated links from TPSD (old tool name) to TPSCRM.  Added "should" guidance to update TPSCRM registry whenever TPS in the offer is changed.
```

# Attributes

    id: SEC-UPS-REGI-FR1
    version: 4
    category: Development Process
    riskArea: Risk Assessment
    legallysensitive: true
    waivable: true
    issueref: ISS_SEC-UPS-REGI
    applicability:
      - force: mandatory
        target:
          restrict: >
            [products](#DEF_Product) containing
            [third party software](#DEF_ThirdPartySoftware)
    priority: 10
    phase: requirements
    tags:
    - EN/PD
    - EN/PI
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
