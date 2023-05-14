# Headline

Support SNMPv3 with cryptographic encryption and authentication.

# Behavior

## SEC-CRY-SNMP-FR1: SNMPv3 support

If an offering supports any version of SNMP, it _MUST_
support SNMPv3.

## SEC-CRY-SNMP-FR2: SNMPv3 encryption and authentication support

SNMPv3 encryption and authentication _MUST_ also be supported.

# Normative References

- RFC3414, User-based Security Model (USM) for version 3 of the Simple
Network [administration](#DEF_Administrator) Protocol (SNMPv3)
- [Server Security Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1411758&ver=approved)
- [Cryptographic Implementation Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806752&ver=approved)

# Informative References

EDCS-278331, IOS SNMPv3 AES Encryption PRD

# History

```yaml
-----
affected_psb: SEC-CRY-SNMP
---
deprecated_psb: SEC-SNM-AES
impact: non-normative
headline: >
  SEC-SNM-AES consolidated in SEC-CRY-SNMP-FR1
---
deprecated_psb: SEC-SNM-SHA96
impact: non-normative
headline: >
  SEC-SNM-AES consolidated in SEC-CRY-SNMP-FR2
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
                      SNMP implementations
    category: Cryptographic Support
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 1
    id: SEC-CRY-SNMP
    issueref: ISS_WeakSNMP
    tags:
    - EN/PI
    - PSB/OnPrem
    - FAST
