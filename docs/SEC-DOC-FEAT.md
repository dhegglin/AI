# Headline

List needed user platform system processes

# Key Benefits

This information is necessary to enable a thorough assessment of the
security risks of using the [application](#DEF_Application), and to
determine what steps should be taken to mitigate them. This includes
making decisions about responding to security advisories and patch
releases.

# Description

If the customer is to provide a platform for an application, the
customer needs to know which services can safely be turned off,
filtered, or restricted to secure that platform.

# Behavior

## SEC-DOC-FEAT-FR1: Describe essential system processes
Each [application](#DEF_Application)'s user documentation _SHOULD_
describe all [system processes](#DEF_SystemProcess) which must be run on
the [user platform](#DEF_UserPlatform) to support any part of the
[application](#DEF_Application). Examples might include database
managers, HTTP servers, hardware configuration daemons (eg udev), D-Bus,
etc.

## SEC-DOC-FEAT-FR2: Describe non-essential system processes
The documentation _SHOULD_ include all [system
processes](#DEF_SystemProcess) which could possibly be disabled by a
knowledgeable [administrator](#DEF_Administrator) without compromising
the [essential](#DEF_Essential) FUNCTIONs of the [user
platform](#DEF_UserPlatform).

**Supplemental Guidance**
The information given for each [system process](#DEF_SystemProcess)
_SHOULD_ include--

-   The name of the [system process](#DEF_SystemProcess), as usually
    known to administrators of the [user platform](#DEF_UserPlatform).

-   A brief description of the function of the [system
    process](#DEF_SystemProcess), including its purpose in general, how
    it is used by the [product](#DEF_Product), and the impact of
    disabling it.

-   Any recommendations or requirements for the configuration of the
    [system process](#DEF_SystemProcess).

-   A list of any [TCP/IP services](#DEF_TcpIpService) provided by the
    [system process](#DEF_SystemProcess).

**Supplemental Guidance**
    In determining what a knowledgeable
    [administrator](#DEF_Administrator) might disable, that person is to
    be assumed to completely understand the internal operation of the
    [user platform](#DEF_UserPlatform), and to be capable of editing
    configuration files, modifying registry entries, removing programs
    and files from the file system, and similar actions. The mere
    absence of a simple user interface for disabling a [system
    process](#DEF_SystemProcess) does not imply that a knowledgeable
    [administrator](#DEF_Administrator) cannot disable it.

# Informative References

ANSI T1.276-2003 Baseline Security Requirements for the Management Plane

ENG-83132, Serviceability Design Requirements for Security

# History

```
-----
affected_psb: SEC-DOC-FEAT-3
impact: non-normative
headline: >
    [SEC-DOC-FEAT](#SEC-DOC-FEAT) migrated to functional requirements.
```


## Older history (manually maintained; may be incomplete)

PSBCTR 5.0: Edits for clarity

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 5
    applicability:
    - force: recommended
      target:
        restrict: |-
          applications
    category: Application Security
    riskArea: Network Security
    waivable: true
    version: 3
    id: SEC-DOC-FEAT
    issueref: ISS_BlackBoxApp
    tags:
    - EN/PI
    - PSB/OnPrem
