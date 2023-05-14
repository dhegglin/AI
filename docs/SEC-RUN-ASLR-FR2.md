# Headline
Randomization Entropy

# Behavior

The randomization of each randomizable segment _MUST_ ensure that the address at which each segment is loaded has at least 8 bits of unpredictability. It _SHOULD_ be more; the limit is low to accommodate certain limitations in 32-bit address spaces, and more is possible in 64-bit spaces. See [SEC-CRY-RANDOM](https://wwwin-github.cisco.com/CSDL/PSB/blob/dev/markdown/requirements/SEC-CRY-RANDOM.md) for detailed requirements on unpredictability.

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
    id: SEC-RUN-ASLR-FR2
    issueref: ISS_SEC-RUN-ASLR
    tags:
    - EN/PD
    - EN/PI
    - G7
    - Critical PSB
    - PSB/OnPrem
    - RTD
    - FAST
