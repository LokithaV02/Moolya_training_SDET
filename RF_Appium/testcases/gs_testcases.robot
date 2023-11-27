*** Settings ***
Resource    ../Resources/general_store_resources.robot


*** Test Cases ***
#Test Case 1
User Opens the General Stores Application and Logs In
    [Tags]  Sign_In
    User Launches the Application
    User selects the country
    User enter the name, selects gender and clicks on shop button
    User selects Product from the products page
    User verifies the product price and clicks on checkbox
    User clicks on Terms and Conditions and Proceed to checkout button
    Close the general Store application