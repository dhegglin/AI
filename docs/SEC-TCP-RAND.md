# Headline

Randomize initial TCP sequence numbers

# Key Benefits

Predictable TCP sequence numbers make it possible for one host to open a
TCP connection which appears to come from another, circumventing
security policies in a way which can be impossible to trace.

# Description

A cracker who can predict the TCP sequence numbers you use may be able
to spoof a TCP connection to you. This is bad.

# Behavior

## SEC-TCP-RAND-FR1: Random Sequence Numbers

Initial TCP sequence numbers _MUST_ be selected in a way unpredictable
to attackers. A cryptographic-grade pseudorandom number generator
_SHOULD_ be used for this purpose.

# History

```yaml
-----
affected_psb: SEC-TCP-RAND
description:  Updated to functional requirements. 

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-

                      TCP implementations

    category: Traffic and Protocol Protection
    riskArea: Network Security
    waivable: true
    version: 1
    id: SEC-TCP-RAND
    issueref: ISS_TCPTamper
    tags:
    - EN/PI
    - PSB/OnPrem
    - EN/PI DT
    - FAST
