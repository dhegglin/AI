# Headline

Authenticate and authorize remote agents seeking access

# Description

Authenticate and authorize remote peers seeking access to any [target](#DEF_Target) that contains private data or resources.  Private data does not necessarily mean it is sensitive or critical, just that it is not meant to be publicly available.

[Authenticate](#DEF_Authentication) the peer first, then ensure the peer is [authorized](#DEF_Authorization) to access the data or resource.

# Behavior

## SEC-AUT-AUTH-FR1: Authenticate and Authorize All Requests

The [offering](#DEF_Offering) _MUST_ apply an appropriate authorization policy prior to providing any [access](#DEF_Access) to any [target](#DEF_Target). Data and resources are [targets](#DEF_Target), and to allow a peer to read or write data is to provide access to a target. Any meaningful behavior in response to any message from a peer is also a target.
- In the case of a [public](#DEF_Public) target the policy is the no authentication or authorization is required.
- In the case of any non-public target, you _MUST_ always determine whether to grant access by applying authorization policy rules.

The offering _MUST_ authenticate [peer](#DEF_Peer) information before using it as input to an explicit authorization policy or otherwise allowing it to affect the outcome of any authorization decision.  This applies to machine peers as well as to human users, and it applies to communication within the offering as well as to communication with users, customers, or other outside entities.

The offering _MUST_ authenticate and apply proper authorization policy to messages they receive from peers. Peers include, but are not limited to:

 - web
 - backend
 - database
 - processes
 - containers


## SEC-AUT-AUTH-FR2:  Console Authentication

If there's a console port, the [standalone device](#DEF_StandaloneDevice) _MUST_ let the administrator define at least one [passphrase](#DEF_Passphrase) for [administrator](#DEF_Administrator) login over the [console](#DEF_Console). This [pass phrase](#DEF_Passphrase) _MUST_ be stored within the [standalone device](#DEF_StandaloneDevice)'s own hardware. This is in addition to the required support for authentication servers.

It _MUST_ be possible to log in on that port even when the network is down and the AAA server is unavailable.

Configuring console authentication _MUST_ be in customer facing documentation.

## SEC-AUT-AUTH-FR3:  Session State (Condition: Force:Mandatory, Restrict:Web Application)

The offer _MUST_ clearly convey the current session state to the user.  Users _MUST_ be [aware](#DEF_Aware) if they are currently authenticated to the application, and who they are currently authenticated as. 

The user _SHOULD_ be [aware](#DEF_Aware) of the currently granted user privileges (anonymous, regular user, admin user, etc.).

**Supplemental Guidance:**  If a user has multiple accounts with differing privileges, the user may forget which account is used for the current session. By indicating the session state the offer provides needed context for capabilities and indicate to the user to drop to a least privilege user if appropriate.

# Informative References

* NIST [Access Control AC-4](https://nvd.nist.gov/800-53/Rev4/control/AC-4)(17) Domain Authentication
* [Access Management and Authentication Procedure](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-11229096)
* [Access Management Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1417318)
* [Access Management Policy: FedRAMP Addendum](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-11212889)
* [Network Access Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-553471)
* RECIPE: [Enterprise Authorization IAM Recipes](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Enterprise%20IAM%20Authorization%20Recipes.aspx)
* [Cisco Enterprise Access Request Tool](https://edsart.cloudapps.cisco.com/createRequest)
* [Cisco Enterprise Management Policy (CEPM) can be requested via EStore](http://estore.cisco.com/RequestCenter/website/ServiceCatalog/index.html?/services/1449)

# History

```yaml
-----
affected_psb: SEC-AUT-AUTH-6
description:  Aggregated related requirements into functional requirements.
---
deprecated_psb: SEC-WEB-STATE
impact: normative
headline: >
  [SEC-WEB-STATE](#SEC-WEB-STATE) migrated to SEC-AUT-AUTH-FR6
---
deprecated_psb: SEC-MAN-PSWD
impact: non-normative
headline: >
  [SEC-MAN-PSWD](#SEC-MAN-PSWD) migrated to SEC-AUT-AUTH-FR5
```

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-AUT-ANCHOR
    roreigntarget: offerings
    relation: connects
    headline: >
        [SEC-AUT-ANCHOR](#SEC-AUT-ANCHOR) requires
        that [authentication](#DEF_Authentication) be based on valid chains of
        inference from local [authentication roots](#DEF_AuthenticationRoot).
    ---
    source: PSB
    foreign_id: SEC-AUT-DEFROOT
    roreigntarget: services
    relation: connects
    headline: >
        [SEC-AUT-DEFROOT](#SEC-AUT-DEFROOT) forbids most
        "default"[authentication roots](#DEF_AuthenticationRoot).
    ---
    source: PSB
    foreign_id: SEC-CRY-PRIM-FR1
    roreigntarget: services
    relation: connects
    headline: >
        [SEC-CRY-PRIM-FR1](#SEC-CRY-PRIM-FR1) defines approved cryptographic
        primitives, including the cryptographic primitives allowed to be used
        in [authentication](#DEF_Authentication) protocols.
    ---
    source: PSB
    foreign_id: SEC-509-VALIDATE
    roreigntarget: services
    relation: connects
    headline: >
        X.509 is often used to satisfy
        SEC-AUT-AUTH.[SEC-509-VALIDATE](#SEC-509-VALIDATE) puts demands on all
        X.509 certificate validation, and includes cross references to other
        requirements that put further demands on such validation.
    ---
    source: PSB
    foreign_id: SEC-CRY-ALWAYS
    roreigntarget: services
    relation: connects
    headline: >
        [SEC-CRY-ALWAYS](#SEC-CRY-ALWAYS) demands cryptographic protection for
        all non-[public](#DEF_Public) data that leave specific kinds
        of [controlled space](#DEF_ControlledSpace). The cryptographic
        protocols and formats that support complying
        with [SEC-CRY-ALWAYS](#SEC-CRY-ALWAYS) can often also be used to comply
        with SEC-AUT-AUTH.
    ---
    source: PSB
    foreign_id: SEC-ASU-TMOD-FR1
    roreigntarget: services
    relation: connects
    headline: >
        [SEC-ASU-TMOD-FR1](#SEC-ASU-TMOD-FR1) requires generating diagrams and
        documents that are usually useful in checking compliance with
        SEC-AUT-AUTH.
    ---
    source: PSB
    foreign_id: SEC-INF-SCAN
    roreigntarget: services
    relation: connects
    headline: >
        [SEC-INF-SCAN](#SEC-INF-SCAN) requires periodic scans that may be
        useful in checking compliance with SEC-AUT-AUTH.
    ---
    source: PSB
    foreign_id: SEC-OPS-ASTMGT
    roreigntarget: services
    relation: connects
    headline: >
        [SEC-OPS-ASTMGT](#SEC-OPS-ASTMGT) requires maintaining inventories that
        may be useful in checking compliance with SEC-AUT-AUTH.
    ---
    source: ISO 27002:2013
    foreign_id: A.9.1.2
    roreigntarget: 9
    relation: connects
    headline: >
        ISO 27002:2013: 9.1.2 Access to networks and network services
    ---
    source: ISO 27002:2013
    foreign_id: A.9.2.1
    roreigntarget: 9
    relation: connects
    headline: >
        ISO 27002:2013: 9.1.2 User registration and de-registration
    ---
    source: ISO 27002:2013
    foreign_id: A.9.2.3
    roreigntarget: 9
    relation: connects
    headline: >
        ISO 27002:2013: 9.2.3 Management of privileged access rights
    ---
    source: ISO 27002:2013
    foreign_id: A.9.2.4
    roreigntarget: 9
    relation: connects
    headline: >
        ISO 27002:2013: 9.2.4 Management of secret authentication information
        of users
    ---
    source: ISO 27002:2013
    foreign_id: A.9.3.1
    roreigntarget: 9
    relation: connects
    headline: >
        ISO 27002:2013: 9.3.1 Use of secret authentication information
    ---
    source: ISO 27002:2013
    foreign_id: A.9.4.1
    roreigntarget: 9
    relation: connects
    headline: >
        ISO 27002:2013: 9.4.1 Information access restriction
    ---
    source: ISO 27002:2013
    foreign_id: A.9.4.2
    roreigntarget: 9
    relation: connects
    headline: >
        ISO 27002:2013: 9.4.2 Secure log-on procedures
    ---
    source: ISO 27002:2013
    foreign_id: A.9.4.3
    roreigntarget: 9
    relation: connects
    headline: >
        ISO 27002:2013: 9.4.3 Password management system
    ---
    source: ISO 27017:2015
    foreign_id: A.9.3.1
    roreigntarget: 9
    relation: connects
    headline: >
        ISO 27017:2015: 27002 for cloud services: CLD 12.1.5 Administrator's
        operational security control

# Attributes

    id: SEC-AUT-AUTH
    version: 6
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    legallysensitive: false
    waivable: true
    issueref: ISS_PrivAccesAcct
    applicability:
      - force: mandatory
        target:
          restrict: >
            offerings
    priority: 9
    phase: requirements
    tags:
    - CloudCritical
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
