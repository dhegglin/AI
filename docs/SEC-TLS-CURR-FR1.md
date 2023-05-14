# Headline
TLS 1.2 and TLS 1.3

# Behavior

The [offering](#DEF_Offering) _MUST_ support TLS version 1.2. It _MAY_ also support TLS 1.3. 

Any of 1.2, 1.3 _MAY_ be enabled by default, with 1.2 being the recommended but not mandatory version. 

# History

```yaml
-----
affected_psb: SEC-TLS-CURR
description:  Updated to functional requirements. 

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
                      TLS implementations
        class: not_HwComp
    category: Cryptographic Support
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 6
    id: SEC-TLS-CURR-FR1
    issueref: ISS_SEC-TLS-CURR
    tags:
    - EN/PI
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
    - FAST
