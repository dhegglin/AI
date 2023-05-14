# Headline

Evaluate the attack surface of an operational offering using automated scanning tools

# Key Benefits

When used appropriately, automated scanning tools enable one to probe various aspects of an offering's attack surface in a scalable, repeatable and informative manner.

# Description

There are a number of PSBs that give specific guidance on how to properly secure a variety of attack vectors.  However, before you can apply that guidance you have to know what vectors are present on your offering.  You also need to evaluate and test how those vectors present themselves on the offering. For example - you can't turn off non-essential services or lock down unneeded ports unless you know what services are running or what ports are open.  And then you need to circle back around the verify that you have indeed turned them off and that no new ones show up.

The first step in characterizing the attack surface of an offering is by creating a threat model.  That step is handled by a different requirement.  This requirement provides guidance for the next step: testing the assumptions inherent in the threat model on an operational offering using automated tools.  The goal is to identify the gaps between what we think the attack surface of the offering should look like and what is actually present.

This is not a "one and done" or static operation.  Every time features get added to the offering or software components get upgraded or modified, we have the potential for changes to the attack surface.  Thus, we need a plan for how to continuously evaluate the product and correct issues that arise.  This is also why we want to heavily utilize automated tooling.  Manually performing these evaluations does not scale.

The problem is: no one scan tool is going to going to be appropriate to evaluate the entire attack surface on a given offering.  Thus, you want to be able to intelligently select tools based on an understanding of the offering and the strengths (and weaknesses) of the tool.

# Behavior

Each of the functional requirements below applies to an operational system.  For each requirement we are performing Dynamic Application Security Testing (DAST).

For some of the functional requirements Static Application Security Testing (SAST) may provide better results.  The testing preference is indicated in the appropriate requirements.

## SEC-ASU-SCAN-FR1: Port and Service Scans

The [Offerings](#DEF_Offering) _MUST_ be scanned to identify all [Open Ports](#DEF_OpenPort) and the [Services](#DEF_TcpIpService) attached to those ports.

## SEC-ASU-SCAN-FR2: Protocol Evaluation Scans

For each protocol associated with [Open Ports](#DEF_OpenPort) or active [Services](#DEF_TcpIpService), the behavior of the [Offering](#DEF_Offering) _MUST_ be evaluated when presented with incorrect or poorly constructed datagrams of that protocol (Protocol Fuzzing).

## SEC-ASU-SCAN-FR3: Flooding and DoS Attack Scanning

Denial of Service (DoS) attack opportunities can present themselves in almost any protocol either due to inherent design flaws or implementation issues.

[Reference Flooding](#DEF_ReferenceFlood) scans _MUST_ be performed on the [Offering](#DEF_Offering) to ensure that the offering's behavior complies with the following:

* [SEC-MGT-FLOOD](#SEC-MGT-FLOOD)
* [SEC-BE-STABLE](#SEC-BE-STABLE)
* [SEC-FOR-ATTCK](#SEC-FOR-ATTCK)

If automated scanning tools are available that simulate flooding or DoS attacks for other protocols associated with the offering, those tools _SHOULD_ be run as well

## SEC-ASU-SCAN-FR4: Software Vulnerability Scanning

The [Offering](#DEF_Offering) _MUST_ be scanned for vulnerable versions of software implementing services on the offering

In this requirement we are not scanning the actual source or object code.  We are scanning an operational system over the network and using version information gleaned from discovered services to determine known vulnerabilities.

If SAST tooling is available to identify vulnerabilities in software versions, then that mechanism is preferred to dynamic system testing.

## SEC-ASU-SCAN-FR5: Web Server Scanning

If the [Offering](#DEF_Offering) presents a Web UI, API or other interface where communication occurs using HTTP as part of the protocol stack then a Web Server scan _MUST_ be performed on all such interfaces.

## SEC-ASU-SCAN-FR6: Default Credential Scan

A default credential scan _MUST_ be performed for every service that authorizes and/or authenticates users based on a credential.

If SAST tooling is available to identify default credentials in software, then that mechanism is preferred to dynamic system testing.

## SEC-ASU-SCAN-FR7: Act on Failures or Anomalies

The offering team _MUST_ institute and follow a process that:

1. evaluates all failures and anomalies reported by the scans,
1. remediates any failures or anomalies that represent actual security exposures, and
1. keeps records of the evaluation and actions taken on any remediation

# Informative References
* RECIPE: [Web UI Testing with AppScan](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Web%20UI%20Testing%20with%20AppScan.aspx)

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-MGT-FLOOD
    relation: connects
    headline: >
      SEC-ASU-SCAN requires that flooding and DoS attack scans be performed.  SEC-MGT-FLOOD requires that
      devices to maintain administrative capability during flood attacks
    ---
    source: PSB
    foreign_id: SEC-BE-STABLE
    relation: connects
    headline: >
      SEC-ASU-SCAN requires that flooding and DoS attack scans be performed.  SEC-BE-STABLE requires that
      devices remain stable during and after an attack.
    ---
    source: PSB
    foreign_id: SEC-FOR-ATTCK
    relation: connects
    headline: >
      SEC-ASU-SCAN requires that flooding and DoS attack scans be performed.  SEC-FOR-ATTCK requires that forwarding
      devices maintain their ability to forward traffic during and after an attack

# History

```yaml
-----
affected_psb: SEC-ASU-SCAN-2
description: >
  Updated to functional requirements.
  Extricated requirements from tight coupling with CDSL Vulnerability testing regime in order to put the focus on what we wanted to acheive rather than dictating the method by which it should be achieved.
---
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
          [offering's](#DEF_Offering)
        class: TurnkeyModule_OR_SwThing
    category: Development Process
    riskArea: Risk Assessment
    waivable: true
    version: 3
    id: SEC-ASU-SCAN
    issueref: ISS_NoScan
    tags:
    - EN/PD
    - EN/PI
    - Critical PSB
    - PSB/OnPrem
    
