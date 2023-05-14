# Headline

Include identifying information in all log entries

# Description

Incident response requires knowing who (or what) did something (or tried to do something), what was tried, when it was tried, and whether it worked. Include important identifying information in log entries after successfully authenticating that identity.

Many Common Criteria security profiles require these particular fields. The stilted definition of “subject” arises from certain somewhat inapt and archaic formalisms underlying the Common Criteria.

These log messages are administrative log messages and not available to the users of the offering.  In some cases logs may contain sensitive data; however, no information as described in SEC-LOG-NOSENS should be included in the logs. 

# Behavior

## SEC-LOG-CONTENT-FR1: Event

Log messages _MUST_ include what information triggered the log:

1.  What happened, including all of the following that exist for the type of event being logged:
    - Natural identifiers for any affected [targets](#DEF_Target), such as hostname, IP, URL, or port number.
    - Any action attempted, regardless of whether it worked.
    - Application Identifier.
1.  The results of the action, including:
    - Success or failure. 
    - Identify and briefly describe any potentially important lasting effects.


## SEC-LOG-CONTENT-FR2: Location

Log messages _MUST_ include where the event was detected if available:

1. Protocol, API, process, or sub-system that caused or requested the action.
2. Hostname or address of the detecting host.
3. Name of the tenant affected by the event, if the event primarily affects a particular tenant.

## SEC-LOG-CONTENT-FR3: Source

Log messages _MUST_ include the source that triggered the event including all of the following if available:

1.  Identity of the [peer](#DEF_Peer) that sent any message provoking the event such as hostname, IP address, or MAC address.  Note that peer identities are not considered sensitive PII information.
2.  If the source was in the name of one or more [principals](#DEF_Principal) such as login name, userid, or subject name from X.509 certificates.  Note that user identifiers are not considered sensitive PII information.

    - Report any principal name(s) the [peer](#DEF_Peer) *tried* to use.  You _MAY_ omit an invalid username if there is any reason to believe that a password may have been entered in a username field by mistake.
    - Authenticated session [peer](#DEF_Peer) to find the events required to be logged for the session under [SEC-AUT-LOG](#SEC-AUT-LOG).
    - Whether and how the [peer](#DEF_Peer) was authenticated to actually represent the principal(s).
3.  [Authorization](#DEF_Authorization) information used in processing the event such as Cisco IOS "enabled" status or privilege level.

## SEC-LOG-CONTENT-FR4: Time

Log messages _MUST_ include date and time of the event:

1.  Date and time formats in log data must adhere to ISO 8601 formats and include Year, Calendar Dates, and Times down to at least a one second interval (smaller measures when possible). 
2.  Accurate to within 500 ms, and _SHOULD_ keep the full precision of the clock on the generating system.
3.  Synchronized to a central time sourcing device (NTP) and configured for UTC time zone. 

## SEC-LOG-CONTENT-FR5: Log Format

Logs _MUST_ be stored in a standard logging format such as JavaScript Object Notation (JSON), Syslog, etc.

**Supplemental Guidance** : JSON is CSIRT's preferred application logging format, as it is both readable and reasonably compact. Reference [CSIRT Application Log Format](http://go2.cisco.com/CSIRT+Application+Log+Format)

# Informative References

DOD Protection Profile for medium robustness for firewalls - FAU_GEN.1 Audit data generation; Network Security Requirements for Devices Implementing Internet Protocol

- [Cisco Incident Management Policy (primarily affects your reporting):](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-726436&ver=approved)
- [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)
- [SANS database logging guide](https://www.sans.org/reading-room/whitepapers/application/setting-database-security-logging-monitoring-program-34222)
- RECIPE: [Log Security-relevant Information](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Log%20SecurityRelevant%20Information.aspx)
- * RECIPE: [Application Logging and Monitoring](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/ASLR%20in%20Linux%20Systems.aspx)
- RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)

# Requirement References

    ---
    foreign_id: SEC-LOG-CENTRAL
    relation: connects
    headline: |-
    
              For services, SEC-LOG-CENTRAL
              requires sending all logging to a central point. Furthermore,
              that central point is required to be able to query
              the logs using the fields required in SEC-LOG-CONTENT.
    
    source: PSB
    ---
    foreign_id: SEC-LOG-PROTO
    relation: connects
    headline: |-
    
              SEC-LOG-CONTENT describes the information to be
              included in log message.
              SEC-LOG-PROTO
              describes how to deliver
              that information, including how to structure it
              for further processing at the collector.
    
    source: PSB
    ---
    foreign_id: SEC-AUT-LOG
    relation: connects
    headline: |-
    
              It must be possible to associate events generated
              during a session with the events that record
              that session's creation. Those events are described
              in SEC-AUT-LOG.
    
    source: PSB
    ---
    foreign_id: SEC-NTP-AUTH
    relation: connects
    headline: Maintain accurate date and time
    source: PSB
    ---
    foreign_id: FTP_ITC.1(AE)
    relation: connects
    headline: |-
      Be able to audit initiation and termination of a
            trusted channel (for remote administration). Related CC NDPP
            requirements include FCS_IPSEC_EXT.1, FCS_TLS_EXT.1,
            FCS_HTTPS_EXT.1, and FCS_SSH_EXT.1.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FTA_SSL.4(AE)
    relation: connects
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
    relation: connects
    headline: |-
      Be able to audit any attempts at unlocking of a
            locked interactive session.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FPT_TUD_EXT.1(AE)
    relation: connects
    headline: |-
      Be able to audit initiation of an update to firmware
            or software. As required by PSB SEC-AUD-FIELD-3, audit detail
            must identify the entity/user that initiated the
            update.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FPT_STM.1.1
    relation: connects
    headline: |-
      Be able to provide reliable time stamps for applying
            timestamps to audit records (i.e. real time clock with battery
            to maintain time during reboot or power loss).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FIA_UIA_EXT.1(AE)
    relation: connects
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
    relation: connects
    headline: |-
      Be able to audit all use of the identification and
            authentication mechanism, with audit detail including the user
            identity (as provided by the user), and the origin of the
            attempt (e.g. IP address). (This audit event is redundant to the
            CC Auditable Event for FIA_UIA_EXT.1.)
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_TLS_EXT.1(AE)
    relation: connects
    headline: |-
      Be able to audit failure to establish a TLS session,
            with audit detail including reason for the failure (the reason
            can be somewhat generic, like failed to negotiate ciphers). This
            audit message may be redundant to an audit message for failure
            to establish an HTTPS session.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_TLS_EXT.1(AE)
    relation: connects
    headline: |-
      Be able to audit establishment and termination of a
            TLS session, with audit detail including identification of the
            remote endpoint (e.g. IP address, hostname, etc.). This audit
            message may be redundant to an audit message for
            establishment/termination of an HTTPS session.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_SSH_EXT.1
    relation: connects
    headline: |-
      CC Requirement Enhancement: Ensure that the
            administrator will have the ability to restrict (inbound and
            outbound) SSH session establishment to use only DH Group 14, or
            at least allow restriction to DH Group 14 or
            larger/stronger. This requires more than just ensuring during
            session negotiation that the remote endpoint supports DH-14, it
            requires ensure that the session will not be established with a
            lesser DH group. Ensure that the SSH implementation supports
            SSHv2, using the latest Cisco Common Cryto Module (C3M) is
            recommended.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_SSH_EXT.1(AE)
    relation: connects
    headline: |-
      Be able to audit establishment and termination of an
            SSH session, with audit detail including identification of the
            remote endpoint (e.g. IP address, hostname, etc.).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_IPSEC_EXT.1(AE)
    relation: connects
    headline: |-
      Be able to audit failure to establish an IPsec SA,
            with audit detail including reason for the failure (the reason
            can be somewhat generic, like failed to negotiate
            ciphers).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_IPSEC_EXT.1(AE)
    relation: connects
    headline: |-
      Be able to audit establishment and termination of an
            IPsec SA, with audit detail including identification of the
            remote endpoint (e.g. IP address, hostname, etc.).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_HTTPS_EXT.1(AE)
    relation: connects
    headline: |-
      Be able to audit failure to establish an HTTPS
            session, with audit detail including reason for the failure (the
            reason can be somewhat generic, like failed to negotiate
            ciphers). This audit message may be redundant to an audit
            message for failure to establish a TLS session.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FCS_HTTPS_EXT.1(AE)
    relation: connects
    headline: |-
      Be able to audit establishment and termination of an
            HTTPS session, with audit detail including identification of the
            remote endpoint (e.g. IP address, hostname, etc.). This audit
            message may be redundant to an audit message for
            establishment/termination of a TLS session.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FAU_GEN.2.1
    relation: implies
    headline: |-
      For audit events resulting from actions of identified
            users, be able to associate each auditable event with the
            identity of the user that caused the event.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FAU_GEN.1.2.a
    relation: implies
    headline: |-
      Each audit record must contain: Date and time of the
            event, type of event, subject identity, and the outcome (success
            or failure) of the event.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FAU_GEN.1.2
    relation: implies
    headline: |-
      The TSF shall record within each audit record at
            least the following information: a) Date and time of the event,
            type of event, subject identity, and the outcome (success or
            failure) of the event; and b) . Refer to any "Event"" and
            ""Detail"" listed in the ""Audit Requirements"" column of this
            spreadsheet."
    targets:
    - WLANPPv1.0(2011)
    source: Common Criteria

# History

```
-----
affected_psb: SEC-LOG-CONTENT-3
description: >
  Updated functional requirements to be more clear.  Moved specific requirements to the appropriate sections.  Added requirement for external time sync.
impact: normative
-----
affected_psb: SEC-LOG-CONTENT-2
description: >
  Incorporated Attributes and Format for Enterprise applications and added details in Verification section.
impact: normative
---
deprecated_psb: SEC-LOG-CONTENT
impact: non-normative
headline: >
[SEC-LOG-CONTENT](#SEC-LOG-CONTENT) migrated to functional requirements, added attributes for enterprise applications, and more detail on verifications
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
    version: 3
    id: SEC-LOG-CONTENT
    issueref: ISS_Underlogging
    tags:
    - EN/PI
    - CloudCritical
    - PSB/OnPrem
    - Cloud
