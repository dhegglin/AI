# Headline

Log cryptographic connection setup and teardown

# Description

Allow the [administrator](#DEF_Administrator) to configure the [offering](#DEF_Offering) to log information for every two-way [cryptographic](#DEF_Cryptography) connection. Some protocols may call such a connection a "security association" or even a "session".

# Behavior

Logging of two-way [cryptographic](#DEF_Cryptography) connection help to provide incident response and audit teams information of what, who, when, and where.  Enough detail on each event to assist in assemble a coherent account of relevant events.

## SEC-CRY-LOG-FR1: Connection Setup

Service offerings _MUST_ enable logging of  *successful or unsuccessful* connection setup. In products, you _MAY_ disable it by default.

This applies to all two-way [cryptographic](#DEF_Cryptography) protocols that establish sessions or "associations", including but not limited to IPsec, SSH, SSL, TLS, DTLS, and 802.1ae.

You _MUST_ adhere to [SEC-LOG-CONTENT](#SEC-LOG-CONTENT) for log content and format and additionally include the following:

1.  The local [listener's](#DEF_Listener) address at the layer underlying the [cryptographic](#DEF_Cryptography) protocol. For an IP-based protocol such as IPsec, this is an IP address. For a TCP- or UDP-based protocol such as TLS, SSH, or DTLS, it's an IP address with a port number. For a link-layer protocol, it's usually a MAC address.
2.  Information identifying the service to which the local [listener](#DEF_Listener) will (or would) deliver the data. If the  [listener](#DEF_Listener) is a server process using a [cryptographic](#DEF_Cryptography) library (for example an HTTP server using CiscoSSL), this _SHOULD_ be the process name and/or process ID of the server, or some similar logging identifier. If the [cryptographic](#DEF_Cryptography) protocol [listener](#DEF_Listener) forwards the traffic to another system or process after cryptographic processing, it _SHOULD_ be some identifier for the ultimate destination.
3.  The [peer's](#DEF_Peer) address at the layer underlying the [cryptographic](#DEF_Cryptography) protocol.
4.  The [principal](#DEF_Principal) name the [peer](#DEF_Peer) has claimed as part of the [cryptographic](#DEF_Cryptography) protocol itself. For SSH, this would ordinarily be a username. For X.509, it would be a distinguished name or alternate name extracted from a certificate. Log any information the [peer](#DEF_Peer) has provided, regardless of whether the negotation is completed.
5.  Whether or not the [peer's](#DEF_Peer) claimed [principal](#DEF_Principal) name was successfully authenticated.
6.  If the [peer](#DEF_Peer) has presented a [certificate](#DEF_Certificate), any serial number included in that [certificate](#DEF_Certificate), or a hash of the certificate itself (such as the one computed by "openssl x509 -sha1-fingerprint").
7.  Whether or not the connection was established successfully.
8.  If the connection wasn't established successfully, the reason for failure (this might be an invalid or revoked [credential](#DEF_Credential), lack of access to an authentication service, a protocol or format error, etc). You _SHOULD_ include as much detail as possible.
9.  A connection identifier, to be used to identify the log entry for the shutdown of the connection. This identifier _MUST_ be unique at least across a single instance of the [offering](#DEF_Offering) through the time between the connection establishment and connection shutdown, and _SHOULD_ be unique across as many systems and as much time as reasonably feasible.

## SEC-CRY-LOG-FR2: Connection Shutdown

Service offerings _MUST_ enable logging of connection shutdown. In products, you _MAY_ disable it by default.

When logging connection shutdown, you _MUST_ adhere to [SEC-LOG-CONTENT](#SEC-LOG-CONTENT) for log content and format and additionally include the following:

1.  Brief identifying information for the peer (for example an IP address, host name, or a [principal](#DEF_Principal) name). This is "convenience" information and need not be as complete as the information in the startup log message.
2.  The unique identifier from the log entry created at session startup.
3.  The reason for the shutdown (for example [peer](#DEF_Peer)-requested shutdown, shutdown requested by the overlying layer, timeout, error, etc).

# Informative References

- RECIPE: [Log Security-relevant Information](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Log%20SecurityRelevant%20Information.aspx)
- RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)

# Requirement References

    ---
    foreign_id: SEC-AUT-LOG
    relation: connects
    headline: |-
    
              If the authentication information used to set up a
              cryptographic association also defines a
              the principal
              associated with a session, then
              SEC-AUT-LOG
              will also apply to the event. This is a common case.
    
    source: PSB
    ---
    foreign_id: SEC-LOG-CONTENT
    relation: connects
    headline: |-
      SEC-LOG-CONTENT
              lists information to be included in all log entries.
    
    source: PSB
    ---
    foreign_id: FTP_TRP.1(AE)
    relation: implies
    headline: |-
      Be able to audit initiation and termination of the
            trusted channel (for remote administration), with audit detail
            including the claimed identity of the user.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FTP_TRP.1(AE)
    relation: implies
    headline: |-
      Be able to audit failures of the trusted channel
            functions.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FTP_ITC.1(AE)
    relation: implies
    headline: |-
      Be able to audit initiation and termination of a
            trusted channel.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FTP_ITC.1(AE)
    relation: implies
    headline: |-
      Be able to audit failure of trusted channel
            functions, with audit detail including identification of the
            initiator and target of any failed trusted channel establishment
            attempt.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_TLS_EXT.1(AE)
    relation: implies
    headline: |-
      Be able to audit Failure to establish a TLS session,
            with audit detail including a reason for the failure, and
            identification of the remote endpoint (IP address).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_TLS_EXT.1(AE)
    relation: implies
    headline: |-
      Be able to audit Establishment/Termination of a TLS
            session, with audit detail including identification of the
            remote endpoint (IP address).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_SSH_EXT.1(AE)
    relation: implies
    headline: |-
      Be able to audit Failure to establish an SSH session,
            with audit detail including a reason for the failure, and
            identification of the remote endpoint (IP address).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_SSH_EXT.1(AE)
    relation: implies
    headline: |-
      Be able to audit Establishment/Termination of an SSH
            session, with audit detail including identification of the
            remote endpoint (IP address).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_IPSEC_EXT.1(AE)
    relation: implies
    headline: |-
      Be able to audit Failure to establish an IPsec
            session, with audit detail including a reason for the failure,
            and identification of the remote endpoint (IP
            address).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_IPSEC_EXT.1(AE)
    relation: implies
    headline: |-
      Be able to audit Establishment/Termination of an
            IPsec session, with audit detail including identification of the
            remote endpoint (IP address).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_HTTPS_EXT.1(AE)
    relation: implies
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria

# History
```yaml
-----
affected_psb: SEC-CRY-LOG
description:  Updated to functional requirements. 

```
# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings
    category: Logging and Auditing
    riskArea: Logging & Monitoring
    waivable: true
    version: 1
    id: SEC-CRY-LOG
    issueref: ISS_Underlogging
    tags:
    - EN/PI
    - PSB/OnPrem
    - EN/PI DT
