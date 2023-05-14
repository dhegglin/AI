# Headline

Require configuring administration authentication

# Description

Naive or inexperienced administrators frequently forget to configure authentication, or are unaware of the need for authentication. By forcing [administrators](#DEF_Administrator) to configure authentication, we alert them to the need to consider authentication,
and to the dangers of not using it.

# Behavior

Configure authentication before allowing to be managed remotely.

## SEC-MGT-AUTH-FR1:  Credential Configuration

Enabling any method of [administration](#DEF_Administrator), except for methods requiring physical access to the hardware of a [standalone device](#DEF_StandaloneDevice), _MUST_ require explicitly configuring the INBOUND [credentials](#DEF_Credential) and authentication methods to be used for that [administration](#DEF_Administrator).

If the [offering](#DEF_Offering) has a generic AAA infrastructure which permits the same user identities and INBOUND [credentials](#DEF_Credential) to be used with multiple protocols or other functions, and if that AAA infrastructure supports the assignment of administrative privileges appropriate to the actions specified by the [administration](#DEF_Administrator) method, and if the AAA infrastructure itself requires specific configuration of INBOUND [credentials](#DEF_Credential) and authorization methods, then authentication and/or authorization may be referred to the AAA infrastructure rather than configured on a per-protocol or per-method basis. If this is done, the implementation of each [administration](#DEF_Administrator) method must fully enforce all authentication requirements and privilege restrictions defined in the AAA infrastructure.

**Supplemental Guidance**: Initial installation may be an exception as described in [SEC-AUT-DEFROOT](#SEC-AUT-DEFROOT).

## SEC-MGT-AUTH-FR2:  Administrative Configuration

A network protocol used both for [administration](#DEF_Administrator) and for other purposes _MUST_ be able to configure authorization for [administration](#DEF_Administrator) separately from other functions.  The the authentication methods required for [administration](#DEF_Administrator) _SHOULD_ be configurable separately from those to be used for other functions.

**Supplemental Guidance**: If the [administration protocol](#DEF_AdministrationProtocol) in use supports only a single authentication method, and if there are no security-relevant configuration options for that method, then it is acceptable to require only configuration of the INBOUND [credentials](#DEF_Credential) and not the authentication method itself.

## SEC-MGT-AUTH-FR3:  Null Credentials

The [administrator](#DEF_Administrator)_MAY_ be permitted to specify null [credentials](#DEF_Credential) or a null authentication method, but _MUST_ be required to explicitly request null authentication, which _MUST_NOT_ ever be offered as a default or recommended choice.

# Requirement References

    ---
    foreign_id: FMT_SMR.2.3
    relation: connects
    headline: |-
      Though PSB5.x doesn't directly address maintaining
            roles/privilege-levels/permission-groups/etc., NDPPv1.1 doesn't
            actually require more than one role.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FMT_SMR.2.2
    relation: connects
    headline: |-
      Though PSB5.x doesn't directly address maintaining
            roles/privilege-levels/permission-groups/etc., NDPPv1.1 doesn't
            actually require more than one role.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FMT_SMR.2.1
    relation: connects
    headline: |-
      Though PSB5.x doesn't directly address maintaining
            roles/privilege-levels/permission-groups/etc., NDPPv1.1 doesn't
            actually require more than one role.
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria

# History

```yaml
-----
affected_psb: SEC-MGT-AUTH-3
description:  Aggregated related requirements into functional requirements.
---
deprecated_psb: SEC-MGT-AUTH-2
impact: normative
headline: >
  [SEC-MGT-AUTH-2](#SEC-MGT-AUTH-2) Modify requirement to clearly cover all administration.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings
    category: Administrative Access Security
    riskArea: Identity & Access Management
    waivable: true
    version: 3
    id: SEC-MGT-AUTH
    issueref: ISS_SurpriseAdmin
    tags:
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
