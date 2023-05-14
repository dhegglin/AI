# Headline

Protect Application Execution Space 

# Key Benefits



# Description
Protect the execution space in which your code runs so that running code cannot be modified maliciously.

## Definitions

A [controlled](#DEF_ControlledSpace) [execution space](#DEF_ExecutionSpace) is one that is protected against tampering by other execution spaces.  Code and data executed within the space are protected from unauthorized modification. Sensitive data within it is protected against unauthorized reading and use.  

# Behavior

## SEC-SW-APPPROT-FR1: Code Runs in Controlled Execution Space 
(was SEC-SW-CLOCONT/OPENCONT-FR1)

The [execution spaces](#DEF_ExecutionSpace) for all [code](#DEF_Code) _MUST_ be [controlled spaces](#DEF_ControlledSpace).

## SEC-SW-APPPROT-FR2: Controlled Execution Space Safeguards
(was SEC-SW-CLOCONT/OPENCONT-FR2)

The [controlled space](#DEF_ControlledSpace) _MUST_ be designed to
prevent any [open](#DEF_Open) entity, as well as any
[closed](#DEF_Closed) entity without an architecturally justified
reason to do so, from directly modifying the internal state of the executing code
or any other contents of the execution space.

Open entities _MAY_ be permitted to exchange messages with closed code, to use its
services, or to provide services to it, but safeguards _MUST_
protect against uncontrolled or unintended modifications to the code's
behavior, whether it is open or closed.

## SEC-SW-APPPROT-FR3: Closed Code Security Assurance
(was SEC-SW-CLOCONT/OPENCONT-FR3)

The [controlled space](#DEF_ControlledSpace) _MUST_ be designed to 
stop any entity from causing executing code to violate any desired security
assurance. This may affect the design of the code itself as well as of other
system elements.

## SEC-SW-APPPROT-FR4 Closed code must be protected by closed code 
(was SEC-SW-INSCHK-FR9)

You _MUST_ rely only on closed technology to control modification of any code, authentication roots, and other data trusted for verification. Do not use anything modifiable by any non-closed system component when verifying closed code.

This means that any installer dealing with [closed](#DEF_Closed) code _MUST_ itself be closed, as must all enclosing executors of such installers. This is only possible with an unbroken chain of closed installers and loaders starting with stage zero base software supplied with closed hardware. If the Cisco offering executes within a non-Cisco provided execution space (e.g. hypervisor that is not part of the offering), the Cisco installer MUST still verify signatures on modules and packages. 

# Informative References

* RECIPE: [Secure Boot](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Secure%20Boot.aspx)
* RECIPE: [EFI Software Signing for UEFI Secure Boot](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/EFI%20Software%20Signing%20for%20UEFI%20Secure%20Boot.aspx)
* RECIPE: [UEFI Secure Boot](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/UEFI%20Secure%20Boot.aspx)

# Requirement References

---
    foreign_id: SEC-CSP-NOCDBG
    relation: implies
    headline: |-

              If SEC-CSP-NOCDBG applies to the
              execution space of some closed code,
              but you don't actually comply with
              SEC-CSP-NOCDBG, then that execution
              space is not a controlled space, and
              therefore your offering does not
              comply with SEC-SW-APPPROT.

    source: PSB

# History

```yaml
-----
deprecated_psb: SEC-SW-CLOCONT
description:  Merged int SEC-SW-APPPROT. 

-----
deprecated_psb: SEC-SW-OPENCONT
description:  Merged int SEC-SW-APPPROT. 
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          [offerings](#DEF_Offering)
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 1
    id: SEC-SW-APPPROT
    issueref: ISS_ClosedMustWork
    tags:
    - EN/PI
    - PSB/OnPrem
