# Headline

Create and Review a System-Level Threat Model

# Behavior

The offering team _MUST_ create a threat model for the offering as a whole. Threat models _MAY_ be created outside of the Threat Builder tool (see implementation guidance), but _MUST_ be created, reviewed, and stored in accordance with the Functional Requirements listed in this Product Security Baseline (PSB).

This threat model _MUST_ include:

1. A data flow diagram that identifies all major functional components of the offering; the flows of data into, out of, and within the offering; as well as all locations of all instances of data copy instances (primary, non-primary, persistant and non-persistant). The data flow diagram _MUST_ be consistent with the data records and elements inventoried in the offer's Privacy Impact Assessment (see SEC-DAT-KNOWWHAT)
2. A defined "Trust Boundary" (a logical or physical separator where the level of trust changes for data or code)
3. Identification of all "high-value" assets that would be attractive to an attacker, how they are currently protected, and
whether they meet requirements for adequate protection
4. Identification of "[Open](#DEF_Open)" parts of the system (e.g., intended to be modifiable by users/customers - like configuration, etc.) and "[Closed](#DEF_Closed)" parts (e.g., intended NOT to be modifiable by users/customers without Cisco intervention - like core software and DRM)
5. Identification of all ["Controlled Space"](#DEF_ControlledSpace) in the offering (refer to the linked definition), including how the space is provably protected and what is stored or executes in each space

Once the data flow diagram is completed, the offering team _MUST_ assess threats to the offering, paying particular attention to "high-value" assets and data that flows across the Trust Boundary. Prioritize threats based on severity of impact and likelihood of exploitation, and plan mitigations accordingly.

**Supplemental Guidance**: Offerings will be considered compliant with this functional requirement if an existing system level threat model for a previous version has been reviewed and found to be still accurate, or has been reviewed and updated (see SEC-ASU-TMOD-FR4).

- "High-Value" assets are those which for reasons of Confidentiality, Integrity, and/or Availability are critical](#Critical) to the offering, and include (but are not limited to):
    - Data that is classified as "Confidential" or higher, such as:
        - Credentials and cryptographic keys.
        - PII (Personally identifiable information).
        - Financial data.
    - Code or functionality that essential to the function of the offering (such as routing tables, management plane functions, etc).
- "Adequately protected" typically involves cryptography, storage or running in a controlled space, access control, or a combination of these.
- Pay special attention to data that flows across a Trust Boundary.  These are often potential vectors of attack or information leakage.
- Also pay special attention to how (or if) "High-Value" assets (data and functionality) are protected, and what potential attack vectors exist for them.
- Review your threat model against your offer's Privacy Impact Assessment.  The two documents should be consistent as far as data and data flows.
- It is most advantageous to perform a threat model during the design phase of an offering or a feature, but there is still value in threat modeling an existing design that will see continued development and use.

Refer to [EDCS-805541, CSDL Threat Modeling Implementation Guide](https://docs.cisco.com/share/page/site/nextgen-edcs/document-details?nodeRef=workspace://SpacesStore/be458860-bd48-47e5-84b4-858e019d42fc) for guidance.

There is a graphical application (Threat Builder) to help you capture your architecture and identify threats. See the implementation guide for more details.

# Attributes

    id: SEC-ASU-TMOD-FR1
    version: 3
    issueref: ISS_SEC-ASU-TMOD
    category: Development Process
    riskArea: Risk Assessment
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
          restrict: >
            [offerings](#DEF_Offering)
    priority: 10
    phase: requirements
    tags:
    - EN/PI
    - EN/PD
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
