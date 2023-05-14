# Headline

Prevent Click-Jacking

# Key Benefits

Click-jacking utilizes multiple rendering layers to trick a user into
clicking on a button or link on a lower-layer page while the click was
intended for the top level page seen by the user. Keystrokes can be
hijacked in a similar fashion using a carefully crafted combination of
stylesheets, iframes, and text boxes. This routes the clicks or
keystrokes to the lower-layer page.

The lower-layer page may be owned by another application accessed with
the victim's credentials, tricking the victim to perform unintended
actions in the invisible application. Alternatively, the lower-layer
page may be owned by the malicious user, tricking the victim into
entering [sensitive](#DEF_Sensitive) information, such as credentials.

# Description

Protect against click-jacking attacks to prevent coerced user actions.

Click-jacking is a type of attack where the attacker tricks the victims
to click on the link which is not visible to them and either redirecting
them to attacker-controlled website or do an action that victim is not
aware of. Click-jacking utilizes multiple rendering layers to trick a user into
clicking on a button or link on a lower-layer page while the click was
intended for the top level page seen by the user. Keystrokes can be
hijacked in a similar fashion using a carefully crafted combination of
stylesheets, iframes, and text boxes. This routes the clicks or
keystrokes to the lower-layer page.

The lower-layer page may be owned by another application accessed with
the victim's credentials, tricking the victim to perform unintended
actions in the invisible application. Alternatively, the lower-layer
page may be owned by the malicious user, tricking the victim into
entering sensitive information, such as credentials.

# Behavior

All web applications have to protect all pages so that they cannot be used
as lower-layer pages in a click-jacking attack. If the page is
explicitly meant to be embedded as an iframe, then mitigations should be
used, where possible, to limit which parent pages are allowed to embed the frame.
Although XFrame header has been traditionally used to provide this protection,
newer browsers are supporting the protection using Content Security Policy.
Hence both mitigations are required.

ClickJacking protection can be built using the below feature requirements.

## SEC-WEB-CLCKJACK-FR1: Defending with Content Security Policy (CSP) frame-ancestors directive

The frame-ancestors directive _MUST_ be used in a Content-Security-Policy HTTP response header to indicate whether or not a browser should be allowed to render a page in a `<frame>` or `<iframe>`. Sites can use this to avoid Clickjacking attacks by ensuring that their content is not embedded into other sites.
frame-ancestors allows a site to authorize multiple domains using the normal Content Security Policy semantics.
    
**Supplemental Guidance:** Include either ‘none’ or ‘self’ to prevent any domain from framing the content. This setting is recommended unless a specific need has been identified for framing.

- Content-Security-Policy: frame-ancestors 'none'; (prevents any domain from framing the content)
- Content-Security-Policy: frame-ancestors 'self'; (which allows current site to frame content)
- Content-Security-Policy: frame-ancestors uri; (which allows
specified uri to frame this page - Ex: frame-ancestors http://www.example.com)

Refer - [Browser support for frame-ancestors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors)

## SEC-WEB-CLCKJACK-FR2: Defending with X-Frame options header

The X-Frame-Options HTTP response header _MUST_ be used to indicate whether or not a browser should be allowed to render a page in a `<frame>` or `<iframe>`. Sites can use this to avoid Clickjacking attacks, by ensuring that their content is not embedded into other sites. Set the X-Frame-Options header for all responses containing HTML content. The possible values are "DENY", "SAMEORIGIN", or "ALLOW-FROM uri"
    
**Supplemental Guidance:** There are three possible values for the X-Frame-Options header:

- `DENY`, which prevents any domain from framing the content. The `DENY` setting is recommended unless a specific need has been identified for framing.
- `SAMEORIGIN`, which only allows the current site to frame the content.
- `ALLOW-FROM` uri, which permits the specified 'uri' to frame this page. (Ex: `ALLOW-FROM http://www.example.com` ).
Web proxies are notorious for adding and stripping headers. If a web proxy strips the X-Frame-Options header then the site loses its framing protection.

Refer - [Browser support for X-Frame-Options](https://caniuse.com/?search=X-Frame-Options)

# Normative References

- [OWASP Click-Jacking Guide](https://www.owasp.org/index.php/Clickjacking)
- [OWASP Click-Jacking Defense Cheat Sheet](https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet)

# Informative References

* [Browser support for frame-ancestors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors)
* [Browser support for X-Frame-Options](https://caniuse.com/?search=X-Frame-Options)

# History

```
    ---
    id: SEC-WEB-CLCKJACK
    version: 3
    affected_psb: SEC-WEB-CLCKJACK
    impact: normative
    headline: |-
      [SEC-WEB-ID-3]
    description: |-
      Updated content in new PSB format with FR
      Mandated both X-Frame-Options and CSP frame-ancestors
      Updated Verification to check for both
```

# Attributes

    ---
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
    id: SEC-WEB-CLCKJACK
    issueref: ISS_Clickjack
    tags:
    - EN/PI
    - CloudCritical
    - PSB/OnPrem
    - Cloud
    - FAST
