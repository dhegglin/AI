# Headline

Generate, request, and obtain certificates securely.

# Behavior

This PSB covers requirements for obtaining and holding any X.509-based digital certificate.
The strictures in this PSB apply to any offering that presents a certificate.  There are different function requirements for TLS and Non-TLS certificates; FRs 2 and 3 are specific to TLS certificates and FR4 applies to x.509 certificates used in non-TLS applications.

## SEC-509-CERT-FR1: Certificate Key-Pairs

Offerings that request x.509 certificates from a Certificate Authority must generate and protect key-pairs used in certificates and generate sane, reasonable certificate requests. To accomplish this:

1. Offerings _MUST_ generate key-pairs for any certificate using the strongest random number generation methods available and following the requirements of [SEC-CRY-RANDOM](#REQ_CRY-RANDOM).
2. Offerings _MUST_ secure the private key of the key-pair to prevent compromise and unauthorized access. Offerings _SHOULD_ protect the private key using hardware encryption such as a hardware TAm or TPM where available. Where private keys are stored in software, offerings _MUST_ limit access to the private key to ensure only authorized individuals or processes may access it.
3. Offerings _MUST_ provide the ability to regenerate a key-pair from scratch when generating new certificate requests, and MAY offer the ability to re-use an existing key-pair instead.
4. TLS certificate requests that are generated as files (as opposed to the use of automated certificate issuance protocols such as ACME or REST) _MUST_ conform to RFC 2986 (PKCS#10 Certificate Signing Request format).  Non-TLS certificates, including SUDI (IEEE 802.1AR) certificates, other anti-counterfeiting certificates, device or offering identity or capability-listing certificates, and the like _SHOULD_ conform to RFC 2986 (PKCS#10 Certificate Signing Request format).

## SEC-509-CERT-FR2: TLS Certificate Requests

**(Partially from SEC-509-FQDN-FR1)**

**Supplemental Guidance: **  This functional requirement covers requirements for obtaining, holding, and presenting X.509-based digital certificates that are used for TLS-based connections. This includes TLS in any network context, such as HTTPS, LDAPS, or SMTPS. The strictures in this PSB cover any offering that presents a certificate as part of a connection, whether the offering is acting as the TLS client or the TLS server.

Offerings need to create certificate requests that comply with RFC-5280 and applicable superseding requirements. In particular, offerings generating a certificate request:

1. _MAY_ generate a Subject request that contains a `CommonName` field entry. Where the request contains a `CommonName` field entry in the Subject, offerings _MUST_ include at least one SAN entry matching this `CommonName` entry exactly.
2. _MUST_ include at least one Subject Alternative Name (SAN) field in the request, containing a unique name.
3.  _MUST_NOT_  use IP addresses as the `CommonName` field entry in the Subject.
4.  _SHOULD_NOT_ generate certificate requests containing IP addresses in a Subject Alternative Name field. If an IP address has to be included in the request (whether as the only name or as one of many), it _MUST_ be placed in a Subject Alternative Name field as an ipAddress-type SAN.
5. _MUST_ generate requests with [fully-qualified domain names (FQDNs)](#DEF_FQDN) or IP addresses in the Common Name and all SAN fields.
6. _SHOULD_ prefer generating a name of type "uniformResourceIdentifier" (URI) to generating a name of type "registeredID" (ASN.1 registered identifier). If they are used, URIs _MUST_ use schemes properly registered with IANA and _MUST_ be used according to the specifications defining those schemes. Included ASN.1 registered identifiers _MUST_ be registered, _MUST_ have clear specifications, and _MUST_ be used according to those specifications.
7. _SHOULD_ NOT generate requests that include a requested certificate validity longer than 390 days.

**Exception:**

* Certificates that are requested only as Client Certificates _MAY_ waive the requirement for FQDNs in certificate names and _MAY_ include additional name types if doing so is required as part of the CA's requirements for issuance.
* Offerings that generate certificate requests as part of their initialization process (e.g., a router that generates a certificate for its management interface as part of first-boot initialization) _MAY_ follow these requirements for certificate names:
  * The offering _MUST_ notify the operator with a visible message if it lacks sufficient information to generate a certificate request without IP addresses or non-fully-qualified domain names. In this case, the offering _SHOULD_ offer the operator the chance to rectify this issue and generate a proper request afterwards.
  * The offering _MAY_ generate a certificate request containing IP addresses or non-fully-qualified domain names, *if and only if* the names included are positively associated with the offering (e.g., the IP addresses are associated with existing interfaces on the offering).  
  * These naming exceptions apply only to the strictures contained in FR-2 above, and *do not* supersede any other requirements in this or other PSBs.

## SEC-509-CERT-FR3: Presenting Digital Certificates for TLS
Whether acting as the TLS client or the TLS server, when presenting a certificate to another [peer](#DEF_PEER) offerings MUST follow good practice for correctly presenting a valid and validatable certificate chain. In particular:

1. Offerings _MUST_ present at least the certificate chain from the [leaf certificate](#DEF_LeafCertificate) up to the certificate for the intermediate CA that chains to a root CA.
2. Offerings _MUST_ support the use of OCSP Stapling to present both the certificate chain and a pre-signed OCSP response as part of the connection.
3. When presenting a certificate that contains an OCSP URI for validation, the offering _SHOULD_ utilize OCSP Stapling, and _SHOULD_ support OCSP stapling for each certificate in its chain, per RFC-6961. Where the certificate contains the OCSP-Must-Staple extension (RFC-7633), the offering _MUST_ utilize OCSP Stapling to present the certificate chain.

## SEC-509-CERT-FR4: Non-TLS Certificate Requests
**Supplemental Guidance:** This functional requirement covers X.509-based digital certificates that are used for identification purposes *other than* for TLS connections. This includes SUDI (IEEE 802.1AR) certificates, other anti-counterfeiting certificates, device or offering identity or capability-listing certificates, and the like. It **does not** cover certificates used for code-signing, image-signing, or similar authentication of software in an executable context.

1. A certificate with a human subject _SHOULD_ identify that subject using one or more RFC822 email addresses (and therefore subjectAltNames of type "rfc822Name"), in preference to other names. 
2. The subject distinguished name in such a certificate _MUST_ include an RFC822 email address, and _MAY_ include other X.500 directory information such as a common name or organization. 
3. Unless required by an external constraint, you _SHOULD_ NOT generate any subjectAltName of type "x400Address" or "directoryName".

## SEC-509-CERT-FR5: Obtaining Certificates from a Certificate Authority

**(From SEC-509-CACHOICE-FR1 and SEC-509-CACHOICE-FR2)**

When obtaining certificates, offerings must obtain certificates from a Certificate Authority regarded as Trusted.

For a Public Certificate, this means:

1. [Public Certificates](#DEF_PublicCertificate) _MUST_ only be obtained from Cisco S&TO's [centralized PKI service](https://sslcerts.cisco.com/sslrequest/) or from a CA in the S&TO [list of Qualified CAs](https://wwwin-github.cisco.com/sto-cryptosvcs/approved-ca). These CAs are approved by the Cisco Cryptographic Services (CCS) Team, and may vary over time. For more details on the S&TO's centralized PKI service, refer to the [Cryptographic Services Wiki](https://cswiki.cisco.com/pages/viewpage.action?pageId=44138673).

   * The S&TO PKI service _MUST_ be used for certificates issued directly under `cisco.com` (e.g. `foo.cisco.com`).
   * For other Cisco-owned domains outside of `cisco.com` and for sub-domains of cisco.com (e.g. `abcd.wxyz.cisco.com`), the S&TO PKI service _MUST_ be evaluated for public certificates before a group decides to obtain certificates from another provider included in the Qualified CAs list (linked above).
   * Note that the use of certain CAs on the approved list may be constrained by additional technical requirements, such as the use of multiple CAs for redundancy. (See [Multi-CA ACME Spec](https://wwwin-github.cisco.com/sto-cryptosvcs/approved-ca/blob/master/multi-ca-acme.md) for details).

2. Offerings opting to obtain Public Certificates from a CA other than Cisco S&TO's [list of Qualified CAs](https://wwwin-github.cisco.com/sto-cryptosvcs/approved-ca) _MUST_ provide an attestation, in the form of a short EDCS document or a risk called out in the [Security Readiness Plan](https://cisco.sharepoint.com/sites/CSDL/SitePages/Security-Readiness-Plan-(SRP).aspx?web=1).  
The attestation document _MUST_ include all of the following:  
   * The reasons for requiring a certificate authority other than the S&TO-provided service.
   * That certificates will be obtained directly from the CA and listing the authority to be used.
   * The product or service team / BU's operational maturity in certificate lifecycle management, including methods of monitoring of certificate expiry and management of certificate revocation.
   * A limited scope such as a specific DNS sub-domain, product-related DNS domain, or acquisition domain for which certificates will be obtained and managed.
   * A reliable, registered emergency contact system for the product or service team / BU for responding to issues with certificates. This may be integrated into other incident response programs so long as they have specific playbooks for certificate-related problems.
3. A number of CAs are not approved for Cisco use for a variety of reasons. These CAs _MUST_ NOT be used to obtain certificates for relevant Cisco products or services. For the list of unapproved providers, along with information on why they are not permitted for Cisco business use, refer to the S&TO [non-approved CA list](https://wwwin-github.cisco.com/sto-cryptosvcs/non-approved-pub-cas.md)). 

For a [Private Certificate](#DEF_PRIVATECERTIFICATE), this means:

1. Offerings MUST consider the set of [Private Certificate Authority](#DEF_PRIVATECERTIFICATEAUTHORITY) services offered by Cisco S&TO Cryptographic Services before evaluating alternative solutions.
2. When the offering itself acts as a CA *and* the offering is operated solely by the customer, offerings _MAY_ obtain Private Certificates from their own service-internal CA. For instance, a router that creates its own CA internally when instructed to do so by the operator _MAY_ then obtain Private Certificates from itself. In this case, customers _MUST_ be given the ability to obtain and install certificates from an outside PKI instead.
3. Offerings opting to use a CA other than Cisco S&TO's Private PKI Services _MUST_ provide an attestation, in the form of a short EDCS document or a risk called out in the Security Readiness Plan.  
The attestation document _MUST_ include all of the following:
   * The reasons for requiring a certificate authority other than the S&TO-provided services.
   * That certificates will be obtained directly from the CA and listing the authority to be used.
   * The product or service team / BU's operational maturity in certificate lifecycle management, including methods of monitoring of certificate expiry and management of certificate revocation.
   * A limited scope such as a specific DNS sub-domain, product-related DNS domain, or acquisition domain for which certificates will be obtained and managed.
   * A reliable, registered emergency contact system for the product or service team / BU for responding to issues with certificates. This may be integrated into other incident response programs so long as they have specific playbooks for certificate-related problems.

**Exception:**

1. Customer-driven requirements MAY mandate the use of certificates issued by a particular CA not included in the Qualified CAs list (linked above). If the resulting certificate will contain any Cisco-owned domains, this use _MUST_ be validated by contacting CCS at ciscopki@cisco.com and _MUST_ be limited to a particular name scope for certificates (e.g. a particular DNS sub-domain or a specific product-related DNS or acquisition domain).
2. Offerings intended for operation by customers on customer premises (e.g., a router, or firewall software) _MUST_ permit the customer to install a certificate from any certificate authority. Certificates issued from a Certificate Authority the product itself does not trust (see SEC-509-TRUST) _MAY_ generate a warning to the operator on certificate installation.

## SEC-509-CERT-FR6: Renewing Digital Certificates

For certificates that can expire (example of a certificate that cannot: SUDI certificates), offerings need to ensure that any such certificate they hold and present are monitored for expiry, and are renewed in a timely fashion. In particular:

1. Offerings intended for operation by customers _MUST_ offer the option to use automated certificate management protocols such as REST, ACME, or EST to obtain and renew [leaf certificates](#DEF_LeafCertificate) held by the offering itself.
2. Offerings operated by Cisco _MUST_ support and utilize automated certificate management protocols such as REST, ACME, or EST to obtain and renew certificates.
3. If automation *is not* used (either because it is not available or because the operator did not opt to use it), offerings _MUST_ alert the operator in a visible manner at least 30 days prior to the expiration of any active certificates in the system.
4. If automation *is* used, offerings _MUST_ alert the operator of any failure to renew a certificate at least 14 days prior to the expiration of the certificate.

## SEC-509-CERT-FR7: Self-Signed Certificates

**(From SEC-509-CACHOICE-FR3)**

The use of a [Self-Signed Certificate](#DEF_SelfSignedCertificate) is considered a significant security risk. Without the use of a structured PKI, elements have no basis on which to trust such certificates and no means to evaluate the certificate's continued validity. Additionally, the lack of structured trust can leave offerings open to "machine in the middle" (MITM) attacks. Nevertheless, there are cases where self-signed certificates cannot be avoided.

1. Self-signed certificates _SHOULD_ NOT be used.
2. Self-signed certificates _MAY_ be used where an outside or out-of-band method of trust may be used to securely evaluate the certificate's trust and validity status. For example, a self-signed certificate might be used to secure SAML assertions where the sender is manually declaring the validity of the certificate beforehand and the receiver is pinning trust specifically to the certificate.
3. Self-signed Certificates _MAY_ be used where offerings are installed in customer domains but lack sufficient configuration to generate or request a more structured certificate. For example, the initial certificate for a product's management interface might be generated as a self-signed certificate at first boot to permit some form of connectivity. When using self-signed certificates in this context, the offering:
   * _MUST_ create a unique key-pair and self-signed certificate per offering instance.
   * _MUST_ provide a method to upgrade the offering with a certificate from an outside CA during the installation process and on demand.
4. If self-signed certificates are used in any other situation, the product or service team _MUST_ provide an attestation in the form of a short EDCS document, including all of the following, and provide the document link to ciscopki@cisco.com for review/approval:
   * The reasons for requiring self-signed certificates over centrally-issued certificates from a CA;
   * The security mitigations preventing the self-signed certificates from being exposed externally or abused;
   * The methods being used for validation of certificates between nodes without a CA;
   * The methods in use for monitoring the expiration and replacement of the certificate (where applicable).
5. In *all* cases, all self-signed certificates:
   * _MUST_ NOT have a BasicConstraints extension with CA:True and SHOULD have a BasicConstraints extension with CA:False.
   * _MUST_ NOT be issued to contain external FQDNs of a customer.
   * _MUST_ be issued in conformance with SEC-CRY-PRIM requirements for encryption algorithms and _MUST_ be replaced when no longer in compliance.

# Normative References

- Cisco Cryptographic Controls Policy,
[EDCS-806748](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806748)
- PKCS #10: Certification Request Syntax Specification [RFC 2986](https://tools.ietf.org/html/rfc2986)


# Requirement References

    ---
    foreign_id: SEC-509-TRUST
    relation: connects
    headline: |-
      SEC-509-TRUST
              constrains which CAs you (and other offerings)
              can accept by
              default.
              SEC-509-CACHOICE requires that any CA you
              use to generate or present certificates
              meet the same constraints.
    source: PSB
    ---
    foreign_id: SEC-509-VALIDATE
    relation: connects
    headline: |-
      SEC-509-VALIDATE describes the
              methods that must be used to validate an X.509 certificate and requires
              your CA to support revocation and OCSP.
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

```

# Attributes
    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: >
          offerings
    category: Cryptographic Support
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 1
    id: SEC-509-CERT
    issueref: ISS_X509Valid
    tags:
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - FAST
