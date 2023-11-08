*** Settings ***
Resource    C:\\Users\\Hp\\PycharmProjects\\Robot_Framework\\operations\\application\\dropdowns.robot
Resource    ../application/Windows.robot
Library     SeleniumLibrary

# User defined varibales sould be present under Variables
*** Variables ***
${browser}      chrome
${url}          https://rahulshettyacademy.com/AutomationPractice

*** Test Cases ***
Multiplewindowtest
    Open Browser    ${url}   ${browser}
    Maximize Browser Window
    ${speed}    Get Selenium Speed
    Log To Console    ${speed}
    Set Selenium Speed    2seconds
#   dropdown
    Alerts
