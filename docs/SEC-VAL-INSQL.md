# Headline

Use primary defenses when the program builds an SQL statement.

# Key Benefits

Structured Query Language (SQL) is the nearly universal language of databases that allows the storage, manipulation, and retrieval of data. Databases that use SQL include MS SQL Server, MySQL, Oracle, Access, Filemaker Pro and NoSQL. These databases are equally subject to SQL injection attack.

SQL injection has become a common issue with database-driven web sites.  Injection (or insertion) of an SQL query using user-supplied input can be used to:

* Bypass a web application's authentication and authorization mechanisms.
* Add, modify and delete records in the database.
* Gain access to sensitive data including personally identifiable information (PII), trade secrets, intellectual property and other sensitive information.
* Retrieve the contents of an entire database.

Any time software creates dynamic database queries that include user-supplied input, it is important to validate the user-supplied data prior to invoking the SQL interpreter. Protecting against SQL injection ensures data integrity for the customers, employees, and business partners who store and retrieve information from databases.

# Description

SEC-VAL-INSQL provides technical requirements for preventing injection vulnerabilities that all SQL databases must be protected against.  These technical requirements can be used with practically any kind of programming language with SQL database.

SEC-VAL-INSQL also contains available implementation options for protecting data, tools for validation and references to background material. Any application that uses SQL database needs to ensure it is not susceptible to SQL injection.

SQL injection vulnerabilities are introduced when software creates dynamic database queries that include user-supplied input. If dynamic SQL strings have to be constructed directly in the application, then it is important to validate the user-supplied data prior to invoking the SQL interpreter.

SQL injection can be avoided by using the following primary defenses:

* Use of Prepared Statements (with Parameterized Queries)
* Use of Stored Procedures
* AllowList Input Validation
* Escaping All User Supplied Input

The use of prepared statements with variable binding (parameterized queries) is the first choice when writing SQL queries. In parameterized queries the SQL code is defined first, and then each parameter is passed to the query later. It provides a query interface that prevents SQL injection.

A second choice is stored procedure. In this case SQL code is prepared and stored in the database itself and then called from the application.  Prepared statements and stored procedures have the same effectiveness in preventing SQL injection.

Character escaping is provided as a last resort in case none of the above are feasible. Input validation is a better choice as character escaping is the weakest defenses and cannot guarantee prevention of SQL Injection in all situations.

# Behavior

The functional units below apply when:

* SEC-VAL-INSQL-FR1: Using prepared statements, stored procedures or dynamic constructed queries.
* SEC-VAL-INSQL-FR2: AllowListing input validation is used.
* SEC-VAL-INSQL-FR3: Escaping user supplied input.
* SEC-VAL-INSQL-FR4: Using quote in constants.

## SEC-VAL-INSQL-FR1: Prepared Statements

Applies when using prepared statements, stored procedures or dynamic constructed queries.

1. The program _SHOULD_ use prepared statements as the first choice to query an SQL database, otherwise the program _SHOULD_ use stored procedures.
1. If dynamic SQL strings are constructed directly in the application, then input validation practices _MUST_ be applied to the user-supplied data prior to invoking the SQL interpreter.
1. Queries _SHOULD_ only use legal locations for variable binding.
1. Various parts of SQL queries are not legal locations for the use of bind variables, such as the names of tables or columns, and the sort order by keyword indicator (ASC or DESC). In such situation, if the query cannot be redesigned to use one of the above methods, the program _MUST_ apply input validation.

## SEC-VAL-INSQL-FR2: White Listing

Applies when AllowListing input validation is used.

1. The program _MUST_ check the characters present in any user-supplied data to be used in any constant in any SQL statement against a whitelist appropriate for the column type.
1. The whitelist _MUST NOT_ include any characters not expected by the consuming code.
1. Each column type _MUST_ have a single whitelist, defined in only one place.

## SEC-VAL-INSQL-FR3: Escaping Special Characters

Applies when escaping user-supplied input.

1. The program _MUST NOT_ construct a query if presented with a string containing unexpected characters.
1. The program _MUST NOT_ simply remove the unacceptable characters and continue.
1. If possible, the program _SHOULD_ escape all user-supplied input using an escape routine specific to database language.
1. The program _MAY_ use an object-relational mapper (ORM) for escaping user-supplied input.

## SEC-VAL-INSQL-FR4: Using Constants

Applies when using constants in a statement.

1. The program _MUST NOT_ copy any user-supplied data into any part of an SQL statement other than a constant.
1. The program _MUST_ quote all user-supplied data used in any string constant in any SQL statement.
1. The program _MUST_ ensure that non-string constants do not contain inappropriate characters.
1. The program _SHOULD_ do this by regenerating them from parsed values rather than by copying user-supplied string representations of these non-string types.
1. The program _MUST_ do all quoting using functions dedicated to that purpose and application logic _MUST NOT_ construct SQL statements from user-supplied data using generic text processing functions.

# Informative References

* ISO/IEC 9075:2016 - [The SQL Standard](https://blog.ansi.org/2018/10/sql-standard-iso-iec-9075-2016-ansi-x3-135/#gref)
* NIST 800-53 SI-15 - [SI-15 INFORMATION OUTPUT FILTERING](https://nvd.nist.gov/800-53/Rev4/control/SI-15)
* OWASP Project - [OWASP Mutillidae 2 Project](https://www.owasp.org/index.php/OWASP_Mutillidae_2_Project)
* NIST National Vulnerability Database - [SQL Injection Vulnerabilities](https://nvd.nist.gov/view/vuln/search-results?query=sql+injection&search_type=all&cves=on)

* Sample Defects: CSCvo23576 - [SQL Injection Vulnerability](https://cdetsng.cisco.com/webui/#view=CSCvo23576)
* Sample Defects: CSCvk30822 - [SQL Injection Vulnerability](https://cdetsng.cisco.com/webui/#view=CSCvk30822)
* Sample Defects: CSCvd61754 - [SQL Injection Vulnerability](https://cdetsng.cisco.com/webui/#view=CSCvd61754)
* Sample Defects: CSCvf47935 - [SQL Injection Vulnerability](https://cdetsng.cisco.com/webui/#view=CSCvf47935)

# Normative References

* ISO/IEC 9075:2016 - [The SQL Standard](https://blog.ansi.org/2018/10/sql-standard-iso-iec-9075-2016-ansi-x3-135/#gref) and NIST 800-53 SI-15 - [SI-15 INFORMATION OUTPUT FILTERING](https://nvd.nist.gov/800-53/Rev4/control/SI-15) _MUST_ be treated as part of SEC-VAL-INSQL. If the offering complies with ISO/IEC 9075:2016 and NIST 800-53 SI-15, then the offering complies to SEC-VAL-INSQL.

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-VAL-CLNIN
    relation: connects
    headline: >
      Input Validation
# Attributes

    id: SEC-VAL-INSQL
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
            [offerings](#DEF_Offering) that include an SQL database
          class: DbSql_OR_DbOther_OR_ServiceThing
    priority: 10
    phase: requirements
    tags:
    - Critical PSB
    - CloudCritical
    - EN/PI
    - PSB/OnPrem
    - Cloud
