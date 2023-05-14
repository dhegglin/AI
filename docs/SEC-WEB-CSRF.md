# Headline

Prevent CSRF Vulnerabilities

# Description

CSRF is an attack that tricks the victim into submitting a malicious request. It inherits the identity and privileges of the victim to perform an undesired function on the victim's behalf. For most sites, browser requests automatically include any credentials associated with the site, such as the user's session cookie, IP address, Windows domain credentials, and so forth. Therefore, if the user is currently authenticated to the site, the site will have no way to distinguish between the forged request sent by the victim and a legitimate request sent by the victim. Further information at: [OWASP CSRF](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)).

# Behavior

HTTP [listeners](#DEF_Listener) have to protect against any state-changing request or sensitive-information retrieval request that a properly functioning user agent could generate in response to a link, submit button, script, or other [code](#DEF_Code) that's part of a page not originated or authorized by the web application.

CSRF protection can be built using various patterns provided in [OWASP CSRF](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md). The pattern would depend upon browser/user-agent requirement or limitation, and/or listener side requirement or limitation. The protections have to detect CSRF using information in each incoming HTTP request. Assuming proper operation of the client browser or other user agent, and assuming that the user agent is able to authenticate the source of any data ostensibly sent from your server, the below functional requirements have to be implemented.

## SEC-WEB-CSRF-FR1: Use CSRF protection patterns

CSRF protection solutions _SHOULD_ follow one of the patterns listed below. In addition, the [Defense in Depth](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md#defense-in-depth-techniques) solutions _MAY_ be implemented.

## SEC-WEB-CSRF-FR2: CSRF tokens

The CSRF token _MUST_ be a separate value created for this specific purpose and not reused from other values in the request. If solutions use the Stateless token pattern, which uses [SEC-WEB-ID](#SEC-WEB-ID), then the solution _MUST_  add anti-replay measures to the [SEC-WEB-ID](#SEC-WEB-ID) as specified in [HMAC Based Token Pattern](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md#hmac-based-token-pattern) and [Encryption Based Token Pattern](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md#encryption-based-token-pattern).

## SEC-WEB-CSRF-FR3: Encrypt HTTP connections for tokens

Encrypted HTTP connections _MUST_ be used to transfer CSRF tokens by adhering to PSB requirements that apply to [SEC-HTP-HSTS](#SEC-HTP-HSTS).

## SEC-WEB-CSRF-FR4: Use session specific tokens

The CSRF token _MUST_ be session specific, and _MAY_ be request specific.

## SEC-WEB-CSRF-FR5: Use safe request mechanisms

[RFC7231](https://tools.ietf.org/html/rfc7231#section-4.2.1), section 4.2.1 _MUST NOT_ be violated, by using GET(or any other safe method) requests for state changing operations, or for retrieval of privacy information. Refer to [SEC-DAT-KNOWWHAT](#SEC-DAT-KNOWWHAT) for privacy information. If for any reason this is violated, then it is a _MUST_  to protect those resources.

## SEC-WEB-CSRF-FR6: CSRF token lifetime policies

Minimum CSRF token lifetime policies _MUST_ be maintained wherein the lifetime of the token _MUST_ be based on the business requirement. As CSRF token is session specific or request specific, the lifetime of the token is tied to the lifetime of either the session or the request.

## SEC-WEB-CSRF-FR7: General adherence to PSB 

The CSRF token _MUST_ adhere to all PSB requirements that apply to [SEC-DAT-KEYMGMT](#SEC-DAT-KEYMGMT).

## SEC-WEB-CSRF-FR8: No embedded URL request parameters

Information used for CSRF protection _SHOULD NOT_ be transmitted using any request parameter embedded in a URL, as CSRF token leaks via Referer can still happen on HTTPS Applications. Parameters in request bodies _MAY_ be used.

## SEC-WEB-CSRF-FR9: Stateless tokens

Stateless tokens _SHOULD_ use strong encryption and authentication functions compliant with [SEC-CRY-PRIM-FR1](#SEC-CRY-PRIM-FR1) and [SEC-CRY-RANDOM-2](#SEC-CRY-RANDOM).

## SEC-WEB-CSRF-FR10: Apply CSRF protection broadly

CSRF protection _SHOULD_ be provided by a general system applied to all HTTP requests, rather than by logic specific to individual [targets](#DEF_Target) or request types - many user agent and server side frameworks come with built in CSRF protections.

## SEC-WEB-CSRF-FR11: Login CSRF

Login CSRF mitigation _SHOULD_ be provided where possible. Login CSRF can be mitigated by creating pre-sessions (sessions before a user is authenticated) and including tokens in login form. These pre-sessions cannot be transitioned to real sessions once the user is authenticated - the session should be destroyed and a new one should be made to avoid session fixation attacks.
Strict Referer validation _MAY_ also be implemented to protect against Login CSRF attacks. Note that the Referer header is supressed often for cross-domain requests. Refer: [Login CSRF](https://seclab.stanford.edu/websec/csrf/csrf.pdf) for different Login CSRF defenses for different use cases.

## SEC-WEB-CSRF-FR12: Do not store tokens in cookies

Tokens _MUST NOT_ ever be stored in cookies at all. In case the solution has dependency on certain brower/user agents (Angular, Django) that follow [Double Submit Cookie pattern](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md#double-submit-cookie), the solution _MUST_ include the token in an encrypted cookie - often within the authentication cookie - and then at the server side matching it (after decrypting authentication cookie) with the token in hidden form field or parameter/header.

## Preferred Patterns

The token based defense is one of the most popular and recommended methods to mitigate CSRF. It can be achieved either with Synchronizer token pattern(Stateful) or Encrypted/HMAC based token pattern(Stateless).

* Synchronizer Token (Stateful)
  An anti-CSRF "synchronizer token" (which does not actually synchronize anything and is not necessarily synchronized with anything) is a random value recorded in server-side session state and used to demonstrate that a request has been generated by the [code](#DEF_Code) that server has provided to the client in some particular session. Application-specific client-side code returns the synchronizer token by non-cookie means, thus showing that a browser hasn't automatically attached the token to an adversarially-generated request. Details on implementation from OWASP - [Synchronizer Token](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md#synchronizer-token-pattern).
* Encryption Based Token Pattern (Stateless)
  Encrypted Token Pattern uses encryption, rather than comparison method of Token-validation. It is most suitable for applications that do not want to maintain any state at server side. Details on implementation from OWASP - [Encryption Based Token Pattern](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md#encryption-based-token-pattern).
* HMAC Based Token Pattern (Stateless)
  HMAC Based Token Pattern mitigation is also achieved without maintaining any state at the server. HMAC based CSRF protection works similar to encryption based CSRF protection. Details on implementation from OWASP - [HMAC Based Token Pattern](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md#hmac-based-token-pattern).

# Informative References

* [Cisco Devnet Security Guide](https://apistyleguide.cisco.com/#!security)
* [OWASP CSRF Prevention Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md)
* [CSRF Advisories](https://tools.cisco.com/security/center/publicationListing.x?product=Cisco&title=forgery&sort=-day_sir&limit=100#~Vulnerabilities)

# Normative References

* [RFC7231, section 4.2.1](https://tools.ietf.org/html/rfc7231#section-4.2.1)

# Attributes

    id: SEC-WEB-CSRF
    version: 3
    category: Web Security
    riskArea: Application & Interface Security
    legallysensitive: false
    waivable: true
    issueref: ISS_CSRF
    applicability:
      - force: mandatory
        target:
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
