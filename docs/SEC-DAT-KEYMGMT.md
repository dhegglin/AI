# Headline
Protect and securely manage cryptographic keys

# Description

Follow best practices around [pass phrases](#DEF_Passphrase), other [credentials](#DEF_Credential), keys, or other [cryptographic secrets](#DEF_CryptographicSecret).  Use a central secrets server or  Key Management System (KMS) to store all secrets.

# Behavior

Note that use of a centralized secret management service still requires the host's credential for access to the secret management service itself to be stored.  See also [Where To Store That Key](https://wwwin-github.cisco.com/CSDL/PSB/wiki/Where-to-store-that-key).

## SEC-DAT-KEYMGMT-FR1:  Trusted Secrets Manager

The KMS being used _MUST_ have appropriate industry standard certifications. The product _SHOULD_NOT_ create a proprietary central secret management service as this would violate SEC-CRY-STDCODE.

## SEC-DAT-KEYMGMT-FR2: Secrets Manager Access

The KMS _MUST_ be configured and operated in a way that assures authentication of [agents](#DEF_Agent) that [access](#DEF_Access) each secret at any given time.

Access control mechanisms in the secrets management service _MUST_ be used to restrict access to each secret to [agents](#DEF_Agent) that have specifically identified needs for such access.

## SEC-DAT-KEYMGMT-FR3:  Secrets Classification

Classify the secrets stored in the secret management system, including:

- The types of [targets](#DEF_Target) to which the secrets enable [access](#DEF_Access).  This includes functions such as application services, backend services, database services, etc.  It should also indicate the sensitivity of the target such as access to [sensitive
  personal information](#DEF_SensitivePII) or processing data for a specific customer.
- The protocols or activities in which the secrets are used, such as if secrets sent over the network or used for local encryption, etc.

## SEC-DAT-KEYMGMT-FR4:  Secrets Sharing

A secret _MUST_NOT_ be used for more than one target.

For example, if the services are divided into application and database classes, the secret value for the application _MUST_ be different from the secret value of the database.

## SEC-DAT-KEYMGMT-FR5:  Secrets Management

The centralized secret management service _MUST_ provide automated assurance that each secret or class of secrets has a
defined lifetime, and is replaced, deleted, or deactivated at the end of that lifetime.

## SEC-DAT-KEYMGMT-FR6:  Secrets Management Logging

The following logging _MUST_ be implemented.  Note that [SEC-SCR-CONFLEAK](#SEC-SCR-CONFLEAK) and [SEC-LOG-NOSENS](#SEC-LOG-NOSENS) forbid logging either the secrets themselves or certain information that could expose the secrets.

- Log secret creation, deletion, and modification; changes to attributes such as lifetime and access controls; and detected or
  reported improper disclosure of any secret.
- Log all [administrative](#DEF_Administer) actions that affect secrets stored in the secret management service. See also [SEC-LOG-ADMIN](#SEC-LOG-ADMIN).
- Log all [access](#DEF_Access) to secrets in ways that would ordinarily involve human action, or that indicate exceptions to the expected use, handling, or life cycle of secrets.

- For example, log any use of mechanisms for responding to lost or compromised secrets, and any use of a function that provides a human [administrator](#DEF_Administrator) with a copy of a secret ordinarily meant to be used by a machine [agent](#DEF_Agent).
- Log all access to secrets in the central secret management system.  Log all uncommon or unusual events, even if they're not specifically listed above.

# Informative References

[Sec Ops Playbook](https://cisco.sharepoint.com/sites/CSDLCloudOfferSecurityCom/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FCSDLCloudOfferSecurityCom%2FShared%20Documents%2FTemplates%2FOperations%20Playbooks&p=true&originalPath=aHR0cHM6Ly9jaXNjby5zaGFyZXBvaW50LmNvbS86Zjovcy9DU0RMQ2xvdWRPZmZlclNlY3VyaXR5Q29tL0VxcVJ0X1VMSG81QnRxU2dMZHJMNDVNQl9ZSzRYNlEtdUg3eXNhbDZfdEtiT1E_cnRpbWU9TWp4NWhaRDkxMGc)

[Cryptographic Controls Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806748&ver=approved)

NIST 800-57 Recommendation for Key Management

- https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-4/final
- https://csrc.nist.gov/publications/detail/sp/800-57-part-2/final
- https://csrc.nist.gov/publications/detail/sp/800-57-part-3/rev-1/final

RECIPE: [Centralized Key Management Service](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Centralized%20Key%20and%20Secret%20Management.aspx)

# Requirement References

    ---
    foreign_id: SEC-OPS-KEYMGMT
    relation: connects
    headline: |-
      SEC-OPS-KEYMGMT
              addresses operational and procedural issues
              surrounding secrets in services, and is a companion
              requirement to SEC-DAT-KEYMGMT. The two requirements
              demand documentation on closely related subjects,
              and the same documentation will often satisfy parts
              or all of both.

    targets:
    - services
    source: PSB
    ---
    foreign_id: SEC-CRY-STDCODE-FR1
    relation: connects
    headline: |-
      SEC-CRY-STDCODE-FR1
              and other FR's demand using standard implementations for
              cryptography (as opposed to "rolling your own").
              This includes cryptographic systems used to store
              and manage secrets as well as the systems in
              which those secrets are themselves used.

    targets:
    - offerings
    source: PSB
    ---
    foreign_id: SEC-SCR-CONFLEAK
    relation: connects
    headline: |-
      SEC-SCR-CONFLEAK
              demands that you avoid certain ways of leaking most of
              the same secrets managed under SEC-DAT-KEYMGMT;
              you will need to satisfy both requirements.
              As applied to data likely to be stored in
              secrets management services in service offerings,
              SEC-SCR-CONFLEAK
              usually duplicates
              SEC-LOG-NOSENS.

    targets:
    - offerings
    source: PSB
    ---
    foreign_id: SEC-LOG-NOSENS
    relation: connects
    headline: |-
      SEC-LOG-NOSENS
              forbids services to log certain data, including
              essentially anything that might be stored
              in a secrets management system. As applied
              to such data,
              SEC-LOG-NOSENS
              usually duplicates
              SEC-SCR-CONFLEAK.

    targets:
    - offerings
    source: PSB
    ---
    foreign_id: SEC-AUT-AUTH
    relation: connects
    headline: |-
      SEC-AUT-AUTH
              demands applying authorization policy, and therefore
              authentication, to any attempt to access any
              non-public target. Any service that provides
              access to secrets must comply.

    targets:
    - services
    source: PSB
    ---
    foreign_id: SEC-CRY-ALWAYS
    relation: connects
    headline: |-
      SEC-CRY-ALWAYS
              demands encrypting non-public information, including
              secrets, when it passes outside of
              controlled space.
              This affects both communication with your secrets
              management system and encryption of the secret management
              system's own persistent storage.

    targets:
    - offerings
    source: PSB
    ---
    foreign_id: SEC-CRY-RANDOM
    relation: connects
    headline: |-
      SEC-CRY-RANDOM
              requires that credentials and cryptographic
              secrets be unpredictable, and describes how
              unpredictable
              values must be generated. SEC-DAT-KEYMGMT reiterates
              the requirement for unpredictability, and sets
              specific unpredictability levels for some secrets
              for which SEC-CRY-RANDOM leaves them undefined.

    targets:
    - offerings
    source: PSB
    ---
    foreign_id: SEC-PWD-CONFIG
    relation: connects
    headline: |-
      SEC-PWD-CONFIG
              requires the ability to enforce a maximum
              password lifetime; SEC-DAT-KEYMGMT requires
              that there actually be such a lifetime.

    targets:
    - passphrase databases
    source: PSB
    ---
    foreign_id: SEC-509-VALIDATE
    relation: connects
    headline: |-
      SEC-509-VALIDATE
              specifies maximum lifetimes for X.509 certificates
              (which will usually also be the lifetimes for
              the underlying keys).

    targets:
    - offerings
    source: PSB
    ---
    foreign_id: SEC-CRY-PRIM-FR1
    relation: connects
    headline: |-
      SEC-CRY-PRIM-FR1
              lists approved
              cryptographic primitives
              and assigns security levels to those primitives.
              Many of the processes described in SEC-DAT-KEYMGMT rely
              on cryptography and are required to use approved
              primitives.

    targets:
    - offerings
    source: PSB
    ---
    foreign_id: SEC-CRY-ALWAYS
    relation: connects
    headline: |-
      SEC-CRY-ALWAYS
              demands encrypting non-public information
              outside of
              controlled space.
              SEC-DAT-KEYMGMT requires certain specific approaches
              of encryption for secrets. A system designed to meet either one
              can't ignore the other.

    targets:
    - offerings
    source: PSB
    ---
    foreign_id: SEC-AUT-AUTH
    relation: connects
    headline: |-
      SEC-AUT-AUTH
              demands applying authorization policy, and therefore
              authentication, to any attempt to access any
              non-public target.
              SEC-DAT-KEYMGMT requires certain specific authentication
              and authorization approaches for various forms of
              access to the secrets it governs.

    targets:
    - services
    source: PSB
    ---
    foreign_id: SEC-AUT-ANCHOR
    relation: connects
    headline: |-
      SEC-AUT-ANCHOR
              requires a valid inference chain for any authentication,
              and therefore puts constraints on how credentials
              may be used. These constraints necessarily interact
              with SEC-DAT-KEYMGMT's credential use, management and
              life cycle concerns.

    targets:
    - offerings
    source: PSB

# History

```yaml
-----
affected_psb: SEC-DAT-KEYMGMT-2
description:  Updated to functional requirements.
---
deprecated_psb: SEC-DAT-KEYMGMT
impact: non-normative
headline: >
  [SEC-DAT-KEYMGMT](#SEC-DAT-KEYMGMT) migrated to functional requirements.
```
# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Cloud Offers using centralized "secret management"
        class: not_MobileApp
    category: Authentication and Authorization
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 2
    id: SEC-DAT-KEYMGMT
    issueref: ISS_NoSecProgram
    tags:
    - Cloud
