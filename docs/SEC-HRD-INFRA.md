# Headline

Harden production software and infrastructure components

# Description

Cisco offerings often use software components (containers, web servers) and infrastructure components (hardware, storage, networking) that can be commonly shipped with insecure configuration settings. Systems and their components are reconfigured (or "hardened") to remove these unneeded risks. Industry accepted hardening standards are typically available and define the necessary configuration changes to properly secure these components. Basic examples of hardening include, but are not limited to: disabling unneeded software packages, using most secure configuration settings, disabling unused settings, changing default settings (well-known credentials and secrets), and disabling default accounts, etc.

Note: SEC-HRD-INFRA covers all component families in an offering that are not explicitly identified in the more specific PSB requirements, i.e. [SEC-HRD-OS](#SEC-HRD-OS).

# Behavior

## SEC-HRD-INFRA-FR1: Harden Production Components

Configure each component in the system in accordance with applicable hardening guides or Cisco hardening scripts (selected as described below).

In order of preference:

1. Refer to the Center for Internet Security's [Benchmarks Hardening Guides](https://www.cisecurity.org/cis-benchmarks/) to find component hardening guides for all included components, and complete the recommendations from those hardening guides. For CIS Benchmarks with both Level 1 and Level 2 recommendations, both Level 1 and Level 2 recommendations _MUST_ be implemented.
1. Alternative hardening guides from the application publisher or other well-known security organizations _MAY_ be used when CIS Benchmarks are unavailable or another standard better aligns with the offering's certification strategy (e.g. DISA STIGs)
1. For Services Offerings, if no applicable well-known hardening guide specific to the component can be found, the Application Platform Hardening Guide offers hardening guidance that _SHOULD_ be used as guidance to identify and document appropriate hardening steps.

You _MAY_ choose not to implement specific recommendations within a guide as necessary (e.g. when the recommendation impedes the offering's performance or functionality), but you _MUST_ document your reasons for each such deviation. You MAY choose an equivalently secure alternative solution to a specified recommendation, but you _MUST_ document your reasons and explain how/why the alternate solution is at least equivalent to the recommendation in the guide.

You _MAY_ use vendor or community hardening guides for additional guidance for further guidance.

## SEC-HRD-INFRA-FR2: Document Hardening Method

You _MUST_ document the components and corresponding hardening guides which are used for components in your offering.

If no hardening guide exists, you MUST perform a risk analysis of that component and either:
* Document your analysis indicates that no additional hardening of that component is required, or
* If the risk analysis indicates risks that require a hardening response, create, apply and document the requisite hardening improvements you apply to that component

## SEC-HRD-INFRA-FR3: Enterprise Hardening

```
   applicability:
      - force: mandatory
        target:
         class: ServiceThing
         restrict: Enterprise
```

1. Follow SEC-HRD-INFRA-FR1 for all software and infrastructure components.
1. Enterprise offerings residing in Cisco on-premise environments manage _MUST_ use the GIS-manintained hardened configurations for network infrastructure:
    * Platform-specific configuration blocks (IOS, NX-OS, ASA, etc.)
    * Implementation of items listed in SEC-HRD-INFRA-FR1

## SEC-HRD-INFRA-FR4: Verify Hardened Components

Hardening _MUST_ be verified prior to component deployed in production.

## SEC-HRD-INFRA-FR5: Periodically Verify Hardened Components in Production

```
   applicability:
      - force: mandatory
        target:
            class: ServiceThing
            restrict: Cloud Offers
```
Hardening _MUST_ be periodically verified in production. Hardening verification scripts must run during [standard](#DEF_Standard) change-windows at least once a month.

## SEC-HRD-INFRA-FR6: Log Critical Configuration Changes and Generate Alerts

Critical runtime configuration changes _MUST_ be logged and generate real-time operational alert notifications.

# Informative References

* [Cisco - Securing Your Network](https://tools.cisco.com/security/center/intelliPapers.x?i=55#~Network%20Security>)
* [Configuration Management Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-11216053&ver=approved)
* [Secure Common Cloud Components Team](https://apps.na.collabserv.com/communities/service/html/communitystart?communityUuid=bfcde877-c33f-4b50-b5ff-9c16f4858d44)
* [Cloud 9 Secure Common Cloud Component Hardening and Validation](https://wwwin-github.cisco.com/pages/sto-ccc/cloud9-docs)
* RECIPE: [Harden Software Components](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook#harden-software-component)
* RECIPE: [Engage with Information Security Infrastructure Architecture Team](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Engage%20with%20Infosec%20Infrastructure%20Architecture%20Team.aspx)

# Normative References

* [Center for Internet Security's Baseline Hardening Guides](https://www.cisecurity.org/cis-benchmarks/)
* [Cisco's Hardening Orchestration and Verification Tools](https://apps.na.collabserv.com/communities/service/html/communitystart?communityUuid=bfcde877-c33f-4b50-b5ff-9c16f4858d44)
* [Cisco Application Platform Hardening](https://wiki.cisco.com/display/CCSINFOSEC/Cisco+Application+Platform+Hardening+Guideline)
* RECIPES: [Harden Software Component](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook#harden-software-component)

# Requirement References

    ---
    source: ISO 27002:2013
    foreign_id: A.12.5
    roreigntarget: 12
    relation: connects
    headline: >
        ISO 27002:2013: A.12.5 Control of operational software
    ---
    source: ISO 27002:2013
    foreign_id: A.12.6
    roreigntarget: 12
    relation: connects
    headline: >
        ISO 27002:2013: A.12.6 Technical vulnerability management

# Attributes

    id: SEC-HRD-INFRA
    version: 3
    category: Threat Surface Reduction
    riskArea: System Hardening
    legallysensitive: false
    waivable: true
    issueref: ISS_SoftHosts
    applicability:
      - force: mandatory
        target:
          restrict: >
              offerings that imbed externally sourced software components such as web
              servers, databases, and middleware
    priority: 8
    phase: requirements
    tags:
    - Hardening
    - CloudCritical
    - EN/PD
    - PSB/OnPrem
    - Cloud
