# Headline

Use standard logging protocols

# Description

Use standard protocols for logging. The "flagship" protocol is SYSLOG over TLS (over TCP). Use structured data, and get the authentication right.

# Behavior

The PSB requires all [offerings](#DEF_Offering) to log certain events that are relevant to security and are commonly called "security events".

Use standard secure transmission protocols when sending security events to any log collector outside of your offering itself.

## SEC-LOG-PROTO-FR1: Network Device Logging Protocols

A standard logging protocol _MUST_ be used when logging security events to any log collector outside of the networking device itself.  It _SHOULD_ be possible to use more than one of the standard protocols as appropriate for the [offering's](#DEF_Offering) components or environment.

Originators _SHOULD_ use structured data for all fields required by [SEC-LOG-CONTENT](#SEC-LOG-CONTENT).

One or more of the following protocols are expected to be implemented in networking devices:

- SYSLOG
  - RFC5425 (TLS/UDP):  SYSLOG speakers using TLS _MUST_ apply bidirectional X.509 authentication to their TLS sessions.  
  - RFC5426 (UDP):  SYSLOG over UDP.
  - RFC6587(TCP):  SYSLOG over TCP.
  - SYSLOG relays and collectors _MUST_ verify the hostname received in *each individual log message* against the authenticated name of the hosts from which they receive those messages, and _MUST_ ensure that any discrepancies are recorded in the log. A collector that accepts messages via one or more relays _MUST_ maintain detailed configuration information describing the hostnames for which each relay is authorized to forward information.
- SNMP Traps
  - Any [offering](#DEF_Offering) that sends SNMP traps to any [agent](#DEF_Agent) outside of the [offering](#DEF_Offering) itself _MUST_ provide a MIB that permits structured recovery of all the fields.
  - SNMPv3 traps _MUST_ be capable of encryption.
- AAA Protocols
  - Examples include Kerberos, TACACS+, and RADIUS

## SEC-LOG-PROTO-FR2: Public Cloud Logging Protocols

Offers that operate in the cloud _MUST_ support cloud native logging protocols.  It is typical for cloud offers to support only one logging method that is specific to the public cloud platform.

One of the following protocols are expected to be implemented in public cloud offers:

- Amazon Web Services (AWS)
  - AWS CloudTrail:  audit logging service that keeps track and records AWS application program interface (API) calls, actions, and changes.
  - VPC Flow Logs:   a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC.

- Microsoft Azure
  - Activity Logs:  Provides insight into the operations that were performed on Azure resources.
  - Network security group (NSG) flow logs:  Displays information about ingress and egress IP traffic through a Network Security Group.
- Google Cloud Platform
  - Cloud Audit Logs:  Provides the admin activity, data access, system events, and policy denied audit logs for each Cloud project, folder, and organization.

# Informative References

Cisco Security Logging Standard:
<https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1401894>

* RECIPE: [Log Security-relevant Information](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Log%20SecurityRelevant%20Information.aspx)
* RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)

# Requirement References

    ---
    foreign_id: SEC-LOG-CENTRAL
    relation: connects
    headline: |-
      SEC-LOG-CENTRAL
              requires a central logging collector for every
              Cisco service. The collector must comply with
              the protocol requirements of SEC-LOG-PROTO.
    
    source: PSB
    ---
    foreign_id: SEC-LOG-PROTO
    relation: connects
    headline: |-
      SEC-LOG-CONTENT
              describes the information to be included in log
              message. SEC-LOG-PROTO describes how to deliver
              that information, including how to structure it
              for further processing at the collector.
    
    source: PSB

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: offerings
    category: Logging and Auditing
    riskArea: Logging & Monitoring
    waivable: true
    version: 1
    id: SEC-LOG-PROTO
    issueref: ISS_LogScatter
    tags:
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
