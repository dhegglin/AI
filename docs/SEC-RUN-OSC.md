# Headline

Use object size checking to detect buffer overflow.

# Description

Buffer overflow is one of the most common attack vectors. A buffer overflow condition exists when a program attempts to put more data in a buffer than it can hold or when a program attempts to put data in a memory area past an allocated buffer boundary. Writing outside the bounds of a block of allocated memory can corrupt data, crash the program, and even enable execution of malicious code. This PSB requires you to use compiler built-in bounds checking to catch and reduce buffer overflows at both compile and run time.

# Behavior

## SEC-RUN-OSC-FR1: Build with object size checking

You _MUST_ build your C and C++ code using either--

1.  the headers and library described in the [OSC Implementation
    Guide](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1482500&ver=latest) using one of the compilers supported by those headers and that library, OR

2.  a "FORTIFY_SOURCE" macro provided with your compiler

While you _MUST_ build your code using one of the two, you _SHOULD_ prefer the Cisco OSC headers and library over generic FORTIFY_SOURCE.

If your C or C++ code can't be built using the above protections, then you _MUST_ modify your code to be buildable using them.

For third-party code, if you can not recompile from source, you _MUST_ choose a version that has been built with FORTIFY_SOURCE.

# Informative References

RECIPE: [Object Size Checking (OSC)](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Object%20Size%20Checking%20(OSC).aspx)


# Normative References

Built-In Object Size Checking Implementation Guide\
[EDCS-1482500](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1482500&ver=latest)

# Requirement References

    ---
    foreign_id: SEC-RUN-ASLR-FR1
    relation: connects
    headline: |-
      SEC-RUN-ASLR-FR1 and other FR's requires you to
              randomize the address space of
              your programs, making most machine code injection
              vulnerabilities harder to exploit.

    source: PSB
    ---
    foreign_id: SEC-RUN-SAFEC
    relation: connects
    headline: |-
      SEC-RUN-SAFEC requires you to
              prefer certain C routines over others to reduce the chance
              of buffer overflows.

    source: PSB
    ---
    foreign_id: SEC-RUN-XSPACE
    relation: connects
    headline: |-
      SEC-RUN-XSPACE requires you to
              avoid memory segments which are writable and executable at the
              same time, making some machine code injection vulnerabilities
              harder to exploit.

    source: PSB

# History

```yaml
-----
affected_psb: SEC-RUN-OSC
impact: non-normative
description:  Minor updates.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
          Cisco controlled
                      software written in C or C++

        class: LangC
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 3
    id: SEC-RUN-OSC
    issueref: ISS_Inject
    tags:
    - EN/PD
    - G7
    - Critical PSB
    - RTD
    - PSB/OnPrem
    - Cloud
