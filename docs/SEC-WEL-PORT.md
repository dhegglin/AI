# Headline

Don't run the wrong protocols on well-known ports

# Key Benefits

Many firewall and IDSes, including Cisco's, make assumptions about
what's listening on various ports. Violating these assumptions can
create security holes.

# Description

Don't mess up people's firewalls by putting unexpected services on
well-known ports.

# Behavior

## SEC-WEL-PORT-FR1: Traffic to Well-Known Ports

1. By default[, offerings](#DEF_Offering) _SHOULD_NOT_ direct incoming traffic on TCP or UDP ports numbered from 0 to 1023 to [listeners](#DEF_Listener) implementing protocols other than those for which those ports are registered with IANA/CANA.

1. For example, TCP port 80 _SHOULD_NOT_ be used for other than HTTP, and TCP and UDP ports 53 _SHOULD_NOT_ be used for other than DNS.

## SEC-WEL-PORT-FR2: Traffic to Non-Standard Ports

1. Ports outside the range from 0 to 1023 _SHOULD_ be evaluated according to their common usages in each [offering](#DEF_Offering)'s usual environment; for example, it rarely makes sense to use port 2049 for other than NFS.

1. This requirement applies only to default behavior. [Offerings](#DEF_Offering) _MAY_ allow [administrators](#DEF_Administrator) to explicitly configure nonstandard port use.

# Informative References

ENG-83132 Product Security Design Requirements

# History
```yaml
-----
affected_psb: SEC-SUP-PATCH
description:  Updated to functional requirements.

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 5
    applicability:
    - force: recommended
      target:
        restrict: |-
          offerings.
    category: Threat Surface Reduction
    riskArea: Network Security
    waivable: true
    version: 2
    id: SEC-WEL-PORT
    issueref: ISS_PortPoach
    tags:
    - EN/PI
    - PSB/OnPrem
    - FAST
    - EN/PI DT
