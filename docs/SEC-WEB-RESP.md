# Headline

Specify type and encoding in HTTP responses; disable type sniffing

# Description

The Content-Type entity header is used to indicate the media type of the resource. In responses, a Content-Type header tells the client what the content type of the returned content actually is. Browsers will do MIME sniffing in some cases and will not necessarily follow the value of this header. This would cause non-executable MIME types transform into executable MIME types.

# Behavior

In order to safeguard against MIME type transformation, it is required to explicitly specify content type and character set used to encode HTTP response data. In responses, where there is no target resource representation, such as 304 NotModified, this protection is not required as there is no content to protect.
Below are the feature requirements to explicitly set the MIME type and character set.

## SEC-WEB-RESP-FR1: Set MIME-type and Charset

Use the HTTP "`Content-type`" to explicitly specify the "`media-type`" and "`charset`" used to construct each HTTP response. Servers will generally add the content type by default (such as "`Content-type: text/html;       charset=utf-8`") but may occasionally get it wrong.

** Supplemental Guidance:** Refer [Content-Type](https://www.iana.org/assignments/media-types/media-types.xhtml) and [CharSet](https://www.iana.org/assignments/character-sets/character-sets.xhtml)

## SEC-WEB-RESP-FR2: Set nosniff option

Include "`X-Content-Type-Options: nosniff`" to prevent (most) browsers from overriding the specified content type based on the response document content.

# Informative References

* [Mozilla Content-Type Header Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)

* [Microsoft nosniff Guide](http://msdn.microsoft.com/en-us/library/ie/gg622941.aspx)

* [Mitigating MIME Confusion Attacks in Firefox](https://blog.mozilla.org/security/2016/08/26/mitigating-mime-confusion-attacks-in-firefox)

* Conditional Responses: [RFC 7232](https://tools.ietf.org/html/rfc7232#section-4.1)
# History

---
    id: SEC-WEB-RESP
    version: 4
    affected_psb: SEC-WEB-RESP
    impact: normative
    headline: |-
      [SEC-WEB-RESP-4]
    description: |-
      Updated content in new PSB format with FR
      Updated verification with CAVE automation information
      Clarified 304 NotModified response
      Mandated for all Content-Types instead of only javascript and CSS


# Attributes

    phase: requirements
    legallysensitive: false
    priority: 9
    applicability:
    - force: mandatory
      target:
        restrict: HTTP servers expected to be used by user agents
        class: HasWebUi_AND_not_MobileApp
    category: Web Security
    riskArea: Application & Interface Security
    waivable: true
    version: 3
    id: SEC-WEB-RESP
    issueref: ISS_Inject
    tags:
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - FAST
