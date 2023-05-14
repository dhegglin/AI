# Headline

Provide for business continuity

# Description

Prepare a business continuity plan to prevent loss of service in the
event of a disaster, massive security breach, or other loss of your
usual infrastructure.

# Behavior

Create a business impact assessment and a business continuity plan
defining policies, processes, and procedures to keep your offering and
the associated functions operating in the event of a catastrophe.

## SEC-OPS-BUSCONT-FR1: Continuity Management Standards

Your business continuity plan _MUST_ meet the requirements of the
[Cloud-Continuity Management Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1453238&ver=approved)
and _MUST_ be accepted by your Global Resliency Team representative.

## SEC-OPS-BUSCONT-FR2: Regular Testing

Your business continuity plan _MUST_ include testing of the defined
processes and procedures, and of the related technical measures, no less
than every 12 months. You _MUST_ conduct these tests as specified in
the plan. You _MUST_ conduct an annual "table top exercise" as
described in the Continuity Management Standard.

Your business impact assessment _MUST_ include security
considerations, including risks to data confidentiality and integrity.

## SEC-OPS-BUSCONT-FR3: Maintain Security Controls

Your business continuity plan _MUST_ provide for uninterrupted
application of all security controls required by the PSB or other
policies. "Emergency" controls _MAY_ differ from "standard" controls,
but must maintain all required security guarantees.

## SEC-OPS-BUSCONT-FR4: Assigned a Manager

You _MUST_ identify the specific manager(s) responsible for defining,
testing, and assuring readiness to execute the security-related parts of
your business continuity plan.

# Informative References

[Global Business Resiliency (GBR) Program Policy](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-872351&ver=approved)
*NB: The Business Continuity Management Policy has authority independent
of CSDL, and may demand substantial work that is not part of this PSB
requirement.*

[Cisco Enterprise Business Continuity Program Overview](https://apps.na.collabserv.com/communities/service/html/communitystart?communityUuid=4770e783-9268-46ca-b023-6327fc21438c)

[Business Continuity Dashboard](https://apps.na.collabserv.com/files/app/file/c93397a9-8ba6-401e-af79-508f705f5ee6)
List of Business continuity representatives per BU

[Business continuity information for customers](http://www.cisco.com/web/about/doing_business/business_continuity/index.html)

# Normative References

[Cloud-Continuity Management Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1453238&ver=approved)

# Requirement References

    ---
    foreign_id: A.17.1.1
    relation: connects
    headline: |-

              ISO 27002:2013: A.17.1.1 Planning information security continuity

    targets:
    - '17'
    source: ISO 27002:2013
    ---
    foreign_id: A.17.1.3
    relation: connects
    headline: |-

              ISO 27002:2013: A.17.1.3 Implementing information security continuity

    targets:
    - '17'
    source: ISO 27002:2013
    ---
    foreign_id: A.17.1.3
    relation: connects
    headline: |-

              ISO 27002:2013: A.17.1.3 Verify, review, and evaluate information security continuity

    targets:
    - '17'
    source: ISO 27002:2013
    ---
    foreign_id: A.17.2.1
    relation: connects
    headline: |-

              ISO 27002:2013: A.17.2.1 Availability of information processing facilities

    targets:
    - '17'
    source: ISO 27002:2013

# History

pm4_filehist

# Attributes

    phase: requirements
    legallysensitive: true
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: Cloud Offers
        class: not_MobileApp
    category: Operational Process
    riskArea: Risk Assessment
    waivable: true
    version: 3
    id: SEC-OPS-BUSCONT
    issueref: ISS_NoSecProgram
    tags: 
    - Cloud
