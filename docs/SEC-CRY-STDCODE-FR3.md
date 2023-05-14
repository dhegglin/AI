# Headline
Third-Party Libraries

# Behavior

If there is no usable C3M module, then you _MUST_ use a mature, widely
used, maintained third-party library, preferably an open-source one from
the [approved list](https://wwwin-github.cisco.com/CSDL/PSB/blob/master/normative-external/crypto-implementations.md). A mature, widely used library is one that has seen multiple adopters that have integrated it in applications and/or operating systems. Examples could include OpenSSL or GoLang. A maintained library is one that sees a new maintainance release at least once a year and provides critical vulnerability fixes in a timely fashion.

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
    version: 3
    id: SEC-CRY-STDCODE-FR3
    issueref: ISS_SEC-CRY-STDCODE
    tags:
    - EN/PI
    - CloudCritical
    - G7
    - Critical PSB
    - PSB/OnPrem
