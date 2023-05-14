# Headline

Do not include unnecessary software

# Key Benefits

Any piece of software has the potential to contain security
vulnerabilities. More software means more avenues for attack. Even if
there are no publicly known vulnerabilities at the time of inclusion,
vulnerabilities will probably be discovered or disclosed in the future.

# Description

Don't put in unnecessary software. It wastes space, creates security
holes, spreads the impact of licensing problems, and makes extra work
when problems are found with those packages.

# Behavior

## SEC-SW-NEEDONLY-FR1: Unnecessary Software

1. Software not needed for the function or customer troubleshooting of the [offering](#DEF_Offering) _SHOULD_NOT_ be included.

1. Unneeded software _SHOULD_ be excluded at the granularity provided by the upstream supplier's package manager or configuration management system. Exclusion of individual files within a package is not required, nor are edits to source code, although these _MAY_ be done when there is low risk of damaging maintainability or inducing failures.

# History

```yaml
-----
affected_psb: SEC-SW-NEEDONLY
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
    riskArea: System Hardening
    waivable: true
    version: 1
    id: SEC-SW-NEEDONLY
    issueref: ISS_ExtraCode
    tags:
    - EN/PD
    - EN/PI
    - PSB/OnPrem
    - Cloud
