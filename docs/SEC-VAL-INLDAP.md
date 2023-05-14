# Headline

Prevent LDAP Injection flows in applications.

# Key Benefits

Software will be more secure if it is written with the intent to control access to levels of functionality that are beyond what is necessary to do the job. In principle, limiting the use of powerful commands that provide rich functionality, the system is inherently more secure. The concept of limiting access to only what is required is referred to as the least-privilege.

# Description

LDAP can allow an attacker to authenticate and gain unauthorized access to system resources.

This requirement provides methods by which to prevent LDAP Injection attacks.

# Behavior

By far, the most common type of LDAP Injection attack is a filter injection. This can happen whenever the program constructs an LDAP search filter from its string representation and include user-supplied data in the process.

However, LDAP directory servers actually have an inherent advantage over many other types of data stores when it comes to injection attacks because LDAP is not a text-based protocol and because LDAP APIs typically do not make it possible to accidentally turn one type of operation into a different kind of operation.

## SEC-VAL-INLDAP-FR1: Input Validation

Validate all input by:

1. When building LDAP queries in application code, Input Validation practices _MUST_ be applied to the user-supplied data prior to building the LDAP query.
1. The program _MUST_NOT_ construct a query if presented with a string containing unexpected characters.
1. The program _MUST_NOT_ simply remove the unacceptable characters and continue.
1. If possible, the program SHOULD escape all user-supplied input using an escape routine specific to LDAP database language (For example, if the program has an input field in which the program expects the user to provide a username or an email address, then the program might only want to allow the input to contain letters, digits, periods, dashes, underscores, plus signs, and the at sign).

## SEC-VAL-INLDAP-FR2: Constructing Filters

When the program constructs filters from user-supplied input:

1. The program _MUST_ never construct an LDAP search filter by concatenating strings, especially when that string contains any user-supplied input.
1. The program _SHOULD_ use the features that the application LDAP library offers to create filters programmatically.
1. If the program is using an LDAP library that doesn’t provide a way to programmatically generate search filters, then the program _SHOULD_ consider selecting a new library to use for LDAP communication.
1. If that is not feasible, and the program has to create filters from their string representations, then the user-provided input included in the generated filter _MUST_ be validated.

## SEC-VAL-INLDAP-FR3: Least Privilege

When binding accounts in the program environment:

1. To minimize the potential damage of a successful LDAP injection attack, the program _SHOULD_ minimize the privileges assigned to the LDAP binding account in the program environment.

# Informative References

* CWE-90 - [LDAP Injection](https://cwe.mitre.org/data/definitions/90.html)
* LDAP.com - [Understanding and Defending Against LDAP Injection Attacks](https://ldap.com/2018/05/04/understanding-and-defending-against-ldap-injection-attacks/)
* OWASP Cheat Sheet Series - [LDAP Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* Prevent LDAP Injection - [LDAP Injection Examples](https://cisco.box.com/s/8adzcpqivc0zyj4atm9op8aqucbiynia)
* Black Hat LDAP Injection - [LDAP Injection and Blind LDAP Injection](https://www.blackhat.com/presentations/bh-europe-08/Alonso-Parada/Whitepaper/bh-eu-08-alonso-parada-WP.pdf)
* SPI Labs - [LDAP Injection](http://www.networkdls.com/articles/ldapinjection.pdf)

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-VAL-CLNIN
    relation: connects
    headline: >
        Input Validation

# Attributes

    id: SEC-VAL-INLDAP
    version: 1
    issueref: ISS_Inject
    category: Threat Surface Reduction
    riskArea: Application & Interface Security
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
          class:  AAA
          restrict: >
            [offerings](#DEF_Offering) that do authentication using LDAP protocol
    priority: 10
    phase: requirements
    tags:
    - Critical PSB
    - CloudCritical
    - EN/PI
    - PSB/OnPrem
    - Cloud
