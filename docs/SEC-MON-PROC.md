# Headline

Provide process listings

# Description

Provide lists of running processes for intrusion detection

# Behavior

## SEC-MON-PROC-FR1: Access to process information
Give [administrators](#DEF_Administrator) access to lists of the running
processes (or other loaded programs) on your [product](#DEF_Product).

If your operating system kernel collects it, display the following
information for each process/program:

1.  The numeric process ID or other unique process identifier.
2.  The process name (if the kernel provides for a process to have a
    name other than that of the loaded program).
3.  The name of the file containing the "main program". You _SHOULD_
    also provide the capability to display the names of the files from
    which shared libraries or other code have been loaded or mapped into
    the process address space.
4.  The command line arguments passed to the process when it was
    started, and/or the current command line if the process can modify
    its command line.
5.  Principals associated with the process, such as usernames or group
    names.
6.  The process ID of the parent process (the one that created the one
    being displayed).
7.  The time and date at which the process was started.
8.  The total CPU time used by the process.

You _MAY_ include more detailed information. You _MAY_ also provide
for abbreviated listings with less information.

You _MAY_ redact *specific* information regarding *specifically
chosen* processes if that information might be useful to an attacker,
but would not reasonably be expected to be useful in detecting an
attack. You _SHOULD_ replace such information with generic
placeholders, rather than simply making processes or data "disappear"
from the listing.

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          institutional
            turnkey modules
    - force: mandatory
      target:
        restrict: Offerings incorporating process schedulers (including kernels
          in VMs)
    category: Threat Surface Reduction
    riskArea: System Integrity
    waivable: true
    version: 1
    id: SEC-MON-PROC
    issueref: ISS_Rootkit
    tags:
    - EN/PI
    - EN/PD
    - Hardening
    - PSB/OnPrem
