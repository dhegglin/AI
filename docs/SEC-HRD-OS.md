# Headline

Harden production components

# Description

Configure each Operating System in the system in accordance with
applicable hardening guides or Cisco hardening scripts.

# Behavior

## SEC-HRD-OS-FR1:  Harden Operating System

Configure each Operating System in the system in accordance with
applicable hardening guides or Cisco hardening scripts (selected as
described below).

Select at least one appropriate hardening guide for your OS from the following
sources, in order of preference:

1.  Refer to the Center for Internet Security's [Benchmarks Hardening
    Guides](https://www.cisecurity.org/cis-benchmarks/) to find
    component hardening guides for all included components, and complete
    the recommendations from those hardening guides. For CIS Benchmarks
    with both Level 1 and Level 2 recommendations, both Level 1 and
    Level 2 recommendations _MUST_ be implemented.
2.  Alternative hardening guides from the application publisher or other
    well-known security organizations _MAY_ be used when CIS
    Benchmarks are unavailable or another standard better aligns with
    the offering’s certification strategy (e.g. DISA STIGs)
3.  You _MAY_ use vendor or community hardening guides for further guidance.

You _MUST_ document all included OS and corresponding OS hardening
guides which are used in your offering. If there is no applicable
hardening guide for an OS, document that fact.

You _MAY_ choose not to implement specific recommendations within a
guide as necessary (e.g. when the recommendation impedes the offering’s
performance or functionality), but you _MUST_ document your reasons
for each such deviation. You _MAY_ choose an equivalently secure
alternative solution to a specified recommendation, but you _MUST_
document your reasons and explain how/why the alternate solution is at
least equivalent to the recommendation in the guide.

# Normative References

[Center for Internet Security's Baseline Hardening
Guides](https://benchmarks.cisecurity.org/downloads/audit-tools/)

[Cisco's Hardening Orchestration and Verification
Tools](https://cisco.sharepoint.com/Sites/Cloud9)

# Requirement References

    ---
    foreign_id: A.12.5
    relation: connects
    headline: |-

              ISO 27002:2013: A.12.5 Control of operational software

    targets:
    - '12'
    source: ISO 27002:2013
    ---
    foreign_id: A.12.6
    relation: connects
    headline: |-

              ISO 27002:2013: A.12.6 Technical vulnerability management

    targets:
    - '12'
    source: ISO 27002:2013

# History
```yaml
-----
affected_psb: SEC-HRD-OS
description:  Updated to functional requirements. 

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: offerings that include an Operating System
        class: SwOs
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 1
    id: SEC-HRD-OS
    issueref: ISS_SoftHosts
    tags:
    - Hardening
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
