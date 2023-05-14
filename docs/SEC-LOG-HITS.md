# Headline

Log traffic filter/ACL hits

# Key Benefits

Logging hits is useful in tracing spoofed packet floods and in intrusion
detection. Logging with source interfaces and MAC addresses greatly
increases the ease of tracing.

# Behavior

## SEC-LOG-HITS-FR1: Must be possible to configure logging for filter hits

It _MUST_ be possible to configure logging of hits against access
lists and similar filtering tables.

## SEC-LOG-HITS-FR2: Must log source MAC and interface

The information logged must include the source MAC address and
interface.

## SEC-LOG-HITS-FR3: Must log all hits

It _MUST_ be possible to comprehensively log all hits. An additional
mode which logs only a representative sample of hits _MAY_ be
provided.

## SEC-LOG-HITS-FR4: Logging must be disabled by default

The logging described in FR's 1-3 _MUST_ be disabled by default.

# Informative References

* RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)

# History
```yaml
-----
affected_psb: SEC-LOG-HITS
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
          forwarding devices
    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-LOG-HITS
    issueref: ISS_L3Spoof
    tags:
    - EN/PI
    - PSB/OnPrem
