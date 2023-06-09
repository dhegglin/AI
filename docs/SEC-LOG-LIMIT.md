# Headline

Control log rates and resource utilization

# Description

It shouldn't be possible to deny service by overwhelming the logging subsystem.

The purpose of rate limiting logs is to ensure that the logging system can't be  used to impact the service of the product.

Denial of service is an *attack of choice* in the modern world.  Processes must not be blocked from running because the log queues are full or because the logging file system is full.  Acknowledged logging protocols are not recommended for this reason.

# Behavior
Logging events typically involves a log originator sending logs to the event collector.  The event collector in turn sends these logs to external systems or stores them locally.  Of the event log actions, the most costly is printing them to the console or saving them locally.  

## SEC-LOG-LIMIT-FR1: Event Logging

Event logs that can be triggered by a user action _MUST_ be limited either directly by the log originator, or by the log collector to prevent a DoS attack from succeeding.  

This _MAY_ be implemented by applying broad limits to logging generated by entire offering instances, entire hosts, or similar large subsystems.  The offer _SHOULD_ have such overall limits even if there are more granular limits.  Such broad limits _SHOULD_ be generous and may be either self-adjusting or configurable by [administrators](#DEF_Administrator).

For example, if the log level set to WARNING and an attacker identifies how to trigger a WARNING level log message, the attacker must not be able to use that vector to impact the service of the device.

## SEC-LOG-LIMIT-FR2: Debug Logging

If turning on debug logging results in a large amount of output, the offer _MUST_ warn the user before enabling this logging level.

The offering _MUST_ provide the ability to specify the verbosity of the debug output, either by limiting the subsystem being debugged, or by varying the level of debug information.

For example, in some cases TAC may turn on logging to debug a problem.  Logs that are not rate limited have overwhelmed systems and caused service disruption.

## SEC-LOG-LIMIT-FR3: Log Alerting

If some events are rate limited to protect the offering, the offering _MUST_ have a way to notify the operator that the logs were limited.  The purpose for such a notification is to allow the operator to respond to a potential security incident.

The logs _SHOULD_ indicate the log message type being limited to allow the operator to quickly identify the source of the attack.  The alerts _MUST_ be such that the operator can programmatically identify the alert.

If some events are not logged because of rate limiting, the total number of suppressed log entries _SHOULD_ still be reported.

# History

```yaml
-----
affected_psb: SEC-LOG-LIMIT-2
description:  Clarification of requirements
---
deprecated_psb: SEC-LOG-LIMIT
impact: normative
headline: >
  [SEC-LOG-LIMIT-2](#SEC-LOG-LIMIT-2) Clarifications and requirements references.
---
deprecated_psb: SEC-LIM-MESS
impact: non-normative
headline: >
  [SEC-LOG-LIMIT](#SEC-LOG-LIMIT) Replaces SEC-LIM-MESS
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
    version: 1
    id: SEC-LOG-LIMIT
    issueref: ISS_LogDoS
    tags:
    - EN/PI
    - PSB/OnPrem
