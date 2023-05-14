# Headline

Protect external management TLS traffic.

# Description

It is important to provide confidentiality and integrity protection to
[administration](#DEF_Administrator) traffic since it could contain
sensitive customer and device information.

# Behavior

Whenever an [offering](#DEF_Offering) provides a TCP-based
[administration](#DEF_Administrator), configuration, management,
or monitoring protocol, the offering _MUST_ support running
that protocol over TLS.

An example management protocol is HTTP. RESTCONF runs over HTTP. 
Every HTTP server and client _MUST_ support HTTPS (HTTP over TLS).

Other management protocol examples include gNMI and NETCONF. TLS 
_MUST_ be enabled by default to protect such management protocols 
unless SSH version 2 is supported instead.

**Exception**: Using non-TLS based encrypted management protocols
is rare and not recommended, but in the rare occasion that the management
protocol itself offers cryptographic confidentiality and integrity protection
of 128 bits of security or higher, TLS based encryption of management
traffic can be omitted. An example is SNMP which is covered in 
[SEC-CRY-SNMP](#SEC-CRY-SNMP).

# Normative References

- [Server Security Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1411758&ver=approved) 

- [Cryptographic Implementation Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806752&ver=approved)

# Informative References

- [RFC7589](https://tools.ietf.org/html/rfc7589) 

- [RFC6242](https://tools.ietf.org/html/rfc6242) 

- [Cisco Common Security Modules](https://cisco.sharepoint.com/Sites/CommonSecurityModules) 

# Requirement References

    ---
    foreign_id: FTP_TRP.1
    relation: connects
    headline: |-
      FTP_TRP.1 Trusted Path FTP_TRP.1.1 Refinement: The
            TSF shall use [selection, choose at least one of: IPSEC, SSH,
            TLS, TLS/HTTPS] provide a trusted communication path between
            itself and remote administrators that is logically distinct from
            other communication paths and provides assured identification of
            its end points and protection of the communicated data from
            disclosure and detection of modification of the communicated
            data. FTP_TRP.1.2 Refinement: The TSF shall permit remote
            administrators to initiate communication via the trusted
            path. FTP_TRP.1.3 The TSF shall require the use of the trusted
            path for initial administrator authentication and all remote
            administration actions.
    targets:
    - WLANPPv1.0(2011)
    source: Common Criteria
    ---
    foreign_id: FTP_ITC.1
    relation: connects
    headline: |-
      FTP_ITC.1 Inter-TSF trusted channel FTP_ITC.1.1
            Refinement: The TSF shall use 802.11-2007, IPSEC, and
            [selection: SSH, TLS, TLS/HTTPS, no other protocols] to provide
            a trusted communication channel between itself and all
            authorized IT entities that is logically distinct from other
            communication channels and provides assured identification of
            its end points and protection of the channel data from
            disclosure and detection of modification of the channel
            data. FTP_ITC.1.2 The TSF shall permit the TSF, or the
            authorized IT entities to initiate communication via the trusted
            channel. FTP_ ITC.1.3 The TSF shall initiate communication via
            the trusted channel for [assignment: list of services for which
            the TSF is able to initiate communications].
    targets:
    - WLANPPv1.0(2011)
    source: Common Criteria
    ---
    foreign_id: FCS_HTTPS_EXT.1(AE)
    relation: connects
    headline: |-
      Be able to audit failure to establish an HTTPS
            session, with audit detail including reason for the failure (the
            reason can be somewhat generic, like failed to negotiate
            ciphers). This audit message may be redundant to an audit
            message for failure to establish a TLS session.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_HTTPS_EXT.1(AE)
    relation: connects
    headline: |-
      Be able to audit establishment and termination of an
            HTTPS session, with audit detail including identification of the
            remote endpoint (e.g. IP address, hostname, etc.). This audit
            message may be redundant to an audit message for
            establishment/termination of a TLS session.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_HTTPS_EXT.1.2
    relation: implies
    headline: |-
      Implement HTTPS using TLS as specified in
            FCS_TLS_EXT.1.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_HTTPS_EXT.1.1
    relation: implies
    headline: |-
      Implement the HTTPS protocol that complies with RFC
            2818.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_HTTPS_EXT.1
    relation: connects
    headline: |-
      If HTTPS is selected as a supported protocol then
            this requirement must be included in the ST. FCS_HTTPS_EXT.1
            Extended: HTTP Security (HTTPS) FCS_HTTPS_EXT.1.1 The TSF shall
            implement the HTTPS protocol that complies with RFC
            2818. FCS_HTTPS_EXT.1.2 The TSF shall implement HTTPS using TLS
            as specified in FCS_TLS_EXT.1.
    targets:
    - WLANPPv1.0(2011)
    source: Common Criteria
    ---
    foreign_id: FTP_TRP.1
    relation: connects
    headline: |-
      FTP_TRP.1 Trusted Path FTP_TRP.1.1 Refinement: The
            TSF shall use [selection, choose at least one of: IPSEC, SSH,
            TLS, TLS/HTTPS] provide a trusted communication path between
            itself and remote administrators that is logically distinct from
            other communication paths and provides assured identification of
            its end points and protection of the communicated data from
            disclosure and detection of modification of the communicated
            data. FTP_TRP.1.2 Refinement: The TSF shall permit remote
            administrators to initiate communication via the trusted
            path. FTP_TRP.1.3 The TSF shall require the use of the trusted
            path for initial administrator authentication and all remote
            administration actions.
    targets:
    - WLANPPv1.0(2011)
    source: Common Criteria
    ---
    foreign_id: FTP_ITC.1
    relation: connects
    headline: |-
      FTP_ITC.1 Inter-TSF trusted channel FTP_ITC.1.1
            Refinement: The TSF shall use 802.11-2007, IPSEC, and
            [selection: SSH, TLS, TLS/HTTPS, no other protocols] to provide
            a trusted communication channel between itself and all
            authorized IT entities that is logically distinct from other
            communication channels and provides assured identification of
            its end points and protection of the channel data from
            disclosure and detection of modification of the channel
            data. FTP_ITC.1.2 The TSF shall permit the TSF, or the
            authorized IT entities to initiate communication via the trusted
            channel. FTP_ ITC.1.3 The TSF shall initiate communication via
            the trusted channel for [assignment: list of services for which
            the TSF is able to initiate communications].
    targets:
    - WLANPPv1.0(2011)
    source: Common Criteria
    ---
    foreign_id: FCS_SSH_EXT.1.7(AE)
    relation: connects
    headline: |-
      Be able to audit failure to establish an SSH session,
            with audit detail including reason for the failure
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_SSH_EXT.1.7
    relation: connects
    headline: |-
      Ensure that diffie-hellman-group14-sha1 is the only
            allowed key exchange method used for the SSH
            protocol.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_SSH_EXT.1.6
    relation: connects
    headline: |-
      Ensure that data integrity algorithms used in SSH
            transport connection is [selection: hmac-sha1, hmac-sha1-96,
            hmac-md5, hmac-md5-96].
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_SSH_EXT.1.5
    relation: connects
    headline: |-
      Ensure that the SSH transport implementation uses
            SSH_RSA and [selection: PGP-SIGN-RSA, PGP-SIGN-DSS, no other
            public key algorithms,] as its public key
            algorithm(s).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_SSH_EXT.1.4
    relation: connects
    headline: |-
      Ensure that the SSH transport implementation uses the
            following encryption algorithms: AES-CBC-128, AES-CBC-256,
            [selection: AEAD_AES_128_GCM, AEAD_AES_256_GCM, no other
            algorithms].
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_SSH_EXT.1.3
    relation: connects
    headline: |-
      Ensure that, as described in RFC 4253, packets
            greater than [assignment: number of bytes] bytes in an SSH
            transport connection are dropped.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_SSH_EXT.1.2
    relation: connects
    headline: |-
      Ensure that the SSH protocol implementation supports
            the following authentication methods as described in RFC 4252:
            public key-based, password-based.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_SSH_EXT.1.1
    relation: implies
    headline: |-
      Implement the SSH protocol that complies with RFCs
            4251, 4252, 4253, and 4254.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_SSH_EXT.1
    relation: connects
    headline: |-
      If SSH is selected as a supported protocol then this
            requirement must be included in the ST. FCS_SSH_EXT.1 Extended:
            Secure Shell (SSH) FCS_SSH_EXT.1.1 The TSF shall implement the
            SSH protocol that complies with RFCs 4251, 4252, 4253, and
            4254. FCS_SSH_EXT.1.2 The TSF shall ensure that the SSH
            connection be rekeyed after no more than 2^28 packets have been
            transmitted using that key. FCS_SSH_EXT.1.3 The TSF shall ensure
            that the SSH protocol implements a timeout period for
            authentication as defined in RFC 4252 of [assignment: timeout
            period], and provide a limit to the number of failed
            authentication attempts a client may perform in a single session
            to [assignment: maximum number of attempts]
            attempts. FCS_SSH_EXT.1.4 The TSF shall ensure that the SSH
            protocol implementation supports the following authentication
            methods as described in RFC 4252: public key-based,
            password-based. FCS_SSH_EXT.1.5 The TSF shall ensure that, as
            described in RFC 4253, packets greater than [assignment: number
            of bytes] bytes in an SSH transport connection are
            dropped. FCS_SSH_EXT.1.6 The TSF shall ensure that the SSH
            transport implementation uses the following encryption
            algorithms: AES-CBC-128, AES-CBC-256-CBC, [assignment:
            AEAD_AES_128_GCM, AEAD_AES_256_GCM, no other encryption
            algorithms]. FCS_SSH_EXT.1.7 The TSF shall ensure that the SSH
            transport implementation uses SSH_RSA and [selection:
            PGP-SIGN-RSA, PGP-SIGN-DSS, no other public key algorithms] as
            its public key algorithm(s). FCS_SSH_EXT.1.8 The TSF shall
            ensure that the data integrity algorithm used in the SSH
            transport connection is hmac-sha1 and [selection: no other
            algorithm, hmac-sha1-96, hmac-md5, hmac-md5-96]. FCS_SSH_EXT.1.9
            The TSF shall ensure that diffie-hellman-group14-sha1 is the
            only allowed key exchange method used for the SSH
            protocol.
    targets:
    - WLANPPv1.0(2011)
    source: Common Criteria
    ---
    foreign_id: FCS_TLS_EXT.1.1
    relation: connects
    headline: |-
      implement one or more of the following protocols
            [selection: TLS 1.0 (RFC 2246), TLS 1.1 (RFC 4346), TLS 1.2 (RFC
            5246)] supporting the following ciphersuites: Mandatory
            Ciphersuites: TLS_RSA_WITH_AES_128_CBC_SHA
            TLS_RSA_WITH_AES_256_CBC_SHA TLS_DHE_RSA_WITH_AES_128_CBC_SHA
            TLS_DHE_RSA_WITH_AES_256_CBC_SHA
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FAU_STG_EXT.1.1
    relation: connects
    headline: |-
      CC Requirement Enhancement: Ensure that all audit
            mechanism that are relied upon to generate any 'CC Auditable
            Event' could be transmitted through at least one of IPsec, TLS,
            or SSH. This could include syslog over TLS, or syslog over IPsec
            (preferably TCP syslog), or TACACS+ over IPsec, or SNMP over
            IPsec, or SNMPv3 over TLS or IPsec.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria

# History

```yaml
-----
affected_psb: SEC-CRY-MGT
---
impact: non-normative
headline: >
  Updated to separate FR's-----
affected_psb: SEC-CRY-MGT
---
impact: non-normative
headline: >
  Updated to include specific details about manbagement 
  protocols like NETCONF, RESTCONF and gNMI.
-----
affected_psb: SEC-CRY-MGT
---
deprecated_psb: SEC-SSH-V2.0
impact: normative
headline: >
  SEC-SSH-V2.0 consolidated in SEC-CRY-MGT-FR1.
---
deprecated_psb: SEC-HTP-SSL3-3
impact: non-normative
headline: >
  SEC-HTP-SSL3-3 consolidated in SEC-CRY-MGT-FR2.
---
deprecated_psb: SEC-MGT-TLS-2
impact: non-normative
headline: >
  SEC-MGT-TLS-2 consolidated in SEC-CRY-MGT-FR2.
description: >
This requirement was introduced in March 2020 and consolidates three
older requirements SEC-SSH-V2.0, SEC-HTP-SSL3-3 and SEC-MGT-TLS-2.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings that support
          text-based or other management
          protocols.

    category: Cryptographic Support
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 1
    id: SEC-CRY-MGT-FR2
    issueref: ISS_SEC-CRY-MGT
    tags:
    - EN/PI
    - Critical PSB
    - PSB/OnPrem
    - FAST
