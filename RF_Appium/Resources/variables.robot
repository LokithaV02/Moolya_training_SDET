*** Variables ***
# Home page
${country_dd}                    id=com.androidsample.generalstore:id/spinnerCountry
${country_frame}                 xpath=/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout
${dd_values}                     xpath=//android.widget.TextView
${verify_dd_text}                id=android:id/text1
${dd_text}                       Angola
${name_field}                    id=com.androidsample.generalstore:id/nameField
${entering_name}                 testing123
${gen_select}                    id=com.androidsample.generalstore:id/radioFemale
${lets_shop_button}              id=com.androidsample.generalstore:id/btnLetsShop

# Products page
${product_name_lists}            id=com.androidsample.generalstore:id/productName
${expected_prod_name}            Converse All Star
${product_add_to_cart}           xpath=//android.widget.TextView[@text='Converse All Star']/..//android.widget.TextView[@text='ADD TO CART']
${product_price}                 xpath=//android.widget.TextView[@text='Converse All Star']/..//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productPrice']
${expected_price}                $55.0
${add_cart_button}               id=com.androidsample.generalstore:id/appbar_btn_cart

# Proceed to checkout page
${prod_price_co}                 id=com.androidsample.generalstore:id/productPrice
${total_price}                   id=com.androidsample.generalstore:id/totalAmountLbl
${checkboxtext}                  xpath= //android.widget.CheckBox[contains(@text,"Send me e-mails on discounts related to selected products in future")]
${terms_and_conditions}          id=com.androidsample.generalstore:id/termsButton
${close_frame}                   id=android:id/button1
${proceed_button}                id=com.androidsample.generalstore:id/btnProceed