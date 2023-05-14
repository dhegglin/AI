# Headline

No fixed or forced null outbound credentials

# Description

When a Cisco [offering](#DEF_Offering) logs into other offerings it needs to allow the use of [credentials](#DEF_Credential) specified by the customer.  It is not sufficient to require the customer to enable a particular credential or force the customer to accept no [authentication](#DEF_Authentication). This applies to *all* credentials, including [pass phrases](#DEF_Passphrase) and private keys.

Not allowing customers to define [outbound](#DEF_Outbound) [credentials](#DEF_Credential) destroys the usefulness of authentication functionality on peers.

# Behavior

This behavior is required when the communication uses a protocol which supports [outbound](#DEF_Outbound) [credentials](#DEF_Credential).

## SEC-OUT-CRED-FR1: No Default Credentials

An offering _MUST NOT_ supply any [default](#DEF_Default) [outbound](#DEF_Outbound) [credential](#DEF_Credential) value, unless an [external constraint](#DEF_ExternalConstraint) requires a default.

## SEC-OUT-CRED-FR2: Configure Credentials

The [Administrator](#DEF_Administrator) _MUST_ be able to configure the [outbound](#DEF_Outbound) [credential(s)](#DEF_Credential) for communication with other offerings.

## SEC-OUT-CRED-FR3: Multiple Peer Credentials

The [Administrator](#DEF_Administrator) _MUST_ be able to specify a different [credential](#DEF_Credential) for each [peer](#DEF_Peer), except in a broadcast or multicast protocol or when [externally constrained](#DEF_ExternalConstraint).

## SEC-OUT-CRED-FR4: Credential Complexity

An offering _MUST_ support all [outbound](#DEF_Outbound) [credential](#DEF_Credential) values that are legal for the protocol.

# History

```
-----
affected_psb: SEC-OUT-CRED-3
description:  Updated to functional requirements.
---
deprecated_psb: SEC-OUT-CRED-2
impact: non-normative
headline: >
  [SEC-OUT-CRED-2](#SEC-OUT-CRED-2) updated to functional requirements.
```

# Requirement References

```
---
source: PSB
foreign_id: SEC-CRY-ALWAYS
relation: connects
headline: >
    [SEC-CRY-ALWAYS](#SEC-CRY-ALWAYS) Provide cryptographic protection outside controlled space.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          ALL offerings
        class: not_MobileApp
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    waivable: true
    version: 3
    id: SEC-OUT-CRED
    issueref: ISS_DefCreds
    tags:
    - EN/PI
    - PSB/OnPrem
