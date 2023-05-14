# Headline
Cisco controlled Packaging Systems

# Behavior

In any [Cisco controlled](#DEF_CiscoControlled) packaging system:

1.  Every [package](#DEF_Package) file _MUST_ have its own digital signature,
    which _MUST_ be embedded as an integral part of that package. This
    applies regardless of whether additional signatures or other
    validation information are included in module or repository
    manifests.

2.  Every package file _MUST_ include its basic identifying information
    as part of its contents.

3.  Any change whatsoever to the contents of any package file _MUST_
    invalidate its signature. This includes changes to headers,
    trailers, or other "irrelevant" metadata.

    This applies only to data embedded in package files; the signature
    need not protect "external" metadata such as the names of the
    package files themselves.

4.  Because package filenames are not necessarily protected, every
    [manifest](#DEF_Manifest)
    referring to any package _MUST_ provide information that can be used to
    verify that a package file is the intended one using only information
    which is embedded in the package itself, *without reference* to the 
    unprotected filename.

    For example, the manifest might include a cryptographic hash of the
    entire package, or the package might contain *embedded, signed* name
    and version information that could be compared with the name and
    version given in the manifest.

5.  Every manifest _MUST_ contain its own basic identifying
    information.

6.  Every manifest _MUST_ be signed, whether as an independent object,
    by signing a package containing that manifest, or both.

7.  Every manifest _MUST_ include unique identifying information for
    every module, every package, and every other manifest to which it
    refers. This unique identifying information _MUST_ be included
    under the signatures of the identified items themselves.

8.  Every manifest _SHOULD_ include a cryptographic digest of the
    entire contents of every package or other external data object to
    which it refers.
    
# History

```yaml
-----
affected_psb: SEC-SW-SIG-4
---
impact: normative
description: >
  Added "Code Signing Keys" FR5
  Added "Cisco controlled Packaging Systems" FR6
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
    id: SEC-SW-SIG-FR6
    issueref: ISS_SEC-SW-SIG
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
    - FAST
