# Headline

Disable or authenticate hardware debug ports

# Description

If you release boards to the field with JTAG, XDP, or other debugging interfaces, then require board-specific credentials to use them.

In this requirement--

1.  An "ephemeral [credential](#DEF_Credential)" is information which would give debugging access to only one physical device instance, and only for one "session" or other clearly limited time, not to exceed the time between two system resets.

1.  A "local [credential](#DEF_Credential)" is information which would give debugging access to only one physical device, but for a longer time or an unlimited number of sessions.

1.  A "global [credential](#DEF_Credential)" is information which would give debugging access to more than 20 percent of all physical devices of a particular type, or to more than a total of 100 devices, or to more devices than you reasonably anticipate that a single entity would need to debug; or which can be used to create an unlimited number of local or ephemeral credentials.

*A **collection** of the local or ephemeral credentials for all or many
devices of a given type is a **global credential**.*

# Behavior

[Authenticate](#DEF_Authentication) or disable access to all boundary scan and other hardware-level debugging interfaces, such as JTAG or Intel XDP, on--

1.  All CPUs
1.  All FPGAs
1.  All chips capable of reading or writing main system memory via DMA or other means.

## SEC-HW-NOJTAG-FR1: Disabling option

If you choose to disable a debugging interface, then it _MUST_ be done in a way designed to be reversible only by physical invasion of a chip die, not from software, from firmware, or by manipulating anything outside a chip package. Blowing on-chip fuses is the usual approach.

## SEC-HW-NOJTAG-FR2: Authentication option

If you choose to provide [authenticated](#DEF_Authentication) access to a debug interface, then you _MUST_ do the following--

1. Only give people and or equipment access to the specific device instances they actually need to debug.

1. When debugging is needed, you _SHOULD_ only give the ability to debug for a single session or otherwise limited time.

1. Don't give debugging access without the permission of an identifiable, authorized Cisco employee.

1. Create a record of each person or equipment using the debugging facility, including who or what used the facility, who or what authorized the use, which individual physical device instance was debugged, and exactly what access was given.

1. Don't make the debugging interface available on the outside of the device chassis, and don't include any connection which might make the debugging interface accesssible to any [remote](#DEF_Remote) agent.

You _SHOULD_ use public-key cryptography for authentication, rather than maintaining a large, and therefore difficult to secure, database of instance-specific credentials that will have to be shared through the manufacturing process.

## SEC-HW-NOJTAG-FR3: Global Credential Handling

You _MUST_ keep each online copy of every global credential, including every large database of local or ephemeral credentials, inside a designated physical device in a physically secured location. For global credentials which are private keys, this device _MUST_ be a purpose-build hardware security module.

You _MUST_ not let more than three online copies of any global credential exist at any one time.

You _MUST_ release global credentials directly to entities doing debugging.

You _SHOULD_ maintain one or more offline backup copies of each global credential. Always keep these copies in guarded physical locations. When not in immediate use, devices containing backup copies _MUST_ be unpowered and physically disconnected from all other equipment. Encrypt each backup using a key or keys which are *not* stored in the same physical location. 

## SEC-HW-NOJTAG-FR4:  Handling local and ephemeral credentials

Any useful authentication system will require releasing local or ephemeral credentials to people or equipment who need to do debugging.

You _SHOULD_ use ephemeral credentials instead of persistent local credentials. Both local and ephemeral credentials _SHOULD_ include information which can be used to trace them back to the particular request that caused them to be issued, and _SHOULD_NOT_ be usable if that information is altered or removed.

Local or ephemeral credentials _MUST_ only be given to entities technically or contractually bound to follow Cisco policy in handling and using them, and only on the authenticated request of an identifiable, authorized Cisco employee. You _MAY_ use ordinary Cisco internal network [authentication](#DEF_Authentication) and [authorization](#DEF_Authorization) practices to validate such requests.

Each copy of any persistent local credential _MUST_ be [erased](#DEF_Erase) as soon as that copy is no longer needed.

Each time a human receives a credential, she _MUST_ be reminded of the proper handling procedures.

Determine the highest expected rate at which each authorized requesteror recipient might need credentials. Any attempt to get credentials at a higher than expected rate _MUST_ be refused and logged. Check periodically for recipients receiving credentials much more frequently than other similarly situated recipients.

Log every release of a local or ephemeral credential. Make the log message identify the requester and the device to be debugged. You
_SHOULD_ also include the stated reason for debugging.

## SEC-HW-NOJTAG-FR5: On-device validation and anchors

The [authentication root](AuthenticationRoot) that each debugged device instance uses to authenticate requests for debugging access, whether they be public keys, shared secrets, or otherwise, _MUST_ be installed at the factory and _MUST_ be immutable thereafter, barring invasion of a chip die. You are permitted to include this "hardwired" authentication root by an exception to [SEC-AUT-DEFROOT](#SEC-AUT-DEFROOT) as described there.

Before giving access, the debugged device instance _MUST_ validate that any presented credential was in fact issued to provide access to that specific instance. In the case of an ephemeral credential, it _MUST_ also validate that the credential is valid for the specific time or session in question.

If the debugged device can trigger software actions in response to debugging attempts, it _SHOULD_ log both successful and failed attempts. If the [credential](#DEF_Credential) used contains information about the request that led to its issuance, that information _SHOULD_ be included in the log entry.

# Informative References

RECIPE: [Secure JTAG](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Secure%20JTAG.aspx)

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: institutional bounded computers
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 1
    id: SEC-HW-NOJTAG
    issueref: ISS_Invade
    tags:
    - EN/PD
    - PSB/OnPrem
