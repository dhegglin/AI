# Headline

Use approved and well seeded random number generation

# Key Benefits

Unpredictable random numbers are essential for many security
operations.  Many commonly used random number generators are
weak, that is, by seeing some of their outputs, the entire
sequence can be reproduced.  Furthermore, initializing even a good
random number generator with a seed that can be guessed can
also allow the sequence to be reproduced.  In either case,
this could void the security that might otherwise
be found within a product.

# Description

Almost all [cryptography](#DEF_Cryptography) (and some non-cryptography)
depends on you knowing numbers that your adversaries can't predict.
Successful prediction leads to total failure. Use
approved sources of [unpredictability](#DEF_Unpredictability) and use it
to seed an approved random number generator.

Remember that, like all PSB requirements, this applies to third party
code you include, as well as to code that you write.

If you're building hardware, this is one of the requirements that
demands you include a Cisco standard trust anchor module (TAm), such as ACT-2 or its successors.
If you're reselling hardware, this
requirement demands that it have a good hardware random number source.

This is a complicated requirement. Don't panic. The implementation
advice gives "worked examples" for the most common cases.

# Behavior

Whenever security depends on an adversary being unable to predict a
random value (including but not limited to cryptographic keys and nonces)
create that value using a cryptographic random number generator
(RNG, also sometimes referred to as a DRBG) as described below. As with all other PSB requirements, this
applies to all third party software you include in any Cisco
[offering](#DEF_Offering) as well as to your code.

When deriving keys or other values from "raw" RNG output, use and
preserve [unpredictability](#DEF_Unpredictability) at least equivalent
to the bits of security (BoS) listed for the consuming primitive in the supplement to
[SEC-CRY-PRIM-FR1](#SEC-CRY-PRIM-FR1).

This PSB requirement sets minimum standards. Beyond what's
described here, cryptographic RNGs _SHOULD_ comply with, and be
evaluated against, NIST 800-90A, 800-90B, and 800-90C.

If you rely on an RNG provided by third-party software, including your
operating system, verify that the RNG meets this requirement *as
deployed and used in your offering*. Many operating
system RNGs use various seed sources, some of which are not PSB
approved.

If you provide software that runs on a [user
platform](#DEF_UserPlatform), that software _MUST_ meet this
requirement on *every* user platform type,
configuration, and version that you tell customers is acceptable. Your
software _SHOULD_ check for unsupported user
platform configurations and refuse to run on them.

## SEC-CRY-RANDOM-FR1 Requirements on random number generators

<a id="SEC-CRY-RANDOM-general-structure"></a>

Each random number generator relied on for any security purpose _MUST_
consist of an approved RNG (listed in the supplement to
SEC-CRY-PRIM), seeded from one or more sources listed
under "approved seed upredictability sources" below.

You _MAY_ additionally use as many other seed sources as you find
appropriate, but *only [unpredictability](#DEF_Unpredictability) from
approved sources may be relied on in meeting any part of this
requirement* , including determining the total
unpredictability of the seed or output data.

1.  The random number generator and all the unpredictability sources relied on in
    assuring adequate output unpredictability, and all data paths
    carrying seed data between them, _MUST_ lie inside of a single
    [controlled space](https://cserv.cisco.com/library/glossary/CG56) (possibly enclosing a
    smaller controlled space reserved exclusively for the DRBG).

    It's rarely possible to extend a controlled space to include a
    network-attached "entropy source", so such sources are almost always
    forbidden. Even when you can extend some sort of controlled space
    around them, you _SHOULD_NOT_ use such devices.
    
2.  You _MUST_ seed your approved RNG with at least 128 bits of unpredictability.
    Some products may have a customer-based need to implement 256 bits of security;
    those products will need to use an RNG with 256 bits of security, and seed the
    RNG with at least 256 bits of unpredictability.

3.  Output passing from the RNG to its clients _MUST_ remain inside of
    a controlled space.

4.  You _MUST_NOT_ use any output from the RNG until it has
    received seed material with unpredictability of at least its listed
    "bits of security" from *each* of its seed sources.

5.  If the controlled space boundary enclosing
    the RNG includes paths that could leak seed material or RNG state
    outside of the controlled space when operating as designed, then
    reseed the RNG from an approved source no less than every 5
    minutes. You _SHOULD_ reseed more often.

    New seed unpredictability _SHOULD_ be
    provided at at least twice the maximimum expected rate of leakage.
    If you can identify specific leakage events, you _SHOULD_ stop
    using the RNG's output after those events until you have fully
    reseeded it, adding as much
    unpredictability as you would add at
    initialization time.

    To reseed an RNG that may leak, you _MAY_ use the same higher-level RNG you used
    to initially seed the RNG, provided that the
    internal state of that source does not lie in the "leakable" part of
    the controlled space enclosing the receiving DRBG. In this case, you
    rely on the fact that, although the internal state of the receiving
    RNG may have been compromised, the internal state of the source has
    not, and therefore the adversary cannot actually know the new input
    that the target RNG is receiving.

6.  You _MAY_ add new seed data to the RNG's pool at any other time.

7.  You _SHOULD_NOT_ ever completely reinitialize the RNG except as
    part of a [bounded computer](#DEF_BoundedComputer) reboot or a
    similar initialization of a larger enclosing system.

8.  If any of your sources of unpredictability provides a self test or
    "health check", then you _MUST_NOT_ rely on unpredictability from
    that source unless you have verified that the test has been
    conducted and passed.
    
## SEC-CRY-RANDOM-FR2 Requirements on seed sources

<a id="SEC-CRY-RANDOM-approved-seed"></a>

The data used to initially seed the approved RNG 
_MUST_ be derived from the seed sources described below.
You _MAY_ use other
seed sources in addition to these, but _MUST_NOT_ rely on other
sources in determining whether any value is
[unpredictable](#DEF_Unpredictability) enough for any use.

You _MAY_ also seed the RNG from a previously instantiated approved RNG,
if the previously instantiated RNG has already been seeded,
and passed any required health tests.

The listed sources are often made available to software using an
operating system service or pseudodevice. Such a service gathers seed
from various sources, combines and conditions the seed data through a
larger random number generation system, and makes the result available
to user-mode programs. However, even if you do not provide the operating
system itself, you _MUST_NOT_ rely on any operating system random
number generator without first assuring that it not only uses the right
seed sources, but also meets all the other rules of this requirement.

NB: When *you* provide an operating system or other programming
environment, it's also required to meet
[SEC-CRY-PLATRAND](#SEC-CRY-PLATRAND).

## SEC-CRY-RANDOM-FR3 Seed Requirements on Services (both "cloud" and "bare hardware")

If your [offering](#DEF_Offering) is a service, then each
[bounded computer](#DEF_BoundedComputer) that's used as part of the
offering and requires [unpredictable](#DEF_Unpredictability) data for
security _MUST_ meet the same standards that would be required of an
equivalent hardware product sold by Cisco. This includes the hardware
underlying third-party "cloud" services.

In practice, this usually simply means using X86 `RDSEED` and/or
`RDRAND`, optionally combined with other sources. This can be done
directly, or through operating system pseudodevices (like
`/dev/urandom`) or other services like (`getrandom()` or `AF_ALG`
sockets). These _MUST_ be configured to meet the other rules in
SEC-CRY-RANDOM, and usually also [SEC-CRY-PLATRAND](#SEC-CRY-PLATRAND),
but the effort involved is usually very small.

This rule applies--

1.  To all operating systems, user-mode software, and other programs, in
    every service offering.

2.  Regardless of the form in which the software is installed or the
    layer it occupies in the software stack. System images, virtual
    machine images, container images, and user-mode programs are all
    required to comply, even if they were created by third parties.

3.  Regardless of whether the underlying infrastructure is operated by
    Cisco or some other party.
    
## SEC-CRY-RANDOM-FR4 Seed requirements on software for turnkey modules

Software provided with any Cisco [turnkey module](#DEF_TurnkeyModule),
including any [standalone device](#DEF_StandaloneDevice), _MUST_ use
sources as follows--

1.  If the hardware of the turnkey module provides
    any fully unpredictable (link to SEC-CRY-RANDOM-fully-unpredictable)
    or FIPS 800-90B approved (link to SEC-CRY-RANDOM-800-90B) sources, then
    it _MUST_ use at least one such source.

2.  If no fully unpredictable sources are available, then a derated source
     (link to SEC-CRY-RANDOM-derated) _MUST_ be used if a derated source is available.

    You _MUST_ process all seed data from any derated source through
    an approved RNG. As described in the listing of derated sources,
    you _MUST_ use extra seed data from each derated source to
    compensate for its limited
    [unpredictability](#DEF_Unpredictability).

3.  If no fully unpredictable or derated sources are available on the
    hardware being updated, then at least one approved
    fallback source (link to SEC-CRY-RANDOM-fallback) _MUST_ be used.

## SEC-CRY-RANDOM-FR5 Seed Requirements on [Software](#DEF_Application) installed on [user platforms](#DEF_UserPlatform)

The requirements for SEC-CRY-RANDOM-FR4 also apply in this case.

If the [user platform's](#DEF_UserPlatform) random number generation
system doesn't meet all the rules of this requirement, but the user
platform gives you direct access to any of the listed seed sources, you
_MUST_ take seed material directly from the available sources and
process it using your own approved RNG.

If your [offering](#DEF_Offering) runs on a user
platform that doesn't allow you access to any
approved sources, then you _MUST_NOT_ rely on any
[unpredictable](#DEF_Unpredictability) values for security. Since it's
usually infeasible to meet this rule, you may be forced to abandon
support for the platform.

## SEC-CRY-RANDOM-FR6 Seed sources on Cisco-controlled bounded computer designs

If your [offering](#DEF_Offering) includes a [bounded
computer](#DEF_BoundedComputer) whose design is [Cisco
controlled](#DEF_CiscoControlled), then it _MUST_ include
a Cisco standard trust anchor module (TAm), such as ACT-2 or its successors. This is also required
by [SEC-CRE-CHIPID](#SEC-CRE-CHIPID). ACT-2 RNG output _MUST_ be
available to the main operating system of the bounded computer.

## SEC-CRY-RANDOM-FR7 Seed sources on non-Cisco-controlled bounded computer designs

If your [offering](#DEF_Offering) includes any [bounded
computer](#DEF_BoundedComputer) at all, then it _MUST_ provide at
least one approved fully unpredictable or
derated sources, and _SHOULD_ provide two or more such sources.

You _MUST_NOT_ resell any bounded computer(#DEF_BoundedComputer
that does not have a specifically approved hardware source seed source
for [unpredictability](#DEF_Unpredictability).

## Approved seed unpredictability sources

<a id="SEC-CRY-RANDOM-appr-seed"></a>

Rely *only* on sources listed in the following sections for any PSB-required
[unpredictability](#DEF_Unpredictability).

You _MAY_ combine other sources with the approved ones, but
_MUST_NOT_ count their output as part of the unpredictable seed
material demanded by this requirement.

Note: All of these are "approved", but some are more "approved" than
others. You _MUST_ use sources from the *particular sublists* required
for your offering under "seed sources hardware must
provide" and meet the requirements listed
in "requirements on seed sources”.

## NIST SP 800-90B Certified entropy sources

<a id="SEC-CRY-RANDOM-800-90B"></a>
These are entropy sources that have been certified to pass the NIST
requirements in NIST SP 800-90B.
If you do so, you MUST
read a sample size that corresponds to the required security strength (which will
be documented by the provider) and you MUST follow the instructions on using
this source (which includes checking for health test failures before usage).

## Fully unpredictable sources

<a id="SEC-CRY-RANDOM-fully-unpredictable"></a>

This is the list of entropy sources that can be treated as fully unpredictable

### Cisco ACT-2 (256 bits of security)

You _MAY_ treat each bit returned from ACT-2's (and successor, such as Aikido)
RNG as providing one
full bit of unpredictability, up to a maximum of 256 bits of
unpredictability from any single power-up or call to the reseed function
on any single ACT-2 instance.

ACT-2's random number generator provides a health check. You _MUST_
verify that the health check has passed before relying on random data
from ACT-2.

Remember that [Cisco controlled](#DEF_CiscoControlled) hardware designs
_MUST_ include ACT-2 or equivalent.

### X86 RDRAND and RDSEED

Data from the `RDRAND` instructions can be used to provide 128 bits
of uncertainty and `RDSEED` instructions can be used to provide
256 bits of uncertainty, assuming you read at least that much data
from the instructions.

`RDSEED` and `RDRAND` include health checks, and clear the CPU's carry
bit if the health check fails.
You _MUST_ verify the carry bit on every use of either instruction,
and _MUST_NOT_ use "random" data returned with the carry bit cleared.
Note that the carry bit is also cleared
on healthy hardware if random data aren't immediately available; you
_MUST_ distinguish these cases by retrying. Intel recommends declaring
the RNG hardware failed after ten successive failed tries.

### ARM TrustZone CryptoCell DRBG

You _MAY_ treat output from the Arm TrustZone CryptoCell DRBG, seeded
the TrustZone TRNG according to ARM's standard design, as unpredictable
at the rate of one bit per bit of DRBG output, up to a maximum of 256
bits per call to its reseeding request function. The TrustZone
CryptoCell DRBG is CTR_DRBG with AES-256.

Note: The "TrustZone CryptoCell DRBG" is different from the "TrustZone
TRNG". The CryptoCell DRBG, *seeded from* the TrustZone TRNG, is a fully
unpredictable source and a complete RNG. The Trustzone TRNG by itself is
a derated seed source, *not* a complete RNG. Don't confuse the two.

## Derated sources

<a id="SEC-CRY-RANDOM-derated"></a>

Derated sources are seed sources only, not complete RNGs. Output from
any of these sources _MUST_ be conditioned through an approved DRBG,
rather than being used directly for security purposes.

Sources in this group provide some
[unpredictability](#DEF_Unpredictability), but not every possible
returned value is equiprobable; their output may have internal
correlations. The available bits of unpredictability are therefore fewer than the
raw data bits returned. The description for each source tells you how
much extra seed you must use from each source to get any particular
amount of unpredictability.

### ARM TrustZone TRNG (not a true RNG)

You _MAY_ treat output from the ARM TrustZone TRNG hardware as
unpredictable at the rate of one bit per 16 bits of TrustZone TRNG
output. Note that the TrustZone TRNG seed source is a different thing
than the TrustZone CryptoCell DRBG.

## Fallback sources

<a id="SEC-CRY-RANDOM-fallback"></a>

Fallback approval applies only to the specific sources listed here. You
_MUST_NOT_ rely on other approaches or implementations even if they
look similar.

### "Generic" hardware RNGs (including most TCG TPMs)

<a id="SEC-CRY-RANDOM-generic-hw"></a>

When allowed to use a fallback source on a [user
platform](#DEF_UserPlatform) that provides hardware purporting to
generate random numbers (or an OS driver that purports to be talking to
such a hardware device), when the specific hardware is unknown or not
NIST 800-90B compliant, you _MAY_ treat its "random" data as
unpredictable at a rate of no more than *1 bit per 32 bits* of RNG
output, and no more than 256 bits of
[unpredictability](#DEF_Unpredictability) per minute of real time.

If the manufacturer's documentation for the source specifies an
unpredictability of *less* than 1 bit per 32 bits of output, or gives
other restrictions, you _MUST_ further derate the source to match the
manufacturer's recommendations.

Note: Neither the TCG specification nor the Common Criteria protection
profile for TPMs addresses the quality of the provided random numbers.
Random number generators vary among TPM manufacturers. Unless your TPM
is NIST certified, you will have to treat it as a generic hardware
source.  If your TPM has been certified to meet the NIST 800-90B
requirements, then it _MAY_ be treated as an 800-90B source.

### Hypervisor random devices

When allowed to use a fallback source, you_MAY_ treat data from a
hypervisor's random "hardware" device (such as KVM's virtio RNG) as
[unpredictable](#DEF_Unpredictability) at the rate of one half bit per
bit of virtual device output.

### Linux Kernel timing measurements

When allowed to use a fallback source, you _MAY_ rely on the timing
measurements and other ad-hoc [unpredictability](#DEF_Unpredictability)
sources used in any Linux kernel after version 3.0. You _MAY_ assume
that the kernel's estimates of available unpredictability are correct, which implies
that you _MAY_ treat data from `/dev/urandom` as having up to 256 bits
of unpredictability, and _MAY_ treat data from `/dev/random` as having
one bit of unpredictability per bit read, with no limit on the number of
bits read.

# Informative References

NIST SP 800-90A Rev 1, "Recommendation for Random Number Generation
Using Deterministic Random Bit Generators":
<https://csrc.nist.gov/publications/detail/sp/800-90a/rev-1/final>

NIST SP 800-90B, "Recommendation for the Entropy Sources Used for
Random Bit Generation":
<https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90B.pdf>

NIST SP 800-90C Second Draft, "Recommendation for Random Bit Generator
(RBG) Constructions":
<https://csrc.nist.gov/publications/detail/sp/800-90c/draft>

NIST Entropy Assessment programs,
<https://github.com/usnistgov/SP800-90B_EntropyAssessment>.

Note that these programs are useful only for assessing raw
*unconditioned* hardware seed sources, and their results are **almost
entirely meaningless** when run against final DRBG output.

"Microsoft Windows 7 Kernel Mode Cryptographic Primitives Library
(cng.sys) Security Policy Document":
<https://csrc.nist.gov/csrc/media/projects/cryptographic-module-validation-program/documents/security-policies/140sp1328.pdf>

"Microsoft Windows 10 (and Server 2016) Non-proprietary Security Policy
for FIPS 140-2 Validation":
[https://csrc.nist.gov/csrc/media/projects/cryptographic-module-validation-program/documents/security-policies/140sp2936.pdf](https://csrc.nist.gov/csrc/media/projects/cryptographic-module-validation-program/documents/security-policies/140sp1328.pdf)

"Microsoft Windows Cryptographic Provider Development Kit":
<https://www.microsoft.com/en-us/download/details.aspx?id=30688>

"AMD Random Number Generator":
<http://support.amd.com/TechDocs/amd-random-number-generator.pdf>

"The Difference Between RDRAND and RDSEED" (Intel):
<https://software.intel.com/en-us/blogs/2012/11/17/the-difference-between-rdrand-and-rdseed>

"Intel Digital Random Number Generator (DRNG) Software Implementation
Guide":
<http://software.intel.com/en-us/articles/intel-digital-random-number-generator-drng-software-implementation-guide>

Using the [Cisco Common Crypto
Libraries](https://cisco.sharepoint.com/Sites/CommonSecurityModules) in accordance with SEC-CRY-STD facilitates compliance with this
requirement.

RECIPE: [RNG Source for Virtual Products](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/RNG%20Source%20for%20Virtual%20Products.aspx)

# Requirement References

    ---
    foreign_id: SEC-CRY-PRIM-FR1
    relation: connects
    headline: |-
      SEC-CRY-PRIM-FR1
              and FR2 lists approved DRBGs to be used in
              the scheme described by SEC-CRY-RANDOM.

    source: PSB
    ---
    foreign_id: SEC-CRY-PLATRAND
    relation: connects
    headline: |-
      SEC-CRY-PLATRAND
              requires seeding the operating system's
              RNG in addition to any RNGs used by
              Cisco code.

    source: PSB

# History


```yaml
-----
affected_psb: SEC-CRY-RANDOM-3
description:  Updates to new format and 128-bit entropy.
-----
deprecated_psb: SEC-CRY-RANDOM-2
impact: normative
description: >
  Backed off demanded entropy requirements to 128
  Generalized ACT-2 requirements to include approved TAm modules.
  Corrected entropy provided by RDRAND to 128 bits.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
          offerings
    category: Cryptographic Support
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 3
    id: SEC-CRY-RANDOM
    issueref: ISS_CryptoError
    tags:
    - EN/PI
    - EN/PD
    - Hardening
    - Critical PSB
    - PSB/OnPrem
    - Cloud
