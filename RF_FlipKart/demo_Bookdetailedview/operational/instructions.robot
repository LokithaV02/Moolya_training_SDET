*** Settings ***
Library          SeleniumLibrary
Resource        ../operational/LocatorsVariable.robot

*** Keywords ***
Open FlipKart website
    Log    ------------Opening Flipkart in Chrome Browser------------
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    Sleep    4s
    Click Element   ${Close_button}

Search for any of your desired Mobile from ‘Mobiles’ section
    Log    ------------Selecting Mobiles category------------
    ${Category_count}   Get Element Count    ${Category_list}
    Sleep    5s
    FOR    ${i}    IN RANGE    1    ${Category_count}
        ${Category_name}   Get Text    (${Category_list})[${i}]
        Log To Console    ${Category_name}
        IF    "${Category_name}" == "${expected_category}"
             Click Element    (${Category_list})[${i}]
             BREAK
        END
    END

Navigate to "Electronics" tab in mobiles section
    Log    ------------Selecting Electronics tab in Mobiles category------------
    ${mobile_category_count}   Get Element Count    ${mobile_sub_category_list}
    Log To Console    ${mobile_category_count}
    Sleep    5s
    FOR    ${i}    IN RANGE    1    ${mobile_category_count}
        ${mobile_category_name}=   Get Text    (${mobile_sub_category_list})[${i}]
        Scroll Element Into View    (${mobile_sub_category_list})[${i}]
        Log To Console    ${mobile_category_name}
        Exit For Loop If    "${mobile_category_name}" == "${select_categoryinmobile}"
             Mouse Over    (${mobile_sub_category_list})[${i}]
    END

Do not select first 5 mobiles from the list
    Log    ------------Selecting mobiles which are not in the range of 1 to 5------------
    ${mobile_count}    Get Element Count    ${diff_mobiles}
    Log To Console    ${mobile_count}
    Sleep    5s
    FOR    ${n}    IN RANGE    6    ${mobile_count}
        ${mobiles_text}=    Get Text    (${diff_mobiles})[${n}]
        Log    ${mobiles_text}
        IF    "${mobiles_text}" == "${expected_honor_mobile}"
             Click Element    (${diff_mobiles})[${n}]
             BREAK
        END
    END

Try scrolling and search for the mobile and go to that specific mobile’s details page
    Log    ------------Selecting ${expected_mobile} Mobile from the list------------
    Sleep    5S
    ${honor_mobile_count}=   Get Element Count    ${honor_mobiles}
    Log To Console    ${honor_mobile_count}
    FOR    ${cnt}    IN RANGE   1   ${honor_mobile_count}
        ${mobile}   Get Text    (${honor_mobiles})[${cnt}]
        Log To Console    ${mobile}
        Scroll Element Into View    (${honor_mobiles})[${cnt}]
        IF    "${mobile}" == "${expected_mobile}"
             Click Element    (${honor_mobiles})[${cnt}]
             BREAK
        END
    END
    Set Global Variable    ${mobile}

Click on ADD TO CART button
    Log    ------------Clicking on Add to Cart Button------------
    Switch Window   New
    Sleep    5
    Scroll Element Into View    ${Add_to_Cart}
    Click Element    ${Add_to_Cart}

Verify if the the Mobile which we added is available in the list
    Sleep    5
    ${mob_text}=    Get Text    ${mobile_in_addcart}
    IF      "${mobile}" == "${mob_text}"
        Log    ---------"Mobile Matching and Available in the list and Click on Proceed to checkout"-------------
        Click Button    ${proceed_to_checkout}
    END

Closing the Browser opened
    Close Browser
