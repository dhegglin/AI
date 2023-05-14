# Headline

Log administrative access

# Description

Log configuration changes using [administrative](#DEF_Administer) UIs, APIs, or other administrative [exposed
interfaces](#DEF_ExposedInterface).

# Behavior

## SEC-LOG-ADMIN-FR1: Changes by Administrative Channel

You _MUST_ log any use of an [exposed interface](#DEF_ExposedInterface) to make a permanent or indefinitely persisting change (i.e. change of firewall rule set or actions that affect secrets stored in the secret manageement service) to the [offering's](#DEF_Offering) behavior with respect to more than one user.  

# Informative References

* RECIPE: [Log Security-relevant Information](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Log%20SecurityRelevant%20Information.aspx)
* RECIPE: [Validate Logging Implementation](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Validate%20Logging%20Implementation.aspx)

# Requirement References

    ---
    foreign_id: SEC-LOG-CONTENT
    relation: connects
    headline: |-
      SEC-LOG-CONTENT
              lists information to be included in all log entries.
    
    source: PSB

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          services
    category: Logging and Auditing
    riskArea: Logging & Monitoring
    waivable: true
    version: 1
    id: SEC-LOG-ADMIN
    issueref: ISS_Underlogging
    tags:
    - EN/PI
    - CloudCritical
    - PSB/OnPrem
    - Cloud
    - FAST
