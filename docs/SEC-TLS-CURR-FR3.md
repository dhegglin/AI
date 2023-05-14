# Headline
SSL 2.0 and SSL 3.0

# Behavior

SSL 2.0 and 3.0 _MUST NOT_ be supported.

**Supplemental Guidance**: This requirement makes a distinction between supported and enabled-by-default versions. A version is supported if there is a way for it to
be enabled in the offering by a configuration knob. A supported version
is not always enabled by default if the knob is not set in the default configuration. An unsupported version has no way of being enabled and used in the [offering](#DEF_Offering).


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
    id: SEC-TLS-CURR-FR3
    issueref: ISS_SEC-TLS-CURR
    tags:
    - EN/PI
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
    - FAST
