
# Headline

Harden the Linux kernel to reduce the attack surface on Linux kernel and Linux system.

# Key Benefits

Protecting the integrity of the Linux kernel is crucial to maintain the complete chain of trust for all components of a Linux System.

# Description

A secure Linux kernel is the foundation of a secure Linux-based product. Kernel security weaknesses exist and often have a long lifetime, and the default kernel configurations are typically not configured for security.  Therefore, it is important to build, configure and run Linux kernel in a way to improve resilience of the kernel to protect against these vulnerabilities. Protecting the integrity of the Linux kernel is also crucial to maintain the complete chain of trust for all components of a Linux System.

# Behavior

## SEC-HRD-LNXKERN-FR1: Build hardened kernel
For each Linux kernel in your offering, refer to the "Securing the Kernel" section of the [Cisco Linux Hardening Guide](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-14993268). If you are compiling the kernel, you _MUST_ implement the recommended build flags to compile the kernel. Apply all flags that are supported by your kernel version and architecture.

If you are not building the Linux kernel you _SHOULD_ choose the kernel that has best compliance according to your business case. And if you are developing a new offer or planning to update your Linux kernel you _MUST_ select a kernel that has the best compliance according to your business case.

## SEC-HRD-LNXKERN-FR2: Configure hardened kernel

For each Linux kernel in your offering, refer to the "Securing the Kernel" section of the [Cisco Linux Hardening Guide](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-14993268). Use the recommended kernel command line options when booting and configuring the kernel. You MUST apply all options that are supported by your kernel version and architecture.

## SEC-HRD-LNXKERN-FR3: Protect kernel integrity
Each Linux Kernel in your offering _MUST_ be signed and verified, and each kernel module _MUST_ also be signed and verified. Update of kernel and kernel modules at run time, if allowed, _MUST_ also be verified.

The Kernel Lockdown feature was introduced since kernel version 5.4, it prevents unauthorized access to the kernel image and information stored in the kernel. You MUST enable Kernel Lockdown feature if it is supported by your kernel version.

**Supplemental Guidance**: Compliance with SEC-SW-SIG and [SEC-SW-INSCHK](#SEC-SW-INSCHK)is required for signing and verifying signature of Linux kernel and kernel modules and updates of Linux kernel and kernel modules.

## SEC-HRD-LNXKERN-FR4: Keep kernel updated with security fixes
Any security-relevant update of Linux kernel _MUST_ be incorporated into the offering in a timely fashion.

**Supplemental Guidance**: Compliance with [SEC-SUP-PATCH](#SEC-SUP-PATCH) is required for kernel updates.

## SEC-HRD-LNXKERN-FR5: Evaluate kernel hardening compliance
For each Linux kernel in your offering, no matter whether it is compiled by Cisco or provided by a third party, you _MUST_ evaluate compliance against the "Securing the Kernel" section of [Cisco Linux Hardening Guide](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-14993268) in order to understand any risks present in your kernel.

You _MUST_ document any non-compliance and attach that document or include as a note in your SRP.


# Informative References

- RECIPE: [Linux Kernel Hardening](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Linux%20Kernel%20Hardening.aspx)
- RECIPE: [Signed Linux Kernel Modules](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Signed%20Linux%20Kernel%20Modules%20(v2.0%20draft).aspx)
- RECIPE: [Secure Boot](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Secure%20Boot.aspx)
- [Cisco Linux Hardening Guide](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-14993268)

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: offerings that include a Linux Operating System
        class: SwOs
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 2
    id: SEC-HRD-LNXKERN
    issueref: ISS_SoftHosts
    tags:
    - Hardening
    - EN/PI
    - PSB/OnPrem
