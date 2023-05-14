# Headline

Enforce idle session timeout

# Key Benefits

Terminals left logged in and idle are attractive to abusers.

This is a step toward compliance with ANSI T1.276-2003 (M-33).

# Behavior

## SEC-IDL-TMOUT-FR1: Systemwide Idle Timeout
It _MUST_ be possible to configure a systemwide timeout after which
idle sessions will automatically be terminated, and/or to configure such
timeouts on per-user or per-group basis, or at other granularities. It
_MUST_ be possible to ensure that some timeout is applied to every
possible user.

# Requirement References

    ---
    foreign_id: FTA_SSL.3(AE)
    relation: connects
    headline: |-
      Be able to audit termination of a remote session
            (initiated by the session timeout/termination
            mechanism).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FTA_SSL.3.1
    relation: implies
    headline: |-
      FTA_SSL.3 TSF-initiated termination FTA_SSL.3.1 The
            TSF shall terminate a remote interactive session after an
            Authorized Administrator-configurable time interval of session
            inactivity.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FTA_SSL.3
    relation: implies
    headline: |-
      Terminate a remote interactive session after a
            [Security Administrator-configurable time interval of session
            inactivity].
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FTA_SSL_EXT.1.1
    relation: implies
    headline: |-
      For local interactive sessions, [selection: (1) lock
            the session - disable any activity of the user's data
            access/display devices other than unlocking the session, and
            requiring that the administrator re-authenticate to the device
            prior to unlocking the session; (2) terminate the session] after
            a Security Administrator-specified time period of
            inactivity.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria

# History

```yaml
-----
affected_psb: SEC-IDL-TMOUT
description:  Updated to functional requirements. 

```


## Older history (manually maintained; may be incomplete)

PSBCTR 4.0 SEC-IDL-TMOUT-2: Don't require systemwide timeout if per-user
timeouts are provided.

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings supporting user
                      "sessions", including AAA servers tracking
                      such sessions

    category: Session Management
    riskArea: Identity & Access Management
    waivable: true
    version: 2
    id: SEC-IDL-TMOUT
    issueref: ISS_AbandSess
    tags:
    - EN/PI
    - PSB/OnPrem
    - EN/PI DT
