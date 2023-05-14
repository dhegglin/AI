# Headline

Mobile applications require specific controls to securely handle, store, and protect sensitive information.

# Description

Mobile applications handle, process, and store highly sensitive personal information. End users can access and interact with this sensitive data in ways that increase the likelihood of an attack. The impacts of an attack can be severe. This is why attack vectors must be kept in mind from the start of development in order to deliver a product that is as secure as possible. Typical threats to mobile applications include:

* Improper platform usage
* Insecure data storage
* Insecure communication
* Insecure authentication
* Insecure authorization
* Insufficient cryptography
* Client code quality
* Code tampering
* Reverse engineering
* Extraneous functionality
* Access privileges exceeding applications intended use
* Unncessary data collection and processing
* Hidden fuctionality
* Incomplete data deletion routines
* Insufficient User Controls
* Lack of transparency

Additional controls and processes are needed to ensure that these threats are properly addressed and mitigated.

# Conditions

Mandatory for mobile applications.  Enterprise Offerings will/may have different requirements from external Cisco customer-based offerings.

# Behavior

## SEC-DEV-MOBILITY-FR1 Authentication and Authorization (Condition: Restrict:Enterprise)
* Enterprise mobile offers _MUST_ integrate with PingFed for authentication. Multifactor authentication is required for all services and is implemented via DUO authentication.
* Enterprise mobile offers _MUST_ implement an authorization model using Cisco Active Directory Groups. AD Groups are the basis for all role-based group authorizations and may be managed by Cisco Groups or the Access Request Tool (ART).

