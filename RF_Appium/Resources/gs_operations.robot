*** Settings ***
Resource    general_store_resources.robot
Library    String

*** Keywords ***
User Launches the Application
    Log    ---------launching General store application----------
    Open Application  ${server}    devicename=${Device_name}  platformName=${platform_name}  appPackage=${App_package}  appActivity=${App_activity}

User selects the country
    Log    ---------Selecting country-------
    Sleep    5
    Click Element    ${country_dd}
    Wait Until Element Is Visible    ${country_frame}
    ${c}    Evaluate    1
    WHILE    ${c} > 0
    ${dd_lists}=   Get Webelements    ${dd_values}
        FOR    ${i}    IN    @{dd_lists}
            ${expectedtext}=    Get Element Attribute    ${i}    text
            Log To Console    ${expectedtext}
            IF    "${expectedtext}" == "${dd_text}"
                Sleep    5
                Log    -------clicking ${expectedtext} value------------
                Click Element    ${i}
                Element Should Contain Text    ${verify_dd_text}    ${dd_text}
                ${c}   evaluate    ${c}-1
                BREAK
            END
        END
    Swipe    789    2088    178    595
    END

User enter the name, selects gender and clicks on shop button
    Log    ---------Entering Name-------
    Input Text    ${name_field}    ${entering_name}
    Element Text Should Be    ${name_field}    ${entering_name}
    Log    ---------Selecting Gender-------
    Click Element    ${gen_select}
    ${checked_value}=    Get Element Attribute    ${gen_select}    checked
    IF    "${checked_value}" == "true"
        Log    Female is selected
    END
    Log    ---------Clicking on Let's shop button-------
    Click Element    ${lets_shop_button}

User selects Product from the products page
    Log    ------------selecting product-------------
    Sleep    5
    ${i}    Evaluate    1
    WHILE    ${i}>0
    ${product_lists}=    Get Webelements    ${product_name_lists}
    log to console      ${product_lists}
    ${prod_list_len}=    Get Length        ${product_lists}
    log to console    ${prod_list_len}
        FOR    ${prod}      IN      @{product_lists}
            ${product_name}=      Get Element Attribute    ${prod}    text
            log to console    ${product_name}

                IF      "${product_name}" == "${expected_prod_name}"
                    Log    ----------Clicking on Add to Cart button for "${product_name}"----------------
                    Click Element    ${product_add_to_cart}
                    ${i}   Evaluate    ${i}-1
                    ${price}=    Get Element Attribute    ${product_price}    text
                    Log    ${price}
                    IF    "${price}" == "${expected_price}"
                        Log   ------Price matching continue to add to cart---------
                        BREAK
                    END
                END
        END
        Swipe    1030    1856    50    270
    END
    Element Should Be Enabled    ${add_cart_button}
    Log    --------Product added to cart successfully and Click on Add Cart button------------
    Click Element    ${add_cart_button}

User verifies the product price and clicks on checkbox
    Sleep    5
    Log    -----------------Verifying the product price---------------------
    ${prod_price_co_value}=    Get Element Attribute    ${prod_price_co}    text
    Log    ${prod_price_co_value}
    ${total_price_value}=   Get Element Attribute    ${total_price}    text
    Log    ${total_price_value}
    ${TP_wo_space}=     Replace String    ${total_price_value}    ${SPACE}    ${EMPTY}
    IF    "${prod_price_co_value}" == "${TP_wo_space}"
        Log    -------------Total price is matching and click on checkbox---------
        Click Element    ${checkboxtext}
        ${checked_value_cp}=    Get Element Attribute    ${checkboxtext}    checked
        IF    "${checked_value_cp}" == "true"
            Log    The checkbox is selected
            END
    END

User clicks on Terms and Conditions and Proceed to checkout button
    Log    ---------Terms and conditions pop is displayed, Click on close button-----------
    Element Should Be Visible    ${terms_and_conditions}
    Long Press    ${terms_and_conditions}
    Page Should Contain Text    Terms Of Conditions
    Click Element    ${close_frame}
    Sleep    5
    Log    ----------Clicking on Proceed to checkout button--------------
    Click Element    ${proceed_button}

Close the general Store application
    Close Application
    Log    -----------General store application closed-------------
