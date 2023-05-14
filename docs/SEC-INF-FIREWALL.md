# Headline

Provide firewall protection between security zones and within the solution.

# Key Benefits

Network inspection and access controls between security zones provide layered security against threats.

# Description

"Firewall" functionality must be implemented between your service and
the Internet and for networks and/or zones where there is a change in
trust boundaries. Firewalls are often categorized as either network
firewalls or host-based firewalls. Network firewall services filter
traffic between two or more networks and run on network appliances,
either virtual or physical, or at the edge of a network. Host-based
firewalls or security groups run on host computers or the hypervisor
that control virtual machines and control network traffic in and out
of those machines.

Implement strong security controls to protect firewall deployment
implementations. With ?firewalls? we not only refer to physical
hardware devices but also to virtual firewall appliances, access
control lists at security boundaries, security groups, etc. It is the
intent of the implementation that defines your ?firewall?, not its
physical presentation.

Create firewall policies as closed as possible (e.g., "default
deny"). Do not forget to consider egress traffic.

# Behavior

## SEC-INF-FIREWALL-FR1 Separation Between Zones

Firewall functionality _MUST_ be implemented between your services
where there is a change in trust boundaries (Security Zones). These trust boundaries
_SHOULD_ align with those found
via [SEC-ASU-TMOD-FR1](#SEC-ASU-TMOD-FR1) activities.

Security Zones are defined within a cloud offering solution by the
security architect, or by the security organization for on-premise
networks. If your offering uses network elements in any of the
following classes, the elements in that class _MUST_ be treated as a
zone separate from any elements in any of the other classes. You _MAY_
subdivide elements into smaller zones, and _MAY_ define additional
zones for other types of network elements

1. The public Internet and other public networks (this includes any network containing a network element over which you do not exercise control).
1. Network elements within your offering providing services to network elements on the public Internet.
1. Network elements providing "backend" services, intended to be process connections or requests only from other network elements that are themselves inside your offering.
1. Network elements dedicated to providing service to any specific customer.
1. Network elements dedicated to management or monitoring of offering assets, but not directly used to provide the offering's services.

## SEC-INF-FIREWALL-FR2 Rule Sets

1. Firewall rule set implementations _MUST_ enforce least privileged
   access. (E.g., Limit protocols in use, Limit endpoint address
   ranges used within protocols, Limit ports when possible, etc.)
1. Firewall _MUST_ meet logging standards
   ([SEC-LOG-CHANGES-FR1](#SEC-LOG-CHANGES), [SEC-LOG-ADMIN](#SEC-LOG-ADMIN), [SEC-LOG-CHANGES-FR6](#SEC-LOG-CHANGES), [SEC-LOG-PROTO](#SEC-LOG-PROTO), [SEC-LOG-CENTRAL](#SEC-LOG-CENTRAL))
1. Firewalls _MUST_NOT_ be bypassed.

## SEC-INF-FIREWALL-FR3 Management and Process

Firewall configuration management process and procedures _MUST_
satisfy the following requirements:

1. Firewall access rules _MUST_ conform to a least access granted model.
1. Properly document firewall rules for both inbound and outbound traffic.
1. Only authorized security or network staff may manage firewall
   configurations and separation of duties _MUST_ be maintained.
1. Follow operational procedures for making and monitoring any
   configuration changes ([SEC-OPS-RDY](#SEC-OPS-RDY)).
1. Regular and formal review of firewalls setups/configurations _MUST_
   be regularly conducted to verify actual firewall settings conform
   with approved firewall changes.
1. Your staging environment(s) _SHOULD_ replicate all of the zones and
   firewalls used in your production environment(s).

## SEC-INF-FIREWALL-FR4 Enterprise Technical Controls (Condition: Restrict:Enterprise)

Enterprise on-premise Firewalls _MUST_ have the following capabilities

1. Support packet filtering including IPv4 and IPv6, protocol, source address, destination address, source port, and destination port
1. Support filtering traffic using identity-based policy integration (ISE/SGA/SGT)
1. Support stateful packet inspection
1. Support Advanced Protocol inspection

## SEC-INF-FIREWALL-FR5 Enterprise Approvals (Condition: Restrict:Enterprise)

1. InfoSec approval is required for security policy changes to access policy implemented between zones (trust boundaries).
1. New on-premise network environments _MUST_ be evaluated with the Infosec to establish the zone security and governance model.

# Informative References

* [Network Zoning to Reduce External Exposure in AWS](https://apps.na.collabserv.com/wikis/home?lang=en-us#!/wiki/W24133c2f3210_4feb_abf6_7c79e730b217/page/Network%20Zoning%20to%20Reduce%20External%20Exposure%20in%20AWS)
* [GCP Network Zoning to restrict external exposure](https://apps.na.collabserv.com/wikis/home?lang=en-us#!/wiki/W42b2253429d0_4bce_9dac_58caeccc09e9/page/GCP%20Network%20Zoning%20to%20restrict%20external%20exposure)
* [Guardrail for Azure Network Zoning](https://apps.na.collabserv.com/wikis/home?lang=en-us#!/wiki/W42b2253429d0_4bce_9dac_58caeccc09e9/page/Guardrail%20for%20Azure%20Network%20Zoning)
* RECIPE: [Engage with Enterprise Infrastructure Architecture Team](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Engage%20with%20Infosec%20Infrastructure%20Architecture%20Team.aspx)

# Normative References

* [Internet Firewall Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1127921)
* RECIPE: [Engage with Enterprise Infrastructure Architecture Team](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Engage%20with%20Infosec%20Infrastructure%20Architecture%20Team.aspx)
# Requirement References

    ---
    source: PSB
    foreign_id: SEC-INF-MONITOR
    roreigntarget: services
    relation: connects
    headline: >
        [SEC-INF-MONITOR](#SEC-INF-MONITOR)requires monitoring for signs of
        intrusion at various points in your network.  Firewall devices are
        sometimes capable of providing the required monitoring services.
    ---
    source: PSB
    foreign_id: SEC-OPS-RDY
    roreigntarget: services
    relation: connects
    headline: >
        [SEC-OPS-RDY](#SEC-OPS-RDY)requires documenting many of the same
        elements as required by[SEC-DAT-ISMS](#SEC-DAT-ISMS)and
        SEC-INF-FIREWALL.
    ---
    source: PSB
    foreign_id: SEC-ASU-TMOD-FR1
    roreigntarget: services
    relation: connects
    headline: >
        [SEC-ASU-TMOD-FR1](#SEC-ASU-TMOD-FR1)requires preparing network maps which
        will include most firewall filtering points, and collecting data that
        may help to determine what firewall policies are needed.
    ---
    source: PSB
    foreign_id: SEC-ASU-TMOD-FR1
    roreigntarget: offerings
    relation: connects
    headline: >
        SEC-ASU-TMOD-FR1](#SEC-ASU-TMOD-FR1) requires analyzing various exposures
        and protections at controlled space boundaries. The firewalls required
        by SEC-INF-FIREWALL are natural places to put controlled space
        boundaries, and many PSB requirements demand controlled space for
        various purposes.
    ---
    source: PSB
    foreign_id: SEC-CRY-ALWAYS
    roreigntarget: offerings
    relation: connects
    headline: >
        [SEC-CRY-ALWAYS](#SEC-CRY-ALWAYS)requires you to cryptographically
        protect all traffic that goes outside of specific types of properly
        analyzed[controlled space](#DEF_ControlledSpace). Since boundaries of
        such[controlled space](#DEF_ControlledSpace)will often fall at
        firewalls, many firewalls will have to enforce that all traffic
        crossing them use encrypted protocols.
    ---
    source: PSB
    foreign_id: SEC-LOG-ADMIN
    roreigntarget: services
    relation: connects
    headline: >
        [SEC-LOG-ADMIN](#SEC-LOG-ADMIN)requires logging all administrative
        changes to service configurations. This duplicates SEC-INF-FIREWALL's
        specific requirement to log firewall policy changes (and any violation
        found in verifying SEC-INF-FIREWALL indicates a violation of
        SEC-LOG-ADMIN).
    ---
    source: PSB
    foreign_id: SEC-LOG-CONTENT
    roreigntarget: offerings
    relation: connects
    headline: >
        [SEC-LOG-CONTENT](#SEC-LOG-CONTENT)describes the information to be
        included in log entries, including the entries required to be
        generated under SEC-INF-FIREWALL.
    ---
    source: PSB
    foreign_id: SEC-LOG-CENTRAL
    roreigntarget: services
    relation: connects
    headline: >
        [SEC-LOG-CENTRAL](#SEC-LOG-CENTRAL)requires that logged information,
        including the information demanded by SEC-INF-FIREWALL, be delivered
        to central collection points in specific ways.
    ---
    source: ISO 27001:2013
    foreign_id: A.10.6.1
    roreigntarget: A
    relation: connects
    headline: >
        ISO 27001:2013: A.10.6.1 Network controls
    ---
    source: ISO 27001:2013
    foreign_id: A.10.6.2
    roreigntarget: A
    relation: connects
    headline: >
        ISO 27001:2013: A.10.6.2 Security of network services
    ---
    source: ISO 27001:2013
    foreign_id: A.11.4.6
    roreigntarget: A
    relation: connects
    headline: >
        ISO 27001:2013: A.11.4.6 Network connection control
    ---
    source: ISO 27001:2013
    foreign_id: A.11.4.7
    roreigntarget: A
    relation: connects
    headline: >
        ISO 27001:2013: A.11.4.7 Network routing control
    ---
    source: ISO 27002:2013
    foreign_id: A.6.2
    roreigntarget: 6
    relation: connects
    headline: >
        ISO 27002:2013: A.6.2 Mobile devices and teleworking
    ---
    source: ISO 27002:2013
    foreign_id: A.12.1
    roreigntarget: 12
    relation: connects
    headline: >
        ISO 27002:2013: A.12.1 Operational procedures and responsibilities
    ---
    source: ISO 27002:2013
    foreign_id: A.13.1.1
    roreigntarget: 13
    relation: connects
    headline: >
        ISO 27002:2013: A.13.1.1 Network controls
    ---
    source: ISO 27002:2013
    foreign_id: A.13.1.2
    roreigntarget: 13
    relation: connects
    headline: >
        ISO 27002:2013: A.13.1.2 Security of network services
    ---
    source: ISO 27017:2015
    foreign_id: CLD 12.1
    roreigntarget: 12
    relation: connects
    headline: >
        ISO 27002:2013: CLD 12.1 Operational procedures and responsibilities

# History

```yaml
-----
affected_psb: SEC-INF-FIREWALL
description:  Updated to functional requirements. 

```
# Attributes

    id: SEC-INF-FIREWALL
    version: 3
    category: Traffic and Protocol Protection
    riskArea: Network Security
    legallysensitive: false
    waivable: true
    issueref: ISS_NetArch
    applicability:
      - force: mandatory
        target:
          restrict: >
            services
    priority: 8
    phase: requirements
    tags:
    - CloudCritical
    - Cloud
