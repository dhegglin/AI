# Headline

Log all sessions

# Description

These events are useful for tracing intrusion attempts. The Common Criteria require making them "auditable" (i.e. logging them). Many other standards and customer RFPs require them as well.

# Behavior

By default, you _MUST_ log all of the following for user sessions and for all uses of authentication subsystems, regardless of whether authentication is successful, whether acting as client or as server, or the underlying protocol.

## SEC-AUT-LOG-FR1: Session Creation

The following _MUST_ be logged:

1.  Session creation or attempted session creation.
2.  Successful or unsuccessful resumption of [administratively](#DEF_Administrator) locked or suspended sessions.

## SEC-AUT-LOG-FR2: Session Termination

The following _MUST_ be logged:

1.  Session termination by user logout.
2.  Session termination because of error.
3.  [Administrative](#DEF_Administrator) session termination or session locking.

The following _SHOULD_ be logged:

1.  Session termination because of timeout. (NOTE: This is a _MUST_ requirement for products seeking Common Criteria certification.)
2.  Session termination due to excessive user sessions or other resource management issues.

# Informative References

* RECIPE: [Log Security-relevant Information](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Log%20SecurityRelevant%20Information.aspx)
* RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)

# Requirement References

    ---
    foreign_id: FTP_TRP.1(AE)
    relation: implies
    headline: |-
      Be able to audit initiation and termination of the
            trusted channel (for remote administration), with audit detail
            including the claimed identity of the user.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FTA_SSL.4(AE)
    relation: implies
    headline: |-
      Be able to audit termination of an interactive
            session (initiated by the user).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
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
    foreign_id: FTA_SSL_EXT.1(AE)
    relation: implies
    headline: |-
      Be able to audit any attempts at unlocking of a
            locked interactive session.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FIA_UIA_EXT.1(AE)
    relation: implies
    headline: |-
      Be able to audit all use of the identification and
            authentication mechanism, with audit detail including the user
            identity (as provided by the user), and the origin of the
            attempt (e.g. IP address).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FIA_UAU_EXT.2(AE)
    relation: implies
    headline: |-
      Be able to audit all use of the identification and
            authentication mechanism, with audit detail including the user
            identity (as provided by the user), and the origin of the
            attempt (e.g. IP address).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_HTTPS_EXT.1(AE)
    relation: implies
    headline: |-
      Be able to audit Failure to establish an HTTPS
            session, with audit detail including a reason for the failure,
            and identification of the remote endpoint (IP
            address).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_HTTPS_EXT.1(AE)
    relation: implies
    headline: |-
      Be able to audit Establishment/Termination of an
            HTTPS session, with audit detail including identification of the
            remote endpoint (IP address).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria

# History
```yaml
-----
affected_psb: SEC-AUT-LOG
description:  Updated to functional requirements. 

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings
    category: Logging and Auditing
    riskArea: Logging & Monitoring
    waivable: true
    version: 2
    id: SEC-AUT-LOG
    issueref: ISS_Underlogging
    tags:
    - EN/PI
    - CloudCritical
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
