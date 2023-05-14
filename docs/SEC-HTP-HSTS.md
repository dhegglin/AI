# Headline

Use HTTP Strict Transport Security

# Description

Whenever you serve an encrypted HTTP request, use HSTS to inform the
client that all future requests should also be encrypted. Redirect
unencrypted HTTP to any corresponding URI available via an encrypted
connection. If you're a client, honor HSTS policy set by the server.

# Behavior

The required behavior at the HTTP clients and Web Application(HTTP servers) are given in the below feature requirement.

## SEC-HTP-HSTS-FR1: HTTP Client Behavior 

If your [offer](#DEF_Offering) receives a "`Strict-Transport-Security`" header (or any standardized successor),
then the offering _MUST_ honor the policy described in that header by automatically sending requests over HTTPS for the target domain.

**Supplemental Guidance:** For a user to take advantage of HSTS, their browser does have to see the HSTS header at least once. This means that users are not protected until after their first successful secure connection to a given domain. Consider [HSTS-PreLoading](https://https.cio.gov/hsts/)

## SEC-HTP-HSTS-FR2: Web Application Behavior

1. Whenever your [offer](#DEF_Offering) replies to an HTTP request over a TLS-encrypted connection, the offering _MUST_include the "`Strict-Transport-Security`" header (or any standardized successor) to inform the client that all future requests to the server are also to be over encrypted connections.


2. Whenever your [offering](#DEF_Offering) receives an HTTP request over an unencrypted connection, and the same resource is available at a TLS ("https") URI, the client _MUST_ be redirected to the TLS URI.

  **Supplemental Guidance:** In the case of Cisco-managed services, disabling 
    HSTS requires a direct request from a *non-Cisco*[controlling policy entity]    (#DEF_ControllingPolicyEntity). Services
    are therefore rarely if ever allowed to disable HSTS.

## SEC-HTP-HSTS-FR3:  HSTS parameters/directives

1. The "max-age" directive _MUST_ be set in the "Strict-Transport-Security" header. The duration _SHOULD_ be long enough that nearly all clients will revisit the service within the set time, so that their HSTS policy data will never expire.

    **Supplemental Guidance:** Set the default to at least 30 days (2592000 seconds). A longer duration such as 180 days
    (15552000 seconds) is often reasonable.

2. The "includeSubDomains" directive _MUST_ be set when all services with FQDNs that are subdomains can support HTTPS when connecting to the offer.

    **Supplemental Guidance:** Strict-Transport-Security: max-age=31536000; includeSubdomains

# Normative References

* [RFC 6797: HTTP Strict Transport Security](https://tools.ietf.org/html/rfc6797)

# Informative References

* [OWASP - HTTP Strict Transport Security](https://www.owasp.org/index.php/HTTP_Strict_Transport_Security)
* [HSTS-PreLoading](https://https.cio.gov/hsts/)

# History
    ---
    id: SEC-HTP-HSTS
    version: 2
    affected_psb: SEC-HTP-HSTS
    impact: non-normative
    headline: |-
      [SEC-HTP-HSTS-2]
    description: |-
      Updated content in new PSB format with FR
      Added Supplemental Guidance and Informative Reference
      Reviewed NIST - Guidance already covered in SEC-WEB-ID 

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: HTTP servers and clients
    category: Web Security
    riskArea: Application & Interface Security
    waivable: true
    version: 2
    id: SEC-HTP-HSTS
    issueref: ISS_HTTPSpoof
    tags:
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - FAST
