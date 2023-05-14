# Headline

Use safe C libraries

# Behavior

## SEC-RUN-SAFEC-FR1: Use SafeC libraries and API elements

Your process for developing code in C and C++ _MUST_ include using the
libraries and API elements described in EDCS-806552, the CSDL Safe
Library Implementation Guide instead of their "unsafe" standard C
alternatives. Your developers _MUST_ be trained or otherwise informed
of this. Your build system _SHOULD_ know which modules are expected to
contain "unsafe" function calls and _SHOULD_ issue error or warning
messages when "unsafe" functions are used in other modules.

You _SHOULD_NOT_ rewrite existing code to use the "safe" functions
unless you have some other reason to modify that code. You
_SHOULD_NOT_ modify third party code to use the "safe" functions
unless the provider of that code will merge your changes into the
[upstream](#DEF_Upstream) version.

# Normative References

CSDL Safe Library Implementation Guide\
[EDCS-806552](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-806552&ver=latest)

# Requirement References

    ---
    foreign_id: SEC-LOG-ATTACK
    relation: connects
    headline: |-
      SEC-LOG-ATTACK
              requires you to log any event that might indicate
              a security attack. Some overruns prevented by
              the functions described in SEC-RUN-SAFEC may
              be indications of possible security attacks.

    source: PSB
    ---
    foreign_id: SEC-RUN-OSC
    relation: connects
    headline: |-
      SEC-RUN-OSC
              requires you use certain compiler
              extensions to reduce buffer overflows, and therefore
              machine code injection vulnerabilities, in C and C++
              code.

    source: PSB

# History

```yaml
-----
affected_psb: SEC-RUN-SAFEC
description:  Updated to functional requirements.

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 9
    applicability:
    - force: mandatory
      target:
        restrict: |-
          Cisco controlled
                    software written in C or C++

        class: LangC
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 2
    id: SEC-RUN-SAFEC
    issueref: ISS_Inject
    tags:
    - EN/PD
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - EN/PD DT
