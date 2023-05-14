# Headline
Control user and system access to personal information

# Key Benefits
This requirement helps ensure that offer will address legal obligations and customer expectations that only customer authorized and authenticated persons or systems will access or process only the personally identifiable  data entrusted to it for authorized purposes.

# Description
Access to [PII](#DEF_PII) and capabilities to [process](#DEF_DataProcessing) this data are only provided to authorized and authenticated persons or systems for authorized purposes. This aligns with SOC-2 P4.1 "The entity limits the use of personal information to the purposes identified in the entity’s objectives related to privacy".

# Behavior

## SEC-PRV-USERAUTH-FR1: Implement Roles Based Access Controls Per PII Purpose
"The [offering](#DEF_Offering) _MUST_ provide the capability to restrict user and system access to [personal information](#DEF_PersonalInformation):
- to the roles and/or systems authorized by the customer/administrator.
- to that necessary for each user to perform the role(s) assigned.

## SEC-PRV-USERAUTH-FR2: Implement Monitoring of Roles Based Access Controls Per PII Purpose
The offering team _MUST_ implement processes or technology to monitor and record/log who and/or what has access to and/or is using PII and what processing took place.

**Supplemental Guidance**: PII being processed during Lawful Intercept will not be logged or visible to any process outside of law enforcement.

# Normative References
Cisco Security & Trust Organization [Privacy and Data Protection Policies and Standards](https://policycentral.cloudapps.cisco.com/cppc/function/6510/)
Cisco [Code of Business Conduct](https://wwwin.cisco.com/c/cec/organizations/legal/ethics/cobc.html)

# Attributes

    ---
    id: SEC-PRV-USERAUTH
    version: 3
    issueref: ISS_Privacy
    category: Privacy and Data Security
    riskArea: Data Governance & Protection
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
            restrict: Offers
    priority: 8
    phase: requirements
    tags:
    - EN/PI
    - Cloud
