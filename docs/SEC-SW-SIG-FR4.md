# Headline
Protected Data

# Behavior

The following protected data _MUST_ have a digital signature. However a [module](#DEF_Module) is packaged or installed, the combination of digital signatures on the packages, [manifests](#DEF_Manifest), or other information used to
install or update the module _MUST_ protect all of the following and equivalently, it _MUST NOT_ be possible to change any of these
without invalidating some digital signature:

1.  The module's basic identifying information.

2.  Any information packaged with the module to describe it to
    [administrators](#DEF_Administrator), including information about
    its general nature, its suitability for a particular purpose, its
    relationship to other modules or packages, the effects of installing
    or removing it, or the methods or options to be used in installing
    it. This includes any release notes or "readme" files packaged with
    a module.

3.  Any data or metadata affecting the existence of non-existence of any
    particular unit of [code](#DEF_Code) or data on the installation
    target after the module has been installed or removed.

    It _MUST NOT_ be possible to add content to, or remove content
    from, any module without invalidating a digital signature, even if
    that module is a "meta-module" that includes other modules with
    their own signatures.

    This implies that digital signatures _MUST_ cover every manifest
    relied on for module or package selection, for selection of files or
    other data items to be installed as part of installing a module, or
    for integrity verification of any kind, including package manifests,
    module manifests, or other manifests.

4.  The content of any [code](#DEF_Code) to installed or run on the
    installation target, including installation-time code as well as the
    installed software itself.

5.  Any metadata applied to installed or installation-time
    [code](#DEF_Code) or data that might affect the operation of the
    installation target, during or after installation, including both
    the [code](#DEF_Code) the target executes and the authorization or
    other policies the target applies. This includes, but is not limited
    to--

    1.  Storage locations, such as devices, partitions, and directories.

    2.  File names and other names used by the installation target.

    3.  Information about [principals](#DEF_Principal) "owning" files or
        other data, and analogous information concerning "group
        ownership" if on systems that support it.

    4.  Permission or restriction information describing the access
        various [principals](#DEF_Principal) (or groups) are permitted
        to files or other data. This includes both basic permission
        information like UNIX file modes and more complex permission
        information like access control lists.

    5.  Other, non-principal-based access control information such as
        type labels, classification labels, or compartmentation labels
        (for example SELinux security context information).

    6.  Information controlling the authorization policy applied to
        code, including but not limited to principals to be used to run
        the code (as with Unix set-UID information), and
        non-principal-based privileges to be given to the code (as with
        Linux "capabilities").

    7.  Digital signatures meant to be checked when the code is loaded
        or run after installation.

    8.  Operating-system-specific file attributes like "hidden",
        "protected", "system file", "immutable", etc.

    9.  Other metadata, such as file modification times, if they will
        affect system operation.
        

## Key management, storage, and use/access control

The following keys are "production" keys--

1.  Any private key used by Cisco to sign software for release to any
    party outside of Cisco, except as described below under "Key storage
    exception".

2.  Any private key--

    1.  Whose signature would be accepted as validating code for
        installation by the [default](#DEF_Default) configuration of any
        Cisco [offering](#DEF_Offering), OR

    2.  That would be accepted for update installation by a [user
        platform](#DEF_UserPlatform) on which a Cisco
        [offering](#DEF_Offering) had previously been installed in the
        most usual and ordinary way.

3.  Any private key that corresponds to any
    [certificate](#DEF_Certificate) which--

    1.  Is issued by any certificate authority accepted by default to
        validate software signatures in any system used for other than
        testing purposes, whether that system is a Cisco offering or a
        [user platform](#DEF_UserPlatform), AND
    2.  Mentions code signing in any human readable text embedded in the
        certificate (frequently done with PGP keys used for signing),
        and/or is marked in a machine processable way as being valid for
        code signing (for X.509 certificates, this corresponds to having
        an extended key usage attribute of `id-kp-codeSigning`,
        1.3.6.1.5.5.7.3.3), AND
    3.  Names as a subject Cisco, any Cisco subsidiary, any company or
        organization existing primarily to distribute Cisco software, or
        any DNS domain owned or administered by any of these.

Production keys _MUST NOT_ be stored outside of STO- and/or
Infosec-approved infrastructure as described in the Cisco Cryptographic
Controls Policy, [EDCS-806748](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806748).

The keys used to sign internal development builds _MUST_ be different
from the keys used to sign code released to customers or other users
outside of Cisco.

## Controls on signature generation

Procedures and infrastructure for generating digital signatures, and
controls over access to keys and over the ability to generate signatures
or cause signatures to be generated, _MUST_ be approved under
[EDCS-806748](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806748).

You _SHOULD_ allow only the people who actually prepare packages for
external release to make signatures using production keys. Those not
directly involved in the release process, including product developers,
_SHOULD NOT_ be able to cause signatures to be made using production
keys. Note that, although this limitation is technically only
_RECOMMENDED_ as regards the actual text of this requirement, you are
unlikely to get [EDCS-806748](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806748)
approval for any system that doesn't enforce such a restriction.

Creating a signature using a production key _SHOULD_ require knowing,
positive action by more than one person. Every signature created
_SHOULD_ be logged in way not alterable by those authorizing or
creating the signatures.

## Key storage exception

You _MAY_ use informal storage and management procedures for keys used
to sign software, or used to sign certificates concerning other keys,
when all of the following are true:

1.  No Cisco [offering](#DEF_Offering) will accept packages signed with
    the informally managed keys by [default](#DEF_Default)
    (equivalently, intentional configuration by a properly authenticated
    [administrator](#DEF_Administrator) is required to make an
    [offering](#DEF_Offering) install a package or module signed with
    such a key).

2.  Each such key is used only for debugging and/or testing activities
    which are either--

    1.  Entirely in laboratory or development environments operated by
        Cisco (this does *not* license informal key storage for any
        production activity or violation of any Infosec policy), OR

    2.  In limited field tests involving no more than five partners,
        customers, or locations, and only when--

        1.  The testing is properly authorized by the [controlling
            policy entity or entities](#DEF_ControllingPolicyEntity) for
            the environment in which it takes place, AND
        2.  The testing is done by or under the direct supervision of
            professional programmers, system administrators, or
            similarly sophisticated people, AND
        3.  Those individuals are clearly instructed that test keys are
            in use, told to remove any trust in the keys from any of the
            test equipment at the end of the test, and given clear
            instructions on how to do so, AND
        4.  Any trust in the keys would not survive "wiping" and
            reinstallation of the test equipment using the procedures
            common for that type of equipment.

3.  If any such key is ever made the subject key of any
    [certificate](#DEF_Certificate), that certificate is issued by a
    certificate authority created and used only for the testing
    activity, and the key is never provided to any "public" CA.

4.  All copies of all keys used for the testing, including any
    certificate authority keys, are deleted at the end of the test.

# History

```yaml
-----
affected_psb: SEC-SW-SIG-3
---
impact: nonnormative
description: >
  Break into discrete FR's
-----
affected_psb: SEC-SW-SIG-3
---
impact: normative
description: >
  Add requirements for loadtime signature checks.
```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        class: 
        restrict: |-
          product code
    category: Boot and System Integrity
    riskArea: System Integrity
    waivable: true
    version: 5
    id: SEC-SW-SIG-FR4
    issueref: ISS_SEC-SW-SIG
    tags:
    - EN/PD
    - G7
    - Image Signing
    - Critical PSB
    - PSB/OnPrem
    - FAST
