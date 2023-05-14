# Headline

Run anti-virus scans on shared files

# Key Benefits

If any requirement for files being stored in the SaaS then that service
_MUST_ scan all files for any [security](#DEF_Security) issues. There
would be no quicker way of spreading malware or a virus then having the
SaaS spread those issues through a customer or even across customers.
Without this the SaaS risks all current and future customers and
depending on the impact of the malware or virus it could bring down the
entire SaaS and impact customers that are not even saving files into the
cloud.

# Description

Provide anti-virus and malware scanning capabilities before storing
files on destination servers.

# Behavior

## SEC-INF-AVSCAN-FR1: Anti-Virus Scanning

The following requirements MUST be met -

1. Provision _MUST_ be in place to scan for malware and viruses uploaded files intended to be shared with other users. 

2. Scanning of the file must be done prior to storing on the destination server or servers.

## SEC-INF-AVSCAN-FR2: Update AV Signatures

Malware and Anit-Virus software/signature must be updated regularly to detect latest known threats.

## Exceptions

There are following exceptions for this requirement:

1.  Text files such as configuration files with strict parsing controls
    and input parameters validation.

2.  Files from trusted sources with verified cryptographic signatures.

# Informative References

As an additional information, mapping to SCF and SOC2 to this PSB is provided below:

SCF Domain:  Threat & Vulnerability Management, SCF Objective: TVM-01,  SCF Control: TVM-01.01
SOC2 Criteria:  CC6.7 and CC6.8

# Normative References

1.  [Cloud Security Alliance Controls Matrix TVM-01](https://cloudsecurityalliance.org/download/cloud-controls-matrix-v3)

# History

```yaml
-----
affected_psb: SEC-INF-AVSCAN
description:  Updated to functional requirements. 

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Hosted and Infrastructure Services
        class: not_MobileApp
    category: Operational Process
    riskArea: Risk Assessment
    waivable: true
    version: 1
    id: SEC-INF-AVSCAN
    issueref: ISS_NoSecPolicy
    tags: 
    - Cloud
