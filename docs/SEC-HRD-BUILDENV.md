# Headline

Register and link your build environment to your offer.

# Key Benefits

Hardening a [build environment](#DEF_BuildEnvironment) makes it significantly more difficult for both external and internal malefactors to
tamper with the code that is compiled and shipped to our customers, and ensures that software that is signed with a
"Release" cryptographic key is as secure and tamper-free as possible.

# Description

Register your build environment for visibility.
Link to the build environment for your offer so that its security can be tracked and kept up to date.
Harden your [build environment](#DEF_BuildEnvironment), including SCM (Source Code Management system), inventory, hosts, base templates, package sources, and access,
so that it is more difficult for a bad actor to tamper with the Cisco software supply chain and compromise your offer.

# Behavior

## SEC-HRD-BUILDENV-FR1
Every Cisco project tracked in Security Insights _MUST_ be linked to one or more registered [build environments](#DEF_BuildEnvironment).

All [build environments](#DEF_BuildEnvironment) _MUST_ be registered in Cisco's [Enterprise Service Platform (ESP)](https://cisco.service-now.com/nav_to.do?uri=%2Fu_cisco_business_application_vw_list.do%3Fsysparm_query%3D%26sysparm_first_row%3D1%26sysparm_view%3D):

  - If the build environment is not registered, contact the Build Security Lead for your organization to get it registered.
  - If you do not know how to contact your organization's Build Security Lead, ask in the **[Build Environment Security](https://eurl.io/#ZDAUDwmEw) Webex Teams room**.
  - Instructions on registering a build environment can be found in the [Build Environment Registration](https://cisco.service-now.com/sp?id=kb_article&sysparm_article=KB0060602) guide.
**Supplemental Guidance:** Most on-prem product build environments, if not all, are already registered in ESP and have a designated Build Security Lead.

# Normative References

* Cisco [Build Environment Security Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-22471141&ver=approved)
* [Baseline Hardening for Build Environments](https://cisco.sharepoint.com/sites/BuildEnvironmentSecurity/SitePages/SFS-Hardening-Guide.aspx)

# Informative References

* [Executive Order on Improving the Nation’s Cybersecurity (14028)](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/)
* [SLSA Framework](https://slsa.dev) - specifically SLSA Level 3
* [OWASP Software Component Verification Standard](https://owasp.org/www-project-software-component-verification-standard/)
* [Secure Software Development Framework](https://csrc.nist.gov/projects/ssdf)



# History

```yaml
-----
affected_psb: SEC-HRD-BUILDENV
description:  Removed FR's 2 and 3
-----
affected_psb: SEC-HRD-BUILDENV
description:  Introduced the requirement.
```

# Attributes

    id: SEC-HRD-BUILDENV
    version: 3
    #links the requirement to a "problem" (security issue) in CSERV.
    issueref: ISS_BuildEnvSec
    category: Boot and System Integrity
    riskArea: System Integrity
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
        - PSB/OnPrem
        - Cloud
        - Critical PSB
