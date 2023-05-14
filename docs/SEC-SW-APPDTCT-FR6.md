# Headline 
Load Verification Trust Chain for Closed Code

(was SEC-SW-LOADCHK-FR9)

# Behavior
The load verification chain for closed code _MUST_ only allow closed code to be trusted at any point.

This implies that any loader dealing with closed code _MUST_ itself be closed, and in fact that every enclosing [executor](#DEF_Executor) of closed code _MUST_ be closed. This is only possible with an unbroken chain of closed loaders and other executors starting with stage zero base software supplied with closed hardware. This demand used to be a standalone PSB requirement called SEC-SW-CLOSURE.

Note that in some offerings (e.g., non-Cisco controlled hardware or hypervisors), portions of the trust chain may be controlled by entities other than Cisco. In that case, the offering _MUST_ provide a complete trust chain for what is being delivered with everything needed by the loading entity to complete the trust chain in their execution space. For example, a Virtual Machine offering may include components of UEFI Secure Boot that are verified by a public key residing in firmware that is not under Cisco control.

**Supplemental Guidance:** [SEC-SW-BASEDTCT](#SEC-SW-BASEDTCT) applies additional rules for base software.



# History

```yaml
-----
Deprecated_psb: SEC-SW-LOADCHK-FR9
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
          product [closed](#DEF_Closed) code
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 1
    id: SEC-SW-APPDTCT-FR6
    issueref: ISS_SEC-SW-APPDTCT
    tags:
    - EN/PD
    - EN/PI
    - G7
    - Image Signing
    - PSB/OnPrem
