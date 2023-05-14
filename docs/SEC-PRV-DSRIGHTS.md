# Headline

Rights of Personally Identifiable Information's Data Subject

# Description

Provide the mechanism and/or process for customers to support [data subjects](#DEF_DataSubject) and/or their legal proxy the ability to manage the Personally Identifiable Data [PII](#DEF_PII) in a manner that respects the data subject's individual rights of:

* Notice
* Access
* Erasure
* Restriction of processing
* Objection to processing
* Data portability

# Key Benefits

Everyone wants to know and manage their personally identifiable data. Data subject rights are the basis of all privacy regulations, and adhering to them throughout an offering's lifecycle ensures that both your offering team and Cisco is in compliance with these regulations, which can have legal ramifications if not followed.

# Behavior

## SEC-PRV-DSRIGHTS-FR1: Provide Up-to-Date Notice

The [offering](#DEF_Offering) team (engineering, legal) _MUST_ provide the customer a mechanism or process to provide the data subject or their legal proxy of the customer's notice describing the [processing](#DEF_DataProcessing) of PII before the PII is created or initially collected.


**Supplemental Guidance**:

* For external-facing websites and web applications, there must be a link to the  customer's privacy notice in a consistent location (for example, the footer) on web pages and screens of web-based applications.  The link must read "Privacy" or "Privacy Statement" and have a consistent font and size as other, similar links. If the web page or web-based application uses cookies, there must also be a link to the customer's Cookie Policy in a consistent location (for example, the footer) on web pages and screens of web-based applications. The link must read "Cookies" and have a consistent font and size as other, similar links. For mobile applications, the link to the appropriate notice (Cookie or Privacy) can be in the top or second level of the main menu for the app. If second level, it must be in an intuitively obvious section, such as "Legal Notices."
* If a user, or proxy on behalf of the user, inputs PII for the first time, and if consent is the legal basis for the processing of the PII, or if passive creation or collection is potentially invasive (for example, cookies tracking specific location or call and web conference recording), the data subject individual _MUST_ acknowledge the relevant notice before the PII is collected.
* For machine-to-machine applications or systems that do not have a user interface, the notice _MUST_ be provided as part of the legal agreement (for example, End-User License Agreement, Master Service Agreement, etc.), which governs the relationship between Cisco and the party that is deploying the application or system.
* If subsequent collection of the same information is required (for example, to log in to a web application), the privacy notice _MUST_ be in proximity to the fields from which PII is collected-at minimum, in the footer of the web page.

## SEC-PRV-DSRIGHTS-FR2: Access: Provide Access Controls to Individuals

The offering team _MUST_ provide the customer the process or mechanism for identified and authenticated data subjects and/or their legal proxy to access their stored personal information for review and, upon request, provide physical or electronic copies of that information to data subjects to meet the offerings objectives related to privacy.

**Supplemental Guidance**: Use SEC-AUT-AUTH-2 and SEC-PRV-USERAUTH as basis for identification and authenication before giving the requestor access.

## SEC-PRV-DSRIGHTS-FR3: Rectification: Allow Data Subjects To Update Their PII

* The offering team whose offering processes PII  _MUST_ provide the customer the mechanism and/or procedure to support the identified and authenticated data subjects and/or their legal proxy to correct objectively false, misleading, or inaccurate PII and to review, add, or change their stored personally identifiable information.

## SEC-PRV-DSRIGHTS-FR4: Erasure: Enable Data Subjects to Delete PII

* The offering team whose offering processes PII  _MUST_ provide the customer the mechanism and/or procedure for the identified and authenticated data subjects and/or their legal proxy to delete PII for which there is no longer a current, valid business need to retain.
* The offering team _MAY_ meet these requirements by providing a mechanism to delete, one-way hash, anonymize, scramble, or otherwise render the PII unreadable by human or machine provided the PII cannot be reconstituted in a human or machine-readable form.
* The offer _MUST_ retain any information needed to authenticate the subject as a user for at least as long as it retains any of the subject's PII.
* If a data subject user has knowingly consented to provide personally identifiable information as part of an agreement affecting other parties, then if other parties would be disadvantaged by removal of that information, the offering team _MAY_ provide a mechanism for the customer to retain the information for as long as originally agreed.
* When PII is removed or changed, whether by deliberate human action or by automatic operation of the system itself, the offering team _MUST_  erase all copies of the old information in the offering's control.

**Supplemental Guidance**: Use SEC-AUT-AUTH-2 and SEC-PRV-USERAUTH as basis for identification and authenication before giving the requestor access.

## SEC-PRV-DSRIGHTS-FR5: Method to Restrict Processing

The offering team whose offering processes PII _MUST_  provide the customer the process or mechanism for identified and authenticated data subjects and/or their legal proxy to request restricting the use of thei PII. The offering team must provide the capability and a procedure to suspend processing an individual's PII if a valid objection to processing is received from the customer. In addition, the offering _MUST_ suspend or deactivate processing until the objection is resolved. The offering _MAY_ meet this requirement by deactivating the user account or equivalent.

## SEC-PRV-DSRIGHTS-FR6: Provide Data Portability Method

The offering team whose offering processes PII  _MUST_ provide the customer a mechanism or process for the identified and authenticated data subjects and/or their legal proxy to provide the requestor with the PII that was actively provided the system or business process.

* This includes user-generated content and account information.
* This does not include passively collected PII (for example, information collected by cookies, logs, and other tracking technologies or records), nor does it include conclusions drawn or derived or Cisco intellectual property developed based on the originally collected PII.

## SEC-PRV-DSRIGHTS-FR7: Capture and Record Explicit Consent from Data Subjects

If the offering team provided a consent mechanism as the legal basis for processing, the offering team _MUST_ provide the customer a process or mechanism for the identified and authenticated data subjects and/or their legal proxy to have the ability to give explicit consent  at or before the time personally identifiable information (PII) is collected or soon thereafter. The offering team _MUST_ confirm authorization, record consent, and implement the individual's purpose preferences as expressed in the data subject’s consent.

If the offering team uses consent as the legal basis for processing, the offering team _MUST_ provide the identified and authenticated data subjects and/or their legal proxy the ability to remove explicit consent. The offering team must suspend all processing of the data subjects provided PII.

## SEC-PRV-DSRIGHTS-FR8: Record All Actions Taken on Behalf of the Data Subject

The offering team whose offering proocesses PII _MUST_ capture an auditable record of all actions outlined above.

# Attributes

    id: SEC-PRV-DSRIGHTS
    version: 1
    issueref: ISS_Privacy
    category: Privacy and Data Security
    riskArea: Data Governance & Protection
    legallysensitive: false
    waivable: true
    applicability:
      - force: mandatory
        target:
            class:
            restrict: >
                offerings
    priority: 8
    phase: requirements
    tags:
    - EN/PI
    - CloudCritical
    - PSB/OnPrem
    - Cloud
    - EN/PI DT
