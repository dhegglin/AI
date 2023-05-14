# Headline

Disable non-essential services by default.

# Key Benefits

Customers have repeatedly been caught unawares by attacks against features they had not protected, because they did not know that those features were enabled. Many large, security-conscious customers specifically ask for features to be disabled by default.

The words "[essential](#DEF_Essential)" and "[listener](#DEF_Listener)" have strict technical definitions. Some things you may not think of as listeners are listeners; for example, listeners include layer 2 services and Web services URLs. Furthermore, many services that you might think of as "essential" do not qualify as essential for PSB purposes.

# Description

Nothing should accept connections unless the customer has knowingly enabled it.

Many functions, particularly Web services and Web applications, rely on large groups of related [listeners](#DEF_Listener); each Web service may provide many URLs and support multiple operations on each. These listeners typically vary in their centrality to the function.

# Behavior

## SEC-OFF-DEFT-FR1: Disable Non-essential Services

1. In [offerings](#DEF_Offering), non-[essential](#DEF_Essential) [listeners](#DEF_Listener) _MUST_NOT_ be enabled by [default](#DEF_Default).
1. In services, [listeners](#DEF_Listener) which are not used or are not intentionally supported _MUST_NOT_ be enabled.

## SEC-OFF-DEFT-FR2: Enabling a function effect on enabling a listener

1. Enabling a function _MUST_NOT_, by [default](#DEF_Default), enable any listeners not actually [essential](#DEF_Essential) for the function.
1. Enabling a function _MUST_NOT_, by [default](#DEF_Default), enable any listeners that are not believed to be actively used in the majority of installations of that function.

## SEC-OFF-DEFT-FR3: Configuration Settings Enabling a Listener

1. If previous configuration settings have (perhaps implicitly) caused a [listener](#DEF_Listener) to be enabled, then disabling those same options must disable the [listener](#DEF_Listener). It _MUST_NOT_ be necessary to take unrelated steps in other parts of the user interface.
1. If listener or other function A relies on listener B, and the system implicitly enables B in order to comply with an [administrator](#DEF_Administrator) command to enable A, then any later command to disable A _MUST_ also disable B unless there is explicit direction to the contrary from the [administrator](#DEF_Administrator).

## SEC-OFF-DEFT-FR4: Disabling a Listener Impact on Services

1. Disabling a [listener](#DEF_Listener) _MUST_NOT_ have more impact on unrelated services than would enabling that [listener](#DEF_Listener).
1. A system reboot or similar operation _MUST_NOT_ be required when a [listener](#DEF_Listener) is disabled unless that operation is also required to enable that [listener](#DEF_Listener).

## SEC-OFF-DEFT-FR5: Rules for Lower Layers

1. If this requirement demands that a [TCP/IP service](#DEF_TcpIpService) or a link-layer [listener](#DEF_Listener) be disabled, there _MUST_NOT_ be a listening socket for that service.
1. If a process exists only to provide the service, that process _MUST_NOT_ be started. It is not enough to block access using a packet filter or other network traffic filtering system, although such a filter _MAY_ be used as secondary backup measure.

## SEC-OFF-DEFT-FR6: Exception - Public Web Content

1. If an [offering](#DEF_Offering) includes an HTTP server or other "file retrieval" server, and that server itself is either [essential](#DEF_Essential) or has been intentionally enabled by an [administrator](#DEF_Administrator), then that server _MAY_ serve static, [public](#DEF_Public) information without explicit configuration to do so.
1. A Web server enabled to support an [administrative](#DEF_Administer) user interface _MAY_ also offer largely unrelated documentation or software files.

This exception does not authorize any listener which might make a lasting change in the state of the system on which it resides.

# History

---
affected_psb: SEC-OFF-DEFT-3
impact: non-normative
description: Content remains essentially the same, but the format changed according to PSB Re-boot guidelines.

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: >
          [offerings](#DEF_Offering)
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 4
    id: SEC-OFF-DEFT
    issueref: ISS_SurpriseListener
    tags:
    - EN/PD
    - Critical PSB
    - PSB/OnPrem
    - FAST
    - Cloud
