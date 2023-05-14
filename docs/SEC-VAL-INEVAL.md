# Headline

Protect command processors from injection vulnerabilities by preventing the execution of arbitrary commands or code.

# Key Benefits

Injection vulnerabilities are amongst the most common and dangerous attacks.  They can lead to data theft, data loss, loss of data integrity, denial of service, as well as full system compromise.

SEC-VAL-INEVAL requires protection against these three types of injection vulnerabilities:

* Command injection is an attack in which arbitrary commands are executed on the host operating system via a vulnerable application. Command injection attacks are possible when an application passes user-supplied data (forms, cookies, HTTP headers etc.) to a dangerous system function (e.g. system(), popen()). The specific issue is the substitution of data into a position where it is parsed as code.

* Eval Injection is an attack in which user-supplied data is passed to an evaluation statement (e.g. eval() in JavaScript, evaluate in ColdFusion) resulting in direct dynamic code execution.

* Code Injection is an attack to introduce (or "inject") code into a vulnerable computer program. The attack is performed when the code in an argument, file or data set is interpreted and executed by the application.

By executing the code, the application gives an attacker a privilege or capability that the attacker would not otherwise have. Access to a higher level of functionality allows a rogue user to alter system behavior significantly.

Software will be more secure if it is written with the intent to control access to levels of functionality that are beyond what is necessary to do the job. In principle, limiting the use of powerful commands that provide rich functionality, the system is inherently more secure. The concept of limiting access to only what is required is referred to as the least-privilege.

Protecting against injection vulnerabilities provides system and data protection for the customers, employees, and business partners.

# Description

SEC-VAL-INEVAL requirement can be used with any kind of programming language with these three types of injection vulnerabilities. In addition, SEC-VAL-INEVAL requirement contains available implementation options, tools for validation and references to background material.

SEC-VAL-INEVAL introduces the term "Command Processor" with the intent of making the requirement independent of the execution environment.

For example, the command shell is the command processor interface. The command processor is the program that executes operating system commands. UNIX systems offer a choice between several different shells, the most popular being the Cshell, the Bourne shell, and the Korn shell. CMD.XE is the command processor for Windows.

The program can give a properly authenticated and authorized agent total control over an execution space by allowing that agent to provide a program to run in that execution space if doing so is an intentional feature.

In SEC-VAL-INEVAL, intentionally giving a peer control over the behavior of the running code does not meet the definition of code injection vulnerability and is not included in a functional requirement.

# Behavior

The functional units below apply when:

* SEC-VAL-INEVAL-FR1: Invoking dangerous functions resulting in system command execution.
* SEC-VAL-INEVAL-FR2: Invoking functions with user-supplied data resulting in direct dynamic code evaluation.
* SEC-VAL-INEVAL-FR3: User input is included in an argument, file or data set interpreted as code.

## SEC-VAL-INEVAL-FR1:  Command Injection

Applies when invoking dangerous functions resulting in system command execution (Command Injection Attack).

1. The program _MUST NOT_ invoke functions that execute dynamically-generated user-supplied system commands interpreted through command processor (for example, system() and popen() in C/C++).

1. The program _MAY_ invoke functions that execute static or hardcoded system commands interpreted through command processor (for example, system() and popen() in C/C++), as long as the runtime environment is secure.

## SEC-VAL-INEVAL-FR2:  Eval Injection

Applies when invoking functions with user-supplied data resulting in direct dynamic code evaluation (Eval Injection Attack)

1. The program _MUST NOT_ invoke functions that run their arguments, created from user-supplied data, as code in the invoking language. Many languages that have such function name them eval().
1. The program _MUST NOT_ invoke functions that run their arguments, created from user-supplied data, as code in an embedded scripting language (such as Lua, VBScript, etc.).
1. When data are entering across a trust boundary, the receiving application _MUST_ validate the inbound data. Application trust boundaries are identified through Threat Modeling.

## SEC-VAL-INEVAL-FR3:  Code Injection

Applies when user input is included in an argument, file or data set interpreted as code (Code Injection Attack).

1. The program _MUST_ apply input validation practices to all user-supplied inputs through libraries coupled to a language or framework before including in any part of an argument, file or other data set that is meant to be interpreted as program code.

# Informative References
* Recipe: [Defend against Command Injection](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Defend%20Against%20Command%20Injection.aspx)
* CWE-77 -- [Command Injection](https://cwe.mitre.org/data/definitions/77.html)
* CWE-78 - [OS Command Injection](https://cwe.mitre.org/data/definitions/78)
* SEI CERT C Coding Standard - [Do NOT Call system()](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152177)
* OWASP Command Injection - [Command Injection Examples](https://owasp.org/www-community/attacks/Command_Injection)
* OWASP Eval Injection - [Eval Injection](https://owasp.org/www-community/attacks/Direct_Dynamic_Code_Evaluation_Eval%20Injection)
* OWASP Code Injection - [Code Injection](https://owasp.org/www-community/attacks/Code_Injection)
* Potentially Dangerous Constructs - [Dangerous Constructs Table](https://cisco.box.com/s/85xq9a9i4k7ag17zpo0yf6jhu0cw3y4i)
* Microsoft Banned Functions - [Banned Functions](https://cisco.box.com/s/j9tou4pg9uik1rtg869qngywgt7u9pi1)

* Sample Defects: CSCve98527 - [Command Injection Vulnerability](https://cdetsng.cisco.com/webui/#view=CSCve98527)
* Sample Defects: CSCvo70892 - [Command Injection Vulnerability](https://cdetsng.cisco.com/webui/#view=CSCvo70892)
* Sample Defects: CSCva65858 - [Command Injection Vulnerability](https://cdetsng.cisco.com/webui/#view=CSCva65858)
* Sample Defects: CSCuw47239 - [Command Injection Vulnerability](https://cdetsng.cisco.com/webui/#view=CSCuw47239)

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-VAL-CLNIN
    relation: connects
    headline: >
        Input Validation

# Attributes

    id: SEC-VAL-INEVAL
    version: 2
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
