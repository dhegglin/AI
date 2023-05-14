# Headline

Trust Anchor Module (TAm) Chip Requirements

# Key Benefits

Maintaining [controlled space](#DEF_ControlledSpace) on general
purpose hardware is very difficult, especially if physical attacks are
considered, and places onerous demands on software development when it
is possible at all. Compromise of even one device's identity
[credential](#DEF_Credential) may have serious implications,
especially if the attacker's goal is to mass produce “clones”. A
dedicated, strongly assured [controlled space](#DEF_ControlledSpace)
is therefore very desirable for [device identity](#DEF_DeviceIdentity)
key-pair. Dedicated Trust Anchor module (TAm) chips are
generally both simpler from an engineering point of view and more
resistant to attack than “ad hoc” solutions, especially solutions
which rely on the correct behavior and attack resistance of large
amounts of system software.

# Description

Use approved, purpose-built hardware that provides device identity credential confidentiality, integrity and availability.

# Behavior

## SEC-CRE-CHIPID-FR2: Internal Key Generation

The TAm chip _SHOULD_ generate the [device identity](#DEF_DeviceIdentity) key-pair internally. If the device identity key-pair is instead
generated outside of the chip, then it _MUST_ be handled and installed
as described under the externally generated keys requirements in
SEC-CRE-PROVID-FR2 and SEC-CRE-PROVID-FR3.

## SEC-CRE-CHIPID-FR12: Device Identity Key Storage (new)

The TAm chip _MUST_ store the [device identity](#DEF_DeviceIdentity) [credential](#DEF_Credential) (i.e. key-pair), preventing any unauthorized change to it once created or loaded. 

## SEC-CRE-CHIPID-FR1: Key Confidentiality

The TAm chip _MUST NOT_ release the device identity private key to any entity including the device itself under any circumstances.

## SEC-CRE-CHIPID-FR6: Device Identity Certificate Storage

The TAm chip _SHOULD_ also store the corresponding
[device identity](#DEF_DeviceIdentity) [certificate](#DEF_Certificate),
preventing any unauthorized change to it once loaded.

## SEC-CRE-CHIPID-FR5 Cryptographic Signature

The TAm chip _MUST_ be capable of producing, without external assistance
and without exposing any [critical](#DEF_Critical) data to external
entities, a message which binds the following under a single
cryptographic signature made with the
[device identity](#DEF_DeviceIdentity) private key:

1. The [device identity](#DEF_DeviceIdentity), in the form used in
   the X.509
   [device identity](#DEF_DeviceIdentity)
   [certificate](#DEF_Certificate), or the entire X.509
   [certificate](#DEF_Certificate) (See
   [SEC-CRE-IDFORM-3](#SEC-CRE-IDFORM-3) for certificate
   requirements).

1. An externally provided per-transaction challenge of at least 128
   bits. Other information, such as the chip identifier, _MAY_ be
   included under such a signature.

## SEC-CRE-CHIPID-FR4: Unique Chip Identifier

The TAm chip _MUST_ have its own, uniquely assigned, immutable chip
identifier.

## SEC-CRE-CHIPID-FR7: Chip Tampering Protection

The TAm chip _SHOULD_ be protected against tampering with the following means:

1. Residing entirely on one silicon die.
1. Being overcoated and/or passivated.
1. Including measures to resist probing with focused ion beams and
   similar tools.
1. Including measures to resist power, timing, and fault induction
   attacks.
1. Including electrical or chemical measures designed to thoroughly
   [erase](#DEF_Erase) all embedded [critical](#DEF_Critical) data
   upon decapsulation or other physical tampering. This
   erasure _SHOULD_ be resistant to recovery through
   physical or electrical probing of the die.




# History

```yaml
-----
affected_psb: SEC-CRE-CHIPID-3
---
impact: non-normative
description: >
  Cosmetic updates.
```

# Attributes

    id: SEC-CRE-CHIPID
    version: 5
    category: Boot and System Integrity
    riskArea: System Integrity
    legallysensitive: false
    waivable: true
    issueref: ISS_DevIDTamper
    applicability:
      - force: mandatory
        target:
          restrict: >
            Trust Anchor modules
    priority: 10
    phase: requirements
    tags:
        - EN/PD
        - G7
        - Critical PSB
        - PSB/OnPrem
