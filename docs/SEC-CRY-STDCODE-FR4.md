# Headline
Cisco Cryptographic Specialists

# Behavior
If there is no third-party library available, then you _MUST_ engage Cisco cryptographic
specialists *before* you begin the design or development of any
[cryptographic](#DEF_Cryptography) code or implementation. You
_MUST NOT_ develop cryptographic code without the approval and direct
participation of at least one cryptographic specialist. One or more
cryptographic specialists _MUST_ have final authority over all
architecture and implementation decisions. For the purposes of this
requirement, a "cryptographic specialist" is a person who has at least
one of the following qualifications:

1.  Has at least one year of at least 50 percent concentration on
    cryptographic architecture or implementation, working with or
    supervised by other cryptographic specialists, *not* including any
    experience on the immediate project in question. Has a continuing
    cryptographic architecture or implementation role inside Cisco.
2.  Has a university degree with a specific concentration in
    cryptography, including research or coursework involving the actual
    design or implementation of cryptography.
3.  Has been a contributing author of adopted cryptography standards or
    peer-reviewed academic publications regarding cryptography.
4.  Has been explicitly found qualified by the leadership of Cisco's
    common security modules program.

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
    id: SEC-CRY-STDCODE-FR4
    issueref: ISS_SEC-CRY-STDCODE
    tags:
    - EN/PI
    - CloudCritical
    - G7
    - Critical PSB
    - PSB/OnPrem
