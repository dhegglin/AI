# Headline

Separation of SaaS logs for customers

# Key Benefits

The separation of Logs for customers/tenants _MUST_ follow applicable legal and/or regulatory requirements. These requirements may vary per different geographic locations. It is [essential](#DEF_Essential) that logs are separated for auditing and investigative purposes for specific customers/tenants.

# Description

Logically separate logs for different customers/tenants.

# Behavior

## SEC-LOG-TENISOL-FR1: Separate Logs

Hosted and Infrastructure Services _MUST_ provide capability to logically separate/isolate logs, when accessed, for specific customers/tenants.

**Supplemental guidance:** Add a separate tag/field to identify the customer/tenant. This will help to ensure that in case of investigation, logs for specific customers or tenants can be separated from other customers. This can be [critical](#DEF_Critical) for investigations, audits, and/or incident response.

# Informative References

* RECIPE: [Log Security-relevant Information](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Log%20SecurityRelevant%20Information.aspx)
* RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)

# Normative References

-   [CSA IS 23 - (Cloud Security Alliance: Information Security - Incident Reporting)](https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v1-4/)
-   [CSA CCM SEF (Security Incident Management)](https://cloudsecurityalliance.org/research/cloud-controls-matrix/)

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Hosted and Infrastructure Services
    category: Logging and Auditing
    riskArea: Logging & Monitoring
    waivable: true
    version: 2
    id: SEC-LOG-TENISOL
    issueref: ISS_TenantMix
    tags: 
    - Cloud
