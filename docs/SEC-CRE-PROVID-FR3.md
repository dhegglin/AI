# Headline
Externally Generated Key Copy Erasure 

(was SEC-CRE-CHIPID-FR10)

# Behavior
If the [device identity](#DEF_DeviceIdentity) key is generated outside of the [turnkey module](#DEF_TurnkeyModule) or TAm chip that will
ultimately store that key in the finished device, then all
copies outside of the chip or device _MUST_ be [erased](#DEF_Erase)
immediately after the key is installed.

# Attributes

    id: SEC-CRE-PROVID-FR3
    version: 1
    category: Boot and System Integrity
    riskArea: System Integrity
    legallysensitive: false
    waivable: true
    issueref: ISS_SEC-CRE-PROVID
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
