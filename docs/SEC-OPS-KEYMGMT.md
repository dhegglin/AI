# Headline

Define procedures and responsibilities for secrets management

# Description

Provide policy, procedure, oversight, and auditing for the creation, use, protection, and retirement of credentials, keys, and other secrets.  Execute the procedures you define.

These requirements follow NIST 800-57 recommendation for Key Mangagement.

# Behavior

Define, document, follow, and audit compliance with policies and procedures for managing secrets such as [credential](#DEF_Credential) and [cryptographic secrets](#DEF_CryptographicSecret).

The documents defining your policies and procedures must identify how you satisfy all of the relevant elements required by the [Cryptographic Controls Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806748&ver=approved), the [Cryptographic Implementation Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806752&ver=approved), and the PSB requirements listed under "Related Requirements", and _MUST_

## SEC-OPS-KEYMGMT-FR1: Planning

1.  Define roles and responsibilites with regard to secrets and their management.

2.  Define classes of secrets according to their use, and define controls to keep any given secret from being used in more than one class.

3.  Describe where and how secrets are generated, installed, stored, transmitted, and used.

4.  Describe how disclosure of secrets is prevented during each of these activities.

5.  Define important events in the life cycle of each class of secret, for example creation, disclosure to new users or custodians, use of various kinds, potential compromise, deactivation, and any necessary [erasure](#DEF_Erase).

6.  Describe how the above events are detected and logged and, how the resulting logs are audited.

7.  Define systems for assuring that secrets are [unpredictable](#DEF_Unpredictability) enough to meet all applicable PSB requirements, other Cisco policies, standard practices, and application-specific strength requirements.

8.  Identify how credentials are revoked or invalidated, and how information about their current validity is communicated to the systems that rely on them for [authentication](#DEF_Authentication).

9.  Define the procedures you use to audit and verify your execution of all of the above.

## SEC-OPS-KEYMGMT-FR2: Document

Complete the "key management template" from the [Sec Ops
Playbook](https://cisco.sharepoint.com/sites/CSDLCloudOfferSecurityCom/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FCSDLCloudOfferSecurityCom%2FShared%20Documents%2FTemplates%2FOperations%20Playbooks&p=true&originalPath=aHR0cHM6Ly9jaXNjby5zaGFyZXBvaW50LmNvbS86Zjovcy9DU0RMQ2xvdWRPZmZlclNlY3VyaXR5Q29tL0VxcVJ0X1VMSG81QnRxU2dMZHJMNDVNQl9ZSzRYNlEtdUg3eXNhbDZfdEtiT1E_cnRpbWU9TWp4NWhaRDkxMGc),
using the information from the applicable parts of your policies and procedures.

# Informative References

<https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-4/final>\
<https://csrc.nist.gov/publications/detail/sp/800-57-part-2/final>\
<https://csrc.nist.gov/publications/detail/sp/800-57-part-3/rev-1/final>\
Recipe Link: [Centralized Key Management Service](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Centralized%20Key%20and%20Secret%20Management.aspx)

# Normative References

[Cryptographic Controls Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806748&ver=approved)\
[Cryptographic Implementation Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806752&ver=approved)\
[Sec Ops Playbook](https://cisco.sharepoint.com/:f:/r/sites/CSDLCloudOfferSecurityCom/Shared%20Documents/Templates/Operations%20Playbooks?csf=1&web=1&e=IMYszR)

# Requirement References

    ---
    foreign_id: SEC-DAT-KEYMGMT
    relation: connects
    headline: |-
      SEC-DAT-KEYMGMT addresses
              technical measures for handling secrets in centralized "secret
              servers", and is a companion requirement to SEC-OPS-KEYMGMT.
              The two requirements demand documentation on closely related
              subjects, and the same documentation will often satisfy parts or
              all of both.  See also the related requirements referenced in
              SEC-DAT-KEYMGMT.

    targets:
    - services
    source: PSB
    ---
    foreign_id: SEC-PWD-CONFIG
    relation: connects
    headline: |-
      SEC-PWD-CONFIG
              requires the ability to enforce a maximum
              password lifetime.

    targets:
    - passphrase databases
    source: PSB

# History

```yaml
-----
affected_psb: SEC-OPS-KEYMGMT-2
description:  Updated to functional requirements
---
deprecated_psb: SEC-OPS-KEYMGMT
impact: normative
headline: >
  [SEC-OPS-KEYMGMT](#SEC-OPS-KEYMGMT) migrated to functional requirements
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Cloud Offers
        class: not_MobileApp
    category: Authentication and Authorization
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 2
    id: SEC-OPS-KEYMGMT
    issueref: ISS_NoSecProgram
    tags:
    - CloudCritical
    - Cloud
