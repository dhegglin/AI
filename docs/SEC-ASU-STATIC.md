# Headline

Perform static analysis

# Key Benefits

Static analysis can find and eliminate many severe software bugs,
especially if used correctly. Regular static analysis also tends to help
developers learn safe coding patterns.

# Behavior

## SEC-ASU-STATIC-FR1: Run Static Analysis

The [offering](#DEF_Offering) team _MUST_ run static analysis using Coverity for C and C++ codebases.  [Offering](#DEF_Offering) teams MAY use an alternative static analysis tool such as Checkmarx, provided the decision is formally approved in advance by the Security and Trust Organization.  For other languages such as Java, Golang, Ruby, Python, the [offering](#DEF_Offering) team _MUST_ run static analysis using the most effective tools available (Coverity, Checkmarx, Find Security Bugs, SonarQube, JTest, etc.).
The [offering](#DEF_Offering) team _MUST_ ensure that static analysis has been run against the complete source code actually used to build your released product.

**Supplemental Guidance**:
- [Coverity for teams in CSG](https://wiki.cisco.com/display/CSTATIC/CSTATIC+Home).
- [Coverity for teams outside of CSG](https://engit.cisco.com/code/coverity).
- [CheckMarx (SCAVA)](https://cisco.sharepoint.com/sites/SES/SitePages/SCAVA.aspx) .
- [SonarQube](https://engit.cisco.com/build/sonarqube).

## SEC-ASU-STATIC-FR2: Enable Security Checkers

The [offering](#DEF_Offering) team _MUST_ enable relevant security checkers when running static analysis tools.  For C and C++ codebase, the following security-related checkers _MUST_ be enabled in Coverity:

  | Category               |   Detail                                         |
  |------------------------|--------------------------------------------------|
  |BAD_COMPARE                   |Misuse of memcmp-style function                   |
  |BAD_COMPARE                   |Unintended comparison to logical negation         |
  |BAD_COMPARE                   |Function address comparison
  |BAD_COMPARE                   |Inequality comparison against NULL
  |BAD_COMPARE                   |Pointer comparison with string literal
  |BAD_FREE                      |Bad Pointer Free
  |BAD_SIZEOF                    |Incorrect sizeof expression
  |BAD_SIZEOF                    |Sizeof pointer expression
  |BUFFER_SIZE                   |Possible buffer overflow
  |BUFFER_SIZE                   |Copy into fixed size buffer
  |BUFFER_SIZE                   |Destination buffer too small
  |BUFFER_SIZE                   |Destination buffer too small
  |BUFFER_SIZE                   |Overlapping buffer in memory copy
  |BUFFER_SIZE                   |Buffer not null terminated
  |CHROOT                        |Insecure chroot
  |DC.STREAM_BUFFER              |Calling risky function
  |DC.STRING_BUFFER              |Calling risky function
  |DC.WEAK_CRYPTO                |Calling risky function
  |FORWARD_NULL                  |Reference null pointer
  |HARDCODED_CREDENTIALS         |Use of hard-coded cryptographic key
  |HARDCODED_CREDENTIALS         |Use of hard-coded password
  |HARDCODED_CREDENTIALS         |Use of hard-coded security token
  |HARDCODED_CREDENTIALS         |Use of hard-coded credentials
  |INTEGER_OVERFLOW              |Overflowed array index read
  |INTEGER_OVERFLOW              |Overflowed array index write
  |INTEGER_OVERFLOW              |Overflowed constant
  |INTEGER_OVERFLOW              |Integer overflowed argument
  |INTEGER_OVERFLOW              |Integer overflow
  |INTEGER_OVERFLOW              |Overflowed pointer read
  |INTEGER_OVERFLOW              |Overflowed pointer write
  |INTEGER_OVERFLOW              |Overflowed return value
  |NEGATIVE_RETURNS              |Negative return
  |OPEN_ARGS                     |Insecure file permissions
  |OVERRUN                       |Illegal address computation
  |OVERRUN                       |Out-of-bounds access
  |OVERRUN                       |Out-of-bounds read
  |OVERRUN                       |Allocation size error
  |OVERRUN                       |Out-of-bounds write
  |REVERSE_NEGATIVE              |reverse negative return
  |READLINK                      |Readlink used insecurely
  |REVERSE_NULL                  |Null pointer dereference
  |RISKY_CRYPTO                  |Violation of user-specified RISKY_CRYPTO policy
  |RISKY_CRYPTO                  |Risky cryptographic hashing function
  |RISKY_CRYPTO                  |Risky cryptographic function
  |SECURE_CODING                 |Calling risky function
  |SECURE_TEMP                   |Insecure temporary file
  |SIZECHECK                     |Size check error
  |STRING_NULL                   |String not null terminated
  |STRING_OVERFLOW               |Copy into fixed size buffer
  |STRING_OVERFLOW               |Destination buffer too small
  |STRING_OVERFLOW               |Buffer overflow
  |STRING_SIZE                   |Unbounded source buffer
  |TAINTED_SCALAR                |Untrusted array index read
  |TAINTED_SCALAR                |Untrusted array index write
  |TAINTED_SCALAR                |Untrusted value as argument
  |TAINTED_SCALAR                |Untrusted loop bound
  |TAINTED_SCALAR                |Use of untrusted scalar value
  |TAINTED_SCALAR                |Untrusted pointer read
  |TAINTED_SCALAR                |Untrusted pointer write
  |TAINTED_STRING                |Format string vulnerability
  |TAINTED_STRING                |Use of untrusted string value
  |TOCTOU                        |Time of check time of use
  |UNENCRYPTED_SENSITIVE_DATA    |Cleartext sensitive data in a cookie
  |UNENCRYPTED_SENSITIVE_DATA    |Cleartext sensitive data in a database
  |UNENCRYPTED_SENSITIVE_DATA    |Cleartext sensitive data in a file
  |UNENCRYPTED_SENSITIVE_DATA    |Cleartext transmission of sensitive data
  |UNINIT                        |Uninitialized array index read
  |UNINIT                        |Uninitialized array index write
  |UNINIT                        |Uninitialized scalar variable
  |UNINIT                        |Uninitialized pointer read
  |UNINIT                        |Uninitialized pointer write
  |USE_AFTER_FREE                |Read from pointer after free
  |USE_AFTER_FREE                |Write to pointer after free
  |USE_AFTER_FREE                |Double close
  |USE_AFTER_FREE                |Double free
  |USE_AFTER_FREE                |Use after free
  |USE_AFTER_FREE                |Use after close
  |USER_POINTER                  |User pointer dereference
  |WEAK_GUARD                    |Check against reverse DNS lookup
  |WEAK_GUARD                    |Check against reverse DNS lookup
  |WEAK_GUARD                    |Comparison of HTTP referer to a constant
  |WEAK_GUARD                    |Comparison of HTTP referer to a constant
  |WEAK_GUARD                    |Comparison of IP address to a constant
  |WEAK_GUARD                    |Comparison of IP address to a constant
  |WEAK_GUARD                    |Check against unreliable data
  |WEAK_GUARD                    |Comparison of OS login to a constant
  |WEAK_GUARD                    |Comparison of OS login to a constant
  |WEAK_GUARD                    |Comparison of principal name to a constant
  |WEAK_GUARD                    |Comparison of principal name to a constant
  |WEAK_PASSWORD_HASH            |Weak password hashing
  |WEAK_PASSWORD_HASH            |Hashing a password with a weak hash function
  |WEAK_PASSWORD_HASH            |Very weak password hashing
  |WEAK_PASSWORD_HASH            |Weak password hashing
  |WEAK_PASSWORD_HASH            |Hashing a password with a weak salt

For other languages, relevant security checkers corresponding to [OWASP Top Ten](https://owasp.org/www-project-top-ten/) _MUST_ be enabled.

## SEC-ASU-STATIC-FR3: Fix anomalies

The [offering](#DEF_Offering) team _MUST_ address all anomalies identified by static analysis security checkers.  The [offering](#DEF_Offering) team _MUST NOT_ disable detection or reporting for an entire class of security-relevant anomalies unless there is a documented rationale to explain that *no* anomaly in that class can represent a
security vulnerability in the [offering](#DEF_Offering).  Any individual anomaly marked as false positive _MUST_ also include a documented reason for doing so.

The [offering](#DEF_Offering) team _SHOULD_ prevent code with unaddressed static analysis anomalies from being checked into the integration codebase.

**Supplemental Guidance**: Follow a process that assesses each security-relevant anomaly as soon as it is identified by the SA tool.  For example, SA tool can be automatically invoked as part of the code merge from a private development branch to the integration branch.  A policy can be put in place where the newly developed code must be "SA Warning Free" prior to being allowed to merge.  SA tool can also be incorporated into other automated processes such as nightly or weekly builds to identify anomalies on a continuous basis.  For large legacy code bases, it may be more efficient to run SA only against newly developed code as they are merged, and periodically go back and run SA on the entire code baseline.

When reviewing anomalies, if the assessment finds a specific and convincing reason that an anomaly represents a security vulnerability or a PSB violation, then treat the anomaly as described under "anomalies as security defects."  If the assessment finds a convincing reason that an anomaly does not represent a security vulnerability or a PSB violation, then treat that anomaly as described under "false positives."

_Anomalies as security defects_

Your development process needs to ensure security defects are properly classified and prioritized according to their security impact. You can use your usual defect tracking and resolution planning systems to manage such defects. Each such defect needs to be resolved in such a way as to actually eliminate the vulnerability. You must not rely on a change that permits the risk to continue while placing it beyond the tool's ability to detect it.

_False positives_

If you find a convincing reason to believe that a detected anomaly doesn't represent a real security vulnerability, then you can treat it as a false positive. An anomaly may be a "false positive" in the sense that it's not an active security vulnerability, but still indicate dangerous code or bad code style. You should always consider modifying your code to eliminate an anomaly, rather than configuring your tools to ignore it.

If you choose not to remedy a false positive by changing the actual code, then you may configure the scanning tool(s) to ignore it entirely or use some separate anomaly tracking tool to remove it from consideration in future runs. In all other
cases, you must assess and ignore anomalies one at a time.

It should be easy for an auditor to find your justification for
ignoring any particular anomaly. For example--

1. If you put a pragma in the analyzed code to disable reporting of an
   anomaly (the recommended method), then you should include the
   justification, or a link to the justification, in a comment near the
   pragma (or as part of the pragma if the tool supports it).

1. If you use a configuration file to disable reporting of an anomaly,
   then you should include the justification or link in the
   the configuration file, as a comment, if necessary.

1. If you use an interactive anomaly tracking user interface to mark an
   anomaly as a false positive, then you should record the
   justification or link in any field that the user interface provides
   for the purpose, or in any available comment field if no
   special-purpose field is available.


# Informative References

- [CSTATIC Home page (for CSG uses of Coverity)](https://wiki.cisco.com/display/CSTATIC/CSTATIC+Home)
- [Engineering IT Coverity page (for non-CSG uses of Coverity)](https://engit.cisco.com/code/coverity)

# History

```yaml
-----
affected_psb: SEC-ASU-STATIC-2
impact: non-normative
description:  Updated to functional requirements.
-----
```


# Attributes

    phase: requirements
    legallysensitive: false
    priority: 10
    applicability:
    - force: mandatory
      target:
        restrict: |-
                      code in C or C++
    - force: recommended
      target:
        restrict: |-
                      code in any programming language
        class: not_HwComp
    category: Development Process
    riskArea: Risk Assessment
    waivable: true
    version: 2
    id: SEC-ASU-STATIC
    issueref: ISS_NoStatic
    tags:
    - EN/PD
    - EN/PI
    - CloudCritical
    - Critical PSB
    - PSB/OnPrem
    - Cloud
    - EN/PD DT
