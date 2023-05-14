# Headline

Prevent cross-site scripting vulnerabilities

# Description

Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it. Further information at: [OWASP XSS](https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)).

# Behavior

HTTP [listeners](https://cserv.cisco.com/library/glossary/CG46) (web applications) have to validate input and encode output. Cross-Site Scripting (XSS) attacks occur when data enters a web application through an untrusted source, most frequently a web request, or when the data is included in dynamic content that is sent to a web user without being validated for malicious content.

The malicious content sent to the web browser often takes the form of a segment of JavaScript, but may also include HTML, Flash, or any other type of code that the browser may execute. The variety of attacks based on XSS is almost limitless, but they commonly include transmitting private data, like cookies or other session information, to the attacker, redirecting the victim to web content controlled by the attacker, or performing other malicious operations on the user's machine under the guise of the vulnerable site.  XSS Attacks are currently categorized into [Stored, Reflected and DOM-Based](https://www.owasp.org/index.php/Types_of_Cross-Site_Scripting).
Stored and Reflected are both caused by Server Side(listener) vulnerability and DOM is caused by Client Side vulnerability.
Below are the feature requirements to safeguard against XSS attacks.

## SEC-WEB-XSS-FR1: Output Encoding
XSS protection solutions _MUST_ follow "AllowList" model that denies everything unless specifically allowed.

The solution _MUST_ identify tags within a HTML page where a developer is allowed to put untrusted data.  Putting untrusted data in other places in the HTML is not allowed. Details of identified tags and escaping content (output encoding) are provided in FR3-FR8

The solutions _MAY_ use popular Encoders available. The [OWASP Java Encoder Project](https://github.com/owasp/owasp-java-encoder) provides a high-performance encoding library for Java.

## SEC-WEB-XSS-FR2: Avoid BlockList

XSS protection solutions _MUST NOT_ construct a BlockList of input.  Only escaping that list of characters will not suffice.

## SEC-WEB-XSS-FR3: HTML Entity Encode

XSS protection solutions _MUST_ implement [HTML Escape](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html#rule-1---html-escape-before-inserting-untrusted-data-into-html-element-content) before inserting untrusted data into HTML element content.

**Supplemental Guidance:** Convert `&` to `&amp;`, Convert `<` to `&lt;`, Convert `>` to `&gt;`, Convert `"` to `&quot;`, Convert `'` to `&#x27;`, Convert `/` to `&#x2F;`


## SEC-WEB-XSS-FR4: Attribute Encode
XSS protection solutions _MUST_ implement [Attribute Escape](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html#rule-2---attribute-escape-before-inserting-untrusted-data-into-html-common-attributes) before inserting untrusted data into HTML common attributes.

**Supplemental Guidance:** Except for alphanumeric characters, escape all characters with the HTML Entity `&#xHH;` format, including spaces. (**HH** = Hex Value)

## SEC-WEB-XSS-FR5: JavaScript Encode
XSS protection solutions _MUST_ implement [JavaScript Escape](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html#rule-3---javascript-escape-before-inserting-untrusted-data-into-javascript-data-values) before inserting untrusted data into JavaScript data values. This would cover both script blocks and event-handler attributes. The only safe place to put untrusted data into this code is inside a quoted "data value."

**Supplemental Guidance:** Except for alphanumeric characters, escape all characters with the `\uXXXX` unicode escaping format (**X** = Integer).

## SEC-WEB-XSS-FR6: JSON Encode

XSS protection solutions _MUST_ implement [HTML JSON Escape](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html#rule-31---html-escape-json-values-in-an-html-context-and-read-the-data-with-jsonparse) in an HTML context and read the data with JSON.parse

The web server _MUST_ respond with the `Content-Type` header as application/json and not text/html. This shall instruct the user-agent to not misunderstand the context and execute injected script.

## SEC-WEB-XSS-FR7: CSS Encode

XSS protection solutions _MUST_ implement [CSS Escape](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html#rule-4---css-escape-and-strictly-validate-before-inserting-untrusted-data-into-html-style-property-values) and _MUST_ validate before inserting untrusted data into HTML style property values.

**Supplemental Guidance:** CSS escaping supports `\XX` and `\XXXXXX`. Using a two character escape can cause problems if the next character continues the escape sequence. There are two solutions - Add a space after the CSS escape (will be ignored by the CSS parser) or use the full amount of CSS escaping possible by zero padding the value.

## SEC-WEB-XSS-FR8: URL Encode
XSS protection solutions _MUST_ implement [URL Escape](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html#rule-5---url-escape-before-inserting-untrusted-data-into-html-url-parameter-values) before inserting untrusted data into HTML URL parameter values.

**Supplemental Guidance:** Standard percent [encoding](http://www.w3schools.com/tags/ref_urlencode.asp)--URL encoding should only be used to encode parameter values, not the entire URL or path fragments of a URL.

## SEC-WEB-XSS-FR9: Sanitize HTML Markup

XSS protection solutions _MUST_ implement [Sanitize HTML Markup](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html#rule-6---sanitize-html-markup-with-a-library-designed-for-the-job)
if the application receives untrusted input that contains HTML. In this case, both input validation and encoding is difficult as it would break all the tags that are supposed to be in the input. A library that can parse and clean HTML formatted text _MAY_ be used.

**Supplemental Guidance:**  There are several libraries to parse HTML formatted text available at [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html#rule-6---sanitize-html-markup-with-a-library-designed-for-the-job).

## SEC-WEB-XSS-FR10: Avoid JavaScript URLs

XSS protection solutions _MUST_ avoid JavaScript URLs. Untrusted URLs that include the protocol javascript will execute javascript code when used in URL DOM locations such as anchor tag HREF attributes or iFrame src locations. All untrusted URLs MUST be validated to ensure they only contain safe schemes such as HTTPS.

## SEC-WEB-XSS-FR11: Prevent DOM-based XSS

XSS protection solutions _MUST_ implement defenses identified in [DOM based XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html).

## SEC-WEB-XSS-FR12: Use Content Security Policy

XSS solutions _MUST_ implement [Content Security Policy(CSP)](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html#bonus-rule-2-implement-content-security-policy). CSP via special HTTP header instructs the client user-agent to only execute or render resources from those sources.

Minimal CSP _MUST_ include at least the following directives (with appropriate arguments)

- `default-src`
- `frame-ancestors`
- `block-all-mixed-content`
- `base-uri`

The default-src directive _MUST_ contain either 'none', or the trusted domain or site, and avoid wildcard. The directive _MAY_ have 'self' followed by any other trusted domain except wildcard.

- `default-src self *.trusted.com`
- `default-src none`

If further directives are required, they _MUST_ contain the trusted domain or site, and avoid wildcard.

The block-all-mixed-content is being deprecated, use it only as needed inorder to support older browsers. The upgrade-insecure-requests directive MUST not be used when block-all-mixed-content is used as it voids the latter. Refer Supplemental Guidance.

Adding unsafe source values such as unsafe-inline, unsafe-eval, unsafe-hashes voids the CSP, and hence _MUST NOT_ be used.  Instead, to allow execution of scripts from unknown source, use source value hash, so that execution is based on the verification of the hash. This would be the same solution for integration with third-party libraries where either the hash verification or the source domain can be used in the CSP. Refer to Supplemental guidance for the supported hash value types.

- `script-src sha256-xyz..`
- `script-src nonce-random..`

Data schemes such as data: filesystem: blob: mediastream: _MUST NOT_ be used as these refer to special pieces of unique content which are often derived from a response body or executed in a Document context which are unsafe.
Broad schemes such as http:, ftp: and others are disallowed. The scheme _MUST_ occur in conjunction with a directive, and _MUST_ contain the trusted domain or site.

- `image-src https://*.trusted.com -- ALLOWED`
- `image-src https: --DISALLOWED`

**Supplemental Guidance:**  Refer to the [Content Security Policy Level 3](https://www.w3.org/TR/CSP3/), [Content Security Policy](https://content-security-policy.com), [Strict Checking](https://www.w3.org/TR/mixed-content/#strict-checking), [Document Checking](https://www.w3.org/TR/CSP3/#directives-document).

## SEC-WEB-XSS-FR13: Use HTTPOnly Cookie Flag

XSS solutions _SHOULD_ set the HTTPOnly flag on your session cookie and any custom cookies you have that are not accessed by any JavaScript you wrote. This cookie flag is typically on by default in .NET apps, but in other languages you have to set it manually.

**Supplemental Guidance**: For more details on the HTTPOnly cookie flag, including what it does, and how to use it, see the OWASP article on [HTTPOnly](https://owasp.org/www-community/HttpOnly).

# Informative References
- Recipe: [Defend Against XSS](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Defend%20Against%20CrossSite%20Scripting%20(XSS).aspx)
- [Cisco Devnet Security Guide](https://apistyleguide.cisco.com/#!security)
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [XSS Advisories](https://tools.cisco.com/security/center/Search.x?keyword=Cross+Site+Scripting&criteria=exact&publicationTypeIDs=1)

# Normative References

None

# Requirement References

    ---
    foreign_id: SEC-VAL-INURL
    relation: connects
    headline: |-

              URLs are common cross-site scripting targets;
              SEC-VAL-INURL gives
              rules for validating them.

    source: PSB
    ---
    foreign_id: SEC-VAL-INEVAL
    relation: connects
    headline: |-

              Any cross-site scripting vulnerability that involves
              JavaScript is also a program injection vulnerability.
              SEC-VAL-INEVAL
              addresses program injection vulnerabilities in all
              contexts (not limited to XSS).

    source: PSB
    ---
    foreign_id: SEC-VAL-INSQL
    relation: connects
    headline: |-

              Any cross-site scripting vulnerability that involves
              SQL is also an SQL injection vulnerability.
              SEC-VAL-INSQL
              addresses SQL injection vulnerabilities in all
              contexts (not limited to XSS).

    source: PSB
    ---
    foreign_id: SEC-LOG-ATTACK
    relation: connects
    headline: |-
      SEC-LOG-ATTACK
              requires you to log any event that might indicate
              a security attack. Anything detected and blocked
              by a cross-site scripting protection measure
              is likely to indicate a possible security attack.

    source: PSB
    ---
    foreign_id: SEC-ASU-SCAN
    relation: connects
    headline: |-
      SEC-ASU-SCAN requires running
              specific tests against Web applications; some of these
              tests may find cross-site scripting vulnerabilities.

    source: PSB

# History

    ---
    id: SEC-WEB-XSS
    version: 4
    affected_psb: SEC-WEB-XSS
    impact: normative
    headline: |-
      [SEC-WEB-XSS-4]
    description: |-
      Updated HTTPOnly links
      Normative changes in FR12:Content Security Policy
        Clarified unsafe inline hash values in source-src
        Clarified none usage in default-src
        Clarified block-all-mixed-content directive
# Attributes

    id: SEC-WEB-XSS
    version: 4
    category: Web Security
    riskArea: Application & Interface Security
    legallysensitive: false
    waivable: true
    issueref: ISS_Inject
    applicability:
      - force: mandatory
        target:
          class: HasWebUi
          restrict: >
            Web user interfaces and HTTP APIs
    priority: 10
    phase: requirements
    tags:
    - EN/PI
    - Critical PSB
    - CloudCritical
    - PSB/OnPrem
    - Cloud
    - FAST
