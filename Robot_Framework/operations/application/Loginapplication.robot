*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
Logintoorange
    Sleep    10
    Input Text    username    Admin
    Input Text    password    admin123
    Click Element    //*[@type='submit']
    Title Should Be    OrangeHRM
    Element Should Be Visible    locator

#    Input Text    css:input[name = 'username']    Admin
#    Input Text    css:input[name = 'password']    admin123
#    Click Element    xpath://*[@type='submit']

LogoutfromApplication
    Sleep    10
    Click Element    xpath://*[@class='oxd-userdropdown-name']
    Click Element    xpath://a[text() = 'Logout']