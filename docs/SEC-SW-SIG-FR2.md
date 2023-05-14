# Headline
Native Signature Formats

# Behavior

If the package or repository format in which the code is
being distributed has a native format for signing, that feature _MUST_
be used in accordance with the standard and best practices for the format.
This requirement calls these "native signatures".

Examples of native signatures are the hashing utility of Java JAR files, ZIP files,
and the hash found with RedHat package managers, as a few examples.

# History

```yaml
-----
affected_psb: SEC-SW-SIG-3
---
impact: nonnormative
description: >
  Break into discrete FR's
-----
affected_psb: SEC-SW-SIG-3
---
impact: normative
description: >
  Add requirements for loadtime signature checks.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        class: 
        restrict: |-
          product code
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 5
    id: SEC-SW-SIG-FR2
    issueref: ISS_SEC-SW-SIG
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
    - FAST
