# Headline

Run network and host vulnerability scans and mitigate or remediate issues found.

# Description

Scan routinely for network and host vulnerabilities, using standard tools. Mitigate or remediate vulnerabilities you find.

# Behavior

## SEC-INF-SCAN-FR1: Vulnerability Management Standard

Your offering _MUST_ comply with the [Vulnerability Management Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1453239&ver=approved) with regards to vulnerability scanning of your production networks and remediation of vulnerabilities identified by that scanning.

The Vulnerability Management Standard contains details on criteria and SLAs for completing infrastructure vulnerability scans, including the definitions of S-Rating (Severity) and Operational Security Rating (OSR) classification.

The Vulnerability Management Standard also specifies an exception process. Offerings with exceptions approved according to that process are compliant with this requirement.

NOTE: The Vulnerability Management Standard is binding Cisco policy in its own right, and may also be referred to by other PSB requirements. To simplify compliance tracking, SEC-INF-SCAN restricts its attention to specific parts of the Vulnerability Management Standard. This does _not_ imply that the rest of the Vulnerability Management Standard doesn't affect your [offering](#DEF_Offering).

## SEC-INF-SCAN-FR2: Self-Scanning Exception Approval (Condition: Optional:Offerings)

The Vulnerability Management Standard allows for an S&TO-approved scanning solution, in which offerings provide some or all scanning services using their own tools and processes. S&TO will approve an alternative self-scanning arrangement that meets the following:

1. The arrangement _MUST_ be documented and the agreement signed by the organization's Security Officer or equivalent.

1. The following items are required beyond what the Vulnerability Management Standard specifies:

   1. All assets
      ([SEC-OPS-ASTMGT](#SEC-OPS-ASTMGT)) must be scanned at least every 72 hours.
   1. Exclusions _MUST_ be documented and approved by the organization's Security Officer.
   1. The scans _SHOULD_ BE at least as comprehensive as those provided by the usual S&TO infrastructure and settings. S&TO's standard
      scanning tool is Qualys, and the usual settings are described
      at [https://cspo-wiki.cisco.com/pages/viewpage.action?pageId=72056877](https://cspo-wiki.cisco.com/pages/viewpage.action?pageId=72056877).
   1. Scan reports _SHOULD_ imported into a tracking system that may be audited.
   1. S&TO Vulnerability Management _MUST_ have access to vulnerability reports.

# Informative References

* Vulnerability Identification and Remediation (Overview and FAQs): [https://cspo-wiki.cisco.com/pages/viewpage.action?pageId=72056877](https://cspo-wiki.cisco.com/pages/viewpage.action?pageId=72056877)
* Engage with S&TO Vulnerability Management Team at [https://vuln-mgmt.cisco.com](https://vuln-mgmt.cisco.com)

# Normative References

* Cisco Vulnerability Mangement Policy,
  EDCS-1453239, [https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1453239&ver=approved](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1453239&ver=approved)
* NIST Special Publication 800-53: Security Controls Control RA-5: Vulnerability Scanning
  [https://nvd.nist.gov/800-53/Rev4/control/RA-5](https://nvd.nist.gov/800-53/Rev4/control/RA-5)

# Requirement References

    ---
    source: ISO 27002:2013
    foreign_id: A.12.2
    roreigntarget: 12
    relation: connects
    headline: >
        ISO 27002:2013: A.12.2 Protection from malware
    ---
    source: ISO 27002:2013
    foreign_id: A.12.5.1
    roreigntarget: 12
    relation: connects
    headline: >
        ISO 27002:2013: A.12.5.1 Control of operational software: installation
        of software on operational systems
    ---
    source: ISO 27002:2013
    foreign_id: A.12.6.1
    roreigntarget: 12
    relation: connects
    headline: >
        ISO 27002:2013: A.12.6.1 Management of technical vulnerabilities
    ---
    source: ISO 27002:2013
    foreign_id: A.12.6.2
    roreigntarget: 12
    relation: connects
    headline: >
        ISO 27002:2013: A.12.6.2 Restrictions on software installation
    ---
    source: ISO 27017:2015
    foreign_id: CLD 13.1
    roreigntarget: 12
    relation: connects
    headline: >
        ISO 27017:2017/27002 for cloud services: CLD 13.1 Network security
        management
# History

```yaml
-----
affected_psb: SEC-INF-SCAN
description:  Updated to functional requirements. 

```

# Attributes

    id: SEC-INF-SCAN
    version: 4
    category: Operational Process
    riskArea: Risk Assessment
    legallysensitive: false
    waivable: true
    issueref: ISS_SoftNodes
    applicability:
      - force: mandatory
        target:
          restrict: >
            Services
    priority: 9
    phase: requirements
    tags:
    - CloudCritical
    - Cloud
