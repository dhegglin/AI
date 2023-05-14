# Headline

Restore default authentication roots on entering clean state.

# Key Benefits

Loss of keys might make it difficult to upgrade the device, and might even leave the device unable to boot and run its installed software. Complete immunity to this would demand retaining user trust information when entering a [clean state](#DEF_CleanState), which might put new uses of cleaned equipment at risk. We therefore compromise by requiring that standard Cisco trust information be preserved.

This is an implication of [SEC-DAT-CLNSTATE](#SEC-DAT-CLNSTATE), but a
subtle enough one that it deserves its own requirement.

# Description

An [authentication root](#DEF_AuthenticationRoot) is a piece of information stored inside a system as part of its code or configuration, to give that system a basis for deciding the validity of credentials it could not otherwise validate.

A [clean state](#DEF_CleanState) of a device is a "blank" state, free of any user information. If user information was formerly on the device, it will have been erased.

Cleaning the device shouldn't leave it without the keys it needs to verify the software it's running.

# Behavior

## SEC-CLN-KEYS-FR1: Restore Authentication Root Keys

1. A [turnkey module](#DEF_TurnkeyModule) entering a [clean state](#DEF_CleanState) _MUST_ restore all default [authentication roots](#DEF_AuthenticationRoot) to the states they would have had on initial installation.

1. Information associated with customer private signature schemes or customers' discretionary modifications to the default trust structure _MUST_NOT_ be retained.

# History

```yaml
-----
affected_psb: SEC-CLN-KEYS
description:  Updated to functional requirements.

```

## Older history (manually maintained; may be incomplete)

-   SEC-CLN-KEYS-2: Simplified and reconciled with 6.0 planned
    authentication requirements.
-   SEC-CLN-KEYS-2: Written in PSB Re-Boot format for September, 2020 Release.

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          turnkey modules
                      purporting to
                      enter clean states
    category: Threat Surface Reduction
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 2
    id: SEC-CLN-KEYS
    issueref: ISS_CleanNoPKI
    tags:
    - EN/PD
    - PSB/OnPrem
    - EN/PI DT
