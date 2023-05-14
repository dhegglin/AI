# Headline

Log unrestricted access to controlled space

# Description

If you give a [peer](#DEF_Peer) "uncontrolled" access to any of your [controlled space](#DEF_ControlledSpace), at least log the fact that you did it.

# Behavior

Logging unrestricted access to controlled space will benefit incident response and auditing by providing what happened leading up to certain event.

## SEC-CSP-LOGTRUST-FR1: Access to Controlled Space

If any external entities, such as [administrators](#DEF_Administrator), with [trusted](#DEF_Trust) with respect to any of your [controlled
space](#DEF_ControlledSpace), then each use of the [trusted](#DEF_Trust) access _MUST_ be logged.

The following _MUST_ be logged at a minimum:

1.  Any access involving the ability to run arbitrary programs with largely unrestricted access to the [controlled space](#DEF_ControlledSpace) (for example access to a shell inside the controlled space).
    
2.  Any access involving the ability to read or modify data inside the [controlled space](#DEF_ControlledSpace) without control over which specific data are accessed or without an independent record of which data are accessed.
    
3.  Any access that is *not* restricted to the use of an [exposed interface](#DEF_ExposedInterface) to perform specific operations on a specific subset of the contents of the [controlled space](#DEF_ControlledSpace).
    
    Because it's mediated by some kind of protection system that restricts what can be done to the [controlled space](#DEF_ControlledSpace), most access that *does* use an [exposed interfaces](#DEF_ExposedInterface) is not [trusted](#DEF_Trust) access. However, when in doubt, log.

**Supplemental Guidance:**  For example, each time that you allow an [administrator](#DEF_Administrator) to log in with shell access to some system, that [administrator](#DEF_Administrator) is in a position to make untracked and possibly unrestricted changes to that system, potentially compromising its status as a [controlled space](#DEF_ControlledSpace). Log the fact that the access has been given.

## SEC-CSP-LOGTRUST-FR2: Log Attributes

You _MUST_ adhere to [SEC-LOG-CONTENT](#SEC-LOG-CONTENT) for log content and format and additionally _SHOULD_ include all principal names, privilege statuses, and other information used to [authorize](#DEF_Authorization) the [peer](#DEF_Peer) for access to the [controlled space](#DEF_ControlledSpace).

# Informative References

- RECIPE: [Log Security-relevant Information](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Log%20SecurityRelevant%20Information.aspx)
- RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)

# Requirement References

    ---
    foreign_id: SEC-LOG-CONTENT
    relation: connects
    headline: |-
      SEC-LOG-CONTENT
              lists information to be included in all log entries.
    
    source: PSB
    ---
    foreign_id: SEC-AUT-LOG
    relation: connects
    headline: |-
    
              Relatively unrestricted access to
              controlled space
              will almost always involve a "session" of some kind,
              and will even more often involve the use of an
              authentication or authorization subsystem. Logging
              the access will therefore usually be required
              by SEC-AUT-LOG
              as well as by SEC-CSP-LOGTRUST. The work
              to comply with both can often be combined.
    
    source: PSB
    ---
    foreign_id: SEC-OPS-SUDO
    relation: connects
    headline: |-
      SEC-OPS-SUDO puts
              demands on methods that are often used
              to grant the kind of access envisioned by
              SEC-CSP-LOGTRUST. Those demands include
              a logging requirement.
    
    source: PSB

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings
    category: Logging and Auditing
    riskArea: Logging & Monitoring
    waivable: true
    version: 1
    id: SEC-CSP-LOGTRUST
    issueref: ISS_Underlogging
    tags:
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
