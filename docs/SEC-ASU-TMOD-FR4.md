# Headline

Review and Update Threat Models as Needed

# Behavior

The offering team _MUST_ review all threat models regularly (upon creation and at each major release or other regular release milestone).

Threat models _MUST_ be reviewed by a person with security expertise. Suitable reviewers include Security Advocates, Security Engagement Managers, Security Architects, Security Ninja (Green Belt and above), or equivalent.

Threat models _MUST_ be updated whenever:

- Assets or components have changed
- "High value assets" are modified or added
- Changes to existing functionality that may increase the offering's attack surface or change the data flow characteristics
- Changes to or by third-party data processors increase the offering's attack surface or change the data flow characteristics

# Attributes

    id: SEC-ASU-TMOD-FR4
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
