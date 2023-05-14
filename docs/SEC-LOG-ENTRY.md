# Headline

Log each filter/ACL entry independently

# Key Benefits

Logging is useful in tracing spoofed packet floods and in intrusion
detection. However, the performance impact of logging all hits can be so
large that it makes it infeasible to enable logging at all.

# Behavior

## SEC-LOG-ENTRY-FR1: Independent logging per filter entry

When configuring logging for packet filter hits, it _MUST_ be possible
to enable or disable this logging independently for each filter entry.

# Informative References

* RECIPE: [Log Security-relevant Information](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Log%20SecurityRelevant%20Information.aspx)
* RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)

# History

```yaml
-----
affected_psb: SEC-LOG-ENTRY
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
    id: SEC-LOG-ENTRY
    issueref: ISS_L3Spoof
    tags:
    - EN/PI
    - PSB/OnPrem
