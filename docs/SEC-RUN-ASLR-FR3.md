# Headline
ASLR Can Not be Disabled

# Behavior

The system _MUST NOT_ allow unauthorized configuration to disable the randomization of one or more of the segments of any of the programs or the kernel. If such a configuration change is absolutely necessary, it _MUST_ be done by an authorized user and the change _MUST_ be logged.

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
    id: SEC-RUN-ASLR-FR3
    issueref: ISS_SEC-RUN-ASLR
    tags:
    - EN/PD
    - EN/PI
    - G7
    - PSB/OnPrem
    - RTD
    - FAST
