# Headline

Don't trust random X.509 certificates or certificate authorities.

# Description

This PSB contains requirements governing which Certificate Authorities (CAs) to regard as trusted or non-trusted for the purpose of validating trust in an X.509 certificate. These apply whether the certificate is being presented as part of a TLS session or in other non-TLS contexts, but the specific requirements will vary according to context.

# Behavior
## [Public Certificate](#DEF_PublicCertificate) Trust

## SEC-509-TRUST-FR1:  Use Cisco CA Bundles

**(was SEC-509-CALIST-FR1)** 

Offerings validating [Public Certificates](#DEF_PublicCertificate) must ensure they are using a carefully tested and current list of trusted Public Certificate Authorities. Cisco operates its own trust store program to support this requirement—details about that program, the lists of certificates available and their contents, and the specifics of generation and maintenance of the bundles is available at the [Cisco Cryptographic Services Trusted Root Store site](https://cswiki.cisco.com/display/EXT/Cryptographic+Services%3A+Trusted+Root+Store+Program).

This means:

1. Offerings _MUST_ use the Cisco-provided Core Trusted Root Store Bundle (Core TRS Bundle) for authenticating the peer when connecting to Cisco services or downloading product updates from Cisco to perform Cisco-specific operations. The offering MAY ship with the Core TRS Bundle included and enabled. The offering _MUST_ NOT enable any other bundles or CAs besides the official Core TRS Bundle without an authenticated, explicit administrative request from an appropriate non-Cisco policy entity or customer administrator. The offering MAY use only a subset of the CAs in the Core TRS Bundle if it chooses.

2. Offerings _MUST_ use the Cisco-provided Intersect Trusted Root Store Bundle for authenticating the peer when connecting to any other public, non-Cisco services on the Internet from Cisco-controlled software. The offering MAY use only a subset of the CAs in the Intersect TRS Bundle if it chooses.

3. Offerings MAY use the Cisco-provided Union Trusted Root Store Bundle *only* when acting as an SSL traffic-inspection proxy under the specific prior approval or documentation for the customer. The offering MAY use only a subset of the CAs in the Union TRS Bundle if it chooses.

4. Offerings _MUST_ use the most up-to-date bundle with every new offering release. For example, shipping with older than the latest Core TRS Bundle version in a new offering version release is not acceptable.

5. Offerings _MUST_ cryptographically verify each signature on obtained updates to *any* Trusted Root Store bundle by using Cisco-held public keys dedicated to that purpose; accept only updates signed by the dedicated corresponding keys. See the implementation section for details on how to do that.

## SEC-509-TRUST-FR2: Offerings Operated By The Customer

**(was SEC-509-CALIST-FR2)** 

In cases where Cisco is providing an offering that will be operated by the customer, the offering:

1. MUST display the list of trusted default roots in the customer documentation for the offering.
2. MUST provide either a documented process for manually installing periodic updates to any Trusted Root Store bundles included in the offering, or a method for automatically checking the Trusted Root Store bundles provided online and downloading / installing new bundles when updates are issued. This update process SHOULD be independent of the normal firmware release process.
3. MUST preserve the non-Cisco controlling policy entities changes to the list(s) (i.e., additional authorities added or authorities disabled or removed), if they were made, even after software updates, firmware upgrades, or any actions of the offering to update its local copy of any Cisco Trusted Root Store bundles.

**Exception:** Customers or other non-Cisco policy entities are not necessarily the appropriate controlling policy entities for license enforcement, DRM, or other cases where an authentication root is being used only to protect the interests of Cisco or of some third-party policy entity. You are therefore not required to permit customers or other non-Cisco controlling policy entities to modify lists of CAs used only for those purposes, even in products.

## SEC-509-TRUST-FR3: Operating an Offering on a Customer's Behalf

**(was SEC-509-CALIST-FR3)** 

When Cisco operates an offering on a Customer's behalf, the offering MAY be configured to trust additional public or private CAs of the customer's choosing. HOWEVER:

1. Enabling trust in this additional CA _MUST NOT_ enable elements of the offering not operated on that customer's behalf to trust the new CA. For example, if Cisco operates an offering on behalf of ACMECO, INC. and on behalf of MFGCO, INC., then Cisco may enable trust in ACMECO's private CA *only if* doing so would not cause the offering operated for MFGCO to also trust that CA.
2. Enabling trust in this additional CA _MUST_ only be done with the explicit request or permission of the customer for whom the offering is operated (although this may be made part of the standard service agreement for the offering).
3. Enabling trust in this additional CA _MUST NOT_ compromise core elements of Cisco's offering security, such as licensing or device identity.
4. The additional CA _MUST NOT_ issue certificates containing Cisco-owned domain names.

## SEC-509-TRUST-FR4: System CA Lists for User Platform Applications

[User Platform Applications](#DEF_UserPlatformApplication):

1. _SHOULD_, by default, use the system list to authenticate such user designated peers. If you use the system list by default, then you SHOULD permit the controlling policy entity to override this and set up a trust list specific to your application.
2. _MUST NOT_ install new CAs into the system list without explicit direction from the controlling policy entity.  This FR covers permission to use the system list, not to modify it by default.
3. This FR does not require or permit you to use the system list when communicating with peers which are not user chosen. For example, if your application communicates with a Cisco server using a "wired in" name, it _MUST_, by default, follow FR-1 above and use a Cisco approved certificate authority to authenticate that communication, even though it MAY use the system list when communicating with other peers chosen by non-Cisco policy entities.

## SEC-509-TRUST-FR5: [Private Certificate](#DEF_PrivateCertificate) Trust

Offerings validating [Private Certificates](#DEF_PrivateCertificate) must ensure they are from a carefully controlled [Private Certificate Authority]](#DEF_PrivateCertificateAuthority) and constrained to particular uses and contexts. Specifically, this means:

1. If your offering is a service, and uses X.509 certificates to authenticate internal communication between Cisco-administered agents that participate *only* in that service, then you MAY trust a "service-internal" CA to issue any certificates used for that internal communication. HOWEVER:
   1. You _MUST_ follow the strictures contained in SEC-509-CA and the Cisco Cryptographic Controls Policy ([EDCS-806748](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806748)) for operating this CA. This will likely require some level of review and approval for operating the CA.
   2. Cisco _MUST_ NOT configure by default any agent to trust this CA when the agent is not part of the service offering in question. When such trust is required for the functionality of the offering, the offering _MUST_ require an authenticated, explicit administrative request from the appropriate non-Cisco policy entity or customer before configuring the agent to trust the private CA.

## SEC-509-TRUST-FR6: Certificate Authority Trust Pinning

In certain cases, offerings might want to "pin" a particular Certificate Authority key or keys so that they will only accept certificates issued by those keys. For example, offerings following [SEC-DEV-MOBILITY](#SEC-DEV-MOBILITY) will be required to do this to prevent tampering. Offerings _SHOULD NOT_ pin to a more restrictive set of CAs than the Cisco Core TRS Bundle. Offerings that do pin to a specific certificate or certificates _MUST_ follow these strictures:

1. You _MUST_ pin to a cryptographically secure value such as the public key or certificate fingerprint and _MUST NOT_ pin to a string value such as the subject or serial number of the certificate. When selecting, you SHOULD favor pinning to the public key over the certificate fingerprint, to allow for re-issuance and certificate content changes over time.
2. You _MUST_ provide a cryptographically secure method for updating the list of pinned CAs in *existing supported offering software* that will permit for secure replacement of a pinned certificate in the event of an issue. This method _SHOULD NOT_ require the customer to upgrade the software in the offering. This method _MUST_ be tied to cryptographic keys controlled by Cisco.

# Informative References

- [Cisco Core Trusted Root Store Bundle](http://www.cisco.com/security/pki/trs/ios_core.p7b)
- [Cisco Intersect Trusted Root Store Bundle](http://www.cisco.com/security/pki/trs/ios.p7b)
- [Cisco Union Trusted Root Store Bundle](http://www.cisco.com/security/pki/trs/ios_union.p7b)
- [Cisco Cryptographic Services Trusted Root Store Information](https://cswiki.cisco.com/display/EXT/Cryptographic+Services%3A+Trusted+Root+Store+Program)
- [Cisco PKI: Services Policies, Certificates, and Documents](https://www.cisco.com/security/pki/)


# Normative References

- Cisco Cryptographic Controls Policy,
[EDCS-806748](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806748)

# Requirement References

    ---
    foreign_id: SEC-509-VALIDATE
    relation: connects
    headline: |-
      SEC-509-VALIDATE describes the
              methods that must be used to validate an X.509 certificate.
    source: PSB
    ---
    foreign_id: SEC-CRY-PRIM-FR1
    relation: connects
    headline: |-
      SEC-CRY-PRIM-FR1 requires
              your CA to support appropriate cryptographic
              primitives.
    source: PSB
    ---
    foreign_id: SEC-OUT-CRED
    relation: connects
    headline: |-
      SEC-OUT-CRED
              forbids "hardwired" certificates that are
              the same in every instance of your
              offering.
    source: PSB
    ---
    foreign_id: SEC-AUT-CREROT
    relation: connects
    headline: |-
      SEC-AUT-CREROT
              Support real-time credentials rotation or renewal functionality.
    source: PSB

# History

```yaml
-----
affected_psb: SEC-509-TRUST
impact: normative
headline: >
  Merged SEC-509-CACHOICE and SEC-509-CALIST
---
deprecated_psb: SEC-509-CACHOICE-4
impact: normative
headline: >
  Merged into SEC-509-TRUST
-----
deprecated_psb: SEC-CRY-CALIST-4
impact: normative
headline: >
  Merged into SEC-509-TRUST
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: >
          offerings which, while being manufactured or operated by Cisco, obtain
          x.509 certificates from any certificate authority of any kind.
          NOTE - This requirement does not apply in cases where Cisco hardware
          devices or software products, when operated by a customer, obtain a
          certificate at the customer's direction from a certificate authority
          of the customer's choice.
        class: not_X509None_AND_not_X509OtherCerts
    category: Cryptographic Support
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 1
    id: SEC-509-TRUST
    issueref: ISS_DefaultCreds
    tags:
    - CSG/PI
    - CloudCritical
    - PSB/OnPrem
    - Cloud

