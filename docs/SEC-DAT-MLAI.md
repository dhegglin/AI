# Headline

Protect Machine Learning and Artificial Intelligence systems

# Description

Rigorous machine learning validation plays a critical role in AI/ML risk management; however, sound development, implementation, and use of AI/ML Models are also vital elements.

AI/ML Model risk management encompasses governance and control mechanisms such as board and senior management oversight, policies and procedures, controls and compliance, and an appropriate incentive and organizational structure.

# Behavior
**Supplemental Guidance**
Machine Learning consists of three main components:

1. Information input component: This delivers assumptions and data. The data is typically quantitative but may also be qualitative.
2. Processing component: This transforms input data into estimates. Selecting the wrong algorithm or data will result in bad estimates and consequently bad business decisions.
3. Reporting component: This translates the estimates into actionable decisions.

Machine Learning risk increases with greater AI/ML Model complexity, longer AI/ML Model deployment, higher uncertainty about inputs and assumptions, broader use, and larger potential impact.  Failure to understand the difference between a narrow and well-defined operating environment in the research context, and the broad and poorly defined operating environment in the deployment context is a main driver of AI incidents.

## SEC-DAT-MLAI-FR1: Machine Learning Model Definition

The [Offering](#DEF_Offering) _MUST_ create a Machine Learning AI/ML Model that aligns with the intended use of the data collected by the offer, as documented in SEC-DAT-KNOWWHAT.  This can most easily be accomplished by completing the [CSDL Responsible AI/ML Assessment](https://cisco.sharepoint.com/sites/AIML/SitePages/Responsible-AI-ML-Assessments.aspx).

The offering AI/ML Model definition _MUST_ describe the probable data subjects as well as the use cases in order to capture the diversity of potential characteristics.  The AI/ML Model _MUST_ call out what is out of scope or unintended as well as what the engine does when it encounters such data.

The AI/ML Model definition *MUST* indicate whether the model is directly involved in [consequential decisions](#DEF_ConsequentialDecisions).  If a model is directly involved in a consequential decision, development teams must complete the fairness section of the [CSDL Responsible AI/ML Assessment](https://cisco.sharepoint.com/sites/AIML/SitePages/Responsible-AI-ML-Assessments.aspx).  See recipe on assessment workflow and tools to assess and document the risk of unintended bias and unintended usage in the performance and outcomes of the AI/ML capability or service.

The AI/ML Model definition _MUST_ be done before going to production and updated as the environment or the intent changes.  The intention of this provision is to ensure lots of freedom in the experimental phase while providing guidelines as the product goes into production.

## SEC-DAT-MLAI-FR2: Input Data Definition

The offer team _MUST_ perform a rigorous assessment of training data quality and relevance, as well as create appropriate documentation. If data and information are not representative of the typical characteristics, or if assumptions are made to adjust the data and information, these changes must be documented and justified.

This documentation _MUST_ characterize the range of expected inputs and the resulting relevant outputs.  It _SHOULD_ include a description of the inputs and outputs as well as negative examples to define what is outside of the scope.  All input training data _SHOULD_ be inspected and analyzed for accuracy, relevance, proper attribution and unintended bias.

Usage of all data (including training data) _MUST_ adhere to copyright and intellectual property rights.  Not all data is in the public domain and experimental, training, and production environments _MUST_ ensure that data is obtained and used legally.

The expected training data _MUST_ be documented as noted in SEC-DAT-KNOWWHAT and adhere to SEC-DAT-MINIMIZE.

Training data _MUST_ be protected to the degree that production data is protected to prevent alteration ("poisoning") of that data by malicious actors.

## SEC-DAT-MLAI-FR3: Model Protection and Monitoring
The offer team _SHOULD_ monitor the AI/ML process to identify drift in inputs, outputs, predictions, and any anomalies while the system is processing data.  Monitoring is essential to evaluate whether changes in input data due to exposures, activities, clients, or market conditions necessitate adjustment.  See the associated [Recipe](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Machine-Learning-Security-Guidance.aspx#model-monitoring-and-analysis) for guidance.

In some instances (such as data including PII), automated monitoring is not possible and the product _SHOULD_ incorporate a feedback process from the end users to alert the development team of incorrect results.  This feedback _SHOULD_ integrate with a bug tracking system and be monitored for trending data.

The AI/ML Model _MUST_ remain operational when the system received data outside of the representative input data.  Unexpected data may provide additional understanding of the AI/ML Model or identify adjustments that can enhance the effectiveness of the AI/ML Model.

Input data  may change over time and there _MUST_ be protection from poisoning and data drift using intermittent monitoring and on-going AI/ML Model verification.  The monitoring capabilities _SHOULD_ include statistical control limits to alert monitoring entities of potential drift.  Exceptions such as negative, inaccurate, ambiguous or hard to explain outcomes should be logged to allow for identification of potential incidents.  Such logged exceptions _SHOULD_NOT_ include any PII or privacy impacting data.

The AI/ML Model _MUST_ be validated before going to production and updated as the environment or the intent changes.

**Supplemental Guidance**:  For features such as background blur/replacement, head detection and noise removal, monitoring might conflict with privacy for users.  It is important that monitoring not log any PII or privacy impacting data.

## SEC-DAT-MLAI-FR4: Third-Party Data Processing or Model
If third party AI/ML Model and/or data are used to develop the AI/ML capability or service, legal _MUST_ be involved in contract negotiation.

If a third-party provides the AI/ML Model or training data, it _MUST_ adhere to all functional requirements in this security control, including details of how that third party completes internal checks on their  system to identify and address statistical inaccuracies, bias and  discrimination in AI systems.  The third party _MUST_ provide documentation to ensure adherence to the AI/ML Model objective, and that the AI/ML Model protects against intended and unintended bias and human rights violations.

If third-party data is used for AI/ML Model training, appropriate rights and permissions MUST be obtained from that third-party prior to using that data. Third-party training datasets, acquired for AI/ML Model training purposes MUST be evaluated for bias and discrimination prior to using that data.

**Supplemental Guidance**:  A "what not to do" example of this would be Zoom harvesting images from Facebook for the benefit of Zoom.

## SEC-DAT-MLAI-FR5: Explicit Consent
When Cisco is the controller and PII is used in the decision making, the AI/ML capability or service _MUST_ include a built-in system to notify the potentially impacted user that AI/ML is being used.  When PII is used in the decision making, the default behavior _MUST_ allow the affected user to opt-in.

**Supplemental Guidance**:  A good example for this approach is the WebEx Desktop offerings.  Even though face detection capability is required for centering an image on a person, WebEx Desktop disables the face detection feature by default and allows the user to enabled it.  Opt-in features of Webex include speech to text translators and virtual backgrounds.  These features are only enabled after explicit customer consent.

## SEC-DAT-MLAI-FR6: Fairness

If the AI/ML Model is directly involved in a [consequential decisions](#DEF_ConsequentialDecisions), development teams MUST complete the fairness section of the [CSDL Responsible AI/ML Assessment](https://cisco.sharepoint.com/sites/AIML/SitePages/Responsible-AI-ML-Assessments.aspx). One Trust will route the assessment to a Responsible AI/ML Assessor who will conduct a risk assessment to determine the risk of unintended bias and unintended usage of the model, as well as whether the intended use cases purposefully violate internationally recognized laws or human rights.

The AI/ML Model _SHOULD_ also enumerate likely risks, biases, ethical issues and misuses as this increases the awareness and likelihood of these issues being addressed.

Developers _MUST_ log [consequential decisions](#DEF_ConsequentialDecisions) and outputs being made by an AI/ML algorithm or AI/ML Model.  The logs _MUST_ provide enough detail to provide transparency in AI/ML Model decision making.  Logs can be used to validate why a certain output was made based on the available inputs.  The logs are not meant to be a debugging mechanism that results in large amount of data.  Continuous video or voice streams make many decisions every second and should only record [consequential decisions](#DEF_ConsequentialDecisions) and exceptions.

This assessment must be done any time there is a major change to the intended use cases or potentially impacted groups or individuals.

## SEC-DAT-MLAI-FR7: Customer Documentation
The offers _MUST_ develop customer-facing documentation that describes the use of AI/ML in the offer.  The offer teams _MUST_ document without specifics, the  use of common open source or proprietary ML package (e.g., "the offer used a standard, open source linear regression AI/ML Model from Python's NumPy package").  Since this is customer-facing documentation, offer teams are not required to document proprietary data or code, AI/ML Model code, algorithmic code, or any other AI/ML Model-related source code.

Customer-level documentation _MUST_ include notice to potentially impacted users that AI/ML is being used as well as capabilities to opt-in or opt-out of the system.  The documentation _SHOULD_ include information indicating if PII data is (not) used to identify individuals.

This customer-facing AI/ML Model Documentation _MUST_ include the following:
- The efficacy/accuracy of the algorithm, the assumptions made by the algorithm, and the inherent risks involved in using the AI/ML Model.  If accuracy of the algorithm cannot be calculated, then share QA test results with the different conditions and scenarios that the algorithm was subjected to as part of QA.

- Disclosure of the risk and issues involved in using a statistical AI/ML Model.  Algorithms are based on probabilistic and statistical AI/ML Models which inherently introduces risk.

- The desired outcomes of the algorithm along with the description of the reasoning systems and statistical AI/ML Model being used in the code.

- Basic information related to the AI/ML’s purpose, inputs, capability and limitations, appropriate level of human oversight, as well as guidance to customers on making such information  available and accessible to potentially impacted groups or individuals. It should  include the attributes which may be considered by the automated decision making process so that customers can bring logical complaints or appeals related to inevitable wrong decisions.

# Informative References

* [Machine Learning Security Recipe](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Machine-Learning-Security-Guidance.aspx)

* [Industry Adversarial ML Threat Matrix](https://github.com/mitre/advmlthreatmatrix)

* [Federal Reserve Model Risk Management](https://www.federalreserve.gov/supervisionreg/srletters/sr1107a1.pdf)

* [NIST Artificial Intelligence Start Page](https://www.nist.gov/topics/artificial-intelligence)

* [Microsoft Failure Modes in Machine Learning](https://docs.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning)

* [OReilly Responsible Machine Learning](http://info.h2o.ai/rs/644-PKX-778/images/OReilly_Responsible_ML_eBook.pdf)

* [Making Black Box Models Explainable](https://christophm.github.io/interpretable-ml-book/)

* [Interactive Machine Learning Risk Framework](https://berryvilleiml.com/interactive/)

* [Artificial Intelligence Incident Database](https://incidentdatabase.ai/)


# Requirement References

    ---
    source: PSB
    foreign_id: SEC-DAT-KNOWWHAT
    relation: connects
    headline: >
      [SEC-DAT-KNOWWHAT](#SEC-DAT-KNOWWHAT): Know what data you are processing
    ---
    source: PSB
    foreign_id: SEC-DAT-MINIMIZE
    relation: connects
    headline: >
      [SEC-DAT-MINIMIZE](#SEC-DAT-MINIMIZE): Minimize data collection
    ---
    source: PSB
    foreign_id: SEC-DAT-PRIV
    relation: connects
    headline: >
      [SEC-DAT-PRIV](#SEC-DAT-PRIV): Comply with Cisco's privacy policy
    ---
    source: PSB
    foreign_id: SEC-PRV-DSRIGHTS
    relation: connects
    headline: >
      [SEC-PRV-DSRIGHTS](#SEC-PRV-DSRIGHTS): Rights of Personally Identifiable Information's Data Subject

# Attributes

    id: SEC-DAT-MLAI
    version: 1
    issueref: ISS_NoPrivacyPol
    category: Privacy and Data Security
    riskArea: Data Governance & Protection
    legallysensitive: true
    waivable: true
    applicability:
      - force: mandatory
        target:
            class: MLAI
            restrict: >
              Services using machine learning or artificial intelligence
    priority: 8
    phase: requirements
    tags:
    - CloudCritical
    - Cloud
