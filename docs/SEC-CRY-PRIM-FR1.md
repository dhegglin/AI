# Headline

Algorithms and Primitives

# Description

This requirement includes a mandatory list of [crypto](#DEF_Cryptography)
algorithms and other [primitives](#DEF_CryptographicPrimitive) to use.
This list affects essentially *every* cryptography-related choice to be
made. This includes not just ciphers, MACs, hashes, and the like, but
things like random number generators and their seed sources. No
other algorithms and primitives should be used in offerings.

# Behavior

The [supplement included in this requirement](https://wwwin-github.cisco.com/CSDL/PSB/blob/master/normative-external/crypto-algs-9.xlsx?raw=true) contains the algorithm primitives and parameters applicable to most common protocols in separate tabs of the file.

The supplement includes the usual "_MUST_", "_SHOULD_", "_MAY_",
"_SHOULD_NOT_", and "_MUST_NOT_" forces. It may also
include "DEPRECATE" or "EC ONLY" which are close in spirit to
gradations of "SHOULD NOT", but demand additional mandatory
protections. Occasionally the conditions when these take effect
are modified by comments in the supplement.

In general,

1. [Offerings](#DEF_Offering) _MUST_ implement each primitive marked
  as "MUST" in the "Implement" column.

1. If a primitive is marked as "MUST" in the
  "Enable by default" column, then the product _MUST_  enable that
  primitive if it implements it. If a primitive is marked as "MUST"
  in an "Enable by default" column, but as other than "MUST" in
  the corresponding "Implement" column, then that primitive _MUST_
  be enabled by default *only if it's implemented*, but is not required
  to *be* implemented to begin with.

1. **Specifically regarding service offerings** ,
  if Cisco is the [controlling policy entity](#DEF_ControllingPolicyEntity)
  for part or all of the cryptographic policy of a
  *service* [offering](#DEF_Offering), the offering is
  not required to *Implement* any primitive unless it is also
  required ("MUST") in the *Enable by [default](#DEF_Default)* column.
  In other words, if the *Enable by default* column
  in the supplement includes a "MUST" then the service offering
  ought to enable that cipher only if the *Implement* column says it
  "MUST" be implemented.
  When it does not include a "MUST, the *Enable by default* column of
  the supplement dictates what a service offering ought to do with
  the cipher. For example, if the column has it as a "MAY" the
  cipher MAY be implemented and enabled by default.
  This does *not* apply to product offerings.

1. The parameters listed for a protocol or format in the supplement _MUST_
   be used whenever implementing a [cryptographic](#DEF_Cryptography)
   protocol or data format that has its own tab in the supplement.
1. You _MUST_ select [cryptographic primitives](#DEF_CryptographicPrimitive)
   as described ιn the "Primitives" tab of the supplement whenever you implement a
   [cryptographic](#DEF_Cryptography) protocol not specifically mentioned in the
   supplement.
1. Regardless of the protocol or the purpose, you _MUST_NOT_ use
   [cryptographic primitives](#DEF_CryptographicPrimitive) that are not
   authorized by the supplement.

The rest of the forces in the supplement are defined as

- SHOULD: You _MUST_ implement each primitive marked as "SHOULD"
  unless you have a *documented* reason *not* to do so. Some identifiable
  person _MUST_ be on record as responsible for the decision. This is
  the usual PSB meaning of "_SHOULD_".
- MAY: Implementing primitives marked with "MAY" is purely optional.
- SHOULD NOT: You _MUST_NOT_ implement any primitive marked as "SHOULD NOT" unless
  you have a *documented* reason to do so. Some identifiable person
  _MUST_ be on record as responsible for the decision. This is the usual
  PSB meaning of "_SHOULD_NOT_".
- DEPRECATE: You _MUST_NOT_ implement any [primitive](#DEF_CryptographicPrimitive)
  marked as "DEPRECATE" unless you know of a *specific, current* customer
  need for it. Past needs, future needs, and hypothetical needs do not
  qualify. You _MUST_ be able to identify particular customers who need the
  primitive, and explain the reasons for their needs. You _SHOULD_
  document this; in the future, you may be required to actively report
  which customers are using deprecated primitives, on pain of those
  primitives being demoted to "MUST NOT".
- EC ONLY: You _MUST_NOT_ implement any [primitive](#DEF_CryptographicPrimitive)
  marked as "EC ONLY" unless a verified [external
  constraint](#DEF_ExternalConstraint) demands it. "Customers want it" is
  not enough to meet the definition of "[external
  constraint](#DEF_ExternalConstraint)". If an [external constraint](#DEF_ExternalConstraint) does demand using an "EC ONLY" primitive,
  then you _MAY_ implement that primitive *for
  the particular communications affected by the external constraint*,
  provided that an entity *other than Cisco* is the [controlling policy
  entity](#DEF_ControllingPolicyEntity) that actually enables your
  [offering's](#DEF_Offering) participation in that communication. Note
  that services can rarely meet this condition.
- MUST NOT: You _MUST_NOT_ implement (or enable by default) any primitive marked
  as "MUST NOT", regardless of "justification". If you really need to do
  something the supplement actively forbids, you will have to go through
  the process to have it modified or to get a waiver.

**Supplemental Guidance**: The supplement lists a preference order for
the various ciphers. This preference order is no longer considered
normative; instead, they can be treated as suggestions. An offering
will not be considered out of compliance because it did not follow
the preference order.

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
    version: 7
    id: SEC-CRY-PRIM-FR1
    issueref: ISS_SEC-CRY-PRIM
    tags:
    - EN/PI
    - CloudCritical
    - Hardening
    - Critical PSB
    - PSB/OnPrem
    - FAST
