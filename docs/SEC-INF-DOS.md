# Headline

Protect against denial of service

# Key Benefits

It should go without saying that any DoS or DDoS would affect every
customer of the SaaS and all the customer SLA's that the SaaS is
required to meet every month. The service cannot go down with the basic
DoS style of attacks; this would be unacceptable to customers of the
service and could impact future business. Any and all systems _SHOULD_
be used to keep all DoS outages from happening using both network and
applications to prevent these styles of attacks.

# Description

## SEC-INF-DOS-FR1: Deploy DoS and DDoS Protection

Deploy Denial of Service (DoS) and Distributed Denial of Service (DDoS)
protection for external end user and server to server communication.

# Behavior

The service _SHOULD_ provide protection against denial of service
attacks both at the network infrastructure and application tiers.

# Normative References

1.  [FedRAMP](https://www.fedramp.gov/) SC-5

2.  [NIST - Computer Security Resource Center (CSRC)](http://csrc.nist.gov/)

# History

```yaml
-----
affected_psb: SEC-INF-DOS
description:  Updated to functional requirements. 

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: External communications
    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-INF-DOS
    issueref: ISS_SoftNodes
    tags: 
    - Cloud
