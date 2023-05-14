# Headline

Encrypt sensitive customer data at rest.

# Key Benefits

When enterprises and individuals are using hosted solutions, i.e.
maintaining data in a cloud environment, protection of certain types of
information or data at rest, can be [critical](#DEF_Critical).
Information of greatest risk would include customer confidential
information (e.g. company secrets, intellectual properties) and/or
[sensitive](#DEF_Sensitive) information (e.g. personal identifiable
information, [sensitive](#DEF_Sensitive) personal information).
Inappropriate information disclosure could potentially result in
multiple detrimental impacts to a data owner or a company's reputation
and financial standing. Encryption of customer data is one of the main
[security](#DEF_Security) controls that can provide a strong method of
protection of customer information.

# Description

Hosted service _MUST_ provide encryption of sensitive customer data at
rest. Encryption of all types of customer data is recommended.

# Behavior

Hosted service _MUST_ provide capability to encrypt customer data at
rest (on disk/storage/volume/database). Where data encryption is not
possible (e.g. ElasticSearch), volumen and/or database encryption with
data protection layers _MUST_ be utilized. Maintain
records/configurators to show how encryption is being used.

Encryption _MUST_ be combined with strong key management as per
[SEC-OPS-KEYMGMT](#SEC-OPS-KEYMGMT) and
[SEC-DAT-KEYMGMT](#SEC-DAT-KEYMGMT)

Data encryption _SHOULD_ be done with a unique encryption key per
customer.

The preferred encryption solution _SHOULD_ include a model where a
client side or a hybrid key management is used.

# Informative References

RECIPE: [Centralized Key and Secret Management](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Centralized%20Key%20and%20Secret%20Management.aspx)


# History

pm4_filehist

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Cloud Offers
        class: ServiceThing_OR_MobileApp
    category: Privacy and Data Security
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 3
    id: SEC-OPS-RESTCRYP
    issueref: ISS_DataMishandled
    tags:
    - CloudCritical
    - Cloud
