# Headline

Display active TCP/IP Services Including Open ports

# Key Benefits

Customers often ask for information about active [listeners](#DEF_Listener), especially [TCP/IP services](#DEF_TcpIpService). They use the information in at least the following ways:

1. To configure firewalls and other filters to permit or deny access to [product](#DEF_Product) services.

2. To verify that they've properly enabled or disabled services when configuring [products](#DEF_Product), and to conduct configuration audits.

3. To identify and disable unneeded services, either for improved security or for improved efficiency.

4. To understand their exposure to newly discovered security vulnerabilities.

# Description

Every [product](#DEF_Product) needs the equivalent of the “netstat” command... and maybe a little more.

# Behavior

## SEC-DSP-PROC-FR1: List of Active Services

1. At any time, the [product](#DEF_Product)'s [administrator](#DEF_Administrator) _MUST_ be able to get a complete, unified list of all active [TCP/IP services](#DEF_TcpIpService) being offered by the [product](#DEF_Product).

2. If the set of active [TCP/IP services](#DEF_TcpIpService) never changes, then this list _MAY_ simply be included in the [product](#DEF_Product)'s user documentation. This rarely happens in real products.

## SEC-DSP-PROC-FR2: Information Included in the List

1. The list _MUST_ include at least the following information:

    1. The identity of [listener](#DEF_Listener) associated with each [TCP/IP service](#DEF_TcpIpService), AND

    2. The [IP](#DEF_IP) addresses, ports, and/or [IP](#DEF_IP) protocol numbers at which the [TCP/IP service](#DEF_TcpIpService) is offered.

2. If the [product](#DEF_Product) is layered over a [user platform](#DEF_UserPlatform), the list _MUST_ either:

    1. Include only [TCP/IP services](#DEF_TcpIpService) belonging to the [product](#DEF_Product), OR

    2. Clearly distinguish [TCP/IP services](#DEF_TcpIpService) belonging to the [product](#DEF_Product) from those of other [applications](#DEF_Application) or of the underlying [user platform](#DEF_UserPlatform).

## SEC-DSP-PROC-FR3: Services Associated with Software Bundles

1. [TCP/IP services](#DEF_TcpIpService) associated with software bundled with the [product](#DEF_Product) _MUST_ be treated as belonging to the [product](#DEF_Product).

## SEC-DSP-PROC-FR4: Identifying the Listeners Associated with Services

1. The [listeners](#DEF_Listener) implementing the listed [TCP/IP services](#DEF_TcpIpService) _MUST_ be identified in a form which can be used, possibly in combination with [product](#DEF_Product) documentation, to do all of the following:

    1. To find the function of the [TCP/IP service](#DEF_TcpIpService) in the context of the [product](#DEF_Product).

    2. To find major [product](#DEF_Product) configuration options associated with that [TCP/IP service](#DEF_TcpIpService).

    3. To identify the actual protocol used to provide the service:

2. If the [product](#DEF_Product) runs on a general-purpose operating system, the list _SHOULD_ include information which can identify the [listeners](#DEF_Listener) to that system's native tools. Appropriate information might include program names and/or process identifiers.

3. In some systems, a configurable dispatcher program, such as the UNIX "inetd" or "xinetd", may register with the system kernel as the [listener](#DEF_Listener) for one or more [TCP/IP services](#DEF_TcpIpService), invoking subsidiary programs to process incoming connections. In this case, the required list _MUST_ identify both the dispatcher and the underlying subsidiary program for each [TCP/IP service](#DEF_TcpIpService).

## SEC-DSP-PROC-FR5: Products Enhanced Behavior

1. The [product](#DEF_Product) _MAY_ provide a way to display lists only of [open TCP ports](#DEF_OpenPort) or only of [open UDP ports](#DEF_OpenPort) as well as to display a unified list.

2. The [product](#DEF_Product) _MAY_ provide similar displays for [listeners](#DEF_Listener) other than [TCP/IP services](#DEF_TcpIpService). This may be required in the future for some classes of [listeners](#DEF_Listener).

# History

```yaml
-----
affected_psb: SEC-DSP-PROC
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
          products
    category: Threat Surface Reduction
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-DSP-PROC
    issueref: ISS_SurpriseListener
    tags:
    - EN/PI
    - EN/PD
    - PSB/OnPrem
    - EN/PI DT
