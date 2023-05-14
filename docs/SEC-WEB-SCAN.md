# Headline

Run application vulnerability scans and fix issues

# Key Benefits

New application and middleware vulnerabilities are reported daily. Moreover, new
application releases introduce known and unknown issues, including those made
through misconfiguration. Performing regularly scheduled assessments (including
penetration testing for enterprise apps), enable the [security](#DEF_Security) and application teams to
identify and mitigate the vulnerability in a timely manner.

# Description

Applications vulnerabilies can be introduced during development (bug fixes, feature enhancements, major functional changes). Before deployment run automated scanning and validation tools to ensure that your code is secure from basic vulnerabilities.

Enterprise Application require a penetration test under risk criteria listed in the Application Vulnerability Standard. (see Normative References)

# Behavior

## SEC-WEB-SCAN-FR1 Application Vulnerability Scanning (Condition: Force:Mandatory, Restrict:Offers)

Application vulnerability assessment _MUST_ be
performed against the application/service prior to GA (General Availability) or
a major release of the hosted service. The assessment _MUST_ be performed at
least once a year.

## SEC-WEB-SCAN-FR2 Remediation of Findings

All detected vulnerabilities _MUST_ go through remediation and revalidation steps until the vulnerability no longer exists.

## SEC-WEB-SCAN-FR3 Enterprise Dynamic Application Security Test (Condition: Force:Mandatory, Restrict:Enterprise)

All applications, web services, and APIs _MUST_ be tested for vulnerabilities prior to production deployment.

The Application Vulnerability Assessment Standard (see Normative References)
contains details on the criteria and Service Level Agreements (SLAs)
for completing Dynamic Application Security Testing (DAST), also referred
to as Baseline Application Vulnerability Assessment (BAVA certification).

## SEC-WEB-SCAN-FR4 Enterprise Manual Application Security Testing (Condition: Force:Mandatory, Restrict:Enterprise)

Application penetration testing, also referred to as Deep Application
Vulnerability Assessment (DAVA certification) is required for a high-risk
application that meets any of the following conditions:

* The application contains or transacts data classified as Cisco Restricted
* The application contains or transacts data classified as Cisco Highly Confidential and is categorized as one of the following from Cisco Data Taxonomy:
  * Customer Data
  * Financial Data
  * Human Resources Data
  * Entrusted Data
  * Telemetry Data
* As determined by S&TO-Infosec and/or Partner Security Architects (PSA) where other high-risk conditions exist, including but not limited to:
  * externally facing or externally hosted offerings
  * a new technology stack
  * non-standard technology or platform
  * prior security issues with the offering

## Note on Dynamic Vulnerability Assessment Scanning

Application teams are encouraged to use ZAP for scanning. STO-automation tool CAVE uses ZAP and provides good coverage for PSB requirements. 

## Note on Static Code Analysis Enterprise Vulnerability Testing

Static Analysis, Static Application Security Testing (also known Static Code Application Vulnerability Assessments or "SCAVA" in the Enterprise environments), is often mentioned in the same breath with BAVA. The requirements for Static Code Analysis can be found in [SEC-ASU-STATIC](#SEC-ASU-STATIC).

# Informative References

* [Enterprise BAVA Request in EStore (For bava.cisco.com)](http://estore.cisco.com/RequestCenter/website/ServiceCatalog/index.html?/services/1775)
* [CSDL AppScan Request in Estore (for appscan-avt.cisco.com)](http://estore.cisco.com/RequestCenter/website/ServiceCatalog/index.html?/services/1576)
* [ASIG Service Desk Request Portal (DAVA, Pen Test request)](https://sra.cisco.com/jira/servicedesk/customer/portal/2)
* [CAVE Documentation - ReadMe](https://wwwin-github.cisco.com/pages/cave/cave_psb_tests/zap/readme/)
* RECIPE: [Engage with Vulnerability Management Team](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Engage%20with%20Vulnerability%20Management%20Team.aspx)
* RECIPE: [Web UI Testing with AppScan](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Web%20UI%20Testing%20with%20AppScan.aspx)
* RECIPE: [Web Application Fuzzing with Codenomicon](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Web%20Application%20Fuzzing%20with%20Codenomicon.aspx)
 

# Normative References

* [Application Vulnerability Assessment Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1308269&ver=approved)
* [Cisco Application Security Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-759651&ver=approved)
* [Vulnerability Management Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1453239&ver=approved)
* ISO 27001: A.12.6.1 Control of Technical Vulnerabilities
* FedRamp RA-5

# Attributes

    id: SEC-WEB-SCAN
    version: 2
    category: Operational Process
    riskArea: Risk Assessment
    legallysensitive: false
    waivable: true
    issueref: ISS_BasicScans
    applicability:
      - force: mandatory
        target:
          restrict: >
              Hosted and Infrastructure Services
    priority: 9
    phase: requirements
    tags:
    - EN/PI
    - Hardening
    - CloudCritical
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
