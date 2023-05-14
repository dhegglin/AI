# Headline
Random Number Generation

# Description
Comply with Cisco standards for Random Number Generation

# Behavior
Regardless of the protocol in use, an offering's random
number generation _MUST_ comply with the "Randomness" tab of the supplement
in this requirement.

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings
    category: Cryptographic Support
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 7
    id: SEC-CRY-PRIM-FR2
    issueref: ISS_SEC-CRY-PRIM
    tags:
    - EN/PI
    - CloudCritical
    - Hardening
    - Critical PSB
    - PSB/OnPrem
    - FAST