**Supplemental Guidance:**  Mobile applications and services deployed for offerings need to comply with [SEC-AUT-AUTH](#SEC-AUT-AUTH):

## SEC-DEV-MOBILITY-FR2 Authentication and Authorization (Condition: Restrict:External Offerings)
For authentication and authorization:
* All mobile application offerings _MUST_ apply an appropriate authorization policy.
* Access services _MUST_ use an Infosec approved access service, such as approved SSO service.
* Multifactor Authentication _MUST_ be used for all Administrator access into cloud and/or OnPrem environments.

**Supplemental Guidance:**  Mobile applications and services deployed for offerings need to comply with [SEC-AUT-AUTH](#SEC-AUT-AUTH):

## SEC-DEV-MOBILITY-FR3 Certificate Pinning 

Mobile applications _MUST_ implement certificate pinning to thwart man-in-the-middle attacks.

## SEC-DEV-MOBILITY-FR4 Activated Security Features 

* Debug mode _MUST_ be disabled for production deployment.
* Enterprise mobile applications _MUST_ obfuscate the code to thwart attacks against reverse engineering.
* Enterprise mobile applications _MUST_ be code-signed in accordance with InfoSec policy.
* Mobile applications _MUST_ be compiled with stack protection and position independent executable options enabled.

## SEC-DEV-MOBILITY-FR5 Vulnerability Scanning 

* Mobile applications _MUST_ be scanned for vulnerabilities using high quality application scanning tools such as Checkmarx, AppScan, Anchore, etc. before production deployment.

## SEC-DEV-MOBILITY-FR6 Jailbroken/Rooted Device 

* Mobile applications with the data classification **Cisco Highly Confidential** or **Cisco Restricted**  _MUST_ be designed to prevent execution on a jailbroken/rooted device.
* Enterprise mobile applications _MUST_ only be deployed on devices that meet the requirements of the [Trusted Device Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1234364&ver=approved).

## SEC-DEV-MOBILITY-FR7 Distribution and Mobile Application Version Control 

* Mobile applications _MUST_ follow the distribution and publishing process defined by External Mobile App Management
* Mobile applications deployment services _MUST_ also support some mechanism for application version control.
* Mobile applications _MUST_ support a service that can notify users that updates are available.
* Mobile applications _MUST also support a service that can deprecate, deactivate, and/or remove versions which are no longer supported.
    *  This service needs to consider the balance between software vulnerabilities, current risks, support for older devices vs newer software features and bug/security fixes.
* Mobile application development _MUST_ provide multi-factor authentication (MFA) access services for administrator accounts.  A few examples might include: Google Authenticator, DUO security,  Microsoft authenticator, etc.
    *  There may be specific versions of the Mobile OS and basic device configurations that are required to support MFA.
* Enterprise mobile applications _MUST_ follow the publishing process defined by [Publish Internal App to eStore](https://estore.cisco.com/RequestCenter/website/ServiceCatalog/application/index.html?/services/eStore+Mobile+Engagement+Form+-+New+App).
* Customer-based mobile applications, MUST use standard application distribution centers and hubs: Amazon Appstore for Android, Google’s Play Store and Apple’s App Stores. All others must be reviewed and approved by Infosec.

## SEC-DEV-MOBILITY-FR8 Accessing Other Services and Apps 
* The mobile application or device _MUST_ access only services or other apps on the mobile device that are necessary to provide the Mobile Application’s functionality.
* The mobile ppp _MUST_ comply with any requirements set forth by the mobile operating system regarding permission to access services or apps on the mobile device.
* The mobile app _MUST_ only activate or access services or other apps with the explicit prior permission of the authorized user of the mobile device.
* Permission _MUST_ be requested on an app-by-app or service-by-services basis (i.e., individually).
* Examples of services or apps commonly accessed by other apps:
    * Bluetooth sharing
    * Calendars
    * Camera
    * Contacts
    * Health
    * Location services
    * Media library
    * Microphone
    * Motion activity and fitness
    * Photos
    * Videos
    * Reminders
    * SMS
    * MMS
    * Social media accounts
    * Speech recognition

## SEC-DEV-MOBILITY-FR9 Sensitive Information or Personal Information Storage 

* Applications _SHOULD_ avoid the use of device UUID.
* Data stored in the iOS Keychain or the Android KeyStore _MUST_ use InfoSec-approved configurations to properly secure the data.
* File permissions _SHOULD_ be set to prevent any other application from accessing, reading, or writing.
* Non-public information _MUST NOT_ be stored in the following places:
    * SD Cards or other external storage
    * Keyboard cache
    * Clipboard

**Supplemental Guidance:**  Application logging has to follow the requirements set in [SEC-LOG-NOSENS-3](SEC-LOG-NOSENS-3).

## SEC-DEV-MOBILITY-FR10 Cloud Sync 

* Mobile applications _MUST NOT_ sync data to any unapproved cloud service.
* Mobile applications users _MUST_ be able to delete personal or user-generated information from the device that is synced to a cloud service.
* Mobile application _MUST_ provide users with instruction on how to delete personal or user-generated information synced to a cloud service when deleting it from the device does not result in deleting copies synced to a cloud service.

## SEC-DEV-MOBILITY-FR11 Interprocess Communication (IPC) 

* Mobile applications _MUST NOT_ pass sensitive information using Interprocess Communication (IPC) on mobile devices.

## SEC-DEV-MOBILITY-FR12 Persistent Data Collection from Other Apps and Services 

* Mobile device and application MUST allow user to set permission (such as, allow or deny) for the level and frequency of data being collected and processed from other apps or services on the device.
* After initial permission is granted, “only when the mobile app is in use”  _MUST_ be the default setting until permission for a longer duration is granted by the user.
* There _MUST_ be one visual cue per service or app whenever the mobile app or device is accessing another service or app on a mobile device.

# Informative References

* [Mobile Application Security Standard](https://docs.cisco.com/share/proxy/alfresco/url?docnum=EDCS-1308268&ver=approved)
* [OWASP Mobile Top 10](https://owasp.org/www-project-mobile-top-10/)
* [Mobile Application Security - Best Practices](https://cisco.sharepoint.com/Sites/SECURECODE/SitePages/Mobile%20Application%20Secure%20Coding%20Guidelines%20%20Best%20Practices.aspx)
* [Mobile Center of Excellence](https://cisco.sharepoint.com/Sites/MobileAppCenterofExcellence)
* [Internal and External App Publishing Steps](https://cisco.sharepoint.com/Sites/MobileAppCenterofExcellence/SitePages/Publishing%20Internal%20and%20External%20Mobile%20Apps.asp)
* [Privacy on the Go](https://oag.ca.gov/sites/all/files/agweb/pdfs/privacy/privacy_on_the_go.pdf)
* [Android 5.0.2 Secure Development Hardening Standard](https://cisco.sharepoint.com/Sites/CiscoProductSecurityCookbook/SitePages/Android%205.0.2%20Secure%20Development%20Hardening%20Standard.aspx)
* [Apple platform security best practices](https://developer.apple.com/documentation/Security)
* [Android platform security best practices](https://developer.android.com/topic/security/best-practices)
* [CoDe - Continuous Delivery Experience - Mobility](https://cisco.sharepoint.com/Sites/CoDE(ContinuousDeliveryExperience)/SitePages/Mobile%20SDK%27s.aspx)

# Requirement References

    ---
    source: PSB
    foreign_id: SEC-DAT-CLNSTATE
    relation: connects
    headline: >
      Securely purge all physical storage to enter a clean state and protect sensitive data.
    ---
    source: PSB
    foreign_id: SEC-DAT-KEYMGMT
    relation: connects
    headline: >
      Generate, store, use, and retire secrets safely
    ---
    source: PSB
    foreign_id: SEC-DAT-KNOWWHAT
    relation: connects
    headline: >
      Know what data your offering or application is processing and document the required controls
    ---
    source: PSB
    foreign_id: SEC-DAT-MINIMIZE
    relation: connects
    headline: >
      Minimize collection and use of data
    ---
    source: PSB
    foreign_id: SEC-DAT-MONEY
    relation: connects
    headline: >
      Don't handle financial identifiers (incl. credit cards)
    ---
    source: PSB
    foreign_id: SEC-DAT-PRIV
    relation: connects
    headline: >
      Comply with Cisco's privacy policy
    ---
    source: PSB
    foreign_id: SEC-PRV-DSRIGHTS
    relation: connects
    headline: >
      Rights of Personally Identifiable Information's Data Subject
    ---
    source: PSB
    foreign_id: SEC-PRV-DSRIGHTS
    relation: connects
    headline: >
      Rights of Personally Identifiable Information's Data Subject
    ---
    source: PSB
    foreign_id: SEC-PRV-USERAUTH
    relation: connects
    headline: >
      Control user and system access to personal information
    ---
    source: PSB
    foreign_id: SEC-AUT-AUTH
    relation: connects
    headline: >
      Authenticate and authorize agents seeking access to any target
    ---
    source: PSB
    foreign_id: SEC-LOG-NOSENS
    relation: connects
    headline: >
      Do not log sensitive data, passwords, credentials, crypto keys, etc.
    ---
    source: PSB
    foreign_id: SEC-WEB-SCAN
    relation: connects
    headline: >
      Run application vulnerability scans and fix issues
    ---
    source: PSB
    foreign_id: SEC-ASU-TMOD-FR1
    relation: connects
    headline: >
      Conduct threat modeling
    ---
    source: PSB
    foreign_id: SEC-SCR-CONFLEAK
    relation: connects
    headline: >
      Don't expose credentials/critical data
    ---
    source: PSB
    foreign_id: SEC-TLS-CURR-FR1
    relation: connects
    headline: >
      Support current TLS versions.  See also other FR's.
    ---
    source: PSB
    foreign_id: SEC-CRY-STDCODE-FR1
    relation: connects
    headline: >
      Use established cryptographic libraries
    ---
    source: PSB
    foreign_id: SEC-CRY-PRIM-FR1
    relation: connects
    headline: >
      Use approved cryptographic primitives and parameters
    ---
    source: PSB
    foreign_id: SEC-CRY-RANDOM
    relation: connects
    headline: >
      Use approved and effective random number generation
    ---
    source: PSB
    foreign_id: SEC-CRY-PLATRAND
    relation: connects
    headline: >
      Provide good OS and platform random number generators
    ---
    source: PSB
    foreign_id: SEC-CRY-MGT-FR2
    relation: connects
    headline: >
      Protect external management traffic.  See also other FR's.
    ---
    source: PSB
    foreign_id: SEC-RUN-ASLR-FR1
    relation: connects
    headline: >
      Randomize program address space layout.  See also other FR's.

# Attributes

    id: SEC-DEV-MOBILITY
    version: 2
    issueref: ISS_MobileAttackSurface
    category: Development Process
    riskArea: Application & Interface Security
    legallysensitive: false
    waivable: true
    #defines the applicability of this requirement to a certain product/technology type
    applicability:
      - force: mandatory
        target:
            class:  MobileApp
            restrict: >
               Mobile Applications
    priority: 10
    phase: requirements
    tags:
    - Critical PSB
