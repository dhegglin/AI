# Headline

Provide good OS and platform random number generators

# Description

If Cisco provides or controls the OS or runtime environment for some
software (including installing it or configuring it), then Cisco must
provide a good [cryptographic](#DEF_Cryptography) random number
generator, and make that RNG available using the normal and expected
APIs on that platform.

# Behavior

## SEC-CRY-PLATRAND-FR1 Minimal Seed Requirements

Everything to which the conditions apply this requirement _MUST_
provide access to a cryptographic random number generator (RNG) meeting
[SEC-CRY-RANDOM](#SEC-CRY-RANDOM) and capable of at least 128 bits of
[unpredictability](#DEF_Unpredictability) in a single output value.

If the entity affected by this requirement--

1.  Is an instance of a system commonly used outside of Cisco (such as
    Linux, Windows, Android, the Java runtime environment, etc), OR

2.  Provides a standard or commonly used API (such as POSIX or "generic
    Unix"), OR

3.  Provides an environment for running [code](#DEF_Code) developed by
    any entity other than Cisco, even if that code is integrated into
    the system by Cisco,

All RNGs demanded by this requirement _MUST_ be seeded in compliance
with [SEC-CRY-RANDOM](#SEC-CRY-RANDOM), directly or indirectly from at
least the following sources (in addition to any other desired sources):

1.  If the hardware or software platform on which the affected runtime
    environment is installed provides it with access to any source
    listed as "fully unpredictable" in
    [SEC-CRY-RANDOM](#SEC-CRY-RANDOM), then at least one such source.
    Note that if the platform is hardware made or resold by Cisco, then
    [SEC-CRY-RANDOM](#SEC-CRY-RANDOM)*requires* the platform to provide
    such a source.

2.  If no fully unpredictable source is available, but two or more
    sources listed as "derated" in [SEC-CRY-RANDOM](#SEC-CRY-RANDOM),
    are available, then at least two derated sources.

3.  If no fully unpredictable source is available, and only one source
    listed as "derated" in [SEC-CRY-RANDOM](#SEC-CRY-RANDOM), is
    available, then that source, and at least one listed "fallback"
    source if any such source is available.

4.  If no fully unpredictable or derated sources are available, but two
    or more sources listed as "fallback" are available, then at least
    two fallback sources.

5.  If no fully unpredictable or derated sources are available, and only
    one source listed as "fallback" is available, then that source.

If none of the above are available, then it is impossible to meet this
requirement.

Even if a fully unpredictable source is available, all RNGs _SHOULD_
use two or more seed sources approved in
[SEC-CRY-RANDOM](#SEC-CRY-RANDOM), and _MAY_ use as many sources as
desired. It is never a mistake to use more sources, no matter how good
your sources are.

## SEC-CRY-PLATRAND-FR2 Linux-specific rules

If an operating system affected by this requirement is an instance of
Linux, the following additional rules apply.

1.  The user space initialization system (`/sbin/init`, initrd,
    initramfs, etc) _MUST_ prevent any user mode program not
    specifically known *not* to require
    [unpredictable](#DEF_Unpredictability) values from using
    `/dev/urandom` until the RNG backing `/dev/urandom` has been fully
    seeded as described above.

    Note: Recent kernels on modern X86 processors will automatically
    seed `/dev/urandom` from `RDRAND` before returning any data, and
    therefore automatically comply with this rule.

2.  `AF_ALG` sockets offering access to the kernel crypto API _MUST_
    be available to unprivileged user space programs. Each container
    system included by Cisco with the Linux OS _MUST_ forward any access
    to these sockets by programs running into the containers to the
    underlying operating system, and _MUST_NOT_ record the data that is returned.

    At least `drbg_pr_hmac_sha512` and `drbg_nopr_hmac_sha512` _MUST_
    be available; all other NIST DRBGs _SHOULD_ be available. Note
    that this will require back-porting modules in kernels earlier than
    version 3.17.

3.  If the physical or virtual platform on which the Linux instance is
    installed provides it with direct access to any random number
    generator or seed source which is--

    1.  listed as "fully unpredictable" or "derated" in
        [SEC-CRY-RANDOM](#SEC-CRY-RANDOM), and

    2.  Not directly available to user mode programs without kernel
        assistance (for example, the `RDRAND` and `RDSEED` instructions
        on X86 *are* available to all programs and therefore don't
        trigger this rule),

    then--

    1.  `/dev/hwrng` _MUST_ be present, world readable, and backed by
        such a source. Note that the driver makes `/dev/hwrng` readable
        only to root at system startup.

    2.  If the underlying platform makes an ACT-2 chip, or a Cisco
        successor such as Aikido, accessible to the Linux kernel, then
        that chip _MUST_ be the source used to back `/dev/hwrng`.

    3.  The module backing /dev/hwrng _MUST_ be installed (generally
        by the initrd or initramfs) before user space programs requiring
        [unpredictability](#DEF_Unpredictability) are permitted to run.

    4.  The kernel RNG _MUST_ be seeded continuously from the module
        backing /dev/hwrng. On 3.17 and later kernels, this means that
        the module _MUST_ declare a nonzero RNG "quality". On kernels
        earlier than 3.17, `rngd` or a similar user space program
        _MUST_ "manually" copy data from `/dev/hwrng` to
        `/dev/random`.

4.  On X86 processors, the kernel RNG _MUST_ be seeded continuously
    from RDSEED and/or RDRAND if those instructions are available.

    Note: On 3.2 and later kernels, this is automatic. If the kernel is
    earlier than 3.2, this behavior will have to be back ported, or
    simulated using a user space program such as `rngd`.

## SEC-CRY-PLATRAND-FR3 Java/JRE specific requirements

Your Java runtime enviroment _MUST_ provide a default
[cryptographic](#DEF_Cryptography) provider and PRNG type that delivers
data from an approved 128-bit (or better) RNG. The data _SHOULD_ come directly
from kernel RNG or from a hardware RNG listed as "fully unpredictable"
in [SEC-CRY-RANDOM](#SEC-CRY-RANDOM).

# Requirement References

    ---
    foreign_id: SEC-CRY-PRIM-FR2
    relation: connects
    headline: |-
      SEC-CRY-PRIM-FR2
              lists approved DRBGs to be used in
              the scheme described by SEC-CRY-RANDOM
              and required by SEC-CRY-PLATRAND.

    source: PSB
    ---
    foreign_id: SEC-CRY-RANDOM
    relation: connects
    headline: |-
      SEC-CRY-RANDOM
              requires using good random number generators
              to generate various values (and defines
              what a "good RNG" is).
              SEC-CRY-PLATRAND requires infrastructure
              to support and ensure this.

    source: PSB

# History

```yaml
-----
affected_psb: SEC-CRY-PLATRAND
impact: normative
description:  FR1:  Reduced required unpredictability to 128.
FR2:  Fixed requirement about providing uncertainty to containers.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-

                      Every operating system, language runtime environment, framework,
                      or other software providing an
                      execution space
                      for any code
                      that uses cryptography or otherwise relies on
                      unpredictable
                      values.

        class: not_MobileApp
    category: Cryptographic Support
    riskArea: Cryptography, Encryption & Key Management
    waivable: true
    version: 2
    id: SEC-CRY-PLATRAND
    issueref: ISS_CryptoError
    tags:
    - EN/PD
    - Hardening
    - Critical PSB
    - PSB/OnPrem
    - Cloud
    - FAST
