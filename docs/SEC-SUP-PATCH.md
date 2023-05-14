# Headline

Propagate upstream security patches

# Key Benefits

Customers can neither be asked to run software that is at risk, nor
prevented from applying security patches due to compatibility concerns.

In many cases, customers may not even be aware of the existence of
third-party software bundled with Cisco [offerings](#DEF_Offering), and
will expect Cisco to provide appropriate protection.

# Description

Upstream security patches need to be incorporated into
[offerings](#DEF_Offering) and into customer installations, and there
must be a process to ensure that users get fixed software.

# Behavior

## SEC-SUP-PATCH-FR1: Determining security relevance of third party software updates:
The offer team _MUST_ evaluate each upstream update to determine whether or not it is security-relevant, and whether the vulnerabilities it addresses are significant to the offer.  Determinations that the vulnerability (or vulnerabilities) addressed in the update are insignificant in the context of the way in which the third-party software is embedded in the offering _MUST_ be documented  by creating, then Junking, a CDETS for that CIAM notification, noting the rationale in the notes of that CDETS.

1.	If an upstream entity reliably designates which of its updates are security-relevant, then all security-relevant updates MUST be incorporated or evaluated for incorporation into the offering in the time frame detailed by PSIRT policy (see FR2) or by documented BE policy (see FR5).

2.	If an upstream entity does not reliably designate security updates, then ALL of that entity's updates MUST be incorporated or evaluated for incorporation into the offering in the time frame detailed by PSIRT policy (see FR2) by documented BE policy (see FR5).

## SEC-SUP-PATCH-FR2:  Applying security updates to software
SEC-SUP-PATCH-FR2:  Applying security updates to software
Any security-relevant (as defined and evaluated per SEC-SUP-PATCH-FR1) upstream update
_MUST_ be actually be incorporated into the offering in accordance with the (Business Entity) policy for patching and updates (see SEC-SUP-PATCH-FR5).  The standard time frame is documented in the [PSIRT defect remediation guidelines](https://psirt.cisco.com/psirt/psirt-risk-communications/#measuring-success), deviations _MUST_ be documented in the BE policy and approved by PSIRT.

## SEC-SUP-PATCH-FR3:  Regular TPS library updates
All Third-Party software versions _MUST_ be updated to the latest stable version in every Major release (as defined in the Business Entity’s policy for patching and updates) of the offering, or at a frequency documented in that policy and approved by the Business Entity and PSIRT (see SEC-SUP-PATCH-FR4).  Exceptions should be documented in the verification notes for this requirement.

## SEC-SUP-PATCH-FR4:  Documented, approved process for applying upstream security updates and patches
The BE _MUST_ have an approved, documented process to guarantee timely incorporation of security-relevant upstream updates, and their propagation into the installed base through customer notification throughout the orderable or supported lifetime of the offering (whichever is longer). It _MAY_ also address policy and rationale for not updating components. This document must be reviewed and approved by the Business Entity responsible executive.  Use the [CSDLThird Party Software Vulnerability Management Process Template](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-20122701) as the basis for this process document.

## SEC-SUP-PATCH-FR5:  Customer notification regarding security updates
Whenever an upstream security update is incorporated into an offering, installed-base customers who are exposed to the vulnerability _MUST_ be notified by PSIRT according to PSIRT’s disclosure process, either individually or via public announcement. Existing customers MUST be given an opportunity to obtain and install the fixed version of the software.

## Evaluating significance

In determining whether a security vulnerability is significant, only
[local](#DEF_Local) behavior, may be considered. The behavior of
[remote](#DEF_Remote) devices is not to be relied upon, even if those
devices are part of the [offering](#DEF_Offering) in question.

Any vulnerability which can be exploited [remotely](#DEF_Remote)
_MUST_ be treated as significant, even if the network communication
required to exploit it involves only “trustworthy” [peers](#DEF_Peer).
This specifically includes the case where the [peer](#DEF_Peer) is known
or expected to be operated by Cisco; customers _MUST_NOT_ be opened
to exploitation by Cisco.

# Normative References
[CSDL Third Party Software Vulnerability Management Process](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-20122701)


# History

```yaml
-----
affected_psb: SEC-SUP-PATCH
description:  Updated to functional requirements.  Clarified timelines, aligned with PSIRT policies.

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings containing third-party software.

    category: Development Process
    riskArea: Software Updates & Patching
    waivable: true
    version: 2
    id: SEC-SUP-PATCH
    issueref: ISS_TPSOld
    tags:
    - EN/PD
    - EN/PI
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
    - Cloud
