*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${searchBar}    //input[@name='q']
${searchVal}    //span[@class='_10Ermr']
${prodTitle}    //*[@class='_4rR01T']
${searchBtn}    //*[@class='L0Z3Pu']
${iphone_val}   APPLE iPhone 14 (Midnight, 256 GB)
${iphone_verify}    //span[@class='B_NuCI']
${check_pincode}    //div[@class='_2Tpdn3 _1Y11nq']
${del_address}  //*[@class='_36yFo0']
${check}    //*[@class='_2P_LDn']
${withEx_btn}   //label[@for='BUY_WITH_EXCHANGE']//div[@class='_1XFPmK']
${buy_with_exchange}    //input[@id='BUY_WITH_EXCHANGE']
${brand_lst}    //div[@class='_21OhbT']//div[@class='_2Tpdn3 S6gRzE']
${ex_pop}   //*[@class='_2_e-g9 ZLCnIT']

*** Keywords ***
Search a product
    Clear Element Text  ${searchBar}
    Input Text    ${searchBar}    iphone
    Press Keys    ${searchBar}    ENTER
    Element Should Be Visible    ${searchVal}


Check the product details
    ${prof_vals}=    Get WebElements    ${prodTitle}
    Get Length    ${prof_vals}
    FOR    ${element}    IN    @{prof_vals}
        ${val}=     Get Text    ${element}
        IF    '${val}' == '${iphone_val}'
            Click Element    ${element}
        END
    END
    Switch Window   NEW

Buy with Exchange flow
    ${val2}=    Get Text    ${iphone_verify}
    IF    '${val2}' == '${iphone_val}'
        ${val3}=    Run Keyword And Return Status    Element Should Be Visible    ${check_pincode}
        IF  ${val3}
            Clear Element Text    ${del_address}
            Input Text    ${del_address}    560047
            Click Element    ${check}
        END
        Execute JavaScript    window.scrollTo(document.body.scrollHeight,0)
        ${radio_btn}=   Run Keyword And Return Status   Wait Until Element Is Not Visible     ${check_pincode}
        IF    ${radio_btn}
            Execute JavaScript    window.scrollTo(0,150)
            Wait Until Element Is Visible    ${withEx_btn}
            Click Element    ${withEx_btn}
            Sleep    5s



            ${brand_val}=   Get WebElements    ${brand_lst}
#            ${brand_val2}=   Get Element Count    ${brand_lst}
            Log To Console    ${brand_val}
            FOR    ${element}    IN    @{brand_val}
                ${val4}=    Get Text    ${element}
                Log    ${val4}
                IF    "${val4}" == "Apple"
                    Click Element    ${element}
                END

            END


        END

    END