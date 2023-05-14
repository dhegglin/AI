# Headline
Adaptation Layers and C3M

# Behavior

If you are writing [code](#DEF_Code) in a programming language that
is not directly supported by C3M, but there's a commonly used, currently
maintained adaptation layer for an API supported by C3M, then an [offering](#DEF_Offering)
_SHOULD_ use the adaptation layer and the [C3M module](https://cisco.sharepoint.com/Sites/CommonSecurityModules).

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
    id: SEC-CRY-STDCODE-FR2
    issueref: ISS_SEC-CRY-STDCODE
    tags:
    - EN/PI
    - CloudCritical
    - G7
    - Critical PSB
    - PSB/OnPrem
