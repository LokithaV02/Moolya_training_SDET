from utilities.BaseClass import BaseClass
from pageObjects.Add_to_Cart_Page import AddCart
from pageObjects.Filter_Page import FilterPage
from pageObjects.Home_Page_Search import HomePageSearch
from pageObjects.Product_selection_Page import ProductPage
from pageObjects.Sort_Page import SortPage


class TestAjio(BaseClass):

    def test_homepage(self):
        log = self.getLogger()
        homepage_obj = HomePageSearch(self.driver)
        homepage_obj.search_clothes_and_verifying_search()
        log.info("searching for clothes and verifying search")
        print("Header matching with the text entered")

    def test_filter(self):
        log = self.getLogger()
        fil_obj = FilterPage(self.driver)
        fil_obj.filter_by_gender()
        log.info("Applying filters for gender category")
        # fil_obj.filter_by_price()
        # log.info("Applying filters for price category")
        # fil_obj.verifying_filters_applied()
        # print("Filters applied are 2")
        # log.info("Verified filters applied")

    def test_sort(self):
        log = self.getLogger()
        sort_obj = SortPage(self.driver)
        sort_obj.sort_the_product()
        log.info("Applying sort by selecting from dropdown")
        print("Whats new option is selected")

    def test_product_selection(self):
        log = self.getLogger()
        prod_obj = ProductPage(self.driver)
        prod_obj.select_product_and_verify()
        log.info("Selecting product based on search")
        print("The product name is matching")
        prod_obj.select_product_color()
        log.info("Selecting product color")
        prod_obj.select_product_size()
        log.info("Selecting product size")

    def test_add_to_cart(self):
        log = self.getLogger()
        add_obj = AddCart(self.driver)
        add_obj.product_add_to_cart()
        log.info("Product added to cart")
        print("The product price is matching hence, proceed to checkout")
        add_obj.proceed_to_checkout()
        log.info("Proceeded to checkout successfully")
        add_obj.screen_shot_capture()
