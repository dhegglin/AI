# Headline

Validate all input before processing it.

# Key Benefits

Input validation is the first line of defense for secure code.
Input validation stops a variety of injection attacks.

When software does not validate input properly, the system is vulnerable
because an attacker can craft inputs not expected by the rest
of the program. This can lead to parts of the system receiving
unexpected input, which can then result in altered control flow,
arbitrary control of a resource, or arbitrary code.

Input validation helps to ensure accurate and correct inputs to the code;
thereby preventing attacks that can severely affect an organization's
infrastructure, cause financial, or reputational damage.

Input validation prevents the following kinds of attacks:

- An attacker could provide unexpected values that cause a program
  crash or excessive consumption of resources such as memory and CPU.
- An attacker could read confidential data if they are able to control
  resource references.
- An attacker could use malicious input to modify data or possibly
  alter control flow in unexpected ways including arbitrary command
  execution.
- An attacker could use malicious input to gain access to a controlled
  space to execute malicious code.

# Description

Validating input prior to processing prevents a wide variety of attacks and
protects against a variety of bad outcomes, both intentionally and
unintentionally caused.

# Behavior

## SEC-VAL-CLNIN-FR1: Reading or copying input into a buffer.

Applies when reading or copying input into a buffer.

1. The program _MUST_ verify that the input length falls within the buffer size.
1. The program _MUST_ check that enough buffer space remains before copying multiple
   inputs (non-null terminated strings included) into a fixed-length buffer.
1. The program _MUST_ reject the input if there is not a delimiter found in the string
   (null-terminated strings included) before the program runs out of buffer space.
   NB: inputs that have un-paired delimiter characters or delimiters that are positionally
   unbalanced warrant heightened scrutiny (default rejection).
1. If an input represents a numeric value, the program _MUST_ verify that the value
   lies within some expected range. If the value is outside the expected range,
   it _MUST_ be rejected.

## SEC-VAL-CLNIN-FR2: Verifying format and content of input.

Applies when verifying the format and content of input.

1. The program _MUST_ verify that input contains only acceptable characters
   and it is of the form identified as expected in valid input.
1. The program _MUST_ reject the input when the input contains invalid characters,
   or it is of the form not identified as expected.
1. The input _SHOULD_ be matched against a character AllowList, not a BlockList.
1. The program _MUST NOT_ strip unexpected characters from input and process
   the result.
1. The program _MUST NOT_ attempt to transform invalid input into valid input.
1. Invalid input _MUST_ be rejected in its entirety and the input source
   _MUST_ re-submit correctly constructed input in order to be accepted.

NB: Rejecting input is safer than trying to sanitize. Sanitization tries to
somehow 'fix' illegal input. Input validation is stricter than
sanitizing inputs. Rather than \"cleaning\" the incoming data, input
validation adheres to specifically-defined formats rejecting the incoming
data entirely when it contains invalid characters.

## SEC-VAL-CLNIN-FR3: Input is in a structured language.

Applies when input data is in a structured language.

1. The program _SHOULD_ use a parser or regular expression provided by
   the programming language library or find a reputable 3rd-party
   implementation to validate the input, as opposed to writing `ad hoc`
   in a general-purpose programming language.
1. The input validation _MUST_  properly recognize the valid and invalid
   examples of the underlying language.
1. The program _MUST NOT_ act on syntactically invalid input except to
   reject the input.
1. The input validation _SHOULD_ validate all available parts of the input
   before acting on any of its contents and only accept the input if all
   of the parts are verified as valid. If any part fails validation,
   the entire input _MUST_ be rejected.
1. Invalid input _MUST_  be rejected in its entirety and the input source
   _MUST_ re-submit correctly constructed input in order to be accepted.

NB: Input validation should happen as early as possible in the data flow.
Preferably as soon as the data is received from any untrusted sources.

## SEC-VAL-CLNIN-FR4: Input used to create objects of a specific type or class.

Applies when input will be used to create objects of a specific type or class.

1. The program _MUST NOT_ permit structured language
   input to create objects with types, classes, structures, members,
   methods, handlers, or other constructs that are not expected by the
   consuming code.
1. The program _MUST_ directly convert the input type into the expected data
   type, such as using a conversion function that translates a string into a number.
1. After converting to the expected data type, the program _MUST_
   ensure that the input\'s values fall within the expected range of
   allowable values and that multi-field consistencies are maintained.
