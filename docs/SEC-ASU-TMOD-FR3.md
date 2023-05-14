# Headline

Create Additional Threat Models for New Features

# Behavior

The offering team _MUST_ create threat models for new features or offer changes. Any new offer feature or change that increases the offering's attack surface or changes the offering data profile or flow, or that adds a new high value asset _MUST_ be threat modeled prior to that feature's release.

# Attributes

    id: SEC-ASU-TMOD-FR3
    version: 3
    issueref: ISS_SEC-ASU-TMOD
    category: Development Process
    riskArea: Risk Assessment
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
          restrict: >
            [offerings](#DEF_Offering)
    priority: 10
    phase: requirements
    tags:
    - EN/PI
    - EN/PD
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
