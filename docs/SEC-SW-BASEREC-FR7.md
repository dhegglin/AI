# Headline 
Backup Mechanism

# Behavior
The device _SHOULD_ provide a method to backup copies of critical configuration data. A host can perform the backup for a [symbiont device](#DEF_SymbiontDevice) and the symbiont _MUST_ be able to consume the backed-up critical configuration data.  This backup mechanism _MAY_ be automatic or operate when instructed by an administrator or trusted component.

If backing up critical configuration data, then the protections for those backups _MUST_ be as good as the protections for [base software](#DEF_BaseSoftware).

If multiple backups are available in recovery, the recovery mechanim _MAY_ allow which backup is used to be configured.

**Supplemental Guidance**:  When dealing with multiple backups, it is good to take a look at implementing a [rollback mechanism](#DEF_Rollback)  system to assist.

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
    id: SEC-SW-BASEREC-FR7
    issueref: ISS_SEC-SW-BASEREC
    tags:
    - EN/PD
    - G7
    - PSB/OnPrem
