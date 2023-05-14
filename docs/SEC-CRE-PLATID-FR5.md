# Headline
Remote Device Identity Verification 

(was SEC-CRE-IDFORM-FR3)


# Behavior
[Standalone devices](#DEF_StandaloneDevice) _MUST_ provide a cryptographic means of using the device identity certificate and credential to remotely verify the identity of the device, and that of all installed sub-modules that are required to have a device identity certificate and credential. 

Multi-device solutions _SHOULD_ use this cryptographic verification means to authenticate and, where applicable, authorize standalone device identity. Examples include wireless LAN controllers authenticating access points, communications managers authenticating phones, and management applications authenticating routers and switches. 

# Normative References 

* Platform Identity and Boot Integrity Visibility Architecture, [EDCS-1497588](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1497588&ver=LATEST)
* Next-Generation Trust Anchor Technology Attestation Functional Specification, [EDCS-1543500](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1543500&ver=LATEST) 


# History
```yaml
-----
created: SEC-CRE-PLATID
description:  New requirement for platform/device hardware trust requirements
-----

affected_psb: SEC-CRE-IDFORM-FR3
description:  merged into this FR 

```

# Attributes

    id: SEC-CRE-PLATID-FR5
    version: 1
    category: Boot and System Integrity
    riskArea: System Integrity
    legallysensitive: false
    waivable: true
    issueref: ISS_SEC-CRE-PLATID
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