1. The program _MUST_ expect a single, specific possible type or class for the
   result, and reject any attempt to specify any other.
1. The program _MUST NOT_ let the input specify an unexpected value for any
   object method, function pointer, dispatch table entry, or equivalent element.
1. The program _MUST_ ensure that is not violating any of the expectations of
   the language with which it is interfacing.

NB: It is important to validate all inputs when invoking code
that crosses language boundaries such as from an interpreted language to
native code. This could create an unexpected interaction between the language
boundaries.

## SEC-VAL-CLNIN-FR5: Input is an unstructured free-form text.

Applies when the input is an unstructured free-form text.

1. If the input is encoded as unstructured free-form text, the program
   _MUST_ verify that it contains only characters identified as expected in
   valid input.
1. The program _SHOULD_ reject characters technically allowed by the input
   protocol or format if those characters are not expected in the specific
   application.
1. The program _SHOULD_ validate unstructured free-format text by matching
   the input against a character AllowList, not a BlockList.
1. The program _MUST_ completely reject input that fails any of the tests
   above and not proceed with an invalid input.
1. Inputs _SHOULD_  be decoded and canonicalized to the application's current
   internal representation, including length, before being validated.

NB: The expected program behavior includes not proceeding with a truncated
version of too-long input, not stripping unexpected characters from
input and processing the resulting input, and not trying to repair
invalid character encodings.

# Informative References
- Recipe: [Defend against Command Injection](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Defend%20Against%20Command%20Injection.aspx)
- FedRAMP Security Controls - [FedRAMP Security Controls Baseline](https://www.fedramp.gov/assets/resources/documents/FedRAMP_Security_Controls_Baseline.xlsx)
- OWASP Project - [OWASP Mutillidae 2 Project](https://www.owasp.org/index.php/OWASP_Mutillidae_2_Project)
- RegExp Security - [Cheat Sheet Series](https://github.com/attackercan/regexp-security-cheatsheet/blob/master/README.md)
- JSON Schema Validation - [A Vocabulary for Structural Validation of JSON](https://json-schema.org/latest/json-schema-validation.html#rfc.section.2)
- CSCtu74257 - [CLI Buffer Overflow Vulnerability](https://cdetsng.cisco.com/webui/#view=CSCtu74257)
- CSCvf32411 - [Path Traversal and Remote Code Execution Vulnerability](https://cdetsng.cisco.com/webui/#view=CSCvf32411)
- CSCvo28194 - [Command Shell Injection Vulnerability](https://cdetsng.cisco.com/webui/#view=CSCvo28194)
- CSCvi46909 - [Command Injection Vulnerabilities](https://cdetsng.cisco.com/webui/#view=CSCvi46909)
- CSCvi48984 - [Software Arbitrary File Upload Vulnerability](https://cdetsng.cisco.com/webui/#view=CSCvi48984)
- CSCvj25068 - [Protocol Denial of Service Vulnerability](https://cdetsng.cisco.com/webui/#view=CSCvj25068)
- NIST National Vulnerability Database - [Input Validation Vulnerability](https://nvd.nist.gov/)

# Normative References

- NIST 800-53 SI-10 - [SI-10 INFORMATION INPUT VALIDATION](https://nvd.nist.gov/800-53/Rev4/control/SI-10#Rev4Statements)
  _MUST_ be treated as part of SEC-VAL-CLNIN. If the offering complies with NIST 800-53 SI-10, then the offering
  complies to SEC-VAL-CLNIN.

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-VAL-INEVAL
    relation: connects
    headline: >
        covers additional requirements when invoking potentially dangerous functions that execute system commands.
    ---
    source: PSB
    foreign_id: SEC-VAL-INSQL
    relation: connects
    headline: >
        covers database injection.
    ---
    source: PSB
    foreign_id: SEC-VAL-INURL
    relation: connects
    headline: >
        covers additional requirements for URLs and Web services.

# Attributes

    id: SEC-VAL-CLNIN
    version: 1
    issueref: ISS_Inject
    category: Threat Surface Reduction
    riskArea: Application & Interface Security
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
          restrict: >
            [offerings](#DEF_Offering)
    priority: 10
    phase: requirements
    tags:
    - Critical PSB
    - CloudCritical
    - EN/PI
    - PSB/OnPrem
    - Cloud
    - FAST
