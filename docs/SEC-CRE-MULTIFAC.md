# Headline

All remote administrator access requires multi-factor authentication

# Description

[Access](#DEF_Access) is often required for [critical](#DEF_Critical) application services, such as release, troubleshooting, support and integration. This requirement is especially the case for [administrators](#DEF_Administrator) who are working off-site or for customer integrations requiring [access](#DEF_Access) to [sensitive](#DEF_Sensitive) systems.  

Compromise of these systems could have significant financial, business and reputational impact and thus poses a higher risk to the enterprise. For this reason, additional protection is required to prevent unauthorized [access](#DEF_Access).

Multi-factor [authentication](#DEF_Authentication) provides an extra layer of protection to ensure that a specific administrative user is truly the one who is allowed to [access](#DEF_Access) a [sensitive](#DEF_Sensitive) systems and infrastructure.

Multi-factor authentication involves a multi stage verification process of user identity prior to granting access. The factors are listed here:

-   A knowledge factor, such as knowledge of a password or passphrase.
-   Based on the possession of some item. For example, the possession of a security token such as a hardware token, authentication token, USB token, cryptographic token, or key fob would qualify for the possession factor.
-   Something you are such as biometrics.
-   Location such as based on IP address.

# Behavior

Provide secure remote authentication.  The scope is limited to Human to machine interaction. Machine to machine and programmatic API access is handled in SEC-AUT-API.

## SEC-CRE-MULTIFAC-FR1:  Administrative Access

Multi-factor authentication is to be used for all external administrator access to Cisco XaaS offerings.

Required for administrative tasks and restricted APIs for Cisco administrative access.  Restricted APIs give the ability to alter the infrastructure or service, this could be from Cisco, or an admin from the customer deployment.

The MFA options listed _SHOULD_ be provided to customers.  

Multi-factor [authentication](#DEF_Authentication) _MUST_ be used for all external [administrator](#DEF_Administrator) [access](#DEF_Access) to Cisco XaaS offering.  [Security](#DEF_Security) tokens such as hardware tokens, [authentication](#DEF_Authentication) tokens, USB tokens, cryptographic software tokens and digital certificates _SHOULD_ be used for [remote](#DEF_Remote) [access](#DEF_Access) in addition to [standard](#DEF_Standard) userid/password [authentication](#DEF_Authentication) options.  

Customers and all other parties requiring administrative access _SHOULD_ be provided with [security](#DEF_Security) tokens as necessary.

In cases where programmatic access is required for restricted APIs, follow the requirements listed in SEC-AUT-API.

## SEC-CRE-MULTIFAC-FR2:  Attribution

Shared accounts _MUST_ be avoided in order to provide attribution to all activities.

Multiple users access shared accounts which makes monitoring and creating an audit trail difficult or impossible.  There is also minimal accountability for shared accounts as users do what they want.  As such, they often times don't feel accountable for the security of the account and will do things that they don't do with their own personal account

With a shared account, the password can not be changed without coordinating the change with everyone that uses the account so that his or her access is not impacted.  This also requires that the password be distributed in a secure manner.

# Informative References
* RECIPE: [Multi-Factor Authentication](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Multifactor%20Authentication.aspx)
* [NIST 800-53](https://nvd.nist.gov/download/800-53/800-53-controls.xml)
* https://www.sans.org/reading-room/whitepapers/basics/administration-shared-accounts-1271

# Requirement References

    ---
    foreign_id: SEC-AUT-API
    relation: connects
    headline: |-
      SEC-AUT-API Specifies authentication requirements for APIs
    
    targets:
    - offerings
    source: PSB

# History
```yaml
-----
affected_psb: SEC-CRE-MULTIFAC-3
description:  Updated to functional requirements. 
-----
deprecated_psb: SEC-CRE-MULTIFAC-2
impact: normative
headline: >
  [SEC-CRE-MULTIFAC-2](#SEC-CRE-MULTIFAC-2) migrated to functional requirements.  Generic users forbidden for administrative access.
---
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 9
    applicability:
    - force: mandatory
      target:
        restrict: Cloud Offers
        class: not_DataConfidential
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    waivable: true
    version: 3
    id: SEC-CRE-MULTIFAC
    issueref: ISS_BadPws
    tags:
    - CloudCritical
    - Cloud
