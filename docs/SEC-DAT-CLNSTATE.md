# Headline
Securely sanitize all physical storage to enter a clean state and protect customer data from exposure.

# Key Benefits
Customers and users of Cisco on-prem offerings expect support for media sanitization. Increasingly, customers will not return, repurpose, recycle, or dispose of a product until it has been sanitized on their premises. A lack of media sanitization capabilities and associated clear, transparent documentation is creating resistance to RMAs and hindering participation in Cisco's Takeback & Reuse Program. Key business outcomes of supporting media sanitization include legal and regulatory compliance, improved customer experience around RMA returns, greater participation in the Takeback & Reuse Program, and lower business costs. If media sanitization is not supported, or only partially supported, sensitive customer data may be exposed, and to the detriment of our customers and our brand.

# Description
Implement and document capabilities and procedures for sanitizing physical media in or attached to on-prem devices. Physical media could include but is not limited to flash-based storage (SSD, eUSB, eMMC, EEPROM), magnetic media (ATA, SCSI), and peripherally attached storage (USB, FireWire). For attached media, only Cisco-branded media are subject to this requirement.

# Behavior

## SEC-DAT-CLNSTATE-FR1: Purge Capabilities
The offering _MUST_ implement data purge capabilities to align to NIST 800-88 guidelines. Purge capabilities _MAY_ be automated (including self-service) or manual. Removable media _SHOULD_ have a purge mechanism.

Purge capabilities _MUST_ render the information unrecoverable by machine or human, but still maintain the integrity of the media for transfer or reuse.

**Supplemental Guidance**: Purging data goes beyond the normal sanitization technique of clearing physical media using standard read write commands. Purging applies physical or logical techniques that render target data recovery infeasible by ordinary and extraordinary means as guided in the implementation section.


Cryptographic erase is a suitable substitute for sanitizing the target data’s encryption key.

The offer team _MUST_ determine and implement the level of sanitization required to remove all user data from each each nonvolatile memory according to the most sensitive data stored.

1.  Use the [Cisco Product Nonvolatile Data Taxonomy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-22727162) to determine the minimum level of sanitization required for each instance of nonvolatile storage in your offer: [NIST Purge](#DEF_NistPurge), [NIST Clear](#DEF_NistClear), or none required.

2.  For all instances that require [NIST Purge](#DEF_NistPurge), enable NIST Purge. For any instances where NIST Purge is required but not enabled, consider the offer as noncompliant with this requirement. In those cases, document the remediation plan, including target software release dates, and reference that remediation plan in the offer SRP. 

Pay particular attention to nonvolatile memory devices with integrated controllers, as the controller may not permit the host to access all of the raw memory locations, including those that may contain remnant customer data. For example, see [Feasibility of NIST SP 800-88r1 Purge with eMMC](https://cisco.sharepoint.com/sites/CSDLTeam/Shared%20Documents/Document%20Administration/Feasibility%20of%20NIST%20SP%20800-88r1%20Purge%20with%20eMMC.pdf). 

**Supplemental Guidance:** Plan on implementing data encryption for data subject to NIST Purge so that cryptographic erase can be used as the Purge mechanism.

3.  For all instances that do not require NIST Purge but do require sanitization, implement [NIST Clear](#DEF_NistClear) or NIST Purge. For any instances where NIST Clear is required but not enabled, consider the offer as noncompliant with this requirement. In those cases, document the remediation plan, including target software release dates, and reference that remediation plan in the offer SRP.

## SEC-DAT-CLNSTATE-FR2: Media Sanitization Records

A sanitization process _MUST_ create or update a record consisting of each sanitization attempt and the result (i.e. success or failure). This sanitization record _MUST_ be readable post-sanitization. A sanitization process _SHOULD_ store the sanitization record in tamperproof storage.

## SEC-DAT-CLNSTATE-FR3: Media Sanitization Documentation

The offer team _MUST_ create a Statement of Volatility (SoV), which will include a listing of the nonvolatile memory/storage devices containing sensitive data and the associated level of sanitization supported by your software. Use the [Cisco Statement of Volatility Template](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-19553646). This SoV _MUST_ be published to the [Cisco Trust Portal](https://trustportal.cisco.com/c/r/ctp/trust-portal.html#/).

# Normative References
*   NIST SP 800-88r1 https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r1.pdf
   
# Requirement (Informative) References
*	Enterprise Records Retention Schedule  https://cisco.sharepoint.com/sites/ERIM/SitePages/Cisco's-Retention-Schedule.aspx
*	Enterprise Data Retention and Destruction Policy https://policy.cisco.com/cppc/policy-advisor/policies/view-policy/1431
*	Cisco Security & Trust Organization Privacy and Data Protection Policies and Standards https://policycentral.cloudapps.cisco.com/cppc/function/6510/
*  Cisco Procedures in handling returned and scrap equipment http://www.cisco.com/c/dam/en/us/products/policy_regarding_the_removal_of_data_on_cisco_equipment.pdf
*	NSA/CSS Storage Device Sanitization Manual https://www.nsa.gov/Portals/70/documents/resources/everyone/media-destruction/storage-device-declassification-manual.pdf
*	UCSD SSD Research http://swanson.ucsd.edu/measuring-memories/
*	Degaussing SSD Drives https://techzone.cisco.com/t5/Whiptail-Legacy/Degaussing-SSD-drives/ta-p/487239/comment-id/58#M58
*	Customer Data and Asset Destruction https://techzone.cisco.com/t5/SRE-Lifecycle/Customer-Data-and-Asset-Destruction/ta-p/1019950
*	ISO 27040 https://www.iso.org/standard/44404.html

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
          [offerings](DEF#Offering)
                      that contain or include physical storage media
        class: not_MobileApp
    category: Privacy and Data Security
    riskArea: Data Governance & Protection
    waivable: true
    version: 2
    id: SEC-DAT-CLNSTATE
    issueref: ISS_BadErasure
    tags:
    - EN/PD
    - PSB/OnPrem
    - Critical PSB
