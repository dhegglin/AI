# Headline

Disable directed broadcasts by default

# Key Benefits

The “smurf” attack in 2000 demonstrated that directed broadcasts were
extremely useful for mounting denial of service attacks. The prevalence
of smurf attacks was reduced to nuisance levels only after essentially
all [IP](#DEF_IP) router vendors disabled directed broadcasts by
default, thus making it more difficult to find smurf amplifier networks.

The legitimate uses of directed broadcasts, although not nonexistent,
were never common. The utility of directed broadcasts has been further
reduced by the ever-increasing prevalence of variable-length subnet
masks.

# Description

The dominant use for [IP](#DEF_IP) directed broadcast is traffic
amplification for denial of service attacks. It shouldn't be on by
default.

# Behavior

## SEC-RTR-NODIRBRO-FR1: Do no forward directed broadcasts

A directed broadcast is an [IP](#DEF_IP) datagram arriving from a source
not within an [IP](#DEF_IP) subnet, with that subnet's broadcast address
as its destination[. By default](#DEF_Default), directed broadcasts
_MUST_NOT_ be forwarded.

In identifying directed broadcasts, the source of each datagram
_SHOULD_ be determined by the interface on which that datagram is
received, and not by the source [IP](#DEF_IP) address in the datagram
itself.

# History

```yaml
-----
affected_psb: SEC-RTR-NODIRBRO
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
          IProuters
        class: Router
    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-RTR-NODIRBRO
    issueref: ISS_Floods
    tags:
    - EN/PI
    - PSB/OnPrem
    - FAST
