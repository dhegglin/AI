# Headline

Authenticate and Encrypt Media and Signaling traffic.

# Description

Media and Signaling protocols such as SIP, CTI, RTP , RTCP, webRTC, H.323, MGCP, Megaco/H.248, UNIStim, SCCP, AES67 transfer sensitive traffic. This traffic needs to adhere to confidentiality, integrity, and accountability requirements.

# Behavior

Secure Control traffic so that control plane cannot be abused to send media to unauthorized destinations.
Below are feature requirements to secure the media protocols. Implement the feature(s) that are applicable to your offering. Refer to [SEC-CRY-PRIM-FR1](#SEC-CRY-PRIM-FR1) to understand accepted ciphers as some of the legacy protocols may not support accepted ciphers. When the protocol does not support accepted ciphers, use the guidance for alternate security mechanism provided in the feature.

## SEC-VVD-MEDIA-FR1: Secure SIP Traffic

**Session Initiation Protocol** (SIP) is an application-layer control protocol that can establish,  modify, and terminate multimedia sessions as well as invite participants to  already existing sessions, such as multicast conferences.

All SIP implementations _MUST_ support SIP over TLS (SIPS).  Clients _MUST_ support the service discovery mechanisms in [RFC 3263](https://tools.ietf.org/html/rfc3263) in order to allow them to discover secure SIP services.  SIP servers, such as proxies _MUST_ authenticate clients by supporting the SIP Digest authentication mechanisms.

## SEC-VVD-MEDIA-FR2: Secure CTI Traffic

**Computer Telephony Integration** (CTI) involves integrating computer systems with telephony resources to augment the capabilities of a call center. The traffic between the CTI client and CTI server _MUST_ be authenticated and encrypted by using HTTPS, secure WebSockets, or other TLS-based transports.

## SEC-VVD-MEDIA-FR3: Secure Session Negotiation

**Session Description Protocol** (SDP) is used in real-time applications to negotiate media parameters, including security protections.  In order to prevent tampering with this negotiation, SDP _MUST_ only be sent over secure channels.  Secure sessions _MUST_ use the SAVP/SAVPF profiles of SDP.  Media keys _MUST_ be established using either DTLS-SRTP or SDP Security Descriptions (SDES).  DTLS-SRTP _SHOULD_ be preferred to SDES.

## SEC-VVD-MEDIA-FR4: Secure NAT and Firewall Traversal

**Interactive Connectivity Establishment** (ICE) protocol is used by real-time endpoints to establish-end-to-end connectivity between media endpoints, even in the presence of intermediaries such as NATs and Firewalls.  Implementations of the TURN protocol (part of ICE) MUST implement the security provisions in [RFC 5766](https://tools.ietf.org/html/rfc5766#section-17) in order to avoid relaying traffic for unauthorized clients.

## SEC-VVD-MEDIA-FR5: Secure RTP Traffic

**Real Time Protocol** (RTP) provides end-to-end network transport functions suitable to applications transmitting real-time data, such as audio, video or simulation data, over multicast or unicast network services.

SRTP provides a framework for encryption and message authentication  of RTP and RTCP streams. Offerings _MUST_ implement Security standards defined in [RFC 3711](https://tools.ietf.org/html/rfc3711)

**Supplemental Guidance:** Refer to [SEC-CRY-PRIM-FR1](#SEC-CRY-PRIM-FR1) to use accepted ciphers.

## SEC-VVD-MEDIA-FR6: Secure RTCP Traffic

**Real Time Control Protocol** (RTCP) augments the data transport to allow monitoring of the  data delivery in a manner scalable to large multicast networks, and  to provide minimal control and identification functionality.

SRTP provides a framework for encryption and message authentication  of RTP and RTCP streams. Offerings _MUST_ implement Security standards defined in [RFC 3711](https://tools.ietf.org/html/rfc3711)

**Supplemental Guidance:** Refer to [SEC-CRY-PRIM-FR1](#SEC-CRY-PRIM-FR1)to use accepted ciphers.

## SEC-VVD-MEDIA-FR7: Secure webRTC

**WebRTC** is a free, open project that provides browsers and mobile applications with Real-Time Communications (RTC) capabilities via simple APIs. WebRTC itself provides good security baseline, by requiring the use of DTLS-SRTP.  In addition, offerings using WebRTC _MUST_ ensure delivery of WebRTC-enabled web applications over HTTPS, as well as the SDP used to negotiate WebRTC sessions _MUST_ be sent over secure channels such as HTTPS and secure WebSockets.

## SEC-VVD-MEDIA-FR8: Secure H323 Traffic

Offerings _MUST_ implement the security standards defined in the H.235 Security Standard unless there is a business case to offer alternative security mechanisms, in which case the business case _MUST_ be documented.

**Supplemental Guidance:** H323 Baseline Security profile is defined in [H235 ITU-T Recommendation](https://www.itu.int/rec/T-REC-H.235.1-200509-I/en). The security profile is applicable to H.323 terminal-to-gatekeeper, gatekeeper-to-gatekeeper, H.323 gateway-to-gatekeeper and to other H.323 entities in administered environments. H.235 standardizes two methods for encrypting media, one is generally called "H.235", the other is SRTP.  Offerings can choose to implement the original H.235 security mechanism instead of SRTP as long as it meets requirements in [SEC-CRY-PRIM-FR1](#SEC-CRY-PRIM-FR1).
Refer to the Implementation Section for Alternate Security Mechanism for Legacy protocols.

## SEC-VVD-MEDIA-FR9: Secure MGCP Traffic

Any entity can send a command to an MGCP endpoint. If unauthorized entities could use the MGCP, they would be able to set-up  unauthorized calls, or to interfere with authorized calls. Offerings _MUST_ implement the security standards defined in [RFC 3435](https://tools.ietf.org/html/rfc3435#section-5), unless there is a business case to offer alternate Security mechanisms, in which case the business case _MUST_ be documented.

**Supplemental Guidance:** Refer to the Implementation Section for Alternate Security Mechanism for Legacy protocols.

## SEC-VVD-MEDIA-FR10: Secure Megaco/H.248 Traffic

**Megaco**  defines the protocol used between elements of a  physically decomposed multimedia gateway, such as Media Gateway and a  Media Gateway Controller. Offerings _MUST_ implement Security standards defined in [RFC 3525](https://tools.ietf.org/html/rfc3525), unless there is a business case to offer alternate Security mechanisms, in which case the business case _MUST_ be documented.

**Supplemental Guidance:** Refer to the Implementation Section for Alternate Security Mechanism for Legacy protocols.

## SEC-VVD-MEDIA-FR11: Secure UNIStim Traffic

**Unified Networks IP Stimulus** ( **UNIStim** ) is a proprietary telecommunications protocol developed by Nortel (now acquired by Avaya) for IP Phone (terminals and soft phones) and IP PBX communications.

An interfacing Cisco Communication Server _MUST_ employ a secure proxy between the UNIStim IP Phone and the Cisco Communication server, providing UNIStim signaling encryption.

**Supplemental Guidance:** Refer to the Implementation Section for Alternate Security Mechanism for Legacy protocols.

## SEC-VVD-MEDIA-FR12: Secure SCCP Traffic

**Skinny Client Control Protocol** (**SCCP**) is a proprietary network terminal control protocol originally developed by Selsius Systems (now acquired by Cisco). It is a lightweight IP-based protocol for session signaling with Cisco Unified Communications Manager. SCCP signalling _MUST_ be authenticated and encrypted.

**Supplemental Guidance:** Refer Implementation Section for Alternate Security Mechanism for Legacy protocols.

## SEC-VVD-MEDIA-FR13: Secure AES67 Traffic

**AES67** is a standard to enable high-performance audio-over-IP streaming interoperability between the various IP based audio networking products currently available, based on existing standards such as Dante, Livewire, Q-LAN and Ravenna. It is not a new technology but a bridging compliance mode common to all IP-Networks; an interoperability mode you can put an AES67 compliant device into, on any participating network. AES67 operates over standard layer 3 Ethernet networks, and layer 3 or layer 2 Security Mechanism _MUST_ be used to secure traffic.

**Supplemental Guidance:** Refer to the Implementation Section for Alternate Security Mechanism for Legacy protocols.

## SEC-VVD-MEDIA-FR14: Confidentiality & Integrity

Although the offering implements all security defined in the feature requirements above, end-to-end media might sometimes still be unsecure. This may be due to traversal through unsecure hops, or when integration with legacy protocols might force a connection to be unsecure. In these situations, the product _MUST_ dynamically identify lack of end-to-end security and trigger explicit service decisions. These decisions would be based on Business usecase, and could include refusal to nail up the session, logging, real-time call participant notification and alerting.

## SEC-VVD-MEDIA-FR15: Accountability

When the offering implements Call Detail Record(CDR) as a feature, it is imperative to treat CDR as highly sensitive information. CDR are used for fraud management, billing and to generate legal response when needed. These records _MUST_ follow privacy, integrity & confidentialy PSB guidelines

## SEC-VVD-MEDIA-FR16: Availability

The offering _MUST_ implement protection guidelines against DOS attacks. Refer to [SEC-INF-DOS](#SEC-INF-DOS). The offering _MUST_ protect against bandwidth theft by defining policies in the proxy or gateway, such as in SBC (Session Border Controller).

## SEC-VVD-MEDIA-FR17: Certifications

**Common Criteria Certified** offerings _MUST_ claim compliance to a [NIAP-approved Protection Profiles](https://www.niap-ccevs.org/Profile/PP.cfm) - [Extended Package for Session Border Controller](https://www.niap-ccevs.org/MMO/PP/ep_sbc_v1.1.pdf) and/or [Collaborative Protection profile for Network Devices](https://www.niap-ccevs.org/Profile/Info.cfm?PPID=440&id=440). Connect with Common Criteria [Certifications Team](https://apps.na.collabserv.com/communities/service/html/communitystart?communityUuid=c46e47c1-f391-4a89-a960-e30e30eaf1b8).

**Protection Profile - EP_SBC_V1.1, EP_VVOIP_V1.0 FCS_SRTP_EXT.1.2 SRTP** offerings _SHOULD_ implement SDES-SRTP with a modification to the cipher list from CommonCriteria_ApprovedCiphers.

**Federal Risk and Authorization Management Program(FedRAMP) Certified** offerings _MUST_ comply with [NIST800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-4/final) as specified by [FedRAMP](https://www.fedramp.gov/). Connect with FedRamp [Certifications Team](https://apps.na.collabserv.com/communities/service/html/communitystart?communityUuid=c46e47c1-f391-4a89-a960-e30e30eaf1b8).

# Informative References
- RECIPE: [Alternate Security Mechanisms for Legacy protocols](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Alternate%20Security%20Mechanisms%20for%20Legacy%20protocols.aspx)
- [SANS VoIP Security Whitepaper](https://www.sans.org/reading-room/whitepapers/voip/security-issues-countermeasure-voip-1701)
- [Cisco IP Phone Security](https://www.cisco.com/c/en/us/solutions/small-business/resource-center/security/tips-ip-phone-security.html)
- [Cisco Unified Communication Security](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/white_paper_c11-620461.html)
- Sample Defects: [H.323 Advisories](https://tools.cisco.com/security/center/Search.x?keyword=H.323&criteria=or&publicationTypeIDs=1,6,9)
- Sample Defects: [MGCP Advisories](https://tools.cisco.com/security/center/Search.x?keyword=MGCP&criteria=or&publicationTypeIDs=1,6,9)
- Sample Defects: [MEGACO Advisories](https://tools.cisco.com/security/center/Search.x?keyword=MEGACO&criteria=or&publicationTypeIDs=1,6,9)
- Sample Defects: [UNIStim Advisories](https://tools.cisco.com/security/center/Search.x?keyword=UNISTIM&criteria=or&publicationTypeIDs=1,6,9)
- Sample Defects: [SIP Advisories](https://tools.cisco.com/security/center/Search.x?keyword=SIP&criteria=or&publicationTypeIDs=1,6,9)
- Sample Defects: [SCCP Advisories](https://tools.cisco.com/security/center/Search.x?keyword=SCCP+Skinny&criteria=or&publicationTypeIDs=1,6,9)
- Sample Defects: [CTI Advisories](https://tools.cisco.com/security/center/Search.x?keyword=CTI&criteria=exact&publicationTypeIDs=1,6,9)
- Sample Defects: [RTP Advisories](https://tools.cisco.com/security/center/Search.x?keyword=RTP&criteria=exact&publicationTypeIDs=1,6,9)
- Sample Defects: [SRTP Advisories](https://tools.cisco.com/security/center/Search.x?keyword=SRTP&criteria=exact&publicationTypeIDs=1,6,9)
- Sample Defects: [RTCP Advisories](https://tools.cisco.com/security/center/Search.x?keyword=RTCP&criteria=exact&publicationTypeIDs=1,6,9)

# Normative References

- H323 Security - [H235 Security Standard](https://www.itu.int/rec/T-REC-H.235.1-200509-I/en)
- MGCP Security - [RFC 3435](https://tools.ietf.org/html/rfc3435#section-5)
- Megaco Security - [H248 Security Standard](https://www.itu.int/rec/T-REC-H.248.1)
- SIP - [RFC 3261](https://www.ietf.org/rfc/rfc3261.txt)
- SIP Location Service - [RFC 3263](https://tools.ietf.org/html/rfc3263)
- NAT Traversal with SIP - [RFC 5766](https://tools.ietf.org/html/rfc5766)
- RTP & RTCP Security - [RFC 3711](https://tools.ietf.org/html/rfc3711)
- [SIP Forum](https://www.sipforum.org/news-events/ietf-drafts/)
- [IETF STIR](https://www.ietf.org/blog/stir/)
- [Megaco](https://tools.ietf.org/html/rfc3525)
- [UNIStim](https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/UNIStim.html)
- [RFC 3261](https://tools.ietf.org/html/rfc3261) and [RFC 3329](https://tools.ietf.org/html/rfc3329)
- [SCCP](https://en.wikipedia.org/wiki/Skinny_Call_Control_Protocol)
- [CTI](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/ctios/ctios4_6x/feature/guide/ctipd1.html)
- [RTP](https://tools.ietf.org/html/rfc3550)
- [AES67](http://www.aes.org/publications/)
- [webrtc](https://webrtc.org/)
- [WebRTCSecurity](https://webrtc-security.github.io/)

# Attributes

    id: SEC-VVD-MEDIA
    version: 1
    category: Cryptographic Support
    riskArea: Cryptography, Encryption & Key Management
    legallysensitive: false
    waivable: true
    issueref: ISS_Cleartext
    applicability:
      - force: mandatory
        target:
          restrict: >
            Media protocols
    priority: 8
    phase: requirements
    tags:
        - EN/PD
        - PSB/OnPrem
        - Cloud
