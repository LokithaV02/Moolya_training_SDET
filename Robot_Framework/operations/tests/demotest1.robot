*** Settings ***
Resource    C:\\Users\\Hp\\PycharmProjects\\Robot_Framework\\operations\\application\\Loginapplication.robot
Library     SeleniumLibrary

# User defined varibales sould be present under Variables
*** Variables ***
${browser}      chrome
${url}          https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***
LoginTest
    Open Browser    ${url}   ${browser}
    Maximize Browser Window
    Logintoorange
#    LogoutfromApplication
#    Close Browser