*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
dropdown
    Sleep    10
#   Select From List By Value    dropdown-class-example     option1
    Select From List By Index    dropdown-class-example     2
    Get Selected List Label    dropdown-class-example

Alerts
    Sleep    5
    ${name}     Set Variable    testing123
    Input Text    enter-name    ${name}
    Click Element    confirmbtn
    ${message}=     Handle Alert    LEAVE
    Log To Console    ${message}
    Sleep    10
    Alert Should Be Present     ${message}
    Handle Alert        Accept



