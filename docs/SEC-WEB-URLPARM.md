# Headline

Pass sensitive information only in request body or headers

# Description

Don't embed [sensitive](#DEF_Sensitive) information in HTTP/HTTPS URLs;
use request bodies or headers instead.

# Behavior

Never include, and never induce or require another agent to include, any
known or probable [sensitive](#DEF_Sensitive) or Personal Identifiable
Information (PII) in the URL used in any HTTP request. Never include any
[sensitive](#DEF_Sensitive) data in the URL of any link on Web page
displayed to a human user. Note that request parameters after a question
mark are still part of the URL.

## SEC-WEB-URLPARAM-FR1: Use headers or request body to pass sensitive information
If a HTTP client passes [sensitive](#DEF_Sensitive) information in an
HTTP request, it _MUST_ do so using headers or request body
parameters.

## SEC-WEB-URLPARAM-FR2: Refuse requests 
Servers _SHOULD_ refuse requests which attempt to use URL parameters
to pass data likely to be [sensitive](#DEF_Sensitive).
This requirement applies to all HTTP requests, regardless of any
encryption in use on the connection.

## SEC-WEB-URLPARAM-FR3: Exceptions
There are instances where there are exceptions to FR1-FR2.

If your [offering](#DEF_Offering) includes non-[Cisco controlled](#DEF_CiscoControlled) software 
that requires [sensitive](#DEF_Sensitive) information to be provided in URL
parameters, then you _MAY_ do so, but only to the minimum extent
required by the non-[Cisco controlled](#DEF_CiscoControlled) component,
and only in HTTP requests that meet all of the following restrictions:

1.  The requests _MUST_NOT_ be initiated by browsers; only requests
    from non-browser machine clients are allowed.
2.  The requests _MUST_NOT_ pass outside of your
    [offering's](#DEF_Offering)[controlled space](#DEF_ControlledSpace)
    unencrypted.
3.  You _MUST_ prevent the requests from causing
    [sensitive](#DEF_Sensitive) information to leave your offering's
    controlled space by secondary paths such as logs, referer headers,
    caches, or history. Your [controlled space](#DEF_ControlledSpace)
    analysis must specifically address at least the aforementioned
    leakage paths.
4.  The requests _MUST_NOT_ be processed in any way by
    [code](#DEF_Code) you have not specifically selected to form part of
    your [offering](#DEF_Offering).

# Normative References

-   W3C HTML Reference, Form Submission Methods

    <http://www.w3.org/TR/1999/REC-html401-19991224/interact/forms.html#h-17.13.1>

-   SEC-DAT-KNOWWHAT

    <https://wwwin-si.cisco.com/psb-requirements/#SEC-DAT-KNOWWHAT>

# History

    ---
    id: SEC-WEB-URLPARAM
    version: 2
    affected_psb: SEC-WEB-URLPARAM
    impact: non-normative
    headline: |-
      [SEC-WEB-URLPARAM-2]
    description: |-
      Updated content in new PSB format with FR


# Attributes

    phase: requirements
    legallysensitive: false
    priority: 9
    applicability:
    - force: mandatory
      target:
        restrict: Web applications, HTTP APIs, and HTTP clients
    category: Web Security
    riskArea: Application & Interface Security
    waivable: true
    version: 2
    id: SEC-WEB-URLPARM
    issueref: ISS_SensUrl
    tags:
    - EN/PI
    - CloudCritical
    - PSB/OnPrem
    - Cloud
    - FAST
