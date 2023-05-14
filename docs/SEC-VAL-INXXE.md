# Headline

Disable entity expansion or validate text content after expansion to
prevent XML eXternal Entity (XXE) Injection

# Key Benefits

XML injection attacks may lead to the disclosure of confidential data,
denial of service, server-side request forgery, port scanning from the
perspective of the machine where the parser is located, and other
system impacts.

The use of properly configured XML parsers can prevent a wide variety of
XXE Injection attacks by controlling external entity expansion and by
applying input validation practices after entity expansion.

# Description

XML entities are a way of representing an item of data within an XML
document, instead of using the data itself.  When an XML parser
recognizes a reference to an entity the application includes its
replacement text.

In general, XML entities can be declared internally or externally. If
an entity is declared within a Document Type Definition (DTD) it is
called internal entity. The purpose of DTD is to define the structure
of an XML document. If an entity is declared outside a DTD it is
called external entity.

An XML entity injection vulnerability is an injection vulnerability in
which an adversarial constructed XML document, containing a reference
to an entity, is processed by a weakly configured XML parser expanding
the XML entity.

# Behavior

## SEC-VAL-INXXE-FR1: Parsing XML Documents

This requirement applies when parsing XML documents.

1. XML parsers _MUST_ be configured to ignore (or to report and
   otherwise ignore) entity definitions in documents that are
   constructed from user-supplied data, or to refuse to expand any
   entity defined in such definition.

1. Parsers _SHOULD_ ignore all DTD information in user-supplied data,
   including both entity definitions and other DTD declarations.

## SEC-VAL-INXXE-FR2: Expanding Predefined Entities

This requirement applies when expanding predefined entities and
applying input validation practices.

1. The program _MUST_ completely disable external entity expansion.

1. If not possible to disable, the program _MUST_ make sure that all
   text content is validated after external entity expansion.

# Informative References

* OWASP XML External Entity (XXE) - [XXE Processing](https://www.owasp.org/index.php/XML_External_Entity_(XXE)_Processing)
* Wikipedia Billion Laughs Attack - [Billion Laughs Attack](https://en.wikipedia.org/wiki/Billion_laughs_attack)
* Common Vulnerability and Exposure (CVE) - [XXE Vulnerabilities](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=xxe)
* CWE-611 - [Improper Restriction of XEE Reference](https://cwe.mitre.org/data/definitions/611.html)
* CWE-776 - XXE - [Improper Restriction of Recursive Entity References in DTDs](https://cwe.mitre.org/data/definitions/776.html)
* CVE-2012-3489 - [PostgreSQL XXE Vulnerability](https://www.owasp.org/index.php/XML_External_Entity_(XXE)_Processing)


# Requirement References

    ---
    foreign_id: SEC-VAL-CLNIN
    relation: connects
    source: PSB
    headline: |-
        Validate all input before processing it

# Attributes

    id: SEC-VAL-INXXE
    version: 2
    issueref: ISS_Inject
    category: Threat Surface Reduction
    riskArea: Application & Interface Security
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
          restrict: Offerings parsing XML data
          class: not_HwComp
    priority: 9
    phase: requirements
    tags:
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - FAST
