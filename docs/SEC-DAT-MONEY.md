# Headline

Use PCI DSS Compliant Payment Processor(s) for processing financial data.

# Key Benefits

Processing bulk financial transactions in offerings is complex, highly regulated, and is not a core competency for Cisco.  As a matter of policy we have decided not to develop such a competency to be Payment Card Industry Data Security Standard (PCI DSS) compliant.  This provides added security for our customers and for Cisco.

# Description

Information that can be used to get money is a huge target with enormous legal, regulatory, and contractual pitfalls. Any
processing of credit cards must be Payment Card Industry Data Security Standard (PCI DSS) compliant.

# Behavior

## SEC-DAT-MONEY-FR1: PCI DSS Compliance
The offering team _MUST_ process (store, transmit, or use) any credit card numbers (Primary Account Numbers, PANs) in
compliance with PCI DSS.

## SEC-DAT-MONEY-FR2:  Use qualified external processors
The offering team _SHOULD_ contract all credit card processing to reputable, properly insured outside services. The services
contract _MUST_ guarantee compliance with PCI and regulatory standards, and _MUST_ meet all PSB requirements for sensitive
PII, and all other Cisco policies for outside service providers and for financial partners.

## SEC-DAT-MONEY-FR3:  Other Financial Identifiers
For other kinds of [financial identifiers](#DEF_FinancialIdentifier), the offer team _SHOULD_ make all possible efforts to
find reputable, properly insured outside payment processors that comply with the PSB, other Cisco policy, and any applicable
industry standards or regulations for the [financial identifier](#DEF_FinancialIdentifier) types in question.

For non-credit-card [financial identifiers](#DEF_FinancialIdentifier) and for which no reliable external processors exist, the
offer team _MUST_ seek help from the privacy office and/or the PCI working group to comply with financial and privacy and data
protection regulations.

# Implementation

The implementation guidance is available in separate documents. Please refer to the implementation guidance template for more
information.

# Verification

The Verification guidance is available in separate documents. Please refer to the verification guidance template for more
information.

# Normative Reference

[Cisco Privacy and Data Protection Policies and Standards](http://policy.cisco.com)

# Informative References

If a PCI processor is needed, contact the [Software Technology Sourcing](https://cisco.sharepoint.com/sites/GSMSoftwareandCloud-CommunicationsPage) team from GPS.

# Attributes

    ---
    id: SEC-DAT-MONEY
    version: 2
    issueref: ISS_DataMishandled
    category: Privacy and Data Security
    riskArea: Data Governance & Protection
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
            restrict: Cloud Offers, Mobile Applications and Enterprise Offerings
            class: ServiceThing_OR_MobileApp
    priority: 8
    phase: requirements
    tags:
    - Cloud
