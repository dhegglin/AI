# Headline

Mutually exclude segment write and execute

# Description

XSPACE is one of the most important security protection techniques that ensures execution and writing permissions are mutually exclusive for all memory segments. This security feature prevents inadvertent execution of code from unauthorized areas and prohibits writing code over executable areas. In the industry, XSPACE is also referred to as NX bit, XD bit, DEP etc.

# Behavior

## SEC-RUN-XSPACE-FR1: Hardware

Each CPU that is part of a Cisco Offering, include those in line cards or other embedded bounded computer, or an associated MMU, MUST be capable of enforcing that memory segments not be simultaneously writable and executable from within the same machine code execution space.

## SEC-RUN-XSPACE-FR2: Operating Systems/Loaders
When loading any object file in a format that supports marking segments to be non-writable or non-executable, every
loader MUST honor all such instructions. "Loaders" include boot loaders and programs that dynamically map their own libraries or other segments. When choosing the object file format(s) to be supported by any loader, always choose a format that supports such metadata (or a loader that uses such a format).

When loading an object file in a format that does not support specifying whether segments should be writable or executable,
every loader SHOULD, by default, load each segment identifiable as containing executable machine code as non-writable by the CPU, and disable CPU execution of data in writable segments, including stacks, heaps, and common segments.

Each loader MUST set up the required CPU access restrictions for every segment in a loaded file before passing control to any code in that file. Loaders are not required to prevent loaded programs from changing the writable or executable status of segments after load time.

## SEC-RUN-XSPACE-FR3: Loadable object code
This section applies to every object file provided by Cisco, and to the default attributes for every object file created by a linker or other program that is part of a Cisco offering. This also includes kernels and intermediate loader stage images. This PSB applies to all third-party software included in any offering, whether provided to Cisco in source or in object form, just as they would apply to Cisco controlled code.

To the maximum extent permitted by the object file format in use:

1.  If any segment contains machine code intended to be executed, then mark that segment to be loaded non-writable.

2.  Mark every other segment to be loaded non-executable.

3.  If any segment contains data meant neither to be modified *nor* executed, then you SHOULD mark that segment to be loaded neither writable nor executable.

4.  If the CPU and loader support machine code segments executable by the CPU, but not readable by the program itself, or readable using only specialized instructions, then you SHOULD mark each segment containing machine code for that treatment.

Except as described under "Exceptions" below, all loaded code MUST maintain these CPU access restrictions after load time. It's not acceptable for the program to load with a read-only text segment and then change that segment to be read-write, nor is it acceptable for the program to create writeable/executable segments or pages at runtime by other means.

Two exception cases as following:

An interpreter containing a dynamic "just-in-time" compiler that translates non-machine-code programs into machine code on demand at runtime MAY maintain one or more segments which are both writable and executable, subject to the following restrictions--

1)  Writable/executable segments MUST be used *only* to store machine code generated dynamically by the just-in-time compiler. All other code and data MUST be stored in other segments.
2)  Each writable/executable segment MUST be bounded above and below by areas of unmapped address space. Any attempt to write to or execute from this unmapped space MUST terminate the just-in-time compiler and all code it has created, and MUST destroy their execution space (typically by forcing a process to exit).
3) The just-in-time compiler MUST confine the code it compiles to a strongly memory-safe environment, regardless of the origin of the code.
4) Each writable/executable segment SHOULD be "double mapped", writable only using one set of CPU addresses and executable only using a different set.

The second exception case applies to boot loaders and real-mode kernel code. A boot loader, including shim in secure boot mode, operating before a long-term resident operating system kernel has been loaded and before virtual memory has been enabled, MAY be loaded as both writable and executable. Kernel code executing without virtual memory need not be protected against writing while in that mode. This does not apply to virtualized kernel code; the kernel's own virtual address space is subject to the same restrictions as the address space of user mode programs.

## SEC-RUN-XSPACE-FR4: Linkers

Except when prevented by an external constraint on a user platform, each linker or other program that createsobject files for later loading into a machine code execution space, MUST, by default, create files that comply with the requirements listed above under SEC-RUN-XSPACE-FR3.

# Informative References

RECIPE: [Executable Space Protection (XSpace)](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Executable%20Space%20Protection%20(XSpace).aspx)

[XCHECK tool](https://wwwin-github.cisco.com/Trust/xcheck)

X-Space User’s Guide,
[EDCS-665071](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-665071&ver=latest)

# Requirement References

    ---
    foreign_id: SEC-RUN-ASLR-FR1
    relation: connects
    headline: |-
      SEC-RUN-ASLR-FR1 and other FR's require you to
              randomize the address space of
              your programs, making most machine code injection
              vulnerabilities harder to exploit.

    source: PSB
    ---
    foreign_id: SEC-RUN-OSC
    relation: connects
    headline: |-
      SEC-RUN-OSC
              requires you use certain compiler
              extensions to reduce buffer overflows, and therefore
              machine code injection vulnerabilities, in C and C++
              code.

    source: PSB


# History

```yaml
-----
affected_psb: SEC-RUN-XSPACE-3
description:  Re-organize and rewrite the requirements to be more accurate and fit with required templage. Removed some ASLR/OSC related text from this PSB.
-----
deprecated_psb: SEC-RUN-XSPACE-2
impact: non-normative
description: >
  Re-organize and rewrite the requirements to be more accurate and fit with required templage. Removed some ASLR/OSC related text from this PSB.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-

                      CPUs to be used to implement network
                      protocols
    - force: mandatory
      target:
        restrict: |-
          Loaders
                      provided with or for such CPUs, including, but
                      not limited to, boot loaders and loaders
                      provided with operating systems.

    - force: mandatory
      target:
        restrict: |-

                      Machine code
                      and object files
                      to be loaded by such operating systems.

    - force: mandatory
      target:
        restrict: |-

                      Linkers and other programs creating
                      object files
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 3
    id: SEC-RUN-XSPACE
    issueref: ISS_Inject
    tags:
    - EN/PD
    - EN/PI
    - G7
    - Critical PSB
    - RTD
    - PSB/OnPrem
    - Cloud
    - FAST
