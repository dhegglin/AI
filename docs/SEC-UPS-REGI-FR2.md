# Headline
Update TPS Registrations Regularly

# Behavior

Third-party software registration _MUST_ be updated regularly to reflect the current status of the software.  Third-party software registration _SHOULD_ be updated as third-party software is added, removed or upgraded in your offering to reflect the current status of the software.

**Supplemental Guidance**  For traditional projects "regularly" means "each major release".  For Cloud and CI/CD offers "regularly" means "at least quarterly" as well as "whenever new Third Party Sofware components are added to the offer".
The frequency of updates to your TPS registration is dependent upon how often the third-party software changes in your software bill of materials.  All offer teams are required to update registration if any component is added, removed or upgraded (version changed) since your last registration.  If your offering modifies third-party software daily, then the updates should occur daily.  Likewise, if a month has passed since any third-party software has changed then a month may pass since your registration is updated.
Note that FedRamp controls require that the registration be updated monthly.
Offers using the CI/CD workflow will benefit from integrating CSB CI/CD Downstream Edition, which provides essentially realtime updates.

# History

```yaml
-----
affected_psb: SEC-UPS-REGI-3
impact:  non-normative
description:  Changed to discrete FR's

-----
affected_psb: SEC-UPS-REGI-3
impact:  non-normative
description:  Updated links from TPSD (old tool name) to TPSCRM.  Added "should" guidance to update TPSCRM registry whenever TPS in the offer is changed.
```

# Attributes

    id: SEC-UPS-REGI-FR2
    version: 4
    category: Development Process
    riskArea: Risk Assessment
    legallysensitive: true
    waivable: true
    issueref: ISS_SEC-UPS-REGI
    applicability:
      - force: mandatory
        target:
          restrict: >
            [products](#DEF_Product) containing
            [third party software](#DEF_ThirdPartySoftware)
    priority: 10
    phase: requirements
    tags:
    - EN/PD
    - EN/PI
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
