# Headline

Protect Ethernet traffic and MAC addresses

# Key Benefits
Attackers within the local broadcast domain can use ARP or ICMPv6 spoofing to hijack sessions, cause denial of service, or create man-in-the-middle attacks. Tools for this are widely available.
STA-ADDR This makes it difficult to hijack traffic intended for any node that's active enough to keep its bridge table entry from timing out.
AUD-MAX This situation is definitely a sign of a problem. One strong possibility is a CAM overflow attack.
DIS-RESV Invalid packet source addresses are a rich hunting ground for security bugs, both in bridges and in the end nodes that eventually receive the packets.

For example, more than one switch has “learned” the broadcast MAC address, preventing broadcast flooding and denying service. By dropping invalid packets as soon as they're seen, we prevent a significant class of known and unknown attacks.

LIM-ADDR This avoids a variety of packet spoofing and blind hijacking attacks.
LIM-MACS This can be used to mitigate MAC address hijacking attacks by limiting the number of stations allowed to access a physical port.

Limiting the number of MAC addresses assigned to each port implicitly limits the bridge table resources which can be consumed by devices attached to a port.

STA-ADDR Static configuration is used to avoid various traffic hijacking and denial of service attacks. These attacks will succeed if the attacker can overwrite the static configuration.


# Description


# Behavior

## SEC-MAC-PROTECT-FR1: Limit MAC addresses per port
**(was SEC-LIM-MACS-FR1)**

Each [bridge](#DEF_Bridge) _MUST_ be able to limit the number of MAC
addresses that are allowed be assigned to a particular port by its
[bridge table](#DEF_BridgeTable). Once this limit has been reached, new
sources on that port must not be learned until old sources have aged
out.

## SEC-MAC-PROTECT-FR2: Do not flood from new MAC source not in table
**(was SEC-LIM-MACS-FR2)**

Traffic from sources not in the table _MUST_, by default, be discarded
rather than being flooded.

## SEC-MAC-PROTECT-FR3: Do not overwrite bridge table entries
**(was SEC-AGE-ADDR-FR1)**

It _MUST_ be possible to configure each [bridge](#DEF_Bridge) such
that active entries in its [bridge table](#DEF_BridgeTable) are not
overwritten unless they have been invalidated by some non-traffic event.

In other words, if the [bridge table](#DEF_BridgeTable) shows MAC
address X as connected to port A, and traffic from MAC X address is seen
on port B, the [bridge table](#DEF_BridgeTable) _MUST_NOT_ be
modified unless the entry for port A has been invalidated by a timeout,
loss of PHY connectivity, spanning tree change, administrative action,
or other normal processes.

Migration of a VM to another segment within a VXLAN or similar under
the direction of a hypervisor is considered to be either an
administrative action or a normal process.

This _SHOULD_ be the default configuration unless there's reason to
believe that many devices will move without PHY disconnects in normal
operation.

[Administrators](#DEF_Administrator)_MAY_ be provided with the option
of modifying this behavior.

## SEC-MAC-PROTECT-FR4: Limit access based on MAC addresses
**(was SEC-LIM-ADDR-FR1)**

[Bridges](#DEF_Bridge) _MUST_ be able to limit input packets accepted
through any port to those bearing the source addresses of devices known,
through static configuration or through an authentication protocol, to
be connected to that port.

## SEC-MAC-PROTECT-FR5: Protect statically configured MAC addresses
**(was SEC-STA-ADDR-FR1)**

Statically configured [bridge table](#DEF_BridgeTable) entries
_MUST NOT_ be overwritten by dynamically learned information.

## SEC-MAC-PROTECT-FR6: Issue log message when MAC count limit reached
**(was SEC-AUD-MAX-FR1)**

If the maximum number of MAC addresses supported by a
[bridge](#DEF_Bridge) or by an individual port is reached, and traffic
is received from a new source, a message _MUST_ be logged.


## SEC-MAC-PROTECT-FR7: Silently discard packets with reserved source MACs
**(was SEC-DIS-RESV-FR1)**

Any received packet whose source address field contains a reserved MAC
address, such as a broadcast or multicast address, _MUST_ be silently
discarded.

Such packets _MUST_ be dropped before populating any [bridge
tables](#DEF_BridgeTable).

**Supplemental Guidance**  According to RFC5342, Section 2.1  "The unicast identifiers from 00-00-5E-00-00-00 through 00-00-5E-00-00-FF are reserved and require IESG Ratification for allocation (see Section 5.1)."

# Informative References

* EDCS-213020 Metro Ethernet Threat Model


# History

```yaml
---
deprecated_psb: SEC-LIM-MACS
impact: non-normative
description: >
  Merged into SEC-MAC-PROTECT
---
deprecated_psb: SEC-AGE-ADDR
impact: non-normative
description: >
  Merged into SEC-MAC-PROTECT
---
deprecated_psb: SEC-LIM-ADDR
impact: non-normative
description: >
  Merged into SEC-MAC-PROTECT
---
deprecated_psb: SEC-STA-ADDR
impact: non-normative
description: >
  Merged into SEC-MAC-PROTECT
---
deprecated_psb: SEC-AUD-MAX
impact: non-normative
description: >
  Merged into SEC-MAC-PROTECT
---
deprecated_psb: SEC-DIS-RESV
impact: non-normative
description: >
  Merged into SEC-MAC-PROTECT
```

# Attributes

    id: SEC-MAC-PROTECT
    version: 1
    issueref: ISS_L2Spoof
    category: Traffic and Protocol Protection
    riskArea: Network Security
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
            restrict: >
              bridges
    priority: 8
    phase: requirements
    tags:
        - EN/PI
        - PSB/OnPrem
