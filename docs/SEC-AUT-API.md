# Headline

Use authentication and authorization to protect the offering's API services

# Description

The audience for this PSB is the development team of a hosted API. With APIs, applications communicate between each other without any user knowledge or intervention. While APIs provide interoperability between computer systems on a network, we are increasing our adversaries' attack surface as we expose API on our services and products. It is important to develop hosted APIs with authentication and authorization protocols in place to lessen this attack surface.

The term "hosted" includes the following scenarios:

- APIs hosted directly on an end device/appliance for public consumption.  This includes routers, switches, firewalls and the APIs may be public or private
- Public and private APIs hosted on a cloud service XaaS.  These APIs may be consumed by applications, other cloud services, or devices.

# Behavior

For any form of authentication towards an API that is considered confidential or highly confidential, strong authentication _MUST_ be implemented.

## SEC-AUT-API-FR1: General

All hosted API resources (web-services) that accept client application connections _MUST_ use authentication and authorization to protect API functionality and accessed data commensurate to the data sensitivity made available by the API.

Highly sensitive APIs _SHOULD_ be designed to be consumable only by humans using MFA as specified in SEC-CRE-MULTIFAC.

Authentication methods depends on the data sensitivity accessed by the API:

-   Public:  No authentication (product data sheet API)
-   Confidential and Highly Confidential:  Strong authentication (API for customer data)
-   Restricted:  Use Multi-factor authentication (API for password change)

Provided APIs _SHOULD_ follow Common Standard Authorization Protocol.

## SEC-AUT-API-FR2:  Default Deny

[Access](#DEF_Access) _MUST_ be explicitly granted to specific user roles. As part of least privilege doctrine, [default](#DEF_Default) permission _MUST_ be denied.

## SEC-AUT-API-FR3: Authentication (Condition: Restrict:Enterprise)

You _MUST_ provide some form of authentication to the resource API.
For a client application that has **a human present at runtime**, you _SHOULD_ integrate Cisco's PingFederate Single Sign-On SSO infrastructure and Cisco's [OAuth2](https://oauth.net/2/) authorization infrastructure into the API.  For more information, please [open a case](https://disco.cisco.com/).

For "Machine to Machine" client applications where **no human is present at runtime** you _MAY_ use these alternate authentication techniques in preference order:

* TLS Mutual Authentication (also known as 2way-SSL)
* Digest Authentication
* Basic Authentication (use a Cisco GenericID from the Cisco GenericID forest) - ONLY for APIs that are non-Internet/non-Externet accessible.
  * GenericID passwords must comply with Cisco password strength, rotation, and history requirements.
* Token or Bearer Token may be used to authenticate clients.

A good guide to follow is the Cisco [DevNet Security Guide](https://apistyleguide.cisco.com/#!security).

## SEC-AUT-API-FR4: Authorization (Condition: Restrict:Enterprise)

You _MUST_ provide some form of authorization/permissions to the resource API. You _SHOULD_ integrate Cisco's PingFederate for [OAuth2](https://oauth.net/2/) or SAMLv2 authorization infrastructure.

For "Machine to Machine" client applications where **no human is present at runtime** you _MAY_ use local authoization via Role Based Access Control (RBAC) as needed.

## SEC-AUT-API-FR5: Network Zone Trust Boundary (Condition: Restrict:Enterprise)

If the client application's traffic crosses a network zone trust boundary to reach the resource API, an offering that includes the API _MUST_ use one of Cisco's API gateway services. API gateways are a reverse proxy and act as the control and inspection point in the API authorization check.

# History

```yaml
-----
affected_psb: SEC-AUT-API-3
description:  Aggregated related requirements into functional requirements.
---
deprecated_psb: WEB-ACCBYURL
impact: normative
headline: >
  [SEC-WEB-ACCBYURL](#SEC-WEB-ACCBYURL) Collapsing requirement to FR5
---
deprecated_psb: SEC-CRE-PRIV
impact: non-normative
headline: >
  [SEC-CRE-PRIV](#SEC-CRE-PRIV) Collapsed duplicate requirement.
---
```

# Requirement References

```
---
source: PSB
foreign_id: SEC-WEB-ID
relation: connects
headline: >
    [SEC-WEB-ID](#SEC-WEB-ID) Use secure session IDs/tokens
---
source: PSB
foreign_id: SEC-HTP-HSTS
relation: connects
headline: >
    [SEC-HTP-HSTS](#SEC-HTP-HSTS) Force encryption and authentication using HTTPS
---
source: PSB
foreign_id: SEC-CRE-MULTIFAC
relation: connects
headline: |-
  SEC-CRE-MULTIFAC specifies the authentication required for administrative access.
```

# Informative References

[OWASP Session Management Cheat Sheet](https://www.owasp.org/index.php/Session_Management_Cheat_Sheet)

# Attributes

    id: SEC-AUT-API
    version: 3
    issueref: ISS_PrivAccesAcct
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
          class: HasWebUi_OR_ProtoHttp
          restrict: >
            Cisco Enterprise Offerings and Web Applications and Services
    priority: 9
    phase: requirements
    tags:
    - CloudCritical
    - PSB/OnPrem
    - Cloud
