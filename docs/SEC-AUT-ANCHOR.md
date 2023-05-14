# Headline

Anchor authentication trust chains

# Description

Authentication, cryptographic or otherwise, needs a trust anchor.  The entire trust chain being relied on must be understood, and every step needs to have adequate security.

Products frequently fail to trace authentication back to a trust anchor.  This has been common with TLS cryptography, where some products simply do not check the peers presented X.509 certificate.

# Behavior

The authentication information used in any [authorization](#DEF_Authorization) decision regarding any [peer](#DEF_Peer) must be based on a logically sound chain of inferences that uses both of the following pieces of information:

1. One or more locally configured [authentication roots](#DEF_AuthenticationRoot) compliant with [SEC-AUT-DEFROOT](#SEC-AUT-DEFROOT).
1. The credentials presented by the [peer](#DEF_Peer).

No unverified information may be relied upon at any stage of this chain of inferences.

## SEC-AUT-ANCHOR-FR1:  Local Credential Validation

Passwords _MUST_ be validated.

The authentication root used to verify a fixed password is almost always a cryptographic hash of that password.  [SEC-PWD-STORE](#SEC-PWD-STORE) requires this for the common case where the [peer](#DEF_Peer) sends the actual password to the [offering](#DEF_Offering).

**Supplemental Guidance:** Any SSH trusted key listed in an authorized_keys file is an authentication root. Using such a root for SSH access requires the remote [peer](#DEF_Peer) to prove possession of the trusted secret key.

## SEC-AUT-ANCHOR-FR2:  Remote Credential Validation

The [offering](#DEF_Offering) _MUST_ have an [authentication root](#DEF_AuthenticationRoot) to authenticate the external [agent](#DEF_Agent) itself.

If passwords are verified using an external [agent](#DEF_Agent) server such as a RADIUS server or LDAP server, the external [agent](#DEF_Agent) is responsible for authenticating the password.

**Supplemental Guidance:** A Kerberos KDC shares a secret with each principal. Both the KDC and the principal use that secret as an authentication root. The shared secret is maintained in a database at the KDC, but is often entered in the device configuration when a principal gets a ticket.  Note however; with PKINIT, Kerberos uses public-key cryptography instead, and the authentication roots are the public keys.

## SEC-AUT-ANCHOR-FR3:  Certificate and Key Validation

The [authentication root](#DEF_AuthenticationRoot) for a [peer](#DEF_Peer) using X.509 or a host-based key _MUST_ be authenticated using one of the following methods:
1. verify the [peer](#DEF_Peer) X.509 signature using a certificate authority in the list of trusted CAs of the [offering](#DEF_Offering) (see also [SEC-509-TRUST](#SEC-509-TRUST)).  The [offering](#DEF_Offering) configuration _MAY_ include only the CA certificate public key or it may include the CA certificate itself.
1. verify the [peer](#DEF_Peer) X.509 certificate or host-based key against the [offering](#DEF_Offering) locally stored X.509 certificates.  Local certificates are frequently referred to as certificate pinning.  Note that certificates pinning _MAY_ be pre-loaded and not be as a result of the initial session with the [peer](#DEF_Peer).*
1. if the [peer](#DEF_Peer) is using a DNS-based name, the [controlling policy entity](#DEF_ControllingPolicyEntity) of the domain may choose to use DNSSEC-signed TLSA records to inform the [offering](#DEF_Offering) which certificates or keys to trust.  In this case, the final [authentication root](#DEF_AuthenticationRoot) will be the DNSSEC root zone key signing key, *instead* of the locally trusted CA list.

*If the [authentication root](#DEF_AuthenticationRoot) for a [peer](#DEF_Peer) is added as part of certificate or host-based key pinning, the [offering](#DEF_Offering) must also allow removal or replacement of that [authentication root](#DEF_AuthenticationRoot).

**Supplemental Guidance:** When a [peer](#DEF_Peer) uses a self-signed [certificate](#DEF_Certificate), and does *not* use DNSSEC-signed TLSA records, the [peers'](#DEF_Peer) [authentication root](#DEF_AuthenticationRoot) is frequently a locally stored copy of that self-signed [certificate](#DEF_Certificate).

# History

```
-----
affected_psb: SEC-AUT-ANCHOR-2
---
deprecated_psb: SEC-AUT-ANCHOR
impact: non-normative
headline: >
    [SEC-AUT-ANCHOR](#SEC-AUT-ANCHOR) migrated to functional requirements.
```

# Informative References

[Mutual TLS Authentication](https://dzone.com/articles/mutual-authentication-two-way-ssl-explained-using)

[TLS Handshake](https://www.ssl.com/article/ssl-tls-handshake-overview/)

[Kerberos Protocol](https://en.wikipedia.org/wiki/Kerberos_(protocol))

[RADIUS Protocol](https://en.wikipedia.org/wiki/RADIUS) and [Diameter Protocol](https://en.wikipedia.org/wiki/Diameter_(protocol))

[LDAP Protocol](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol)

# Requirement References

```
---
source: PSB
foreign_id: SEC-AUT-DEFROOT
relation: connects
headline: >
    [SEC-AUT-DEFROOT](#SEC-AUT-DEFROOT) Lists the allowable authentication roots in offerings.
---
source: PSB
foreign_id: SEC-PWD-STORE
relation: connects
headline: >
    [SEC-PWD-STORE](#SEC-PWD-STORE) Requires encrypted storage of local credentials.
---
source: PSB
foreign_id: SEC-509-TRUST
relation: connects
headline: >
    [SEC-509-TRUST](#SEC-509-TRUST) Lists the allowable Certificate Authorities.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    waivable: true
    version: 2
    id: SEC-AUT-ANCHOR
    issueref: ISS_DefaultCreds
    tags:
    - EN/PI
    - EN/PD
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
    - Cloud
    - FAST
