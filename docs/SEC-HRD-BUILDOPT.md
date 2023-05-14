# Headline

Build C/C++ programs using hardened options.

# Description

Modern compilers provide options to help harden the resulting binaries against memory corruption and other types of attacks. This PSB requires you to use available hardening options when building binaries. Currently, this PSB focuses on C/C++ programs.

# Behavior

## SEC-HRD-BUILDOPT-FR1: Build with read-only relocation

You _MUST_ build your C and C++ code using using flags supported by your complier to enable Read-Only Relocation if your build target is ELF file. The required flags can be found in implementation guidance of this PSB.

If your C or C++ code can't be built or cannot run correctly using the above protections, then you _MUST_ modify your code to be able to use them.

For third-party code, if you cannot recompile from source, you _SHOULD_ choose the binary with a version that has been built with read-only relocation options.

**Supplemental Guidance**
Read-only relocation technique prevents a type of arbitrary code execution by making GOT – Global Offset Table that is used to locate dynamic functions at run time - section to be read-only.

## SEC-HRD-BUILDOPT-FR2: Build with stack smash protection

You MUST build your C and C++ code using flags supported by your complier to enable Stack Smash Protections, if your operating system supports this protection. The required flags can be found in implementation guidance of this PSB.

For third-party code, if you can not recompile from source, you SHOULD choose a version that has been built with Stack Smash Protection enabled.

**Supplemental Guidance**  When Stack Smash Protection (SSP) is enabled the compiler will push a “canary” (a randomly chosen integer) on the stack just after a function return pointer has been pushed. Additional code is inserted to inspect the canary.  The canary value is then checked before the function returns; if it has changed, the program will abort. Generally, stack buffer overflow (aka "stack smashing") attacks will have to change the value of the canary as they write beyond the end of the buffer before they can get to the return pointer. Thus, the stack protection aborts the program protecting it against buffer overflow attack.

## SEC-HRD-BUILDOPT-FR3: Build with warning options

You _MUST_ also turn on the following warning options when building C/C++ programs:
1.	 -Werror=format-security
“format-security” warns about uses of format functions where it could introduce security problems. By using -Werror=format-security, compiling will be stopped when such security warning is issued.
2.	-Wall
This enables all the warnings about constructions that are considered questionable and could easily turn into security problems. You SHOULD stop the build for any warning to make sure you fix all the issues as soon as they arise instead of ignoring them and accumulate them over time.

You _MUST_ build with optimization to enable better analysis.

This requirement also applies when building kernel modules.

**Supplemental Guidance**: Compliance with SEC-RUN-ASLR, [SEC-RUN-OSC](#SEC-RUN-OSC) is also required when building C/C++ programs.


# Informative References
- RECIPE: [ASLR](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/ASLR%20in%20Linux%20Systems.aspx)
- RECIPE: [OSC](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Object%20Size%20Checking%20(OSC).aspx)
- RECIPE: [SSP](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Stack%20Smash%20Protection.aspx)
- RECIPE: [Stack Smash Protection (SSP)](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Stack%20Smash%20Protection.aspx)

# Requirement References

    ---
    foreign_id: SEC-RUN-OSC
    relation: connects
    headline: |-
      SEC-RUN-OSC
              lists compiler options to enable Object Size Checking

    source: PSB
    ---
    foreign_id: SEC-RUN-ASLR-FR1
    relation: connects
    headline: |-
      SEC-RUN-ASLR-FR1
              and other FR's list compiler options to enable Address Space Layout Randomization

    source: PSB

# History


```yaml
-----
affected_psb: SEC-HRD-BUILDOPT
impact: normative
description:  New PSB requirement setting mandatory build flags for C/C++ code.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: offerings that compile code written in C/C++ with the gcc or clang compilers
        class: LangC
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 1
    id: SEC-HRD-BUILDOPT
    issueref: ISS_SoftHosts
    tags:
    - Hardening
    - EN/PI
