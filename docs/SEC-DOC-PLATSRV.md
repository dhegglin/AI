# Headline

List needed user platform TCP/IP services

# Key Benefits

This information is necessary to enable a thorough assessment of the
security risks associated with the operation of the
[product](#DEF_Product), and to determine what steps should be taken to
mitigate risk. This includes making decisions about responding to
security advisories and patch releases.

# Description

If the customer is to provide a platform for an application, the
customer needs to know which servers need to be running on the
platform... and what ports they're using, what they're doing, what
happens if they're turned off...

# Behavior

## SEC-DOC-PLATSERV-FR1: Document essential services
Each [application](#DEF_Application)'s user documentation _MUST_ list
all [TCP/IP services](#DEF_TcpIpService) that the
[product](#DEF_Product) requires the [user platform](#DEF_UserPlatform)
to offer.

## SEC-DOC-PLATSERV-FR2: Document non-essential services
The documentation _MUST_ include every [TCP/IP
service](#DEF_TcpIpService) which could possibly be disabled by a
knowledgeable [administrator](#DEF_Administrator) without compromising
the [essential](#DEF_Essential) FUNCTIONs of the [user
platform](#DEF_UserPlatform).

## SEC-DOC-PLATSERV-FR3: Required service descriptors
The information given for each [TCP/IP service](#DEF_TcpIpService)
_MUST_ include--

- The name of the [TCP/IP service](#DEF_TcpIpService), as usually
  known to [administrators](#DEF_Administrator).

- A brief description of the function of the [TCP/IP
  service](#DEF_TcpIpService), including its purpose in general, how
  it is used by the [product](#DEF_Product), and the impact of
  disabling it.

- An explanation of which specific network nodes must have access to
  the [TCP/IP service](#DEF_TcpIpService) to enable proper
  [product](#DEF_Product) operation, e.g.--

  - "This service must be accessible to all end users"
  - "This service must be accessible from any network management
    station"
  - "This service need only be accessible via IP loopback from the
    local host"

- The name of the protocol used by the [TCP/IP
  service](#DEF_TcpIpService), and, if the protocol is a standard or
  publicly documented protocol, a reference to the protocol
  specification.

- Any recommendations or requirements for the configuration of the
  [TCP/IP service](#DEF_TcpIpService).

- Any recommendations or requirements for restricting access to the
  [TCP/IP service](#DEF_TcpIpService).

- The TCP and UDP port numbers[, IP](#DEF_IP) protocol numbers, or
  other addresses used by the [TCP/IP service](#DEF_TcpIpService).

  If the [TCP/IP service](#DEF_TcpIpService) uses dynamically assigned
  port numbers, this _SHOULD_ include the ranges from which those
  numbers may be drawn.

  If there is a reasonable method of configuring the [user
  platform](#DEF_UserPlatform) or the [product](#DEF_Product) to
  restrict the ranges from which dynamically assigned port numbers
  will be taken, that method _SHOULD_ be described.

- Recommended methods of recognizing traffic associated with this
  service for filtering or QoS purposes.

**Supplemental Guidance**
- In determining what a knowledgeable
  [administrator](#DEF_Administrator) might disable, that person is to
  be assumed to completely understand the internal operation of the
  [user platform](#DEF_UserPlatform), and to be capable of editing
  configuration files, modifying registry entries, removing programs
  and files from the file system, and similar actions. The mere
  absence of a simple user interface for disabling a [TCP/IP
  service](#DEF_TcpIpService) does not imply that a knowledgeable
  [administrator](#DEF_Administrator) cannot disable it.

# Informative References

ANSI T1.276-2003 Baseline Security Requirements for the Management Plane

ENG-83132, Serviceability Design Requirements for Security

# History


```
-----
affected_psb: SEC-DOC-PLATSERV
impact: non-normative
headline: >
    [SEC-DOC-PLATSERV](#SEC-DOC-PLATSERV) migrated to functional requirements.
```
# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          applications
    category: Application Security
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-DOC-PLATSRV
    issueref: ISS_BlackBoxApp
    tags:
    - EN/PI
    - PSB/OnPrem
