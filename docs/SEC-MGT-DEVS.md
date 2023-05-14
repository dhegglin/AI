# Headline

Maintain security of administered devices

# Description

A security hole opened by an [administration](#DEF_Administrator) system is just as serious as one opened by the [administered](#DEF_Administer) device itself.

For a network management system to reconfigure a device to be insecure is no better than for the device to be insecure on its own. For a management system not to support basic security functions is no more acceptable than for the underlying device.

# Behavior

Maintain the security of the [agents](#DEF_Agent) your [offering](#DEF_Offering) configures, just as the managed [agent](#DEF_Agent) would be required to maintain its own security.

## SEC-MGT-DEVS-FR1:  Default Functionality

If the managed [agent](#DEF_Agent) is required to behave in some way by [default](#DEF_Default) or as [standard](#DEF_Standard), then your _MUST_ maintain that [default](#DEF_Default) or [standard](#DEF_Standard) behavior unless a change is [essential](#DEF_Essential) to the function of the combined [offering](#DEF_Offering) and managed [agent](#DEF_Agent), specifically directed otherwise by an [administrator](#DEF_Administrator).

**Supplemental Guidance**: For example, HTTP servers are usually required to be disabled by default. Therefore, a network [administration](#DEF_Administer) system must not enable an HTTP server unless directed to do so by an actual [administrator](#DEF_Administrator).

## SEC-MGT-DEVS-FR2:  Enhanced Functionality

If the managed [agent](#DEF_Agent) is required to offer a configuration option, then your [offering](#DEF_Offering) _MUST_NOT_ prevent that configuration option from working properly, unless the option is completely incompatible with an [essential](#DEF_Essential) function of the combined [offering](#DEF_Offering) and managed [agent](#DEF_Agent).

If the managed [agent](#DEF_Agent) is required to support a configuration option related to your [offering](#DEF_Offering)'s scope of action, then your [offering](#DEF_Offering) _MUST_ actually support setting that configuration option, unless the option is completely incompatible with an [essential](#DEF_Essential) function of the combined [offering](#DEF_Offering) and managed [agent](#DEF_Agent).

**Supplemental Guidance**: For example, some network [administration](#DEF_Administer) systems use CDP for device discovery. These _MUST_ support configuring CDP transmission and hold timers, and in fact _MUST_ support completely disabling CDP on the managed [agents](#DEF_Agent).

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings that configure
                      agents.
    
    category: Administrative Access Security
    riskArea: Identity & Access Management
    waivable: true
    version: 1
    id: SEC-MGT-DEVS
    issueref: ISS_BadManager
    tags:
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
