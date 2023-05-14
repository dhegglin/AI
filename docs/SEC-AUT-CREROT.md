# Headline

Support real-time credentials rotation or renewal functionality

# Description

A system password, token, certificate, or key rotation in an enterprise environment that supports a large number of servers is a costly and time consuming process. Errors are more likely to occur during credential rotation that can lead to unavailable servers or other unexpected failures. These failures could impact an administrator's ability to frequently change credentials since systems have to be taken offline during credential changes or updates.

Real-time password rotation functionality supports new passwords, tokens, certificates, and keys while allowing seamless credential rotation that does not impact system availability.

# Behavior

[NIST SP 800-57](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-57pt1r4.pdf) is the basis for password storage requirements.

Implement support for offerings to change back-end system password, token, certificate, or key in real time without impacting system availability.

## SEC-AUT-CREROT-FR1: Credential Continuity

The offering _MUST_ support 2 credentials with overlapping lifetimes, or the ability to refresh the existing credentials.

**Supplemental Guidance**:  Use of overlapping credentials is one specific design choice.  Other possible implementations are active-active, various failover-failback or load balanced-rolling update across worker pools.

## SEC-AUT-CREROT-FR2: Authenticate All Credentials

The offering _MUST_ support authentication with all credentials before failing the connection.  This is critical in the instance where the product supports 2 overlapping credentials and both of them are valid.

## SEC-AUT-CREROT-FR3: Update Credentials Efficiently

The offering _MUST_ support updating passwords, tokens, certificates, and keys without impacting system availability.

## SEC-AUT-CREROT-FR4: Credential Revocation

The offering _MUST_ support the revocation of passwords, tokens, certificates, and keys.  Credentials _MUST_ be revoked if the credential has been compromised or the user has left the company.

# HISTORY

    -----
    affected_psb: SEC-AUT-CREROT-2
    description:  Updated to functional requirements.
    ---
    deprecated_psb: SEC-AUT-CREROT
    impact: non-normative
    headline: >
      [SEC-AUT-CREROT](#SEC-AUT-CREROT) updated to functional requirements.

# Normative References

[NIST SP 800-57](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-57pt1r4.pdf) Recommendation for key management

# Attributes

    id: SEC-AUT-CREROT
    version: 2
    category: Authentication and Authorization
    riskArea: Identity & Access Management
    legallysensitive: false
    waivable: true
    issueref: ISS_BadPws
    applicability:
    - force: mandatory
      target:
        restrict: Cloud Offers
    priority: 8
    phase: requirements
    tags:
    - Cloud
