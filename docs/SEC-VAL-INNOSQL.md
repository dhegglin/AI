# Headline

Validate user-supplied input before the program builds a NoSQL database query.

# Key Benefits

The NoSQL DBMS offers efficient solutions for storing and analyzing big data. The NoSQL data model provides better
flexibility, a schema less model, and an efficient storage and access mechanism.

As opposed to traditional databases (RDBMS) NoSQL databases focuses more on performance and availability compared to security
and consistency. Historically NoSQL databases were created with security assigned a lower design priority.

NoSQL databases are susceptible to inappropriate use and abuse. They can be hacked, injected with malicious codes, modified
or even destroyed. Thus security is a critical consideration.

# Description

By requiring fewer relational constraints and consistency checks, NoSQL databases often offer performance and scaling
benefits. Yet these databases are still potentially vulnerable to injection attacks, even if they are not using the
traditional SQL syntax.

Because these NoSQL injection attacks may execute within a procedural language , rather than in the declarative SQL language,
the potential impacts are greater than traditional SQL injection.

NoSQL database calls are written in the application's programming language, a custom API call, or formatted according to a
common convention (such as XML, JSON, LINQ, etc). Malicious input targeting those specifications may not trigger the
application filtering checks. For example, filtering out common HTML special characters such as `< > & ;` will not prevent
attacks against a JSON API, where special characters include `/ { } :`.

The main mechanisms of NoSQL injections attacks are:

* Tautology
* Union Queries
* Syntax Errors
* JavaScript Injections

The attacker takes the advantage of incorrect filtering and poor validation for user input within part of NoSQL statements and
injects arbitrary data into a string that is eventually run by the NoSQL database engine. Although NoSQL queries are typically
constructed from objects in a programming language, the object can be deserialize to a string format that an attacker can
attempt to manipulate.

A NoSQL database also introduces a new type of vulnerability, JavaScript Injection. Use of JavaScript may provide an attack
surface to the hackers as they may perform an injection of arbitrary JavaScript code to hack the system and to execute illegal
data extraction or alteration. The principle of NoSQL injection is similar to SQL injection, but the form of injection is
different.

# Behavior

The functional units below apply when:

* SEC-VAL-INNOSQL-FR1: Building queries from user-supplied data
* SEC-VAL-INNOSQL-FR2: Using dangerous operators and functions
* SEC-VAL-INNOSQL-FR3: Code is injected in a query executed by the database

## SEC-VAL-INNOSQL-FR1: User Supplied Data

FR1 applies when building queries from user supplied data.

1. The program _SHOULD_ use prepared parameterized query as a first choice to query a NoSQL database.
1. The program _MUST NOT_ build queries from user-supplied data directly.
1. If user-supplied data is necessary to build a query, then input validation practices _MUST_ be applied prior to query
    execution.
1. Input validation _MUST_ be applied to tautologies, unions, and syntax errors in queries
    (i.e. MongoDB `$ne, $or, ' " \ ; { }`).
