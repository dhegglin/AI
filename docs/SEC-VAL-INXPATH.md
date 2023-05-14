# Headline

Use prepared statements or validate user input to construct XPath
queries.

# Key Benefits

The use of parameterized queries (prepared statements) and input
validation techniques can prevent a wide variety of XPath Injection
attacks.

Parameterized queries are precompiled queries where user-supplied input is
passed as parameters rather than expressions. This avoids having
user-supplied data parsed as part of the XPATH expression.

# Description

An XPATH Injection vulnerability is an injection vulnerability in
which an offering builds an XPATH expression from user-supplied data
in a way that permits the data source to cause the expression to
return different data than intended.

Depending on the purpose for which the vulnerable query is being used,
an attacker may be able to exploit an XPath injection flaw to read
sensitive application data or interfere with application logic.

An XML injection is facilitated by sending intentionally malformed
information into the website. The attacker can then find out how the
XML data is structured, or access data not normally accessible. The
attacker may even be able to elevate privileges on the website if the
XML data is being used for authentication.

# Behavior

## SEC-VAL-INXPATH-FR1: XPath Prepared Statements and Input Validation

This requirement applies when XPath queries utilize user-supplied input.

1. The program _MUST_ use XPath prepared statements as the first
   choice to query XML data. Otherwise, the program _MUST_ apply input
   validation practices to user-supplied inputs prior to dynamically
   constructing XPath queries.

## SEC-VAL-INXPATH-FR2: Constants in XPath Statements

This requirement applies when user input is used in prepared statements
or dynamically constructed XPath expressions.

1. The program _MUST NOT_ copy any user-supplied data into any XPath
   expression other than a constant.

1. The program _MUST_ quote all user-supplied data used in any string
   constant in any XPath expression.

1. The program _MUST_ have only one quoting function provided by any
   third-party library or application framework used to create the
   XPath queries.

1. The program _MUST_ ensure that non-string constants do not contain
   inappropriate characters. Do this by regenerating them from parsed values
   rather than by copying user-supplied string representations of these
   non-string types.

## SEC-VAL-INXPATH-FR3: AllowListing to Validate a Constant

This requirement applies whenever AllowListing is used to validate a
user-controlled constant.

1. The program _MUST_ check the characters present in any
   user-supplied constant that will be used in an XPath expressions
   against a AllowList of legal characters for that constant.

1. The AllowList _MUST NOT_ include any characters not expected by the
   consuming [code](https://cserv.cisco.com/library/glossary/CG35).

1. The AllowList _MUST NOT_ include any control characters, newlines,
   whitespace other spaces, or single or double quotes.

1. The program _MUST NOT_ construct an XPath expression if presented
   with a string containing any unexpected characters. The string
   _MUST_ be rejected.

# Implementation guidance:

- RECIPE: [Defense Against XPATH Injection](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Defense%20Against%20XPATH%20Injection.aspx)
- OWASP XPath Injection - [XPath
  Injection](https://www.owasp.org/index.php/XPATH_Injection)
- OWASP XPath Injection Java - [XPath Injection
  Java](https://www.owasp.org/index.php/XPATH_Injection_Java)
- CWE-643 XPath Injection - [Improper Neutralization of Data within
  XPath Expressions](https://cwe.mitre.org/data/definitions/643.html)
- CWE-91 XML Injection - [Blind XPath
  Injection](https://cwe.mitre.org/data/definitions/91.html)

# Informative References

*Optional, Not Normative*

- W3C Recommendations - [XML Path Language (XPath)
  3.1](https://www.w3.org/TR/xpath-31/)
- XML Security - [XML Security Cheat
  Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html)
- XML Path Language - [XPath](https://www.w3.org/TR/xpath/all/)
- Simple and Blind XPath Injection - [XPath
  Injection](https://dl.packetstormsecurity.net/papers/bypass/Blind_XPath_Injection_20040518.pdf)
- NIST National Vulnerability Database - [XPath Injection
  Vulnerabilities](https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query=xpath+injection&search_type=all)
- Common Vulnerabilities and Exposures (CVE) - [CVE
  List](http://cve.mitre.org/cve/)
- CWE-643 XPath Injection - [Improper Neutralization of Data within
  XPath Expressions](https://cwe.mitre.org/data/definitions/643.html)
- CWE-91 XML Injection - [Blind XPath
  Injection](https://cwe.mitre.org/data/definitions/91.html)

# Requirement References

    ---
    foreign_id: SEC-VAL-CLNIN
    relation: connects
    source: PSB
    headline: |-
        Validate all input before processing it

# Attributes

    id: SEC-VAL-INXPATH
    version: 2
    issueref: ISS_Inject
    category: Threat Surface Reduction
    riskArea: Application & Interface Security
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
          restrict: Offerings using XPATH to select data (usually from XML)
          class: not_HwComp
    priority: 9
    phase: requirements
    tags:
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - FAST
