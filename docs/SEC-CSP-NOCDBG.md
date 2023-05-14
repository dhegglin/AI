# Headline

Control debuggers

# Key Benefits

This is in effect an implication of other requirements; it's impractical for a low-level debugger to have the [authentication](#DEF_Authentication) or [authorization](#DEF_Authorization) features to provide a boundary for controlled space other than by physical access verification. It's included here for clarity and separate tracking.

# Description

It shouldn't be possible the use of an existing tool on the system that is remotely accessible and can read or write across a large amount (arbitrary) of memory.

It shouldn't be possible to use a ROM debugger (or similar) to subvert code signing, etc.

# Behavior

## SEC-CSP-NOCDBG-FR1: Control Debuggers

1. Physical access to the [turnkey module](#DEF_TurnkeyModule) _MUST_ be required in order to use any debug feature which can make arbitrary modifications to the internal state of [turnkey module](#DEF_TurnkeyModule) or any [controlled space](#DEF_ControlledSpace) inside it, or extract arbitrary data from [controlled space](#DEF_ControlledSpace). This includes, but is not limited to, [console](#DEF_Console) debuggers embedded in [base software](#DEF_BaseSoftware).

# History

```yaml
-----
affected_psb: SEC-CSP-NOCDBG
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
          turnkey modules
                      containing closedexecution space
                      or
                      critical targets
                      (almost all
                      bounded computers)

    category: Threat Surface Reduction
    riskArea: Application & Interface Security
    waivable: true
    version: 2
    id: SEC-CSP-NOCDBG
    issueref: ISS_Debugger
    tags:
    - EN/PD
    - EN/PI
    - PSB/OnPrem
