# Headline

Use Cisco standard device identity certificates


# Key Benefits

Using common Cisco Certificate Authorities avoids the need for customer equipment to know about numerous [authentication roots](#DEF_AuthenticationRoot) and reduces Cisco's dependence on external organizations for [authentication root](#DEF_AuthenticationRoot) management.

A consistent profile frees customers and Cisco [offerings](#DEF_Offering) from the need to
parse multiple X.509 distinguished name formats.

Operating a Certificate Authority securely is difficult, expensive, and sometimes
involves inobvious risks. Having a central Certificate Authority prevents every product
team from learning the pitfalls through painful experience, possibly
at significant cost to customer security.

# Description

Customers and the rest of Cisco have set up a lot of tools and trust
hierarchies based on standard device identity practices. Use them.

# Behavior

## SEC-CRE-IDFORM-FR1: Device Identity Encoding

The [device identity](#DEF_DeviceIdentity) for each unit _MUST_ be encoded in an X.509 [certificate](#DEF_Certificate) associated with its device identity [credential](#DEF_Credential) (i.e. a key-pair).

**Supplemental Guidance**: See also [SEC-509-CA](#SEC-509-CA) (describing the validity periods of device identity certificates). 

## SEC-CRE-IDFORM-FR4: Device Identity Names

The Subject Distinguished Name field of each [device identity](#DEF_DeviceIdentity) [certificate](#DEF_Certificate) _MUST_ represent the device identity in the format of the Secure UDI Certificate Profile ([EDCS-576121](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-576121)). This document specifies how to embed customer-facing identifiers including Product ID (PID) and serial number.

The PID and serial number provisioned into the device's SUDI Certificate _MUST_ match the PID and serial number that is stamped on the outside of the offering, is displayed through management protocols, web, and CLI interfaces, and is in the customer packlist.

A device frequently consists of multiple assemblies such as printed circuit boards (PCB). The PID and serial number provisioned into the device's SUDI Certificate _MUST_ be that of the orderable FRU and _MUST NOT_ be that of a non-orderable assembly such as a PCB.

If the FRU can be ordered as a bundle consisting of other FRUs (such as a chassis containing multiple RPs), the SUDI for each FRU must contain the PID and serial number of the individual FRU and not that of the bundle.

## SEC-CRE-IDFORM-FR5: Certificate Signature

The X.509 [certificate](#DEF_Certificate) _MUST_ be signed by a Certificate Authority (CA) designated for device identity certificates and operates according to Cisco's Cryptographic Controls Policy. 

# History

```yaml
-----
affected_psb: SEC-CRE-IDFORM-4
---
impact: non-normative
description: >
  Cosmetic updates.
```

# Normative References

* [Cisco Cryptographic Controls Policy](https://policy.cisco.com/cppc/policy-advisor/policies/view-policy/1818)

* [EDCS-576121](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-576121): Secure UDI Certificate Profile

# Informative References

* The secure UDI web pages:
  [SUDI page](https://cisco.sharepoint.com/Sites/TrustworthyTechnologies/SitePages/sUDI.aspx).

  This includes process and measurement information as well as
  technical information.

* RECIPE: [Platform Identity via SUDI Certificate](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Platform%20Identity%20via%20SUDI%20Certificate.aspx)

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-509-VALIDATE
    relation: connects
    headline: >

        [SEC-509-VALIDATE](#SEC-509-VALIDATE)
        lists required lifetimes for various kinds of certificates, including
        device identity certificates.
    ---
    source: PSB
    foreign_id: SEC-509-TRUST
    relation: connects
    headline: >
        [SEC-509-TRUST](#SEC-509-TRUST)
        governs the choice of CAs to be used to sign certificates identifying
        Cisco-controlled entities. This includes device identity certificates.

# History
```yaml
-----
affected_psb: SEC-CRE-IDFORM
description:  Updated verbiage, dropped several FR's. 

```

## Older history (manually maintained; may be incomplete)
PSBCTR 5.0: Added

# Attributes

    id: SEC-CRE-IDFORM
    version: 4
    category: Boot and System Integrity
    riskArea: System Integrity
    legallysensitive: false
    waivable: true
    issueref: ISS_CiscoRoots
    applicability:
      - force: mandatory
        target:
          restrict: >
            [device identity](#DEF_DeviceIdentity)
            [credentials](#DEF_Credential)
    priority: 8
    phase: requirements
    tags:
        - EN/PD
        - G7
        - PSB/OnPrem
        
