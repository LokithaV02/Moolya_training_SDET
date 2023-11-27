*** Variables ***
#Opening the Flipkart Application
${url}                          https://www.flipkart.com/
${browser}                      chrome
${Close_button}                 //span[@role='button']
# Category Selection
${expected_category}            Mobiles
# Mobile selection under electronics tab
${select_categoryinmobile}      Electronics
${Category_list}                (//div[@class='_3sdu8W emupdz']/a[@class='_1ch8e_'])
${mobile_sub_category_list}     //span[@class='_2I9KP_']
${diff_mobiles}                 //div[@class='_1fwVde'][1]/a
${expected_honor_mobile}        Honor
#selection of mobile
${honor_mobiles}                //div[@class='_4rR01T']
${expected_mobile}              Honor 90 5G (Emerald Green, 256 GB)
# Add to cart and Proceed to checkout page
${Add_to_Cart}                  //button[@class='_2KpZ6l _2U9uOA _3v1-ww']
${mobile_in_addcart}            //a[@class='_2Kn22P gBNbID']
${proceed_to_checkout}           //button[@class='_2KpZ6l _2ObVJD _3AWRsL']