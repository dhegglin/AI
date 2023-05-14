# Headline

Control equipment used by support personnel

# Key Benefits

One of the common ways [sensitive](#DEF_Sensitive) data are lost is due
to the misplaced or stolen mobile devices. Human errors or deliberate
policy violations in storing [sensitive](#DEF_Sensitive) information in
wrong type devices as well as failure to protect these devices result
into numerous [security](#DEF_Security) incidents each year. If a system
within the network, or removed from the network has any data on that
system that would be considered [sensitive](#DEF_Sensitive) it has
be controlled up to the point of disposal/destruction who can see or
[access](#DEF_Access) that data. BYOD systems are not allowed to do
[administration](#DEF_Administer) for software or network
infrastructure. It will require management approval for any nonstandard
equipment to be used in a [critical](#DEF_Critical) area or for
[administration](#DEF_Administer) of system/network.

# Description

Control equipment used by support personnel.

# Behavior

## SEC-OPS-EQUIP-FR1: Configure Devices

1.  All devices (including laptops, smart phones) which is used by
    support/operations to [access](#DEF_Access) production
    infrastructure/services _MUST_ be configured based on the Cisco
    corporate [security](#DEF_Security) policy.

2.  Mac and PC operating system _MUST_ have Anti-virus software
    installed.

## SEC-OPS-EQUIP-FR2: Implement Logout and Lockout Timings

Procedure to logout and screen lockouts for unattended equipment _MUST_ be in place.

## SEC-OPS-EQUIP-FR3: Employee Security Awareness

All support and operations employees _MUST_ be [aware](#DEF_Aware) of their responsibilities for leaving unattended
equipment in a secure manner.

# Normative References

1. Policy - Protection Against Malicious and Mobile Code

   - A.10.4 Protection against malicious and mobile code

1. [CSA IS 16](https://cloudsecurityalliance.org/research/ccm)

1. [CSA IS 32](https://cloudsecurityalliance.org/research/ccm)


# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Hosted and Infrastructure Services
        class: not_MobileApp
    category: Operational Process
    riskArea: System Hardening
    waivable: true
    version: 1
    id: SEC-OPS-EQUIP
    issueref: ISS_NoSecProgram
    tags:
    - Cloud
