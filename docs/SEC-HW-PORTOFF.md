# Headline

Disable ports not meant for field use.

# Description

Completely disable unused externally accessible ports (for example USB interfaces, serial console ports, storage slots, etc). Disable unneeded functions on enabled external ports. Completely disable unused internal debug and storage ports.

A "port" is any electrical or electromagnetic interface (including optical and RF interfaces) intended to exchange data with a removable module or modules, or with any module not permanently attached to a circuit board. A port need not include a connector; a set of exposed pads that form a communication interface is still a port.

A "debug port" is a port dedicated to hardware or software debugging activities such as interrogating system state or modifying the usual course of operation. Examples include JTAG ports, console ports, etc.

An "externally accessible port" is one which either--

1. Can be connected to without using tools to disassemble a device chassis, opening a locked cover, or removing the [turnkey module](#DEF_TurnkeyModule) from a larger assembly
1. Is protected only by a cover shared with ports that might be used in ordinary operation
1. Is protected only by a cover that could be left off unobtrusively
1. Is part of a subassembly that might be removed from a chassis without causing a system reboot, and returned with a readily available device quickly and unobtrusively attached to the port (for example a MicroSD slot on a line card).

"Field use" is using a port while the [turnkey module](#DEF_TurnkeyModule) is in operation and doing work for customers, as opposed to within Cisco for testing, debugging, characterization, or the like. Use by or at the direction of Cisco support is still "field use" if the [product](#DEF_Product) is in "production" when the use happens.

# Behavior

## SEC-HW-PORTOFF-FR1: Disable unused externally accessible ports

Unless they are specifically intended for field use, externally accessible ports _MUST_ be completely disabled.

## SEC-HW-PORTOFF-FR2: Disable debug and storage ports
Internal debug and storage ports _MUST_ be completely disabled for which connectors or pads appear on production boards. 

**Supplemental Guidance**: For debugging ports which *are* intended to be used in the field, see also [SEC-HW-NOJTAG](#SEC-HW-NOJTAG).

## SEC-HW-PORTOFF-FR3: Disable for intented field use
If the intended field use for a port is to install expansion modules, then you _SHOULD_ disable that port in any software that doesn't actually support such expansion modules.

If a port is enabled because it is in fact intended for field use, then you _MUST_ disable any *functions* on that port which aren't specifically meant to be used in the field. For example, a USB port intended only for mass storage devices _MUST_NOT_ accept keyboard or other HID events, and vice versa.

**Supplemental Guidance**: A port is not disabled if the system will exchange data with any device connected to it. You _MAY_ disable ports in software but _SHOULD_ use any available hardware assistance. Don't permit the disabled ports or functions to be reenabled.

# Requirement References

    ---
    foreign_id: SEC-ASU-TMOD-FR1
    relation: connects
    headline: |-

              Even if a port is intended for field use, and you
              therefore do not disable that port, then
              the port forms part
              of the boundary and attack surface of any controlled
              space embodied in the hardware, and
              SEC-ASU-TMOD-FR1
              requires you to document it and describe how you
              control any access it may provide.

    source: PSB
    ---
    foreign_id: SEC-HW-NOJTAG
    relation: connects
    headline: |-

              If a hardware debug port like a JTAG port
              is enabled for field use, then
              SEC-HW-NOJTAG
              requires you to apply certain authentication
              and access control measures for access to
              that port.

    source: PSB
    ---
    foreign_id: SEC-CSP-NOCDBG
    relation: connects
    headline: |-
      SEC-CSP-NOCDBG
              requires that any field debugging, including
              not only JTAG but things like console-based
              debuggers, be accessible only with physical
              access to the
              turnkey module.

    source: PSB

# History

```yaml
-----
affected_psb: SEC-HW-PORTOFF
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
          institutionalturnkey modules
                    and their components

    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 1
    id: SEC-HW-PORTOFF
    issueref: ISS_Invade
    tags:
    - EN/PI
    - EN/PD
    - PSB/OnPrem
