# Headline

Log ENC services to protect sensitive log data

# Key Benefits

The protection and integrity of logs, being transported across the network, requires a combination of both strong Encryption and [Authentication](#DEF_Authentication) services to be in place.

# Description

Implement protection and integrity of logs in the transit.

Authentication services to be in place.

# Behavior

## SEC-LOG-TRANS-FR1: Secure Transport

All logs that are sent across the network to a centralized logging system, and/or any other log monitoring/alerting system _MUST_ have control in place to provide a combination of [authentication](#DEF_Authentication) and encryption services to ensure the integrity of logs sent across the network.

Customer requirements _MUST_ also be taken into account.

# Informative References

* RECIPE: [Log Security-relevant Information](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Log%20SecurityRelevant%20Information.aspx)
* RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)


# Normative References

1.  [CentOS Hardening Standards and Encryption of logs](https://wiki.cisco.com/display/CSGSECARC/CentOS Hardening Standard)
2.  [Cisco Records Management Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-880241) (specified maximum log retention time of 3 years) and [Cisco Monitoring and System Logging Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1401894&ver=approved)
3.  [Information Security Policies](https://docs.cisco.com/share/page/site/nextgen-edcs/documentlibrary#filter=path|Security and Trust Organization%2FInformation Security%2FCompliance%2FPolicies)

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Hosted and Infrastructure Services
        class: ServiceThing
    category: Logging and Auditing
    riskArea: Logging & Monitoring
    waivable: true
    version: 1
    id: SEC-LOG-TRANS
    issueref: ISS_DataMishandled
    tags: 
    - Cloud
