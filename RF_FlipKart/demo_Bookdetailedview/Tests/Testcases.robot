*** Settings ***
Resource        ../operational/instructions.robot
Resource        ../operational/LocatorsVariable.robot
Resource        ../operational/flipkartiphone.robot



*** Test Cases ***
User should be able to Land on Book details page
    Open FlipKart website
    Search for any of your desired Mobile from ‘Mobiles’ section
    Navigate to "Electronics" tab in mobiles section
    Do not select first 5 mobiles from the list
    Try scrolling and search for the mobile and go to that specific mobile’s details page
    Click on ADD TO CART button
    Verify if the the Mobile which we added is available in the list
    Closing the Browser opened