# Headline
TLS 1.0 and TLS 1.1

# Behavior

TLS 1.1 _MAY_ be supported, but it _SHOULD NOT_ be enabled by default. Offers that currently have it enabled should consider disabling TLS 1.1 by default carefully to prevent inadvertent outages with peers that only support 1.1.  

TLS 1.0 _MAY_ be supported, but it _MUST NOT_ be enabled by default.

**Exception**: When an [external constraint](#DEF_ExternalConstraint) requires it, TLS 1.0 _MAY_ be enabled by default, but only when communicating with particular types of peers specifically known to require TLS 1.0. 

**Supplemental Guidance**: Readers should note that [RFC8996](https://tools.ietf.org/html/rfc8996) deprecated both TLS 1.0 and 1.1 in March 2021.
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
    id: SEC-TLS-CURR-FR2
    issueref: ISS_SEC-TLS-CURR
    tags:
    - EN/PI
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
    - FAST
