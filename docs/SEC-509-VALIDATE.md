# Headline

Validate X.509 Certificates

# Description

Follow all standard practices when validating X.509 certificates presented by [peer](#DEF_Peer) entities.

# Behavior

In all cases where this requirement is relevant,
[certificates](#DEF_Certificate) are validated according to RFC5280
by the tool, [code](#DEF_Code) or library responsible for X.509 parsing
and verification. When validating an X.509
[certificate](#DEF_Certificate) that is presented by a [peer](#DEF_Peer), the following requirements apply to all [offerings](#DEF_Offering). Note that these requirements *do not apply* when evaluating a certificate being installed on the offering itself (such as when the offering obtains a certificate for its own use from a Certificate Authority).

## SEC-509-VALIDATE-FR1: Validation of Names

Offerings _MUST_ validate that the name of the [Peer](#DEF_Peer) and the names in the [Peer Certificate](#DEF_PeerCertificate) contain a match. Specifically:

**Supplemental Guidance: Using an approved TLS stack (per [SEC-CRY-PRIM](#SEC-CRY-PRIM) ) will address this FR**

1. Offerings _MUST_ check that the name of the Peer appears either in the Common Name or in a Subject Alternative Name field in the Peer Certificate. (formerly SEC-509-VALIDATE-FR1 )
2. When validating a certificate presented by a peer, follow RFC6125. The entire "source domain" _MUST_ be checked against the entire dNSName in the certificate as defined in RFC6125 and the name-matching requirements of RFC-5280, including case-matching and the detection and parsing of character sets to ensure an exact match. In particular, the entire "source domain" _MUST_ be checked against the entire dNSName in the certificate as defined in RFC6125. (formerly SEC-509-FQDN-FR2)
3. Offerings _MUST_ reject a certificate presented that does not contain a match between the Peer's name and the name list in the Peer Certificate. 
4. "Source domains" that are generated internally by software, or are part of static configuration data, _MUST_ be treated as verbatim FQDNs in the validation process. Offerings _MUST NOT_ automatically add trailing components and _MUST NOT_ automatically strip leading components. For example, `www` _MUST_ NOT be expanded to `www.cisco.com`; the literal string `www` _MUST_ be compared against the contents of the certificate. Conversely, `www.cisco.com` _MUST NOT_ match `cisco.com`. (formerly SEC-509-FQDN-FR2)
5. "Source domains" entered interactively (for example in the URL bar of a Web browser) MAY be expanded to FQDNs by appending locally configured default suffixes. For example, if a user types `foo`, and `foo` itself fails to resolve, then you MAY try expanding it it to `foo.cisco.com` by appending the suffix `.cisco.com`. This is a relaxation of section 6.2.1 of RFC 6125, and carries some risk. However, the expanded name is not necessarily an RFC6125 "derived domain" since the added suffix is not itself based on information from DNS. All appended suffixes _MUST_ come from local configuration, not from DNS lookups. You _MUST_ display the fully expanded name to the user who entered the abbreviated name. When validating the peer certificate, you _MUST_ compare the fully expanded name to the names in the peer's certificate. (formerly SEC-509-FQDN-FR2)
6. Offerings _MUST_ alert the operator to a name-based rejection with information at least containing the Peer's name and the list of certificate names found in the Peer Certificate.

## SEC-509-VALIDATE-FR2: Validation of Certificate Dates

Offerings must ensure that the Peer Certificate is valid at the time it is presented. In particular:

1. Offerings _MUST_ ensure that the current time and date as known by the offering fall between the notBefore and notAfter timestamps in the Peer Certificate. Per RFC-5280, if the Peer Certificate contains a notAfter of `99991231235959Z`, offerings MAY choose to bypass the date-checking requirements. As an example, a device identity certificate such as Cisco's SUDI certs represents a non-expiring attestation of Cisco's manufacture of the device—these certificates would ship with a notAfter of `99991231235959Z` (indicating that the attestation of device identity in the certificate does not expire) and offerings could choose to bypass date validation for these certificates.
2. 19 January 2038 is the maximum date supported by signed 32-bit integer values. Offerings _MUST_ support dates greater than this value and _SHOULD_ support 64-bit date values.
3. Date and Time matching performed by the offering _MUST_ conform to the requirements stipulated in RFC-5280 section 4.1.2.5 ("Validity") or superseding requirements provided by the IETF. 
4. Offerings _MUST_ reject a certificate when the current time and date as known by the offering fall outside the notBefore/notAfter time window in the Peer Certificate.
   * Exception: An agent _MAY_, even though it _SHOULD NOT_, rely on a certificate without checking its validity period if any of the below is true:
     * The agent has no way of learning the time and date.
     * The certificate is a manufacturer's cert that is expected to "live forever" and cannot be revoked. An example of such certs are Cisco's SUDI manufacturer certs.
5. Offerings _SHOULD_ attempt to establish the correct current date and time *before* evaluating certificate contents, particularly when the offering has first initialized or booted up. (new)
6. Offerings _MUST_ alert the operator when a certificate is rejected due to a date mismatch (when the current timestamp falls outside of the notBefore/notAfter date range), with information at least containing the current timestamp and the notBefore/notAfter values from the certificate. Offerings _MUST_ alert the operator upon accepting a certificate under one of the exceptions in point 4.

## SEC-509-VALIDATE-FR3: Certificate Cryptographic Elements

Offerings _MUST_ ensure that the cryptographic elements and content of the certificate are internally consistent and conform to requirements such as RFC-5280. Specifically:

1. The signature algorithm identifier _MUST_ be the same as the signature field in the sequence tbsCertificate in the certificate ASN.1 distinguished encoding rules (DER) structure (RFC5280 section 4.1). (was SEC-509-VALIDATE-FR4)
2. The offering _MUST_ accept x.509 version 3 certificates, _MAY_ accept x.509 version 1 certificates, and _MUST NOT_ accept x.509 certificates with other version indicators than 3 or 1.
3. The offering _MUST_ parse and validate X.509 extensions marked as Critical (which also ensures that X.509 v3 is supported). Unknown critical extensions in the certificate received as a Peer Certificate _SHOULD_ trigger a certificate validation failure. (was SEC-509-VALIDATE-FR5)
4. The certificate _MUST_ be used for functions that conform to the ExtendedKeyUsage (EKU) field OIDs in the certificate.
   * Supplemental Guidance: For example, if the only EKU present in the certificate is `TLS Web Server Authentication` (OID `1.3.6.1.5.5.7.3.1`), the certificate _MUST NOT_ be used to verify code signatures. (was SEC-509-VALIDATE-FR6)
5. A Peer Certificate regarded as a Certificate Authority _SHOULD_ use an X.509 v3 certificate and include a basicConstraints extension with value CA:True. If a certificate is v1 or v3 with the basicConstraints extension missing then that certificate is to be considered an end-entity (leaf) certificate, and 
6. _MUST_ NOT be used to validate additional certificates. (was SEC-509-VALIDATE-FR7)

## SEC-509-VALIDATE-FR4: Certificate Validity Status

**(from SEC-509-REVOKE-FR2, with addition of SEC-509-REVOKE-FR4 and one new addition (point 4))**
Offerings _MUST_ then check the validity of Peer Certificates using the information supplied in the Peer Certificate (e.g., OCSP, CRL). In particular:

1. If the Peer Certificate contains OCSP or CRL information, the offering _MUST_ utilize at least one of these to check the current revocation status of the certificate. Where both CRL and OCSP URIs are present, offerings _MAY_ prefer one option over the other (but see 'Supplemental Guidance' section).
2. For each certificate in the Peer Certificate's certificate chain, the offering _MUST_ check validity using the revocation authority information included (if present), except for the root CA. 
3. If the offering makes a request to an included revocation authority URI and receives no response, the offering _SHOULD_ check another included source of revocation information (if available) before making a decision. For example, if the offering queries the OCSP URI and receives no response, the offering _SHOULD_ consult the included CRL URI instead. If no revocation authority consulted can be reached, then the certificate _SHOULD_ be rejected (fail-close). Certificates with unreachable revocation authorities MAY be accepted (fail-open) to prevent outages, but such failures _SHOULD_ be logged, tracked and acted upon. (was SEC-509-REVOKE-FR2)
4. Offerings _MUST_ reject a TLS peer certificate if *either* the OCSP or CRL check positively indicates the certificate is revoked. This is true *even if the two checks disagree*: an indication from either OCSP or CRL that the certificate is revoked _MUST_ trigger a rejection of the certificate. (new)

When the revocation information in a certificate contains an OCSP URI, offerings:

1. _MUST_ support OCSP status checking using the URL in the peer certificate and certificate chain (section 4.2.2.1 of RFC 5280) as described in RFC6960. According to Section 4.2.2.2 of RFC6960, the entity signing and providing the responses should be the CA that originated the certificate being validated, or an authorized responder identified by a valid certificate containing the id-kp-OCSPSigning extended key usage extension.
2. _MAY_ limit the rate at which they will retry requests to any OCSP responders in order to prevent inadvertent Denial of Service situations.
3. _SHOULD_ cache OCSP responses from responders to improve performance. Responses _SHOULD_ NOT be cached for longer than the nextUpdate time in them.
4. _SHOULD_ support OCSP staples and _SHOULD_ request stapled OCSP information whenever authenticating a TLS peer using X.509 (unless it already knows that it will not be doing OCSP validation because one of the exceptions in FR4 applies). If the OCSP staple information is outdated, invalid, from the wrong authority, or otherwise unacceptable, a system _MUST_ reject the certificate.
5. _MUST_ reject a TLS peer certificate if it contains the "must staple" extension (RFC7633) but the peer does not actually staple any OCSP information.

In specific cases, validity checking MAY be partially or completely omitted:
(was SEC-509-REVOKE-FR4)

1. The offering actively maintains a trusted certificate AllowList that tracks only non-revoked, valid certificates to be validated.
2. The maximum Certificate Lifetime of the certificate can be considered short-enough to assume that there is not enough time for it to be compromised. In most cases, "short enough" will be less than 7 days; this value may differ according to the specific risk analysis of the offering. If the offering opts to do this, the value selected as "short enough" _MUST_ be documented as part of the product risk analysis. In addition, when bypassing this check the offering _MUST_ log that it has done so with sufficient information to identify the specific certificate accepted and the reason for doing so.
3. It can be assumed that the absence of revocation information is a commitment from the CA issuer that the certificate will never be revoked. This would be true, for example, in the case of SUDI/IEEE802.1AR certificates issued by Cisco for device identities. If the offering opts to do this, it _MUST_ document which Certificate Authorities it will ignore revocation information from as part of the product risk analysis. In addition, when bypassing this check the offering _MUST_ log that it has done so with sufficient information to identify the specific certificate accepted and the reason for doing so.
4. The certificate is self-signed (that is, the issuer public key for the certificate's signature is the same as the subject public key) and the offering operator has explicitly instructed the offering to trust the certificate. In this case, the offering _MUST_ log that it has accepted the certificate with sufficient information to identify the specific certificate accepted and the reason for doing so.
5. A "chicken and egg" case where the offering has reason to believe that not accepting that certificate might keep the revocation information from becoming available. For example, if there will be no network route from the offering to the needed OCSP authority unless/until it accepts a particular certificate. In this case, the offering _MUST_ log that it has accepted the certificate with sufficient information to identify the specific certificate accepted and the reason for doing so.
6. If there is a current DNSSEC-authenticated TLSA record indicating that a particular certificate is valid for a peer. This only applies when the TLSA record identifies the peer's own leaf certificate, not that of an issuing authority (certificate usage 1 or 3 as described in section 2.1.1 of RFC6698). Systems _MUST_ still check revocation if the TLSA record only identifies the CA expected to have issued the certificate.


**Supplemental Guidance**:

* Offerings should be aware of the privacy and availability risks of relying solely and primarily on OCSP, and should consider using CRL as a backup information source if OCSP is unavailable. 

## SEC-509-VALIDATE-FR5: Validation of Certificate Trust


**(new addition)**

Offerings _MUST_ validate that the Peer Certificate is *either*:

* Signed by a Certificate Authority regarded as Trusted according to the requirements in SEC-509-TRUST, or
* Is a Self-Signed Certificate meeting the requirements stated in [SEC-509-CERT](#SEC-509-CERT)-FR-3.
 
Certificates regarded as Non-Trusted _MUST_ be rejected.

## SEC-509-VALIDATE-FR6: Rejection of Validation

**(new addition)**

Unless more specific requirements apply (such as from the requirements above), offerings that reject a certificate as untrusted _MUST_ log this rejection with sufficient information for the operator to identify the Peer Cert presented and the reason for rejection.

# Informative References

- RECIPE - [Certificate Management](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Certificate%20Management.aspx)
- [CWE-295: Improper Certificate Validation](https://cwe.mitre.org/data/definitions/295.html)
- [CWE-295: Improper Certificate Validation](https://cwe.mitre.org/data/definitions/297.html)

# Normative References

- [RFC 5280](https://tools.ietf.org/html/rfc5280): "Internet X.509 Public
Key Infrastructure Certificate and Certificate Revocation List (CRL)
Profile" (aka PKIX)

# History

```yaml
-----
affected_psb: SEC-509-VALIDATE-6
description: > Honor self-signed cert expiration.
---
deprecated_psb: SEC-509-VALIDATE-5
impact: normative
headline: >
  Added FR7.
-----
affected_psb: SEC-509-VALIDATE-5
description: > Honor self-signed cert expiration.
---
deprecated_psb: SEC-509-VALIDATE-4
impact: normative
headline: >
  Removed FR2 exception for self-signed certs expiration checking.
-----
affected_psb: SEC-509-VALIDATE-4
headline: > Simplified FRs
---
impact: non-normative
description: >
  Removed FR3 regarding root signatures. Removed FR8 Exception and consolidated it in FR3.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: >
          offerings
    category: Cryptographic Support
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 8
    id: SEC-509-VALIDATE
    issueref: ISS_X509Valid
    tags:
    - EN/PI
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
    - Cloud
    - FAST
