import pytest

from pageObjects.HomePage import HomePage
from pageObjects.Filter_Page import FilterPage


@pytest.mark.usefixtures("setup")
class TestAjio:

    def test_homepage(self):
        homepage_obj = HomePage(self)
        homepage_obj.search_item_on_searchbar().send_Keys("clothes")
        homepage_obj.click_on_search_icon().click()

    def test_filter(self):
        fil_obj = FilterPage(self)
        fil_obj.click_on_more_link().click()
        fil_obj.select_men().click()
        fil_obj.click_on_apply_button().click()
        fil_obj.click_on_price_filter().click()
        fil_obj.enter_min_price().send_keys("100")
        fil_obj.enter_max_price().send_keys("700")
        print(len(fil_obj.verify_filter()))
        assert len(fil_obj.verify_filter()) == 2
        print("Filters applied are 2")



