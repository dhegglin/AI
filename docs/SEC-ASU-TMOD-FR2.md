# Headline

Assess and Mitigate Threats Against High Value Assets

# Behavior

For each "high-value asset" identified through SEC-ASU-TMOD-FR1, the offering team _SHOULD_ assess the threats, mitigations, and protections that apply. If the system threat model does not have sufficient detail to determine this, then the offering team _SHOULD_ create a more detailed threat model focused on that asset that details threats, potential attack vectors, existing protections, and possible additional protections or mitigations for identified threats.

If it is not feasible to threat model each high value asset in the current development cycle, the offering team _MUST_ document and commit to a plan/schedule for creating these additional threat models with a target for one per major release or other regular development/release milestone and then meet that plan as committed.

**Supplemental Guidance**: For threat modeling to be effective it must look at various levels of the offering, most specifically at high value assets.  While it may not be feasible for each offering to do multiple threat models at each release, additional threat models should be done regularly until all high value assets and their associated risks, protections, and needed mitigations have been documented.

# Attributes

    id: SEC-ASU-TMOD-FR2
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
