# Headline

Enforce password strength requirements for all user,
local, administrative, and system account passwords

# Description

An effective password policy prevents passwords from being guessed or cracked. All users that use credentials have access to resources or functions that are deemed important enough to require protection. For these reasons, the credentials must be protected from guessing or [brute-force attacks](https://en.wikipedia.org/wiki/Brute-force_attack).

Systems with weak passwords can be easily breached through a number of attacks. Some of these attacks have included [dictionary](https://en.wikipedia.org/wiki/Dictionary_attack), [rainbow table](https://en.wikipedia.org/wiki/Rainbow_table) or [brute force attacks](https://en.wikipedia.org/wiki/Brute-force_attack).

Bad actors are able to exploit common weaknesses in passwords, which includes common mistakes in creating and protecting passwords:

* Users often pick passwords that are simple and easy to remember. However, the downside of passwords that are easy to remember
  is that they are easy for   attackers to predict. Most users tend to pick a single password, use it for all of their accounts,
  and rarely change it. It is also very common for users to write down the password for future reference.
* Since passwords are associated with a person's identity, users often tend to reveal themselves in their passwords,
  by choosing simple names, birth dates, addresses, telephone numbers, or possibly Social Security Numbers.
* Writing passwords down, putting them in desk draws, under keyboards, or on monitors is a very common practice.
  Often users will share passwords with co-worker/friends or through social networks.

Password strength is a measure of the effectiveness of a [password](https://en.wikipedia.org/wiki/Password) against guessing or  [brute-force attacks](https://en.wikipedia.org/wiki/Brute-force_attack). In its usual form, it estimates how many trials an attacker who does not have direct access to the password would need, on average, to guess it correctly. The strength of a password is a function of length, complexity, and unpredictability.

It is important to enforce password strength requirements for all passwords such as [user accounts](https://en.wikipedia.org/wiki/User_%28computing%29#User_account), [local](#DEF_Local), [superuser accounts](https://en.wikipedia.org/wiki/Superuser) and system account.

For products that exclusively externalize password management, this requirement is not applicable. Externalizing password management is frequently done using RADIUS, TACACS+, or Single Sign-On solutions.  In this case it is the responsibility of the external password management solution to enforce SEC-PWD-STRENGTH.

# Behavior

All employees, contractors, consultants, temporary, and other workers at Cisco and its subsidiaries are required to comply with [Cisco Password Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-536562).

[NIST SP 800-63b Section 5.1.1](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecret) is the basis for password requirements for accounts not covered by the Cisco password policy.

Conforming to the [NIST SP 800-63b Section 5.1.1](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecret) password authenticator requirements is sufficient to satisfy this PSB requirement.

## SEC-PWD-STRENGTH-FR1: Character length (entropy)

Password length _MUST_ support an 8 character minimum and 64 character or longer maximum length. For purposes of the length requirements, each Unicode code point _MUST_ be counted as a single character.

Supplemental Guidance: Very strong passphrases (16+ characters) are RECOMMENDED for long password duration accounts (6 months +) and/or for highly sensitive privileged, system and administrative accounts.

## SEC-PWD-STRENGTH-FR2: Character choices

User _MUST_ be able to use all special characters, but there should not be any requirement to use them. All printing ASCII [[RFC 20]](https://pages.nist.gov/800-63-3/sp800-63b.html#RFC20) characters as well as the space character _SHOULD_ be acceptable in memorized secrets. Unicode [[ISO/ISC 10646]](https://pages.nist.gov/800-63-3/sp800-63b.html#ISOIEC10646) characters _SHOULD_ be accepted as well.

## SEC-PWD-STRENGTH-FR3: No unauthenticated "hints"

Agent _MUST NOT_ be allowed to store a “hint” that is accessible to an unauthenticated claimant. Verifiers _MUST NOT_ prompt subscribers to use specific types of information (e.g., “What was the name of your first pet?”) when choosing memorized secrets or when attempting to recover a memorized secret.

## SEC-PWD-STRENGTH-FR4: Additional password restrictions

Password MUST be checked against a list that contains values known to be commonly used, expected, or compromised. A frequently referenced list is provided in the section below and includes dictionary words as well as repetitive or sequential characters (e.g. ‘aaaaa’, ‘1234abcd’).  Selecting the appropriate size list is left to the product team.

If the chosen secret is found in the list, the verifier MUST reject the password and require the subscriber to choose a different value.

The passwords _SHOULD_ also be checked against context specific words, such as service name, username, product name, and derivatives thereof.  Passwords _SHOULD_ also be checked against previous breach corpuses (e.g ‘cisco123’,’c1sco123’).

# History

```yaml
-----
affected_psb: SEC-PWD-STRENGTH
description:  Aggregated related requirements into functional requirements.
---
deprecated_psb: SEC-OPS-STRENGTH-2
impact: normative
headline: >
  [SEC-OPS-STRENGTH-2](#SEC-OPS-STRENGTH-2) deprecated in favor of NIST 800-63b.
---
deprecated_psb: SEC-PWD-MINMAX-2
impact: normative
headline: >
  [SEC-PWD-MINMAX-2](#SEC-PWD-MINMAX-2) migrated to SEC-PWD-STRENGTH-FR1.
---
deprecated_psb: SEC-PWD-DEFMIN
impact: normative
headline: >
  [SEC-PWD-DEFMIN](#SEC-PWD-DEFMIN) migrated to SEC-PWD-STRENGTH-FR1.
---
deprecated_psb: SEC-PWD-UNICODE
impact: normative
headline: >
  [SEC-PWD-UNICODE](#SEC-PWD-UNICODE) migrated to SEC-PWD-STRENGTH-FR2.
---
deprecated_psb: SEC-PWD-DICCHK
impact: normative
headline: >
  [SEC-PWD-DICCHK](#SEC-PWD-DICCHK) migrated to SEC-PWD-STRENGTH-FR4.
```

# Normative References

* [NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html)
* [Cisco Password Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-536562&ver=approved). This policy is used by the Cisco IT organization as password requirements for anyone utilizing Cisco internal resources.

# Informative References

* [Password Construction Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1436886&ver=approved): Creating a strong password,
  passphrase, or personal identification number (PIN)
* RECIPE: [Password Management](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Password%20Management.aspx)  Implementation guide on product password management
* [Common Credentials List](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials): Provides a list of top 10 million well known passwords

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-PWD-CONTROL
    relation: connects
    headline: >
        [SEC-PWD-CONTROL](#SEC-PWD-CONTROL) Control passwords usage and behavior to ensure security and awareness.

# Attributes

    id: SEC-PWD-STRENGTH
    version: 1
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    legallysensitive: false
    waivable: true
    issueref: ISS_WeakPws
    applicability:
      - force: mandatory
        target:
            restrict: >
              offerings
    priority: 8
    phase: requirements
    tags:
    - CloudCritical
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