1. The program _MUST_ do all input validation using functions dedicated to the specific database and programming language
    (i.e. [mongo-sanitize](https://github.com/vkarpov15/mongo-sanitize), [mongoose](https://mongoosejs.com)).

## SEC-VAL-INNOSQL-FR2: Dangerous Operations and Functions

FR2 applies when using dangerous operators and functions.

1. The program _MUST_ avoid the use of query operators that an attacker can exploit by manipulating the query and passing
    a string evaluated inside the database engine (i.e. MongoDB: $where and mapreduce() allow running JavaScript expressions).
1. The program _MUST_ build queries using safer operators (i.e. MongoDB: $eq or $gt) or special mechanisms if user-supplied
    data must be passed to a dangerous operator (i.e. MongoDB: CodeWScope for passing data to $where).

## SEC-VAL-INNOSQL-FR3: Injected Code in a Database Query

FR3 applies when code is injected in a query executed by the database.

1. The program _SHOULD_ validate the use of functions and operators allowing script execution in the query engine
    (i.e. MongoDB: mapReduce() and the $where operator).
1. The program _SHOULD_ avoid using dangerous functions and commands (i.e. JavaScript eval())
1. The program _SHOULD_ use safer functions and command when possible (i.e. JavaScript JSON.parse, parseXXXX methods).
1. The program _MAY_ enable strict mode within a function (i.e. JavaScript "use strict").
1. The program _MAY_ monitor the functions arguments to identify the script code or queries executed by the database
    (i.e. MongoDB JSON).
1. The program _MAY_ use abstract syntax tree (AST) techniques to detect illegitimate script code or queries
    (i.e. MongoDB JavaScript or JSON).

# Generic Testing Guidance

* OWASP Testing Guide v4.0 - [Testing Guide Release 4.0](https://www.owasp.org/images/1/19/OTGv4.pdf)
* PentesterLab - [MongoDB Injections](https://pentesterlab.com/exercises/web_for_pentester_II/course)
* JavaScript Injection Tutorial - [Test And Prevent JS Injection Attacks On Website](https://www.softwaretestinghelp.com/javascript-injection-tutorial/)
* MongoDB Pentesting - [MongoDB Pentesting for absolute beginners](https://github.com/nixawk/pentest-wiki/blob/master/2.Vulnerability-Assessment/Database-Assessment/mongodb/MongoDB%20Pentesting%20for%20Absolute%20Beginners.pdf)

# Informative References

* A NoSQL Injection Primer (MongoDB) - [MongoDB Injection Examples](https://nullsweep.com/a-nosql-injection-primer-with-mongo/)
* NoSQL Injection - [NoSQL Injection](https://medium.com/rangeforce/nosql-injection-6514a8db29e3)
* NoSQL Injection in MongoDB - [NoSQL Injection](https://zanon.io/posts/nosql-injection-in-mongodb)
* Show to pull-off a NoSQL Injection Attack. - [NoSQL Injection Attack](https://medium.com/@shukla.iitm/nosql-injection-8732c2140576)
*Hacking NodeJS and MongoDB - [Hacking NodeJS and MongoDB](https://blog.websecurify.com/2014/08/hacking-nodejs-and-mongodb.html)
* OWASP Server-Side JS Injection - [NodeGoat Tutorial](https://ckarande.gitbooks.io/owasp-nodegoat-tutorial/content/tutorial/a1_-_sql_and_nosql_injection.html)
* MongoDB 4.2 Manual - [MongoDB Manual](https://docs.mongodb.com/manual/)
* Fuzzdb - [Attack patterns and primitives for black-box application](https://github.com/fuzzdb-project/fuzzdb)
* NoSQLMap Exploitation Tool - [NoSQLMap Tool](https://github.com/codingo/NoSQLMap)
* NoSQL Exploitation Framework - [Framework for Scanning and Exploitation](https://github.com/torque59/Nosql-Exploitation-Framework)
* NoSQL Databases - [List of NoSQL Databases](https://bigdata-madesimple.com/a-deep-dive-into-nosql-a-complete-list-of-nosql-databases/)

# Sample Defects

* CSCuv48155 - [Implement an input validation framework to prevent NoSQL injection](https://cdetsng.cisco.com/webui/#view=CSCuv48155)
* CVE-2018-1784 - [IBM API Connect is affected by a NoSQL Injection in MongoDB](https://nvd.nist.gov/vuln/detail/CVE-2018-1784)
* CVE-2018-3783 - [Privilege escalation in flintcms allows account takeover due to blind MongoDB injection](https://nvd.nist.gov/vuln/detail/CVE-2018-3783)
* CWE-943 - [Improper Neutralization of Special Elements in Data Query Logic](https://cwe.mitre.org/data/definitions/943.html)
* Sample code vulnerable to NoSQL injection - [Client NoSQL Injection](https://github.com/vdeturckheim/mongodbi)
* Login bypass attack MongoDB/NodeJS - [Vulnerability Demonstration MongoDB/NodeJS](https://github.com/websecurify/acme-no-login)

# Normative References

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-VAL-CLNIN
    relation: connects
    headline: >
      Input Validation

    ---
    source: PSB
    foreign_id: SEC-VAL-INSQL-2
    relation: connects
    headline: >
      Input Validation

# History

```yaml
-----
affected_psb: SEC-VAL-INNOSQL
---
impact: non-normative
headline: >
  SEC-VAL-INNOSQL New Requirement.
description: >
  This requirement was introduced in March 2020.
  NoSQL databases complement SQL databases.
  Systems using SQL databases should refer to SEC-VAL-INSQL.
  Systems using NoSQL databases should refer to SEC-VAL-INNOSQL.
```

# Attributes

    id: SEC-VAL-INNOSQL
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
            [offerings](#DEF_Offering) that include NoSQL type databases
          class: DbNoSql_OR_DbOther_OR_ServiceThing
    priority: 9
    phase: requirements
    tags:
    - PSB/OnPrem
    - Cloud
