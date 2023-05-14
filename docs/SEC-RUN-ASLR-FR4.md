# Headline
Do Not Leak Addresses

# Behavior

A memory leak that references a memory location defeats ASLR. The system _MUST NOT_ leak the address of any memory sections through debugging, logs, or other operations. This includes the memory locations of code and kernel data, programs, and libraries.

# History

```yaml
-----
affected_psb: SEC-RUN-ASLR
description:  Update to discrete FR's, reduced priority to 8 (mandatory)
-----
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          Loaders
                      for object files,
                      including, but not limited to,
                      boot loaders and loaders provided with operating systems.
        class: not_HwComp
    - force: mandatory
      target:
        restrict: |-

                      Object files and other machine code

    - force: mandatory
      target:
        restrict: |-

                      Linkers and other programs creating
                      object files
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 3
    id: SEC-RUN-ASLR-FR4
    issueref: ISS_SEC-RUN-ASLR
    tags:
    - EN/PD
    - EN/PI
    - G7
    - PSB/OnPrem
    - RTD
    - FAST
