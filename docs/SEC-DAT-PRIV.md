# Headline

Comply with Cisco’s privacy policies that reflect relevant privacy regulations and standards  

# Description

Cisco's privacy policy outlines the comprehensive set of requirements needed to meet global privacy regulations. This requirement defines the high-level list of capabilities and procedures to be implemented and maintained whenever Personally Identifiable Information ([PII](#DEF_PII)), also known as "personal data" and "personal information" is processed in a Cisco [offering](#DEF_Offering). These capabilities and procedures include:

* Transparency
* Fairness
* Purpose limitation
* Proportionality
* Data integrity
* Data retention
* Data security
* Individual rights

# Key Benefits

Customers, stakeholders and users of Cisco offerings require products and services that process personal information in a manner so that they can meet their privacy obligations.

# Behavior

## SEC-DAT-PRIV-2-FR1: Transparency

The [offering](#DEF_Offering) team _MUST_ provide documentation to customers on the PII that is processed in the offer  so the customer can provide adequate notice to individuals before PII is created or initially collected as outlined in SEC-PRV-DSRIGHTS.  


## SEC-DAT-PRIV-2-FR2: Fairness

When implementing functions that [process](#DEF_DataProcessing) PII, the offering team _MUST_ provide functions that processes personal data fairly as determined via the asssesment(s) required in SEC-DAT_KNOWWHAT and/or in SEC-DAT-MLAI.

**Supplemental Guidance**:
Fair means: Cisco offering should process personal data in a manner that is consistent with the fairness statement Cisco has publicly committed to in its public privacy notice, certifications, and Responsible AI Principles. Examples of fairness in functions includes minimization of bias in conseqential decisions, representation of end users in training data, and processes requiring a human in the loop for automated decisions about an individual.  

## SEC-DAT-PRIV-2-FR3: Purpose Limitation

When implementing functions that [process](#DEF_DataProcessing) PII, the offering team _MUST_ identify and verify the purposes for processing for each element of PII and process the PII only for those stated purposes via the documentation for SEC-DAT_KNOWWHAT.

**Supplemental Guidance**:
Cisco's purposes are listed in the [Business Personal Data Protection and Privacy Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1106658&ver=approved).

## SEC-DAT-PRIV-2-FR4: Proportionality

When implementing functions that [process](#DEF_DataProcessing) PII, the offer _SHOULD_ only process PII that is adequate, relevant, and not excessive for the purpose(s) as outline in SEC-DAT-MINIMIZE.

## SEC-DAT-PRIV-2-FR5: Data Integrity

When implementing functions that [process](#DEF_DataProcessing) PII, tThe offering team _MUST_ provide a mechanism or process to keep personal data accurate, complete, and up-to-date as is reasonably necessary for the purpose(s) for which it is processed as outlined in SEC-PRV-DSRIGHTS

## SEC-DAT-PRIV-2-FR6: Data Retention

When implementing functions that [process](#DEF_DataProcessing) PII, the offering team _MUST_ provide a mechanism or process to keep personal data in a form that is personally identifiable for no longer than necessary to accomplish the purpose(s) for which the personal data was obtained as outlined in SEC-DAT-MINIMIZE.

## SEC-DAT-PRIV-2-FR7: Data Security

When implementing functions that [process](#DEF_DataProcessing) PII, the offering team _MUST_ provide a mechanism or process to safeguard personal data against accidental or unlawful destruction or accidental loss, alteration, unauthorized disclosure, use, or access. Highly confidential and restricted PII, including sensitive PII, _MUST_ support encryption for data at rest and in transit.  Administrators MUST be able to manage or limit access to this data by role or group.

## SEC-DAT-PRIV-2-FR8: Individual Rights

When implementing functions that [process](#DEF_DataProcessing) PII, the offering team _MUST_ provide mechanisms and/or processes when processing personal data that respects individuals' rights of notice, access, rectification, erasure, restriction of processing, objection to processing, and data portability as outlined in SEC-PRV-DSRIGHTS.

# Normative References

* [ISO/IEC 27701:2019](https://www.iso.org/standard/71670.html)
* [General Data Protection Regulation GDPR](https://gdpr-info.eu/)
* [Cisco Security & Trust Organization Privacy and Data Protection Policies and Standards](https://policycentral.cloudapps.cisco.com/cppc/function/6510/)
* [Cisco Code of Business Conduct](https://wwwin.cisco.com/c/cec/organizations/legal/ethics/cobc.html)

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-DAT-KNOWWHAT
    relation: connects
    headline: >
      [SEC-DAT-KNOWWHAT](#SEC-DAT-KNOWWHAT): Know what data you are processing
    ---
    source: PSB
    foreign_id: SEC-DAT-MINIMIZE
    relation: connects
    headline: >
      [SEC-DAT-MINIMIZE](#SEC-DAT-MINIMIZE): Minimize collection of personal information
  
# Attributes

    id: SEC-DAT-PRIV
    version: 5
    issueref: ISS_NoPrivacyPol
    category: Privacy and Data Security
    riskArea: Data Governance & Protection
    legallysensitive: true
    waivable: true
    applicability:
      - force: mandatory
        target:
            class: not_DataNone
            restrict: >
              Services interacting directly with PI subjects
    priority: 8
    phase: requirements
    tags:
    - CloudCritical
    - PSB/OnPrem
    - Cloud
