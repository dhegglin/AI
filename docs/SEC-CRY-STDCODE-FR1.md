# Headline
Cisco Common Cryptography Modules (C3M)

# Behavior
If there is a released and supported [Cisco common cryptography module (C3M)](https://cisco.sharepoint.com/Sites/CommonSecurityModules)
that has bindings for your programming language(s) and supports a
needed [cryptographic](#DEF_Cryptography) function in your
[code](#DEF_Code), then you _SHOULD_ develop using that module. 

Cisco's own IC2M library is also approved as a VPN crypto implementation for 
Cisco's routing platforms. It is grandfathered in as it pre-existed any 
C3M modules. 

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
    id: SEC-CRY-STDCODE-FR1
    issueref: ISS_SEC-CRY-STDCODE
    tags:
    - EN/PI
    - CloudCritical
    - G7
    - Critical PSB
    - PSB/OnPrem
