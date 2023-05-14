# Headline

Mandatory Access Controls (MAC) must be enabled and constraining all network services.

# Key Benefits

No software is free from defects. Due to this we need to take steps to contain the damage an attacker can do with said defects. To that end we need to apply policies to the system to limit what each network facing service can do via MAC policies.

# Description

MAC systems can watch for misbehavior by programs running on general-purpose operating systems. This is useful in the case of RCE (Remote Code Execution) and EoP (Escalation of Privilege) as the process is still contained by the policy.

# Behavior

## SEC-HRD-MANDACC-FR1
If a [product](#DEF_Product) includes an operating system capable of
using a policy enforcement system such as SELinux or other listed MAC, then such a policy
enforcement system _MUST_ be preinstalled on the
[product](#DEF_Product).

Currently approved these MAC policy enforcement systems are SELinux, SMACK or AppArmor.  To submit another MAC system for approval contact sto-mac-info@cisco.com .

If the linux distribution in use publishes and maintains a SELinux policy the system _MUST_ run SELinux.

## SEC-HRD-MANDACC-FR2
Policy enforcement _MUST_ be preconfigured to permit any actions
required for the [product](#DEF_Product) to be installed and operated,
and to disallow any actions not required by the [product](#DEF_Product).
The policy _MUST_ be at least granular enough to restrict access to
files in particular system directories to specific [system
processes](#DEF_SystemProcess), and to restrict specific [system
processes](#DEF_SystemProcess) to connecting to particular [TCP/IP
services](#DEF_TcpIpService).

## SEC-HRD-MANDACC-FR3
The chosen MAC system must be in enforcing mode.

## SEC-HRD-MANDACC-FR4
All network processes _MUST_ be confined by the chosen MAC.
- For AppArmor this means policies are enforcing mode and not complain.
- For SELinux this means that no network processes are running with the "unconfined" label.
- For SMACK it requires that each network process is not in the default label.

# Informative References

RECIPE: [Enforce SELinux Policy Template](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Enforce%20SELinux%20Policy%20Template.aspx)

# History


```yaml
-----
affected_psb: SEC-HRD-MANDACC
description:  Updates and replaces SEC-RFM-INST
---
deprecated_psb: SEC-RFM-INST
impact: normative
headline: >
  [SEC-RFM-INST](#SEC-RFM-INST) Use SELinux or equiv on capable operating systems

```


## Older history (manually maintained; may be incomplete)

PSBCTR 3.0: Replaces SEC-CSA-INST-2. Permit alternatives similar to CSA.

PSBCTR 4.0: Remove CSA (no longer supported by Cisco).

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings that include capable operating systems
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 1
    id: SEC-HRD-MANDACC
    issueref: ISS_OnlyDAC
    tags:
    - EN/PD
    - SecDev
    - PSB/OnPrem
    - Cloud
