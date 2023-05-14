# Headline

Provide authentication/authorization for proxies

# Description

We shouldn't be creating open proxies by default, nor should we force
customers to create them by not providing authentication.

## Examples of proxy services

The following provide proxy services. This is not an exhaustive list.

1.  SOCKS servers.

2.  HTTP servers supporting the CONNECT command.

3.  SSH servers implementing the SSH tunneling protocol.

4.  Essentially all VPN and TCP/IP over TCP/IP tunneling servers,
    including mobility services.

5.  Text-based interactive systems which provide access to unrestricted
    Telnet clients or to similar programs such as netcat. This includes
    the IOS CLI and almost any UNIX or Windows shell.

6.  Systems which execute software obtained from remote clients and give
    that software largely unrestricted network access.

7.  Exit nodes for TCP or [IP](#DEF_IP) anonymity services such as Tor,
    which allow connections to devices not themselves participating in
    the anonymity protocol.

# Behavior

If an [offering](#DEF_Offering) provides a proxy, tunnel, or equivalent
relaying service capable of creating substantially unrestricted
transport or network layer connections or sending substantially
unrestricted traffic on behalf of remote clients, other than by ordinary
[IP](#DEF_IP) routing between local subnets, then:

## SEC-IP-PRXAUTH-FR1: Proxy Not Enabled By Default

That proxy service _MUST_NOT_ be enabled [by default](#DEF_Default)
unless it is an [essential](#DEF_Essential) function of the
[offering](#DEF_Offering).

## SEC-IP-PRXAUTH-FR2: Proxy Client Auth

If the protocol used to provide the proxy service provides for
authentication of client identity or of other client attributes, then
it _MUST_NOT_ be possible to enable the proxy service without also
selecting the authentication and authorization methods to be used, and
configuring the necessary INBOUND [credentials](#DEF_Credential).

## SEC-IP-PRXAUTH-FR3: Proxy Port and Service Restrictions

The proxy service _SHOULD_ permit the
[administrator](#DEF_Administrator) to restrict the addresses and
ports to which clients may connect, and
_SHOULD_ [by default](#DEF_Default) be restricted to connecting to the
services which were the reasons for including the proxy server in the
[offering](#DEF_Offering).

# History

```yaml
-----
affected_psb: SEC-IP-PRXAUTH
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
          IP, TCP, and UDP proxies and
                    tunnels running over any TCP/IP layer
    - force: recommended
      target:
        restrict: |-
          network-accessible proxies providing access to any general-purpose
                    transport or session protocol (e.g. SCTP, RTP, etc).
    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-IP-PRXAUTH
    issueref: ISS_OpenProxy
    tags:
    - EN/PI
    - PSB/OnPrem
