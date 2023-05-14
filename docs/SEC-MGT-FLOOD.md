# Headline

Maintain administration during flood attack

# Key Benefits

[Administration](#DEF_Administrator) functions are often particularly
critical during attacks, since they are often the only means of
characterizing or controlling the attack.

# Behavior

## SEC-MGT-FLOOD-FR1: Maintain administration during flood attack

If the [standalone device](#DEF_StandaloneDevice) has a physical
interface which does not actually carry flood traffic, it _MUST_ be
possible to continue networked [administration](#DEF_Administrator) of
the [standalone device](#DEF_StandaloneDevice) via that interface, even
during any of the [reference floods](#DEF_ReferenceFlood).

# History
```yaml
-----
affected_psb: SEC-MGT-FLOOD
description:  Updated to functional requirements. 

```

## Older history (manually maintained; may be incomplete)

PSBCTR 5.0: Replaced “connection path” with “physical interface”.

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          standalone devices.

    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-MGT-FLOOD
    issueref: ISS_Floods
    tags:
    - EN/PI
    - PSB/OnPrem
    - EN/PI DT
