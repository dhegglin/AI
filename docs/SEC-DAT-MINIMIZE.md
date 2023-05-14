# Headline

Minimize collection, use, and storage of data

# Description

The offering team provides functions that minimizes the data processing (collection, create, use, analysis, retention) throughout an offering's lifecycle to only that which is needed for the function to be successful or required by law. This applies to all [processed data](#DEF_DataProcessing) with a special focus on personally identifiable information (PII) about an individual.

# Key Benefits

Minimizing the data that is processed by an offering during its design lowers the risk of harm as well as the cost of managing, protecting, and storing data to the customer, organization, and person the data identifies.

# Behavior

## SEC-DAT-MINIMIZE-FR1: Data Collection Minimization

The offering team _MUST_ minimize the amount of data that their offering collects to only what is absolutely necessary for the offering to perform its functions.

If the data inventory documented in compliance by SEC-DAT-KNOWWHAT shows data collection is more than what is absolutely necessary, the offer team _SHOULD_ not collect the excess data, (unless the collection method has no feasible method to remove during collection and then the excess data _MUST_ be deleted as soon as possible during use).

When the data capture mechanism does not have the functionality to minimize PII (e.g. video, voice, 3rd party data set, etc), the offering team _MUST_ implement procedures or mechanisms to delete the captured PII as soon possible if it is not needed for its stated legitimate business purpose.

## SEC-DAT-MINIMIZE-FR2: Active Use of PII

The offering team _MUST_ have functions that use the PII data that is collected at the time of data collection.

## SEC-DAT-MINIMIZE-FR3: Documented and Approved Purpose for PII

The offering team _MUST_ use PII for only the specific purposes that has been documented in compliance by SEC-DAT-KNOWWHAT and documented externally in the Cisco's Privacy Statement and/or Privacy Data Sheet.  

## SEC-DAT-MINIMIZE-FR4: Legal Basis for PII

The offering team _MUST_ minimize the PII data processed to that for which [legal basis](#DEF_LegalBasis) is established and documented in compliance by SEC-DAT-KNOWWHAT.

[Sensitive PII](#DEF_SensitivePII) _MUST_ be collected only under explicit opt-in consent.  If explicit consent mechanisms are embedded in the service or product, explicit consent must be captured and viewable along with the purpose for processing. If any use  of sensitive personal information differs from the use the subject expected at the time of collection, consent _MUST_ be updated for this new purpose before using the data. If the consent mechanism is embedded in the service or product and consent is withdrawn, the processing of that data _MUST_ be stopped. 

## SEC-DAT-MINIMIZE-FR5: Proportion

The offering team _SHOULD_ only process personally identifiable information (PII) that is adequate, relevant, and not excessive for the purpose(s) for which it is processed. If substituting more proportional PII elements is not possible or practical, additional controls (such as pseudonymization, encryption, masking, or limited retention) _MAY_ be sufficient to make the processing of the PII fair and legitimate; however, this option _MUST_ be reviewed and approved by Cisco Legal or the Cisco Chief Privacy Office and documented as part of the relevant Privacy Assessment (see SEC-DAT-KNOWWHAT).

The offer team _SHOULD_ verify that the quantity and sensitivity of the PII is proportionate to the purpose for which it is being processed and document as part of the Privacy Assessment.

The offer team _SHOULD_ verify that the PII being processed is relevant to the purpose for which it is being processed and that the least amount of PII needed for the purpose will be processed.

## SEC-DAT-MINIMIZE-FR6: Local Identifiers

The offering team _SHOULD_ create local identifiers for individuals. Offering-local personal identifiers _SHOULD_ be generated at random, not derived from other identifiers or other personal information, and not assigned serially or based on the time at which a person was added to a database.

The offering team _SHOULD NOT_ use or store personal identifiers that are meaningful outside of its offering, unless a specifically identified need requires the use of those particular identifiers to interoperate with some external system that uses them. If an external personal identifier is the only choice, the offering team _SHOULD_ expose it only to parts of the offering that actually need to communicate with the external systems that use it. In this instance, the offering team _SHOULD_ use OS-level or database-level access controls and internally generated identifiers to communicate between different parts of the offering itself in order to enforce this restriction.

## SEC-DAT-MINIMIZE-FR7: PII Data De-identification

The offering team _SHOULD_ use other de-identification techniques such as encryption or masking where ever possible to de-risk the processing of PII. These de-identification techniques still require the controls outlined in the PSBs for PII.

## SEC-DAT-MINIMIZE-FR8: PII Data Anonymization

The offering team _MAY_ design its offering to process data in such a way that it can no longer be used to identify a natural person by using 'all the means reasonably likely to be used' and is irreversible by either the controller or a third party.

**Supplemental Guidance**: Once PII has been anonymized, it is not considered PII and no longer requires PII specific controls. The offering team should verify the anonymization technique with Cisco Chief Privacy Office to ensure anonymization has been met.

## SEC-DAT-MINIMIZE-FR9: Data Storage

The offering team _MUST_ design the offering to minimize the amount of data stored to meet the customer's retention policy, and is adequate, relevant, and not excessive for the purpose(s) for which it is processed.

## SEC-DAT-MINIMIZE-FR10: PII Data Deletion

The offering team _MUST_ design the offering to delete captured PII when it is no longer required for its current, legitimate business purpose.  

**Supplemental Guidance**: When the products/services data capture mechanism does not have the functionality to minimize PII (e.g. video, voice, 3rd party data set, etc), the development team must implement procedures to delete the captured PII as soon possible if it is not needed for its current, legitimate business purpose.

# Normative References

* [NIST 800-53 Security and Privacy Controls](https://csrc.nist.gov/publications/detail/sp/800-53/rev-4/final)
* [SOC](https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/serviceorganization-smanagement.html)
* [Cisco Security & Trust Organization Privacy and Data Protection Policies and Standards](https://policycentral.cloudapps.cisco.com/cppc/function/6510/)
* [Cisco Code of Business Conduct](https://wwwin.cisco.com/c/cec/organizations/legal/ethics/cobc.html)
* [General Data Protection Regulation (GDPR)](https://ec.europa.eu/info/law/law-topic/data-protection_en)

# Attributes

    id: SEC-DAT-MINIMIZE
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
    priority: 8
    phase: requirements
    tags:
    - EN/PI
    - CloudCritical
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
