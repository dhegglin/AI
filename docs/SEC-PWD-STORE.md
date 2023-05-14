# Headline

Hash and salt non-recoverable stored credentials.  Store recoverable credentials using a password manager.

# Description

Storing a recoverable form of a [credential](#DEF_Credential) belonging to a [peer](#DEF_Peer) increases the impact of any security breach that discloses the stored data.

This risk is especially acute in the case of user-selected [passphrases](#DEF_Passphrase), which are often reused for many services and are therefore likely to give access to things completely unrelated to the [offering](#DEF_Offering).

Key derivation functions take a password, a salt, and a cost factor as inputs then generate a password hash. Their purpose is to make each password guessing trial by an attacker who has obtained a password hash file expensive and therefore the cost of a guessing attack high or prohibitive.

This sort of hashing is a widely accepted industry norm, and providing it helps protect Cisco's security reputation against hacks that would reflect poorly on Cisco's general competence.  The UNIX password file pioneered this nearly universal practice in the early 1970s.

# Behavior

[NIST SP 800-63b Section 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecret) is the basis for non-recoverable password storage requirements.

## SEC-PWD-STORE-FR1: Cleartext Passwords

Passwords and credentials _MUST_NOT_ be stored in cleartext.

If an [offering](#DEF_Offering) authenticates an agent using the agent's cleartext password, the offering _MUST_ store only salted and hashed values derived from the [credential](#DEF_Credential) by a key derivation function that complies with [SEC-CRY-PRIM](#SEC-CRY-PRIM-FR1).

## SEC-PWD-STORE-FR2: Salt Length & Value

When storing non-recoverable passwords, the salt _MUST_ be at least 32 bits in length and be chosen randomly so as to minimize salt value collisions among stored hashes.

The chosen salt value _MUST_ be randomly generated and stored for every password.

## SEC-PWD-STORE-FR3: Hash Algorithm

When storing non-recoverable passwords, the hash algorithm _MUST_ be stored along with the hashed password if multiple hash algorithms are in use.  This is typically achieved by enumerating the hash algorithm and allows the flexibility to deal with algorithm changes.

The offering _MUST_ store only hashed values derived from the [credential](#DEF_Credential) by a key derivation function that complies with [SEC-CRY-PRIM](#SEC-CRY-PRIM).

## SEC-PWD-STORE-FR4: Reversible Passwords

Storing passwords in a reversible manner directly violates [CWE-257](https://cwe.mitre.org/data/definitions/257.html).  However, in some cases it is necessary to use the cleartext password for authentication to another device or service as is the case of an NMS application.

Passwords _MUST_ be stored through a central password manager that will securely encrypt, store, and decrypt it. Once encrypted, they may be stored in readable file systems, however, the same code, library, or program _MUST_ be used exclusively to encrypt and decrypt the password.

Access to the password manager _MUST_ be limited to individual users, systems, and/or trusted networks.  Any credentials needed to access the password manager must be stored securely.  This may be an onboard TPM, a separate control space, or through interactive input.  

*Supplemental Guidance*:  Frequently used password managers are Vault, AWS Credentials Manager, or GCP Secret Manager.  Of these, Vault can be deployed for on-prem devices.

# HISTORY

    -----
    affected_psb: SEC-PWD-STORE-2
    ---
    deprecated_psb: SEC-PWD-STORE
    impact: normative
    headline: >
      [SEC-PWD-STORE](#SEC-PWD-STORE) added FR4 to address recoverable passwords.
    ---
    affected_psb: SEC-PWD-STORE
    description:  Updated to functional requirements and referencing cryptographic primitives requirement.
    ---
    deprecated_psb: SEC-NRCV-CRED
    impact: normative
    headline: >
      [SEC-NRCV-CRED](#SEC-NRCV-CRED) updated to functional requirements.

# Normative References

* [NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html)
* RECIPE: [Centralized Key and Secret Management](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Centralized Key and Secret Management.aspx)

# Informative References

* [Linux /etc/shadow file format](http://www.yourownlinux.com/2015/08/etc-shadow-file-format-in-linux-explained.html)
* [Change linux password hashing algorithm](http://techlister.com/linux/linux-how-to-change-the-hashing-algorithm-on-linux-system/796/)
* RECIPE: [Password Management](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Password%20Management.aspx)

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-CRY-PRIM-FR1
    relation: connects
    headline: >
        [SEC-CRY-PRIM-FR1](#SEC-CRY-PRIM-FR1) Use approved cryptographic primitives and parameters

# Attributes

    id: SEC-PWD-STORE
    version: 2
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    legallysensitive: false
    waivable: true
    issueref: ISS_ClearCreds
    applicability:
      - force: mandatory
        target:
          restrict: >
            [offerings](#DEF_Offering)
    priority: 10
    phase: requirements
    tags:
    - EN/PI
    - Critical PSB
    - CloudCritical
    - PSB/OnPrem
    - Cloud
    - FAST
