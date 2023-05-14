# Headline

Disable Unused HTTP Methods


# Description

Disable all HTTP methods that are not used by the web application to
avoid exploitation of the unused functionality.

# Behavior

HTTP supports the many methods such as - OPTIONS, GET, HEAD, POST, PUT,
DELETE, TRACE, CONNECT.
These methods can be used for unintended information leaks about the web
application, its technologies or its data. They may also be used to
modify or destroy resources or data of the web application. Tight
control over which methods are enabled for any web application helps
reduce the attack surface.Feature requirements are provided below.

## SEC-WEB-HTTPMETH-FR1: Disable unneeded HTTP methods
Web applications _MUST_ disable all HTTP methods that are not needed for the proper operation of the web application especially TRACE method as that leads to Cross Site Tracing(CST) Attacks

# Normative References

-   W3C HTTP Methods

    <http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html>

-   Techstacks: Disable HTTP Methods In Tomcat

    <http://www.techstacks.com/howto/disable-http-methods-in-tomcat.html>

-   OWASP Cross-Site Tracing Guide

    <https://www.owasp.org/index.php/Cross_Site_Tracing>

# Informative References
* [Cross Site Tracing White Paper](https://www.cgisecurity.com/whitehat-mirror/WH-WhitePaper_XST_ebook.pdf)

# History

    ---
    id: SEC-WEB-HTTPMETH
    version: 2
    affected_psb: SEC-WEB-HTTPMETH
    impact: non-normative
    headline: |-
      [SEC-WEB-HTTPMETH-2]
    description: |-
      Updated content in new PSB format with FR
      Connected XST Attack with TRACE method and clarified in FR1
      Updated informative reference section

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 9
    applicability:
    - force: mandatory
      target:
        restrict: Web Applications
    category: Web Security
    riskArea: Application & Interface Security
    waivable: true
    version: 2
    id: SEC-WEB-HTTPMETH
    issueref: ISS_HTTPMisConf
    tags:
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - FAST
