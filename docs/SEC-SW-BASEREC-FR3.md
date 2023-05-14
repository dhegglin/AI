# Headline 

(was SEC-SW-DETECT-FR2)

# Behavior
The system administrator _SHOULD_ be able to initiate the recovery of [base software](#DEF_BaseSoftware) and/or critical configuration data. Recovery _MAY_ also be initiated through verified platform-level authorization.

The system _MAY_ automatically attempt to initiate recovery without administrator intervention or when notified to do so by another device in the chain of trust.  If a device's critical data is detected to be corrupt, then the [Root of Trust for Detection](#DEF_RootOfTrustForDetection) (and/or Chain of Trust for Detection) _MUST_ be able to initiate a recovery process to restore the critical data of the device.

**Supplemental Guidance**: For example, component 'A' has corrupted data and it is unknown if other components in its trusted chain have also been corrupted.  When recovery is initiated in component 'A' by an administrator, instead of the administrator going through every trusted device manually, component 'A' tells component 'B' and so on to also perform recovery.  This results in a completely recovered chain of trust.



# History

```yaml
-----
Deprecated_psb: SEC-SW-BASEREC-1
---
impact: nonnormative
description: >
  Break into discrete FR's


```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        class: 
        restrict: |-
          product code
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 2
    id: SEC-SW-BASEREC-FR3
    issueref: ISS_SEC-SW-BASEREC
    tags:
    - EN/PD
    - G7
    - Image Signing
    - PSB/OnPrem
