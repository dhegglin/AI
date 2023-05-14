# Headline

Separate the management of the infrastructure and administrative
interfaces from the solution user space

# Key Benefits

Within the zones for the network deployment there is a hard requirement
that there be a management zone. This zone will be used by privileged
[administrators](#DEF_Administrator) to configure and maintain the
hardware and software in the system or systems that are currently in
production. Along with this logical separation of this management zone,
physical separation of the management gear would be preferred if
possible to keep physical [access](#DEF_Access) to the managements
systems.

# Description

Implement dedicated management zone to maintain hardware and software
configurations.

# Behavior

## SEC-INF-MGTZONE-FR1: Use a dedicated management zone
Use a dedicated management zone to [access](#DEF_Access) the
infrastructure for any administrative or restricted activities. If the
cloud provides does not support a management zone, adhere to the
requirements in SEC-CRE-MULTIFAC.

If available, the management zone _MUST_ only be accessed through
dedicated [access](#DEF_Access) point (example VPN).

# Informative References

-   CSA CCM V3 IAM-30

    <https://cloudsecurityalliance.org/group/cloud-controls-matrix/>

-   Cisco Server Security Policy

    <https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-536567>

# Requirement References

    ---
    foreign_id: SEC-CRE-MULTIFAC
    relation: connects
    headline: |-
      SEC-CRE-MULTIFAC Use MFA to access the management zone.

    targets:
    - offerings
    source: PSB

# History


```yaml
-----
affected_psb: SEC-INF-MGTZONE
description:  Updated to functional requirements.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Hosted and Infrastructure Services
        class: ServiceThing
    category: Administrative Access Security
    riskArea: System Hardening
    waivable: true
    version: 2
    id: SEC-INF-MGTZONE
    issueref: ISS_NetArch
    tags:
    - CloudCritical
    - Cloud
