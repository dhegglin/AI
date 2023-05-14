# Headline
Do not use third-party software with known high risk.

# Key Benefits

We deliver more secure and robust software when we avoid using known, vulnerable software. This helps avoid embarrassment and reputation damage when known vulnerable software is found in our offerings.

# Description
Third-party software is present in most Cisco offerings, and provides many attack vectors.  We can identify components and component versions known to have serious associated risk.  Those components should not be included in our software.

This requirement currently refers to two sources for known risk in TPS components - Cisco's [PSIRT Exclusion List](https://corona.cisco.com/exclusion_list?sortKey=name&sortDirection=asc) and the component [Kenna risk score](https://help.kennasecurity.com/hc/en-us/articles/360026160592-Vulnerability-Scoring-in-Kenna).  Other sources may be included as technologies and tools improve.

# Behavior


## SEC-UPS-TPSQUAL-FR1: Component versions listed on the PSIRT Exclusion List
Component versions listed on the [PSIRT Exclusion List](https://corona.cisco.com/exclusion_list?sortKey=name&sortDirection=asc) _MUST_NOT_ be included in released software.  
These component versions _MUST_ be updated to versions (or replaced by other components) that are not prohibited by this requirement (e.g versions or components with acceptable Kenna risk scores and which are not on the PSIRT Exclusion List).

## SEC-UPS-TPSQUAL-FR2: Other components with identified known, significant risk
A "risk score" for each component in an SBOM is present on the Corona "Image BOM Report".

Component versions with a Kenna risk score of 67 or greater have a high probability of being used as attack vectors and _SHOULD_NOT_ be included in released software.  These components _SHOULD_ be removed from the code and replaced with components or functionality that are not prohibited by this requirement.

**Exceptions** Exceptions to FR1 and FR2 can be made for cases where the offer team has reviewed all CVEs that are relevant to the component version and that have SIR scores of Critical, High, or Medium, and have ascertained and documented that those CVEs have either been mitigated or are not applicable to the offer.

# Normative References
[CSDL Third-Party Software Vulnerability Management Process](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-20122701)

# History

```yaml
-----
..affected_psb: SEC-UPS-TPSQUAL
..description:  Created requirement

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings containing third-party software.

    category: Development Process
    riskArea: Software Updates & Patching
    waivable: true
    version: 1
    id: SEC-UPS-TPSQUAL
    issueref: ISS_TPSOld
    tags:
    - EN/PD
    - EN/PI
    - PSB/OnPrem
    - Cloud
