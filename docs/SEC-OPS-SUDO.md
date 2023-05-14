# Headline

Implement restricted root and sudo access

# Description

Root privileges provide the maximum level of privileges or capabilities to the root account on systems. This account has absolute power over the system, including complete [access](#DEF_Access) to all files, directories, and commands. These powers extend the users privilege levels to a point where they can now modify the system in any way desired, and to grant and revoke [access](#DEF_Access) permissions (i.e., the ability to read, modify and execute specific files and directories) for other users, including any of those that are by  [default](#DEF_Default) reserved for root. Unrestricted root and sudo [access](#DEF_Access) potentially could be exploited in combination with other vulnerabilities and increases the overall risks that a complete system compromise could be successful.

# Behavior

Restrict root and sudo [access](#DEF_Access) for all systems to ensure accountability and traceability of operations performed by
administrators.

Adminstrators performing privileged operations must follow the SEC-CRE-MULTIFAC requirement.  Logging of the privileged operations are part of the SEC-CSP-LOGTRUST requirement.

Implement strong security controls for root and sudo access.

## SEC-OPS-SUDO-FR1:  Operating Procedure

The organization _MUST_ have verifiable standard operational procedures that outlines the rational towards access control. The
operating procedure must outline the life cycle by which access is granted to users.

For all root and sudo access, access to the privileged space _SHOUD_ follow the sudo security recipe listed below.

The access policy _SHOULD_ be reviewed on a quarterly basis.

# Informative References

* [Use Sudo Securely](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Use%20Sudo%20Securely.aspx)
* [Limit File Access Permission](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Limit%20File%20Access%20Permission.aspx)
* [OWASP Category: Access Control](https://www.owasp.org/index.php/Category:Access_Control)


# Requirement References

    ---
    foreign_id: SEC-CRE-MULTIFAC
    relation: connects
    headline: |-
      SEC-CRE-MULTIFAC Authenticates administrators before allowing privileged operations.
    
    targets:
    - offerings
    source: PSB
    ---
    foreign_id: SEC-CSP-LOGTRUST
    relation: connects
    headline: |-
      SEC-CSP-LOGTRUST Requirement to log privileged operations.
    
    targets:
    - offerings
    source: PSB
    ---

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Cloud Offers
        class: ServiceThing
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    waivable: true
    version: 2
    id: SEC-OPS-SUDO
    issueref: ISS_PrivAccesAcct
    tags:
    - CloudCritical
    - Cloud
