# Headline

Provide cryptographic protection outside controlled space

# Description

There are two ways to protect (unerased) data: [controlled
space](#DEF_ControlledSpace) and [cryptography](#DEF_Cryptography). Use
at least one of them to protect all non-[public](#DEF_Public) data.
Protect both confidentiality and integrity.

Network links usually pass outside of [controlled
space](#DEF_ControlledSpace), so encrypt non-[public](#DEF_Public)
network traffic. Storage devices always leave [controlled
space](#DEF_ControlledSpace) at the end of their lives, so encrypt
non-[public](#DEF_Public) data "at rest".

# Behavior

This requirement governs your protection of the confidentiality and
integrity described in the [affected
data](#SEC-CRY-ALWAYS_affected_data) subsection.

By [default](#DEF_Default), keep all affected data either--

1.  In [controlled space](#DEF_ControlledSpace) as described under
    "[Controlled space rules](../implementation/SEC-CRY-ALWAYS.md#SEC-CRY-ALWAYS_Controlled_Space)" in the Implementation
    Guidance for this reqirement,

    OR

2.  Protected using [good cryptography](#DEF_GoodCryptography).

### Affected data

<a id="SEC-CRY-ALWAYS_affected_data"></a>

For releases starting the CSDL/PSB compliance tracking process after
January 1, 2019, protect--

1.  Confidentiality and integrity of all data not affirmatively known to
    be [public](#DEF_Public).

2.  Integrity of all data affecting the behavior of any
    non-[public](#DEF_Public)[target](#DEF_Target), even if knowledge of
    the data themselves is [public](#DEF_Public).

The CSDL/PSB compliance tracking process starts when you create a
project in CSERV, or do something analogous in any alternate or
successor system.
## SEC-CRY-ALWAYS-FR1: Sending Affected Data Outside Controlled Space

1. You _MUST_NOT_ not send affected data outside of [controlled
space](#DEF_ControlledSpace) without cryptographic protection, and
_MUST_NOT_ require any *outside entity* to do so.

2. You _MUST_ prevent affected data from leaving controlled space unprotected
even when hardware devices fail. This usually requires encrypting all
affected data written to [persistent](#DEF_Persistent) storage (aka
"data at rest").

3. Cisco _MUST_NOT_ change the required default behavior without
an explicit outside request.

NB: The definition of "[default](#DEF_Default)" means that any
deviation, *even in a service offering*, _MUST_ be requested by a
*non-Cisco*[controlling policy entity](#DEF_ControllingPolicyEntity) for
the data and/or for the targets whose behavior would be affected by the
data.

An example of a controlling policy entity is an enterprise network's in
which almost always the corporation owns the network.

## SEC-CRY-ALWAYS-FR2: Receiving Data from Outside Controlled Space

1. You _MUST_NOT_ rely on affected data arriving from outside of
[controlled space](#DEF_ControlledSpace) unless you can
cryptographically verify the source and integrity of those data.

2. You _MUST_NOT_ enable incoming logins using passwords over cleartext
Telnet (or HTTP) by default, because that would force your
[peer](#DEF_Peer) to send an unencrypted password.

## SEC-CRY-ALWAYS-FR3: Exception: external constraints

<a id="SEC-CRY-ALWAYS_external_constraints"></a>

1. You _MAY_, by [default](#DEF_Default), omit protection for data
passing in or out of [controlled space](#DEF_ControlledSpace) if
required to do so by an [external constraint](#DEF_ExternalConstraint),
provided that--

2.  You apply the exceptional default to the smallest possible part of
    the system.

    For example, if some universally used protocol X can't function
    without your sending some information outside of controlled space
    unencrypted, then you _MAY_ do so *when protocol X is enabled*,
    but--

    1.  You _MUST_NOT_ *enable* protocol X by default unless doing so
        is [essential](#DEF_Essential) to the system as a whole, or to
        some larger part of the system which has been explicitly enabled
        by an [administrator](#DEF_Administrator). If protocol X is not
        essential, then the external constraint exception only applies
        to the default *within the context* of protocol X, not to the
        decision to use protocol X to begin with.

    2.  You _MUST_ omit protection *only* for the data actually
        affected by the external constraint.

3.  You make the minimum sacrifice of protection required by the
    [external constraint](#DEF_ExternalConstraint).

    The example of DNS illustrates several cases:

    1.  As of 2018, overwhelmingly common practice prevents most
        [offerings](#DEF_Offering) from using encryption (by default) to
        protect DNS *confidentiality*. Nonetheless,
        DNS-[aware](#DEF_Aware)[offerings](#DEF_Offering) _MUST_ still
        use DNSSEC to protect DNS *integrity*.

    2.  Similarly, unsigned DNS zones are very common. This creates an
        external constraint; DNS resolvers are forced to accept
        non-integrity-protected data from unsigned zones. However, since
        DNSSEC provides a definitive way to determine *whether* a zone
        is signed, resolvers aren't allowed to skip validation for
        *signed* zones.

    3.  Since every non-DNSSEC-[aware](#DEF_Aware) resolver can use data
        from any signed zone, there is no external constraint at all to
        free any DNS *server* from the requirement to sign its own
        zones.

4.  You describe the external constraint clearly in your design
    documentation and/or in your CSDL/PSB compliance evaluation,
    identifying the affected data and describing how the
    [external constraint](#DEF_ExternalConstraint) is met.

# Informative References

RECIPE: [Best Practices Using SSL TLS](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Best%20Practices%20Using%20SSLTLS.aspx)

Cisco TAmServices library (provides a relatively portable secret storage
API): [Cisco TAm
Services](https://apps.na.collabserv.com/communities/service/html/communitystart?communityUuid=04b7660c-7ea5-446d-acb1-3eb54351ecdb)

"Where to store that key":
<https://wwwin-github.cisco.com/CSDL/PSB/wiki/Where-to-store-that-key>

# Requirement References

    ---
    foreign_id: SEC-ASU-TMOD-FR1
    relation: connects
    headline: |-
                SEC-CRY-ALWAYS demands that you keep certain data in
                controlled space.
                SEC-ASU-TMOD-FR1 is the main
                requirement defining what you must do to claim you
                have controlled space.
    source: PSB
    ---
    foreign_id: SEC-SCR-CONFLEAK
    relation: connects
    headline: |-
                SEC-CRY-ALWAYS (usually) demands encrypting all of your
                storage.
                SEC-SCR-CONFLEAK
                requires a second layer of encryption for
                credentials,
                cryptographic secrets,
                and other
                critical
                configuration data that you put in
                certain likely-to-leak places, notably
                logs and configuration files.
    source: PSB
    ---
    foreign_id: SEC-LOG-TRANS
    relation: connects
    headline: |-
      SEC-LOG-TRANS requires
                encrypted logging protocols in Cisco services
                (even inside of controlled space).
    source: PSB
    ---
    foreign_id: SEC-OPS-RESTCRYP
    relation: connects
    headline: |-
      SEC-OPS-RESTCRYP requires
                encryption of most customer data stored in
                Cisco services (even inside of controlled space).
    source: PSB
    ---
    foreign_id: SEC-CRY-MGT-FR1
    relation: connects
    headline: |-
      SEC-CRY-MGT-FR1 requires
                specific cryptographic technology for
                interactive text-mode logins.
    source: PSB
    ---
    foreign_id: SEC-CRY-MGT-FR1
    relation: connects
    headline: |-
      SEC-CRY-MGT-FR1 requires
                specific cryptographic technology for
                HTTP management.
    source: PSB
    ---
    foreign_id: SEC-DNS-SECURE
    relation: connects
    headline: |-
                The standard referred to by
                SEC-DNS-SECURE requires
                specific cryptographic protocols for
                DNS integrity.
    source: PSB
    ---
    foreign_id: SEC-CRY-SNMP
    relation: connects
    headline: |-
        SEC-CRY-SNMP requires specific
        cryptographic technology for
        SNMP confidentiality and
        authentiocation.
    source: PSB
    ---
    foreign_id: FMT_MTD.1(3)
    relation: connects
    headline: |-
      FMT_MTD.1(3) Management of TSF Data (for reading of
            all symmetric keys) FMT_MTD.1.1(3) Refinement: The TSF shall
            prevent reading of all pre-shared keys, symmetric key, and
            private keys.
    targets:
    - WLANPPv1.0(2011)
    source: Common Criteria
    ---
    foreign_id: FPT_SKP_EXT.1.1
    relation: connects
    headline: |-
      Prevent reading of all pre-shared keys, symmetric
            keys, and private keys.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: C.8.3
    relation: connects
    headline: |-
              ISO 27001:2013: C.8.3 Information security risk treatment
    targets:
    - C
    source: ISO 27001:2013
    ---
    foreign_id: 8.3.1
    relation: connects
    headline: |-
              ISO 27002:2013: 8.3.1 Management of removable media
    targets:
    - '8'
    source: ISO 27002:2013
    ---
    foreign_id: 8.3.2
    relation: connects
    headline: |-
              ISO 27002:2013: C.8.3.1 Disposal of media
    targets:
    - '8'
    source: ISO 27002:2013
    ---
    foreign_id: A.11.2.7
    relation: connects
    headline: |-
              ISO 27001:2013: A.11.2.7 Secure disposal or re-use of equipment
    targets:
    - A
    source: ISO 27002:2013
    ---
    foreign_id: A.18.1
    relation: connects
    headline: |-
              ISO 27001:2013: A.18.1 Compliance with legal or contractual requirements
    targets:
    - A
    source: ISO 27002:2013

# History

```yaml
-----
affected_psb: SEC-CRY-ALWAYS
description:  Updated to functional requirements.

```

## Older history (manually maintained; may be incomplete

This requirement is descended from the old SEC-SCR-CONTROL.

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 9
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings
    category: Threat Surface Reduction
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 2
    id: SEC-CRY-ALWAYS
    issueref: ISS_DataMishandled
    tags:
    - EN/PI
    - CloudCritical
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
