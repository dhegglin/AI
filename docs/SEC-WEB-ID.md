# Headline

Use secure Session Tokens (session IDs/state tokens)

# Description

"Session Tokens" as typically used by Web applications are
[credentials](#DEF_Credential) and can be used to impersonate users.
Prevent them from being leaked, guessed, or stolen.

# Behavior

A Web session is a sequence of HTTP request and response transactions, all of which the HTTP server is assured involve the same HTTP [peer](#DEF_Peer). Such a peer is often a Web browser or an instance of some known program running in a particular tab within a Web browser. Non-browser HTTP clients can also have sessions.

Generally the server identifies some [principal](#DEF_Principal)
associated with each session at the beginning of that session,
authenticates that the client represents that [principal](#DEF_Principal), records that information as part of the session state, and uses it to make [authorization](#DEF_Authorization) decisions throughout the life of the session.

An HTTP session token is a value provided by a server to a client, and returned in later HTTP transactions, to associate transactions in the same session, and/or to allow the server to find state information associated with that session. A session token may last for the entire life of a session, or may be updated during the session.

Below are the feature requirements to create and handle the session tokens securely.

## SEC-WEB-ID-FR1:  Approved patterns for Session Tokens
The offering _MUST_ implement one of the approved patterns provided below.
### Session ID pattern

A session ID is a random value used only to identify a particular
session. The HTTP server uses the session ID to locate session state
information in its own database of active sessions. A session ID does not itself encode any session state information; it serves only as a lookup key.

1.  Each session ID _MUST_ have at least 128 bits of [unpredictability](#DEF_Unpredictability), independent of every other session ID.

2.  You _MUST_NOT_ assign one session the same session ID used for any
    other session, including sessions which are no longer active and
    including all other current or previous sessions for the same user
    or other [principal](#DEF_Principal). The session ID for each
    session _MUST_ be generated independently from every other session
    ID.

    **Supplemental Guidance:** If each session ID is created
      separately as required in (1), by obtaining a value with at
      least 128 bits of [unpredictability](#DEF_Unpredictability) from
      a [cryptographic](#DEF_Cryptography) random number generator
      that complies with [SEC-CRY-RANDOM](#SEC-CRY-RANDOM), then there
      is no meaningful chance of collision between session
      IDs. Furthermore, there is no feasible way of reducing the
      negligible chance that remains. You are not required to keep or
      check against a database of past session IDs to prevent
      collisions, only to generate session IDs properly and avoid
      actively reusing them.

3.  Generate a new session ID and invalidate the old session ID whenever there's a change of client [principal](#DEF_Principal) or authorization (including  "privileges", "roles", or other offering-specific authorization information).
Logging in is always a change of principal and authorization. If a session ID is used to track a session which has not logged in, then that session ID _MUST_ be changed at login.

4.  Session IDs _SHOULD_NOT_ be derived, in whole or in part, from any information other than the output of a cryptographic random number generator.
If a session ID is derived from any other data, then this _MUST_
be done by applying a [good-cryptography ](#DEF_GoodCryptography) cryptographic hash function with at least 128 "bits of security", in a single operation, to a string of data including both that information *and* a cryptographic random value having at least 128 bits of [unpredictability](#DEF_Unpredictability), where the random value is never used for any other purpose.

5.  A session ID _MUST_NOT_ contain or disclose any information other than the random value or hash output. Refer to [SEC-DAT-KNOWWHAT](#SEC-DAT-KNOWWHAT) for privacy information.

6.  The HTTP server _MUST_ reject every transaction that attempts to use as a session ID any value that is not the current session ID associated with an identified, active session authorized to perform that transaction.

### State token pattern (JWT, etc)

A state token is a cryptographically protected copy of some or all of
the state information associated with a session (generally including
[principal](#DEF_Principal) and authorization information). A state
token *encodes* session state, whereas a session ID only *identifies*
such state by selecting it from a server-side database. State tokens
free the server from the need to maintain or access a local database of all session state.

JSON Web Tokens (JWT) provide a prominent example of state tokens.

1.  Protect the integrity of each state token by processing the entire state token as a single message in a [good-cryptography](#DEF_GoodCryptography) authenticated encryption mode, message authentication code, or public key digital signature scheme. Digital signatures may allow you to keep the key on fewer servers.

2.  If a state token includes any non-[public](#DEF_Public) information, then protect its confidentiality and integrity by encrypting the entire state token as a single message using a [good-cryptography](#DEF_GoodCryptography) authenticated encryption mode or encrypt-then-MAC scheme. Refer to [SEC-DAT-KNOWWHAT](#SEC-DAT-KNOWWHAT) for privacy information.

3.  If the state token is updated with new information during the course of a session, it _MUST_ be impossible for a client to violate any [security](#DEF_Security) guarantee by replaying a superseded state token.
**Supplemental Guidance:** As a special case, if any [authorization](#DEF_Authorization)-relevant session information changes (including the case where a user explicitly logs out), the old token _MUST_ become invalid. This will generally require maintaining at least some limited state at the server.

4.  Each state token _MUST_ encode an expiration time, or a creation time from which an expiration time can be calculated. The server _MUST_ refuse any transaction using a state token whose expiration time has passed. The expiration time _MUST_ be within the bounds defined in SEC-WEB-ID-FR6 for Session Expiration.

5.  Except for public keys in approved public-key systems, never disclose any encryption/authentication keys used for any state token to any client or to any system outside of your [offering](#DEF_Offering).

6.  Never include any non-cryptographically-protected information in or with the state token. Refer to [SEC-DAT-KNOWWHAT](#SEC-DAT-KNOWWHAT) for privacy information.

7.  If the state token encodes only part of the session state, with other state information being kept at the server, then the information in the state token _MUST_ be sufficient to uniquely identify the session information on the server side, and the server _MUST_ reject any transaction using a state token for which the corresponding server-side information is not available, shows the
session to have ended, or shows the transaction to be unauthorized.

## SEC-WEB-ID-FR2: Session Token Handling

The following apply to all session tokens, including both session IDs
and state tokens.

1.  Never embed any session token in a URI, including in a URI query parameter.

2.  Never embed any session token in an element you expect to be logged.

3.  By default, do not send or accept any session token over an unencrypted connection. If a non-Cisco [controlling policy entity](#DEF_ControllingPolicyEntity) configures your [offering](#DEF_Offering) to support sessions over unencrypted HTTP, then you _MUST_ maintain a distinction between encrypted and unencrypted sessions and their associated session tokens. Never permit a session token created over an encrypted connection to be used over an unencrypted one or vice versa.

4.  You _SHOULD_ use only one session token, which _SHOULD_ be stored in only one client-side storage location (such as a cookie, other client storage element, JavaScript variable, or DOM element).
If you use more than one session token, you _MUST_ validate all of them on every request, and reject the request if any are invalid or if they give inconsistent information.
**Supplemental Guidance:** If you receive a request with multiple session tokens which would be valid taken individually, but which give inconsistent information, you _SHOULD_ permanently invalidate all of those tokens, terminate the associated sessions, and treat the event as a possible security attack.

5.  When a transaction explicitly ends a session, explicitly remove all client-side copies of the corresponding session token. Do not allow session tokens to be stored in places from which they cannot be removed.

## SEC-WEB-ID-FR3: Exchange Mechanism
There are multiple mechanisms available in HTTP to maintain session state within web applications. Cookies are the one of the most extensively used as it allows defining advanced token properties, such as the token expiration date and time, or granular usage constraints.  Cookies _MUST_ follow the below configuration.

1. Make the cookie a single-session one. Do *not* supply an  "`Expires`" or "`Max-age`" attribute.

2. Set the "`Secure`" cookie attribute to prevent the client from returning the cookie over unencrypted HTTP (unless that token was set over unencrypted HTTP and is only used over unencrypted HTTP , which _MUST_NOT_ be enabled by [default](#DEF_Default)).

3. Unless scripts intentionally sent to the client actually require access to the cookie value, set the "`HttpOnly`" attribute to prevent JavaScript from reading the cookie.

4. Set the "`Path`" attribute to prevent the client from returning the cookie to any URI outside of your software's own URI space. You _SHOULD_ restrict the client to send the cookie only to the specific URIs within your software that actually need to process the session token.

5. Don't set the "`Domain`" attribute unless you specifically know that the cookie needs to be returned to servers other than the one that set it. You _SHOULD_ design your system to avoid the need. If you do set the "`Domain`" attribute, set it to the most restrictive possible value.

6. Unless your software actively requires the session ID to appear in cross-site requests, use the "`SameSite`" attribute to reduce the cookie's availability to CSRF. You _SHOULD_ eliminate design patterns that rely on cross-site requests.

**Supplemental Guidance:** Note that not all browsers support "`SameSite`", and its CSRF protection would in any case be incomplete. See also [SEC-WEB-CSRF](#SEC-WEB-CSRF).

## SEC-WEB-ID-FR4: Caching
 Control caching of session tokens as follows:

1. If any session token is embedded in the body of any HTTP  response, then direct caching proxies not to cache that response, and direct browsers not to keep the response in local caches, using the "`Cache-Control`" HTTP header. Send only one "`Cache-Control`" header in any response. Include both the "`no-cache`" and "`no-store`" directives.

**Supplemental Guidance:** If your server supports HTTP/1.0 clients, also include
    "`Pragma: no-cache`" in affected HTTP/1.0 responses. You _MAY_ include this in HTTP/1.1 as well.

2. If a session token is embedded in a cookie, but is known *not* to be embedded in the response body, then HTTP/1.1 and HTTP/2 servers _MAY_ restrict caching for cookies only, using
    "`no-cache="Set-Cookie,Set-Cookie2"`" in the "`Cache-Control`" header. Do *not* include this if you disable caching for the entire response.

3. If a session token is included in a HTTP header other than a cookie setting header, then disable caching for that header in a way analogous to that described for
    "`Set-Cookie`" and "`Set-Cookie2`" above.

## SEC-WEB-ID-FR5: Validate before use
 Session IDs allow managing web application sessions. Malicious injection of session IDs can lead to hijacking of sessions. Meticulous tracking and validation of the session IDs is crucial for secure session management. When using session ID to keep [authentication](#DEF_Authentication) state and track user progress within a web application, the application _MUST_ treat the session ID as untrusted data, and sanitize and validate it before use.

## SEC-WEB-ID-FR6: Session Expiration
In order to minimize the time period an attacker can launch attacks over active sessions and hijack them, it is mandatory to set expiration timeouts for every session. Implement Session Expiration as follows:

1. Session timeout management and expiration _MUST_ be enforced server-side and not on the client-side. Session timeout can be set for idle, absolute and renewal sessions.
**Supplemental Guidance:** Idle and Absolute timeout values are highly dependent on how critical the web application and its data are.
[OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#session-expiration) recommends common idle timeouts ranges are 2-5 minutes for high-value applications and 15-30 minutes for low risk applications.
[NIST SP 800-63b Section 4.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#aal1reauth) recommends authentication of the subscriber should be repeated at least once per 12 hours during an extended usage session, regardless of user activity. Reauthentication of the subscriber should be repeated following any period of inactivity lasting 30 minutes or longer. The session should be terminated (i.e., logged out) when either of these time limits is reached.

2. Idle timeout defines the amount of time a session will remain active in case there is no activity in the session. Idle timeout _MUST_ be implemented and _MUST_ adhere to the above recommendation.

3. Absolute timeout defines the maximum amount of time a session can be active, closing and invalidating the session upon the defined absolute period since the given session was initially created by the web application. This does not depend on activity in the session.  Absolute timeout _MUST_ be implemented.

4. Renewal timeout defines the amount of time after which the session token is automatically renewed, in the middle of the user session, and independently of the session activity and, therefore, of the idle timeout.  Renewal timeout _MUST_ be implemented when offering has Absolute timeout outside the range of recommended values.


# Normative References
* [NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html)

# Informative References
* RECIPE: [Secure Session Management](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Secure%20Session%20Management.aspx)
* [Cisco Devnet Security Guide](https://apistyleguide.cisco.com/#!security)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


# Requirement References

    ---
    foreign_id: SEC-WEB-CSRF
    relation: connects
    headline: |-
      SEC-WEB-CSRF deals with cross-site
              request forgery, which is often addressed using tokens
              somewhat similar to the session tokens of SEC-WEB-ID.

    source: PSB
    ---
    foreign_id: SEC-IDL-TMOUT
    relation: connects
    headline: |-
      SEC-IDL-TMOUT
              requires limited session lifetimes.

    source: PSB
    ---
    foreign_id: SEC-LOG-CONTENT
    relation: connects
    headline: |-
      SEC-LOG-CONTENT requires
              logging certain information. If you use an architecture where
              all session state is encoded in a state token, you will have
              to include information needed to create the log entries.

    source: PSB
    ---
    foreign_id: SEC-CRY-PRIM-FR1
    relation: connects
    headline: |-

              All use of cryptography, including the encryption
              and hashing mentioned in SEC-WEB-ID, is required
              to use primitives
              approved under SEC-CRY-PRIM-FR1.
              This is part of the PSB definition of
              good cryptography.

    source: PSB
    ---
    foreign_id: SEC-CRY-RANDOM
    relation: connects
    headline: |-

              All security-sensitive unpredictable quantities, including
              session IDs and encryption/MAC keys, are required
              to be generated as described in
              SEC-CRY-RANDOM.
              This is part of the PSB definition of
              good cryptography.

    source: PSB
    ---
    foreign_id: SEC-CRY-STDCODE-FR1
    relation: connects
    headline: |-
      SEC-CRY-STDCODE-FR1 and other FR's require use
              of standard libraries for cryptographic functions,
              including the encryption, MACs, hashes, and signatures demanded
              by SEC-WEB-ID.
              This is part of the PSB definition of
              good cryptography.

    source: PSB


# History

    ---
    id: SEC-WEB-ID
    version: 4
    affected_psb: SEC-WEB-ID
    impact: normative
    headline: |-
      [SEC-WEB-ID-4]
    description: |-
      Updated content in new PSB format with FR
      Merged SEC-WEB-IDVALID into this PSB as FR5
      Added FR6 to clarify Session Expiration with data from NIST and OWASP


# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: Web user interfaces and HTTP APIs
    category: Web Security
    riskArea: Application & Interface Security
    waivable: true
    version: 4
    id: SEC-WEB-ID
    issueref: ISS_BadSessMgt
    tags:
    - EN/PI
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
    - Cloud
    - FAST
    - EN/PD DT
