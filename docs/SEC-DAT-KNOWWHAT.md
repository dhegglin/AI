# Headline

Know what data your product or service processes and assess the privacy risk.


# Key Benefits

Customers, stakeholders and employees expect Cisco offerings to process all data per data regulations and data principles of confidentiality, integrity, fairness, accessibility,accountability, transparency, privacy, and security. With an inventory of data being processed, the functions provided, and the controls already being applied, Cisco can determine what controls should be embedded to meet privacy and data standards and regulations. Cisco can then be transparent about the data the product or service processes and the controls available to the customer to meet their privacy policy. 

# Description

All offer (development and legal) teams must document what data is being processed by its offering's functions,
including [personally identifiable information (PII)](https://cserv.cisco.com/library/glossary/CG47),customer data, and corporate data and then provide this documentation for assessment to determine the controls required to meet data standards and regulations data policies by reviewing.

# Behavior

All offers _MUST_ document what data is being processed by the offering's functions, whether or not they believe or determine that the offer does not process PII (Personally Identifiable Information).

Perform your data analysis using the [One Trust tool](https://privacybydesign.cisco.com/).  Guidance and instructions at the [CSDL Data Assessment]( https://cisco.sharepoint.com/sites/STO-CPO-OneTrustAtCisco/SitePages/CSDL-Data-Assessment.aspx) page.

The following functional requirements provide steps to accomplish an assessment of how an offering processes data. These
functional requirements are followed during an offering's design phase and any time the major changes of policy, the offer's functions, the data processed by the offer, and/or embedded controls occur. If no major changes occur within one year of the previous assessment, the assessment must be done annually.

## SEC-DAT-KNOWWHAT-FR1: Data Inventory

All development teams _MUST_ inventory and document all [data elements](#DEF_DataElement) and groups of data elements that are processed by their offering that could identify a person.. These data elements include data that has been:

* Created by the offering
* Captured by the offering
* Stored with other personal data, becoming PII given its inferred relationship
* Used by the offering as training data for its Artificial Intelligence/Machine Learning (AI/ML) algorithms.
* Shared with/from other offerings/telemetry/data collections/third-parties and processed by this offering

**Supplemental Guidance**: All [data elements](#DEF_DataElement) include data categories used for administration, management, debugging, licensing, metadata as well as offer's function and any customer provided data. Processing includes collection, creation, storage, use, analysis, organization, recording,
alignment, combination, disclosure by transmission/sharing, consultation, erasure, destruction, alteration, and so on.

## SEC-DAT-KNOWWHAT-FR2: Data Classifications

For each [data element](#DEF_DataElement) or collection of data elements, the development team _MUST_ document a classification of its
confidentiality level and PII along with its purpose. For data being used for training AI/ML, the development team _MUST_
document the information about its collection (legal basis, data owner/steward, integrity state, data bias given coverage or
non-coverage of person or groups of people which will be affected by the automated decision)


## SEC-DAT-KNOWWHAT-FR3: Data Governance
(Previously SEC-DAT-KNOWWHAT-FR4)

The development team _MUST_ document the existing inventory of data governance control mechanisms and any default settings required for data retention,
accuracy, and availability.

1. Data Retention
  * Process or mechanism to implement enterprise and/or customer data archiving/retention functionality including retention
  period
  * Set a default retention period and establish a retention process/technology to manage this retention policy across the data
  lifecycle.

## SEC-DAT-KNOWWHAT-FR4: Data Security Controls
(Previously SEC-DAT-KNOWWHAT-FR6)

The development team _MUST_ document the existing data security controls provided to protect the data, including protection at rest, protection in transit, and access management. 

**Supplemental Guidance**:
For all offerings:

* Encryption mechanisms to protect customer data and sensitive data such as PII and enterprise sensitive data classified
highly confidential or restricted in transit and at rest [(SEC-CRY-ALWAYS-2)](#SEC-CRY-ALWAYS-2).

## SEC-DAT-KNOWWHAT-FR5: Privacy Governance & Controls
(Previously SEC-DAT-KNOWWHAT-FR7)

The development team _MUST_ document existing data privacy controls (embedded technology and/or process) provided to protect
the data.

**Supplemental Guidance**:
Examples of privacy governance controls include:

1. Data Subject Rights [(SEC-PRV-DSRIGHTS)](#SEC-PRV-DSRIGHTS)
  * Access to the Notice
  * Consent when PII is sensitive and product is going for SOC Certification
  * Process or mechanism to allow PII data subject the ability to access, add, change, delete, block, and port PII provided to the offer.
1. Minimization [(SEC-DAT-MINIMIZE)](#SEC-DAT-MINIMIZE)
  * Process data per the legal basis and purpose
  * Collect and use the minimum amount of PII needed per the function 
  * Process or mechanism to delete unneeded personal information 
1. Transparency
  * Process or mechanism to provide notice on the data being processed
  * Process or mechanism to provide data sheet about the offering

## SEC-DAT-KNOWWHAT-FR6: Impact Assessment
(Previously SEC-DAT-KNOWWHAT-FR8)

The development team _MUST_ send the documented information from FR1-FR5 to a trained data privacy and protection subject
matter expert (see recipe on assessment workflow and tools).

This trained data privacy and protection subject matter expert _MUST_ respond with an assessment documenting the current risk and any required
protection, governance, and privacy controls (as either embedded technology or processes) required to remediate the offering. 
Any high risks not remidated in the current release are added to the Security Readiness Plan with a planned date for the remediation to be complete.
The completed assessment status _MUST_ be documented (with the documented remediation plan for controls not currently
supported) to indicate this requirement is complete.

This assessment _SHOULD_ be done during the design phase. This assessment _MUST_ be done any time there is a major change of
data, its classification, or its operational environment's context at any stage of the offering's development or operational
lifecycle.

**Supplemental Guidance**: This assessment determines if the current level of controls sufficiently meets our data policies
given the data, its classification, and its context and will lead to one of the following status:

1. All controls are already in the offering or the offering has a process in place to meet the policies
1. All controls will be in the offering or the offering has a process in place before release/launch
1. The must-have controls are in place or in the release plan and the desirables are in the plan for future releases (with
dates)
1. The must-have controls are not in the plan (this requires an escalation between the data protection and privacy office and
the business owner to determine a remediation plan)

## SEC-DAT-KNOWWHAT-FR7: Data Transparency
(Previously SEC-DAT-KNOWWHAT-FR9)

Product and Services development teams _SHOULD_ produce customer-level documentation on what data the offering or application
processes. _If_ a privacy data sheet is to be shared, then it _MUST_ be reviewed the by legal and
the Cisco privacy office to be shared per business need.


## SEC-DAT-KNOWWHAT-FR8: Up-to-Date Documentation
(Previously SEC-DAT-KNOWWHAT-FR10)


The development team _MUST_ keep the inventory, classification, context, and control documentation up-to-date given data
content, classification, and control changes during the development of an offering or application; be it agile,
continuous development, or waterfall methodologies.

The development team _MUST_ re-submit for a new assessment if any changes require new functions or controls.
If no major change, an annual assessment _SHOULD_ be made to ensure the documentation is up to date.


# Informative References

* Recipe: [Building and Maintaining Privacy Data Sheets and Data Flow Maps](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Producing%20A%20Privacy%20Data%20Sheet%20and%20Data%20Map.aspx)

# Normative References

* The Cisco [One Trust tool](https://privacybydesign.cisco.com/)
* NIST 800-53 Security and Privacy Controls
* FedRamp SSP-A04-FedRAMP-PIA-Template
* [SOC](https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/serviceorganization-smanagement.html)
* Cisco  [Privacy and Data Protection Policies and Standards](https://policycentral.cloudapps.cisco.com/cppc/function/6510/)
* Cisco [Code of Business Conduct](https://wwwin.cisco.com/c/cec/organizations/legal/ethics/cobc.html)

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-PRV-DSRIGHTS
    roreigntarget: services
    relation: connects
    headline: >
      Rights of Personally Identifiable Information's Data Subject
    ---
    source: PSB
    foreign_id: SEC-DAT-MINIMIZE
    roreigntarget: services
    relation: connects
    headline: >
      Minimize collection of personal information
    ---
    source: PSB
    foreign_id: SEC-PRV-USERAUTH
    roreigntarget: services
    relation: connects
    headline: >
      Control user access to personal information

# Attributes

    id: SEC-DAT-KNOWWHAT
    version: 2
    issueref: ISS_Privacy
    category: Privacy and Data Security
    riskArea: Data Governance & Protection
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
          class:
          restrict: >
            offerings
    priority: 10
    phase: requirements
    tags:
    - EN/PI
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
    - Cloud
