# Headline

Limit PCB silkscreen

# Description

Don't print reverse engineering hints on PCBs.

# Behavior

## SEC-HW-SILK-FR1: Exclude Information
The PCB _MUST NOT_ include silkscreen information describing the functions or types of components or headers. Examples include--

1.  Header descriptions, such as "JTAG", "DEBUG", "UART", "CONSOLE", "I2C", etc.
1.  Descriptions for individual signals on headers, such as "TCK", "TMS", "TXD", "RXD", etc.
1.  Internal bus or signal group types or functions, such as "PCI-E".
1.  Chip manufacturer part numbers when those part numbers might not be obvious from the markings on the chips themselves, or for chips that might not be populated on some production boards.

## SEC-HW-SILK-FR2: Includable Information
You _SHOULD NOT_ include any description of the board's overall function unless the board is intended to be a customer-replaceable component.

You _MAY_ include reference designators which are only meaningful to those with schematics or other internal design information (e.g. "U23", "R109", "J42"), provided that they do not give away functional information that wouldn't be obvious from inspection of the board or the parts populating it.

You _MAY_ identify headers, switches, jumpers, and similar items explicitly intended to be used by customers in the field.

You _MAY_ include basic identifying information such as board part number, model, revision, production date, and serial number. You _MAY_ include manufacturing facility information, but _SHOULD_ code it to avoid directly giving away the names or locations of contract manufacturing facilities.

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: institutional bounded computers and their components
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 1
    id: SEC-HW-SILK
    issueref: ISS_Invade
    tags:
    - EN/PD
    - PSB/OnPrem
