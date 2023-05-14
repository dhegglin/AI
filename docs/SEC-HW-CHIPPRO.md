# Headline

Securely store and verify the digital imprint of key HW components  

# Key Benefits

Counterfeit systems can be manufactured when the attacker can replace a CPU, ASIC, or a SoC components with counterfeit or substituted ones in order to complete the manufacture of fake product.  Chip protection helps prevent counterfeiting of Cisco HW platforms by providing a way to validate that the parts used to manufacture a particular system are the same specific ones that are in use in the actual product that the customer received.

# Description

The goal of this requirement is to assure integrity of Cisco HW platforms and help prevent counterfeiting by verifying at run-time that the components in the running product are the same ones that were used to build it.   

# Behavior
If there is a high risk that the product will be subject to counterfeiting, then support for this requirement is highly desirable.    

**Suplemental Guidance:** To assess the risk of counterfeiting for your product, see EDCS-551800 v7.2, Section 3.
 
## SEC-HW-CHIPRO-FR1: Add Serial Numbers to Components
Cisco designed computational components, such as ASICs, CPUs, FPGAs, and SoCs, SHOULD include Electronic Chip Identification (ECIDs) such as serial numbers or other digital fingerprints. 

Commodity-sourced components SHOULD include ECIDs. 
## SEC-HW-CHIPRO-FR2: Sign and store the ECIDs associated with the Device 
During platform manufacturing, Cisco SHOULD sign the set of ECIDs that correspond to the components in use on a particular device. 

If signed, the signature MUST be bound to the secure identity of the device that is manufactured with those components.   For example, the Cisco Chip Protection solution signs the platform identity and the ECIDs within the SUDI certificate.    

The TAm (Trusted Anchor module) for the device, or other root of trust, SHOULD securely store the signature of the set of IDs. 

**Supplemental Guidance:** Using Cisco Chip Protection is a way to comply with this FR. 

## SEC-HW-CHIPRO-FR3: Detection
If signed, the signature of the ECIDs MUST be accessible to the device. 

If signed, the system MUST check the ECIDs of the components at boot-time and verify the signature. 

If the verification check fails, then the system MUST notify the platform administrator.  In that case, the system SHOULD NOT boot successfully.    

## SEC-HW-CHIPRO-FR4: Attestation 

The system SHOULD provide a means of remote attestation in a trusted manner.   

# Normative References
* [Counterfeit Risks and Controls](https://docs.cisco.com/share/page/site/nextgen-edcs/document-details?nodeRef=workspace://SpacesStore/777b5d47-1e7f-4339-bc7a-f78da5d0ac45) EDCS-551800 v7.2.
* [TAm Device Chip Guard Design Specification](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-11565116&ver=LATEST). EDCS-11565116 
* [Next-Generation Trust Anchor Technology Attestation Functional Specification](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1543500&ver=LATEST).  EDCS-1543500
* [Platform Identity and Boot Integrity Visibility Architecture](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1497588&ver=LATEST). EDCS-1497588

# Requirement References

```yaml
---
source: PSB
foreign_id: SEC-CRE-CHIPID
relation: connects
headline: >
  [SEC-CRE-CHIPID](#SEC-CRE-CHIPID)
  requires use of a Trusted Anchor Module.
```

# History

```yaml
-----
affected_psb: SEC-HW-CHIPPRO
description:  Introduced new requirement.
```

# Attributes

    id: SEC-HW-CHIPPRO
    version: 1
    category: Boot and System Integrity
    riskArea: System Integrity
    legallysensitive: false
    waivable: true
    issueref: ISS_DevIDTamper
    applicability:
      - force: mandatory
        target:
          restrict: >
            [turnkey modules](#DEF_TurnkeyModule)
    priority: 7
    phase: requirements
    tags:
        - CSG/PD
        - PSB/OnPrem
