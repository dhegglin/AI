# Headline 
Memory Interface Attacks from Compromised Interface Cards

(was SEC-SW-BASECONT-FR1)

# Behavior

In the specific case of [base software](#DEF_BaseSoftware), the following requirements apply to the
perimeter analysis for this [controlled](#DEF_ControlledSpace)
[execution space](#DEF_ExecutionSpace).

**Via DMA:**

Memory interfaces _SHOULD NOT_ be enabled until after the execution of
base code to prevent attacks to the base execution space.

**Via I2C, SPI, or similar abuses to rewrite configuration data (such as IDPROM or boot flags) or software memories:**

Interfaces to persistent storage of configuration data (IDPROM, boot flags, etc.)
and software _SHOULD_ only be accessible by components requiring it.

Boot behavior _SHOULD_ be based on the identity (PID) contained in
the SUDI certificate since boot behavior can be influenced by the
identity of the hardware offering (number of active ports,
performance level, etc.). If an alternate source of PID
information is used by base code, per [SEC-CRE-IDFORM-4](#SEC-CRE-IDFORM-4), that PID _MUST_ first be
verified to match what is held in the SUDI certificate.

# History

```yaml
-----
Deprecated_psb: SEC-SW-BASECONT-FR1
---
impact: nonnormative
description: >
  Break into discrete FR's

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        class: 
        restrict: |-
          product code
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 1
    id: SEC-SW-BASEPROT-FR7
    issueref: ISS_SEC-SW-BASEPROT
    tags:
    - EN/PD
    - G7
    - Image Signing
    - PSB/OnPrem
