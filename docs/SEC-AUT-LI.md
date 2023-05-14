# Headline

Control authentication and authorization for Lawful Intercept (LI) feature

# Description

Lawful Intercept is a special case of offer administration authentication and authorization.  The Lawful Intercept feature  separates authorization and authentication from the highest levels of offer administrator (or security administrator if it exists) and the Lawful Intercept Administrator (LIAdmin). Only the LIAdmin and the Law Enforcement Agency members with proper authority should be able to know about active taps and tap subjects under investigation.

# Behavior

## SEC-AUT-LI-FR1: Lawful Intercept Administrator (LIAdmin)

The offering _MUST_ provide a Lawful Intercept Admininistrator (LIAdmin) role.

## SEC-AUT-LI-FR2: LIAdmin as a Separate Role

The LIAdmin _MUST_ be a separate role from any level of offering or security administrator.  The LIAdmin user _MUST_ be the only user (administrative, root, shell or otherwise) to administer or view the LI feature configuration.

## SEC-AUT-LI-FR3: LIAdmin as a Separate Role in an Offering

The offering _MUST_ separate the Lawful Intercept Admin (LIAdmin) role from all levels of administrative or security access on the offering.

## SEC-AUT-LI-FR4: LIAdmin Account Password Reset

The offering _MUST_ reset LI 'tap' and configuration data if the offering or security administrator resets the password for an account assigned the LIAdmin role.

## SEC-AUT-LI-FR5: LIAdmin Account Disabled or Removed

The offering _MUST_ reset all LI 'tap' and configuration data and remove an LIAdmin account from the offering if a LIAdmin account assigned the LIAdmin role is disabled or removed.

## SEC-AUT-LI-FR6: LIAdmin Passwords

The offering _MUST_ conform to SEC-PWD-CONTROL-FR9 for LIAdmin role users.

## SEC-AUT-LI-FR7: LIAdmin Privileges

The Lawful Intercept Administrator (LIAdmin) role _MUST NOT_ be given general offering privileges such as creating user accounts, deleting user accounts, running platform commands, updating the offering configuration other than the Lawful Intercept feature controls.

## SEC-AUT-LI-FR8: Lawful Intercept Feature

The offering _MUST NOT_ allow an offering or security administrator to use debugging, diagnostics, or other administrative commands to view or modify the Lawful Intercept feature or data.

# Informative References

* RECIPE: [Incorporate Lawful Intercept](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Incorporate%20Lawful%20Intercept.aspx)

# Requirement References

    ---
    foreign_id: SEC-PWD-CONTROL
    relation: implies
    headline: |-
        Control password usage and behavior to ensure security and awareness
    source: PSB

# Attributes

    id: SEC-AUT-LI
    version: 1
    issueref: ISS_LawfulIntercept
    category: Privacy and Data Security
    riskArea: Data Governance & Protection
    legallysensitive: true
    waivable: true
    applicability:
      - force: mandatory
        target:
          restrict: >
            offerings
    priority: 8
    phase: requirements
    tags:
      - EN/PI
      - EN/PD
      - PSB/OnPrem
      - Cloud
