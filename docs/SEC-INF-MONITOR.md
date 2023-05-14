# Headline

Provide traffic monitoring and threat detection

# Behavior

## SEC-INF-MONITOR-FR1: Attack and Threat Detection

Threats can be detected by content signature recognition and/or behavioral monitoring. You _MUST_ look for attacks on Cisco or others from people and sources both inside and outside Cisco. Use automated systems to examine:

* Logs generated by your application software
* Logs generated by the underlying operating systems and other infrastructure
* Network data collected at the same monitoring points mentioned above

You _SHOULD_ use the information in these logs to monitor for the following threats:

1. Data leakage/breaches: Information read or copied by unauthorized
   people or machine [agents](#DEF_Agent), or moving outside of
   the [controlled spaces](#DEF_ControlledSpace) intended to contain it.
1. Account hijacking: Taking control of an account, for example by
   exploiting a password change system or falsely changing contact
   information. You _SHOULD_ monitor for any unauthorized use of any
   account.
1. Use of improperly secured APIs or APIs not meant to be available.
1. Unusual or unexpected numbers of unauthorized access attempts, or
   other signs of attempts to gain access by brute force trial This
   applies both to attempts to access the offering's own services and
   to attempts to access the underlying infrastructure. You _SHOULD_
   detect both "fast" high-volume attacks and "slow" attacks over long
   periods of time.
1. Denial of service attacks, including flooding attacks and
   participation in distributed denial of service.
1. Abuse of services, including--
   1. Providing malicious Web or other services (phishing landing points,
      malware distribution, illegal data distribution, etc).
   1. Botnet control.
   1. Scanning or other reconnaissance for attacks on networks inside or outside of Cisco.
   1. Service-specific forms of abuse.
1. Propagation or execution of [malware](#DEF_Malware).

## SEC-INF-MONITOR-FR2: Incident Response

Humans _MUST_ continuously watch for and respond to incidents including, but not limited to:

* Attack and threat detection system events
* Security events
* Incidents reported by users or staff

You _SHOULD_ use CSIRT's incident response services. All other incident response systems _MUST_ be approved by CSIRT, including your own incident responst system.

Human monitoring and response _MUST_ continue whenever any part of
the [offering](#DEF_Offering) or its infrastructure is operating or
reachable over any network, including during nights, weekends, holiday
or vacation periods, etc.

## SEC-INF-MONITOR-FR3: CSIRT Access to Systems

Give CSIRT as a group, or responders designated by CSIRT, the
below-listed access to your [offering](#DEF_Offering) and its underlying
infrastructure. CSIRT _MAY_ choose to delegate this access as part of
approving an offering-specific incident response function.

1. If you create your offering using non-Cisco services (for example
   virtual machine "cloud infrastructure"), designate the CSIRT
   responders as security incident contacts for your service
   providers.
   Authorize the responders to have whatever authority the service
   providers usually give to such contacts. This includes the
   authority to have service shut down temporarily in emergencies.
   You _MUST_ see to it that the right CSIRT responders are enrolled
   in any authentication system the provider uses for incident
   contacts.  CSIRT will provide you with an email address for
   incoming reports; at the time of this writing, the address is
   "csirt-notify@cisco.com".
1. Allow the responders to view and copy all logs in the central
   logging system required by [SEC-LOG-CENTRAL](#SEC-LOG-CENTRAL),
   without any need to involve non-CSIRT staff. You _MAY_ do this by
   forwarding all log entries to a system designated by CSIRT.
   Note that [SEC-LOG-ATTACK](#SEC-LOG-ATTACK) requires the logs to
   include the events reported by your attack and threat detection
   system.
1. Allow the responders to view and copy all flow data you are
   required to collect under the "traffic monitoring" section above,
   without any need to involve non-CSIRT staff. You _MAY_ do this by
   sending all flow data to a central system designated by CSIRT.
1. Allow the responders to trigger any data preservation, freezing, or
   "snapshotting" capability of the [offering](#DEF_Offering) or its
   underlying infrastructure. This _SHOULD NOT_ include any operation
   that would seriously degrade [offering](#DEF_Offering) performance.

Without help from regular operation staff, CSIRT _SHOULD NOT_ not be
allowed to change offering configurations, to modify offering data, or
to view any customer-provided data or any sensitive PII not included
in logs. You _SHOULD_ log CSIRT's use of any access beyond that
available to [offering](#DEF_Offering) users in general.

## SEC-INF-MONITOR-FR4: Incident Reporting

Your procedures _MUST_ ensure that any sign of any of the incidents
below, noticed by any member of your staff, is reported to CSIRT within
24 hours of discovery. Incidents _SHOULD_ be reported immediately.

1. An unauthorized agent getting access to the infrastructure
   underlying an [offering](#DEF_Offering). Examples include unexpected
   operating-system-level logins to servers, routers, or other
   devices, unexpected access to databases or other "backend"
   services, etc. This does not include unauthorized use of
   the [offering](#DEF_Offering) itself, except where there is some
   other reason to report the incident.
   Exception: You need not report access by a Cisco employee or other
   "internal" user if the access:
   1. appears to have been accidental,
   1. hasn't caused service disruption or unauthorized use of data, and
   1. shows no sign of being malicious or of having compromised other
      security
      An example of a non-reportable event might be an SSH login to the
      "wrong machine" followed immediately by logging out.
1. An unusually sustained, widespread, systematic, or well-resourced
   attempt at unauthorized [access](#DEF_Access)to
   the [offering](#DEF_Offering) or any [target](#DEF_Target) in
   the [offering](#DEF_Offering).
1. An unusual method of attempting unauthorized access.
1. Any malicious activity that degrades or threatens the availability
   or usability of the [offering](#DEF_Offering).
1. Non-[public](#DEF_Public) information appearing outside of
   the [controlled space](#DEF_ControlledSpace) meant to contain that
   information, or corruption or modification of information that
   should have been protected by
   any [controlled space](#DEF_ControlledSpace), if any of the
   following apply--
   1. The event results from intentionally disrupting the normal
      operation of the system, evading any technical or procedural
      security control, or violating any applicable policy or law.
   1. You are not sure you understand how or why the event happened.
   1. You are not sure that you have found and deleted _all copies_ of
      all "leaked" information outside of the appropriate controlled
      space.
   1. You suspect that the event may recur.
1. Any bug, misconfiguration, misclassification, overauthorization, or
   other error by Cisco or its service providers, making any of the
   following information available against the intentions of
   its [controlling policy entity](#DEF_ControllingPolicyEntity), even
   if you're not sure the information was actually viewed or copied.
   1. Data classified as Cisco Confidential or higher, or as Customer
      data, under the classification scheme of
      Cisco's [Data Protection Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806757&ver=approved).
   1. Data classified as [sensitive personally identifiable information](#DEF_SPII) under
      _any_ of the following conditions:
      1. The [PSB definition](#DEF_SPII)
      1. [Cisco's Business Personal Data Protection and Privacy Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1106658&ver=approved)
      1. An applicable law or regulation of any jurisdiction in which
         the [offering](#DEF_Offering) operates or is available.
   1. Any other [sensitive](#DEF_Sensitive) information as defined in
      the PSB.
1. [Malware](#DEF_Malware) executing on any system involved in
   the[offering](#DEF_Offering), presence of [malware](#DEF_Malware)
   _capable_ of infecting the [offering](#DEF_Offering), or presence of
   any [malware](#DEF_Malware) code at all outside of user-uploaded
   data.
1. Presence of data which the [offering](#DEF_Offering) cannot legally
   hold or process (eg child pornography).

## SEC-INF-MONITOR-FR5: Traffic Monitoring

Note: This section applies only to data center deployments. It does not currently apply to public cloud deployments.

Record the identifying information, time, duration, and data volume of
each network connection or flow--

1. Between any part of the service and any network element outside of
   the service,
1. Between major components of the service, and
1. At any other point(s) you think would be useful for forensic analysis.

Unless required by another PSB requirement or a non-PSB Cisco policy, retain the records according to the [SEC-LOG-RET PSB](#SEC-LOG-RET). Provide a system for viewing, querying, and analyzing the information.

## SEC-INF-MONITOR-FR6: Enterprise Monitoring

```
   applicability:
      - force: mandatory
        target:
         class: ServiceThing
         restrict: Enterprise
```

Infrastructure event monitoring _MUST_ be configured for devices, hosts and platforms hosting Enterprise applications.

1. If the offering is hosted on an IT-managed platform, then infrastructure monitoring should be in place.
1. If the offering is **not** hosted on an IT-managed platform, you _MUST_ engage with CSIRT to establish infrastructure security monitoring. _(See Informative References)_

## SEC-INF-MONITOR-FR7: Log Content

You _MUST_ adhere to [SEC-LOG-CONTENT](#SEC-LOG-CONTENT) for log content and format.

# Informative References

* RECIPE: [Log Security-relevant Information](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Log%20SecurityRelevant%20Information.aspx)
* RECIPE: [Application Logging and Monitoring](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/ASLR%20in%20Linux%20Systems.aspx)
* RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)
* [Cisco Incident Management Policy (primarily affects your reporting):](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-726436&ver=approved)
* [Cisco’s Data Protection Policies](http://wwwin.cisco.com/c/cec/organizations/security-trust/infosec/policies.html)
* [CSIRT: Engagement Guide for new AND non-standard Platforms/Environments](https://cisco.sharepoint.com/sites/CSIRTCloudSecurityMonitoring)
* [CSIRT: AWS Implementation Guide](https://cisco.sharepoint.com/:w:/r/sites/CSIRTCloudSecurityMonitoring/_layouts/15/Doc.aspx?sourcedoc=%7B4B1FEEB1-4FC3-4A44-B549-7A948B56241C%7D&file=AWS%20Implementation%20Guide.docx&action=default&mobileredirect=true)
* [CSIRT: Azure Implementation Guide](https://cisco.sharepoint.com/sites/CSIRTCloudSecurityMonitoring/CSIRT%20Cloud%20Security%20Monitoring%20Docs/Public%20Clouds%20(AWS,%20Azure,%20GCP)/Azure/CSIRT-Azure_Initial_Account_Creation-20200326-002.pdf?csf=1&e=3EfENx&cid=c2a9c5e5-d3ba-4fd1-b024-c26926bdb2d9)
* [CSIRT: Cisco Data Center](https://cisco.sharepoint.com/:w:/r/sites/CSIRTCloudSecurityMonitoring/_layouts/15/Doc.aspx?sourcedoc=%7BA30A7579-A970-49F5-AE49-DF2E872805D9%7D&file=Data%20Center%20Implementation%20Guide.docx&action=default&mobileredirect=true)
* [CSIRT: GCP Implementation Guide](https://cisco.sharepoint.com/sites/CSIRTCloudSecurityMonitoring/CSIRT%20Cloud%20Security%20Monitoring%20Docs/Public%20Clouds%20(AWS,%20Azure,%20GCP)/GCP/GCP%20CSIRT%20Implementation%20Guide.pdf?csf=1&e=WydYn2&cid=0bfb975c-3797-4ed7-9438-43c24bf07920)

# Normative References

* [Data Protection Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806757&ver=approved)
* [Business Personal Data Protection and Privacy Policy (Internal)](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1106658&ver=approved)

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-LOG-CENTRAL
    relation: connects
    headline: >
        [SEC-LOG-CENTRAL](#SEC-LOG-CENTRAL)requires delivering logged data to
        a central location. Logs in general are used together with information
        required by SEC-INF-MONITOR, and many of the events you detect by
        complying with SEC-INF-MONITOR will generate events in the central log
        stream.
    ---
    source: PSB
    foreign_id: SEC-LOG-CONTENT
    relation: connects
    headline: >
        [SEC-LOG-CONTENT](#SEC-LOG-CONTENT)Incident response requires knowing
        who (or what) did something (or tried to do something), what was tried,
        when it was tried, and whether it worked. Include important identifying
        information in log entries.
    ---
    source: PSB
    foreign_id: SEC-LOG-ATTACK
    relation: connects
    headline: >
        [SEC-LOG-ATTACK](#SEC-LOG-ATTACK)requires logging detected indications
        of malicious activity. The monitoring required by SEC-INF-MONITOR will
        generate many such events.
    ---
    source: PSB
    foreign_id: SEC-PRV-ERASE
    relation: connects
    headline: >
        SEC-INF-MONITOR requires you to collect monitoring data including flow
        data. Since these include[PII](#DEF_PII)in the form of IP addresses
        and possibly other information, in nearly all
        cases[SEC-PRV-ERASE](#SEC-PRV-ERASE) _forbids_ you to retain the data
        for more than 180 days.

#History

-----
affected_psb: SEC-INF-MONITOR-4
description: >
  Added Funtional Requirement FR7 to point to SEC-LOG-CONTENT for mandatory format for associated logs.
impact: normative
---

# Attributes

    id: SEC-INF-MONITOR
    version: 5
    category: Operational Process
    riskArea: Logging & Monitoring
    legallysensitive: false
    waivable: true
    issueref: ISS_NetArch
    applicability:
      - force: mandatory
        target:
          class: ServiceThing
          restrict: >
            Services
    priority: 8
    phase: requirements
    tags:
    - CloudCritical
    - Cloud