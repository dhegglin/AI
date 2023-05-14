# Headline

Audit and Authorize Identity Provisioning (new)

# Behavior

Device identity (certificate and credential) provisioning _MUST_ be performed with infrastructure that authorizes the manufacturing site for the identity being requested. All provisioning occurrences _MUST_ be audited. 

# Informative References 

* [Cryptographic Services Offerings](https://cswiki.cisco.com/pages/viewpage.action?pageId=72943510)


# Attributes

    id: SEC-CRE-PROVID-FR1
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
    priority: 8
    phase: requirements
    tags:
        - EN/PD
        - G7
        - PSB/OnPrem
