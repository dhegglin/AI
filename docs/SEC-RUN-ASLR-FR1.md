# Headline
Randomize Memory Segments

# Behavior

In this requirement, "randomizable segments" include all segments in the virtual memory of a program that contain executable code, data initialized from or mapped to the contents of object files, uninitialized data space for general program use, stacks, or heaps.

New random addresses _MUST_ be generated for these randomizable segments each time that a program, a task, or a thread is loaded and each time that a shared object file or segment is mapped.

The memory location of the kernal _MUST_ be randomized whenever the system is rebooted and the kernel is reloaded.

A boot loader, including shim in secure boot mode, that operates only before a long-term resident kernel or operating system that has been loaded _MAY_ not be randomizable. This boot loader _MUST_ cease to provide executable code or affect the execution flow before loading is complete and _MUST NOT_ act as a network element or process data from outside of the bounded computer being initialized. This exception applies only to the code of the boot loader itself.

Addresses _MUST_ be randomized in all code and data left resident when the system enters normal operation.

# History

```yaml
-----
affected_psb: SEC-RUN-ASLR
description:  Update to discrete FR's
-----
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
          Loaders
                      for object files,
                      including, but not limited to,
                      boot loaders and loaders provided with operating systems.
    - force: mandatory
      target:
        restrict: |-

                      Object files and other machine code

    - force: mandatory
      target:
        restrict: |-

                      Linkers and other programs creating
                      object files
        class: not_HwComp
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 3
    id: SEC-RUN-ASLR-FR1
    issueref: ISS_SEC-RUN-ASLR
    tags:
    - EN/PD
    - EN/PI
    - G7
    - Critical PSB
    - PSB/OnPrem
    - RTD
    - FAST
