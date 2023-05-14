# Headline
SEC-HW-PLATID-FR6: CPU-to-Chip Bus Protection 

(was SEC-CRE-CHIPID-FR11)

# Behavior
Attackers can place implants on the PCB that capture communication with the chip that provides device identity. The lost integrity of communication allows the implant to spoof the identity at a later step in the boot process.

Communication with the chip _SHOULD_ be authenticated. If supported, authentication _MUST_ take place with each interaction.

If communication with the chip includes [critical](#DEF_Critical) data, then that communication _MUST_ be encrypted if the chip supports it.

# Informative References

* [Aikido Bus Encryption Wiki](https://wiki.cisco.com/display/TAMAIKIDO/Aikido+Bus+Encryption)
* [TPM Bus Protection Wiki](https://wiki.cisco.com/display/TAMAIKIDO/TPM+Bus+Protection)

# History
```yaml
-----
created: SEC-CRE-PLATID
description:  New requirement for platform/device hardware trust requirements
-----

affected_psb: SEC-CRE-CHIPID-FR11
description:  merged into this FR 

```

# Attributes

    id: SEC-CRE-PLATID-FR6
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
    priority: 8
    phase: requirements
    tags:
        - EN/PD
        - G7
        - PSB/OnPrem
