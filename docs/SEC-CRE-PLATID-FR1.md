# Headline
Use a Trust Anchor Module

# Behavior

A Cisco standard Trust Anchor module (TAm) chip _MUST_ be used to store a device’s identity credentials if: 

* The hardware design is [Cisco controlled](#DEF_CiscoControlled) (i.e., it’s not OEM hardware), and 
* the offering can physically accommodate a Cisco TAm chip, and 
* the offering can accommodate the cost of a Cisco TAm solution 

Non-TAm chip credential storage solutions _MAY_ be used only if the above criteria cannot be met.

Approved TAm chips include Aikido, Cisco TPM, ACT-2 and successors.

# History
```yaml
-----
created: SEC-CRE-PLATID
description:  New requirement for platform/device hardware trust requirements

```

# Attributes

    id: SEC-CRE-PLATID-FR1
    version: 1
    category: Boot and System Integrity
    riskArea: System Integrity
    legallysensitive: false
    waivable: true
    issueref: ISS_SEC-CRE-PLATID
    applicability:
      - force: mandatory
        target:
          restrict: >
            [turnkey modules](#DEF_TurnkeyModule)
    priority: 10
    phase: requirements
    tags:
        - EN/PD
        - G7
        - PSB/OnPrem
        - Critical PSB
