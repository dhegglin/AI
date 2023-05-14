# Headline

Externally Generated Key Copy Encryption 

(was SEC-CRE-CHIPID-FR9)

# Behavior

If the [device identity](#DEF_DeviceIdentity) key is generated outside of the
[turnkey module](#DEF_TurnkeyModule) or TAm chip that will
ultimately store that key in the finished device, then all copies of
an externally generated key _MUST_ be encrypted (using
[good cryptography](#DEF_GoodCryptography)) or stored in
[controlled space](#DEF_ControlledSpace) at all times from
generation to installation in the chip.

The protections on such controlled space _MUST NOT_
[trust](#DEF_Trust) any [policy entity](#DEF_PolicyEntity) not
under Cisco's direct control and supervision.

# Normative References

* [Cisco Cryptographic Controls Policy](https://policy.cisco.com/cppc/policy-advisor/policies/view-policy/1818)

# Attributes

    id: SEC-CRE-PROVID-FR2
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
    priority: 10
    phase: requirements
    tags:
        - EN/PD
        - G7
        - Critical PSB
        - PSB/OnPrem
