# Headline

Prevent customer data from being taken for test etc.

# Description

Don't use customer data for non-production uses. This protects against data theft from less secure environments. Also adheres to strict data [security](#DEF_Security) guidelines of some countries.

# Behavior

Do not replicate production data in a non-production or test environment to avoid leaking sensitive data

## SEC-OPS-NPROD-FR1: Production Data in Non-Production Environment

Procedures MUST be in place to ensure customer production data shall not be replicated or used in non-production or test environments to prevent leaking sensitive data.

Non-production environments are typically less secure than production environments and copying production information into test environments allows access to potentially sensitive information.

Supplemental Guidance: Artificial Intelligence and Machine Learning based applications MAY use production data for training in non-prod environment after masking all the sensitive and customer related information.  Customer data used in AI/ML applications as training data must be controlled in the following manner:

Training data must be assessed like any other data via SEC-DAT-KNOWWHAT and privacy and data protection controls applied.

a.The legal basis must be met (usually a contract with explicit wording indicating data will be used for specific function's automated decisions)

b. Any PII being used as training data must meet both legal basis as well as the purpose for processing outlined in the notice. If PII can be proven to be anonymized, it can be used without the PII purpose limitation. Masking often does not meet this requirement as it can be re-identified. The PII, if collected directly from the end user, is still subject to data subject rights to change/add/delete/port/view.

c. Customer data must be protected by encryption and role based access

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Hosted and Infrastructure Services
        class: not_DataNone_AND_not_DataConfidential
    category: Operational Process
    riskArea: Risk Assessment
    waivable: true
    version: 1
    id: SEC-OPS-NPROD
    issueref: ISS_NoSecProgram
    tags:
    - CloudCritical
    - Cloud
