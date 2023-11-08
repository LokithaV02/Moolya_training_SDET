*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
tabshandling
    Sleep    10
    Click Element    opentab
    @{windows}=      Get Window Handles
    Log To Console    ${windows}
    @{Titles}=       Get Window Titles
    Log To Console    ${Titles}
    Switch Window     title=${Titles}[1]
#    Close Window
#    Switch Window     title1=${Titles}[0]
#    Close Window