# Headline

Remain stable during flooding attack

# Key Benefits

Denial of service attacks remain very popular on the Internet, both in
their own right and as components of larger attack strategies. A device
which crashes, or, worse, becomes corrupt in its operation when flooded
permits relatively long-term disruption with a relatively small
investment of the attacker's bandwidth.

# Description

Products need to survive common flooding-based denial of service
attacks.

# Behavior

The following FRs apply during and after any series of [reference
floods](#DEF_ReferenceFlood) directed to through any [standalone
device](#DEF_StandaloneDevice).

## SEC-BE-STABLE-FR1: Do Not Reload

The device _MUST_ continue to operate without reloading its software,
including performing its [essential](#DEF_Essential) functions, albeit
perhaps with greatly reduced performance.

## SEC-BE-STABLE-FR2: Maintain Consistency and Integrity

The device _MUST_ Maintain the integrity and consistency of its
internal data structures.  Memory _MUST NOT_ be leaked due to the
flooding attack.

## SEC-BE-STABLE-FR3: Automatically Recover Gracefully

The device _MUST_ recover gracefully, without human intervention,
after the attack.

# History

```yaml
-----
affected_psb: SEC-BE-STABLE
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
          standalone devices
    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-BE-STABLE
    issueref: ISS_Floods
    tags:
    - EN/PD
    - EN/PI
    - PSB/OnPrem
