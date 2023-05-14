# Headline

Support NTP, NTP authentication, and filtering.

# Behavior

## SEC-NTP-AUTH-FR1: NTPv4

[Offerings](#DEF_Offering) _MUST_ support NTPv4
(RFC5905).

## SEC-NTP-AUTH-FR2: Symmetric Key Authentication

[Offerings](#DEF_Offering) _MUST_ support symmetric key
authentication in client, server and peer mode.

Offerings _SHOULD_ support AES-CMAC for NTP authentication.
AES-CMAC is defined in RFC8573.

MD5-based NTP authentication is insecure. It _MAY_ be
supported for backwards compatibility, but it _SHOULD NOT_
be enabled by default.

## SEC-NTP-AUTH-FR3: Autokey

Autokey defined in RFC5906 should not be used because it is insecure
and provides a false sense of security. Offerings _MAY_ support
Autokey for customer perception reasons, but they _MUST NOT_ enable
it by default.

## SEC-NTP-AUTH-FR4: IP Filtering

It _MUST_ be possible to specify separate [IP](#DEF_IP)
address filters in the NTP configuration which lists
hosts considered as time sources NTP clients / peers.

## SEC-NTP-AUTH-FR5: Asymmetric Key Authentication

Offerings _MAY_ support NTS for TLS-based Authenticated Encryption
with Associated Data (AEAD) in client-server mode as defined in
draft-ietf-ntp-using-nts-for-ntp.

## SEC-NTP-AUTH-FR6: Exceptions

Requirements FR1-5 do not apply in these instances:

- When NTP is tunneled over encrypted and authenticated
  tunnels like IPSec.

- In rare ocassions where other protocols are used
  instead of NTP for time synchronization. Examples
  include PTP or Roughtime.

# Normative References

- [RFC5905](https://tools.ietf.org/html/rfc5905)
- [RFC8573](https://tools.ietf.org/html/rfc8573)
- [draft-ietf-ntp-using-nts-for-ntp](https://tools.ietf.org/html/draft-ietf-ntp-using-nts-for-ntp)

# Requirement References

    ---
    foreign_id: FPT_STM.1.1
    relation: connects
    headline: |-
      Be able to provide reliable time stamps for applying
            timestamps to audit records (i.e. real time clock with battery
            to maintain time during reboot or power loss).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FPT_STM.1.1
    relation: connects
    headline: |-
      Be able to audit all changes to the time, and ensure
            that audit detail will include the old and new values for the
            time, and the origin of the attempt to change the time
            (e.g. username, or IP address of an NTP server).
    targets:
    - NDPPv1.1(2012)
    source: Common Criteria
    ---
    foreign_id: FPT_STM.1
    relation: implies
    headline: |-
      FPT_STM.1 Reliable Time Stamp FPT_STM.1.1 The TSF
            shall be able to provide reliable time stamps for its own
            use.
    targets:
    - WLANPPv1.0(2011)
    source: Common Criteria

# History

```yaml
-----
affected_psb: SEC-NTP-AUTH
---
deprecated_psb: SEC-NTP-AUTH3
impact: normative
headline: >
  SEC-NTP-AUTH3 consolidated in SEC-NTP-AUTH-FR3,4,6
---
deprecated_psb: SEC-NTP-IPFILT
impact: non-normative
headline: >
  SEC-NTP-IPFILT consolidated in SEC-NTP-AUTH-FR5
description: >
  This requirement was introduced in March 2020 and consolidates
  three older requirements SEC-NTP-IPFILT and SEC-NTP-AUTH3.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
           NTP implementations
    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-NTP-AUTH
    issueref: ISS_UnauthNTP
    tags:
    - EN/PI
    - PSB/OnPrem
    - EN/PI DT
    - FAST
