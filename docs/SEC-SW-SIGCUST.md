# Headline

Allow customers to sign software

# Description

Every system _SHOULD_ let customers choose the software they want to
accept and mark it with their own digital signatures. [Open](#DEF_Open)
systems _MUST_ do this, since customers are the only source of
legitimacy for the software they choose to run.

# Behavior

## SEC-SW-SIGCUST-FR1: Permit Customer Signatures

The signing and verification systems used for affected [code](#DEF_Code)
_MUST_ permit customers to attach their own digital signatures to each
installable package.

## SEC-SW-SIGCUST-FR2: Use Open Source Tools

This _SHOULD_ be done with standard open-source tools; if not,
appropriate tools and documentation _MUST_ be made available to
customers.

## SEC-SW-SIGCUST-FR3: Preserve Cisco Signature

It _SHOULD_ be possible to attach a customer signature in addition
to any Cisco signature, without removing or invalidating the Cisco
signature.

## SEC-SW-SIGCUST-FR4: Check Both Signatures

It _MUST_ be possible to configure all signature-verifying
[loaders](#DEF_Loader) and INSTALLERS which handle the affected
[code](#DEF_Code) to check customer signatures. It _SHOULD_ be
possible to check both Cisco signatures and customer signatures.

## SEC-SW-SIGCUST-FR5: Customer Signature Root of Trust

It _MUST_ be possible to configure at least one
customer-administered root of trust for verifying customer
signatures. This _MUST_ _NOT_ affect the root of trust used for any
verification of Cisco signatures.

# History

```yaml
-----
affected_psb: SEC-SW-SIGCUST
description:  Updated to functional requirements. 

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          opencode
                      for standalone devices,
                      except for configuration files.

    - force: recommended
      target:
        restrict: |-
          code
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 1
    id: SEC-SW-SIGCUST
    issueref: ISS_RandomCode
    tags:
    - EN/PI
    - PSB/OnPrem
    - FAST
    - EN/PI DT
