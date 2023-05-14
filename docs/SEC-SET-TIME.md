# Headline

Maintain accurate date and time

# Key Benefits

Time stamps must be accurate for correlation of logged events. Some
authentication protocols, notably Kerberos and PKI certificate
verification, rely on time of day.

# Description

Products need to know the time and date. NTP is almost always the best
way to do this.

# Behavior

## SEC-SET-TIME-FR1: Maintaining Accurate Time

1. Each [offering](#DEF_Offering) _MUST_ support maintaining accurate knowledge of the current time, within 500 milliseconds of actual clock time. Absolute time referenced to UTC _MUST_ be maintained; local time zone information _MAY_ additionally be maintained.

# Informative References

ANSI T1.276-2003: Baseline Security Requirements for the Management
Plane

# Requirement References

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
    foreign_id: FPT_STM.1.1
    relation: connects
    headline: |-
      Be able to audit all changes to the time, and ensure
            that audit detail will include the old and new values for the
            time, and the origin of the attempt to change the time
            (e.g. username, or IP address of an NTP server).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FPT_STM.1
    relation: implies
    headline: |-
      FPT_STM.1 Reliable Time Stamp FPT_STM.1.1 The TSF
            shall be able to provide reliable time stamps for its own
            use.
    targets:
    - WLANPPv1.0(2011)
    source: Common Criteria

# History

```yaml
-----
affected_psb: SEC-SET-TIME
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
          standalone devices
    - force: mandatory
      target:
        restrict: |-
          offerings not receiving
                      time information from
                      a user platform
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 1
    id: SEC-SET-TIME
    issueref: ISS_BadTime
    tags:
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - FAST
    - EN/PI DT
