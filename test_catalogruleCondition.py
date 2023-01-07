# Generated by Selenium IDE
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestAddcartrule():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_addcartrule(self):
        discount_percentage = '15'
        # Test name: add_cart_rule
        # Step # | name | target | value
        # 1 | open | http://34.118.122.203/administration/index.php?controller=AdminLogin&token=1e53b83c6f3b96a3ca75976d5bab155e&redirect=AdminDashboard |
        self.driver.get(
            "http://34.118.122.203/administration/index.php?controller=AdminLogin&token=1e53b83c6f3b96a3ca75976d5bab155e&redirect=AdminDashboard")
        # 2 | setWindowSize | 1936x1056 |
        self.driver.set_window_size(1936, 1056)
        # 3 | click | id=email |
        self.driver.find_element(By.ID, "email").click()
        # 4 | type | id=email | user@example.com
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        # 5 | click | id=passwd |
        self.driver.find_element(By.ID, "passwd").click()
        # 6 | type | id=passwd | VTR6WmtBCvnZ
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        # 7 | click | css=.ladda-label |
        self.driver.find_element(By.CSS_SELECTOR, ".ladda-label").click()
        self.driver.implicitly_wait(2)
        # 8 | click | css=#subtab-AdminCatalog > .link |
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link").click()
        # 9 | click | linkText=Discounts |
        self.driver.find_element(By.LINK_TEXT, "Discounts").click()
        # 10 | click | id=subtab-AdminSpecificPriceRule |
        self.driver.find_element(By.ID, "subtab-AdminSpecificPriceRule").click()
        # 11 | click | css=#page-header-desc-specific_price_rule-new_specific_price_rule > div |
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#page-header-desc-specific_price_rule-new_specific_price_rule > div").click()
        # 12 | click | id=name |
        self.driver.find_element(By.ID, "name").click()
        # 13 | type | id=name | Games15
        self.driver.find_element(By.ID, "name").send_keys("Games15")
        # 14 | click | id=from |
        self.driver.find_element(By.ID, "from").click()
        # 15 | click | css=.ui-datepicker-current |
        self.driver.find_element(By.LINK_TEXT, "1").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-current").click()
        # # 16 | click | css=.form-wrapper |
        # self.driver.find_element(By.CSS_SELECTOR, ".form-wrapper").click()
        # 17 | click | id=to |
        self.driver.find_element(By.ID, "to").click()
        # 18 | click | linkText=31 |
        self.driver.find_element(By.LINK_TEXT, "30").click()
        # 19 | click | css=.form-group:nth-child(10) > .col-lg-8 |
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(10) > .col-lg-8").click()
        # 20 | click | id=reduction_type |
        self.driver.find_element(By.ID, "reduction_type").click()
        # 21 | select | id=reduction_type | label=Percentage
        dropdown = self.driver.find_element(By.ID, "reduction_type")
        dropdown.find_element(By.XPATH, "//option[. = 'Percentage']").click()
        # 22 | click | id=reduction_tax |
        self.driver.find_element(By.ID, "reduction_tax").click()
        # 23 | select | id=reduction_tax | label=Tax included
        dropdown = self.driver.find_element(By.ID, "reduction_tax")
        dropdown.find_element(By.XPATH, "//option[. = 'Tax included']").click()
        # 24 | click | id=reduction |
        self.driver.find_element(By.ID, "reduction").click()
        self.driver.find_element(By.ID, "reduction").clear()
        # 25 | type | id=reduction | 15
        self.driver.find_element(By.ID, "reduction").send_keys(discount_percentage)
        # 26 | click | id=add_condition_group |
        self.driver.find_element(By.ID, "add_condition_group").click()
        # 27 | mouseOver | id=add_condition_group |
        element = self.driver.find_element(By.ID, "add_condition_group")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 28 | mouseOut | id=add_condition_group |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset((element), 0, 0).perform()
        # 29 | click | id=id_category |
        self.driver.find_element(By.ID, "id_category").click()
        # 30 | select | id=id_category | label=(10) Games
        dropdown = self.driver.find_element(By.ID, "id_category")
        dropdown.find_element(By.XPATH, "//option[. = '(10) Games']").click()
        # 31 | click | id=add_condition_category |
        self.driver.find_element(By.ID, "add_condition_category").click()
        # 32 | mouseOver | id=add_condition_category |
        element = self.driver.find_element(By.ID, "add_condition_category")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 33 | mouseOut | id=add_condition_category |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset((element), 0, 0).perform()
        # 34 | click | id=specific_price_rule_form_submit_btn |
        self.driver.find_element(By.ID, "specific_price_rule_form_submit_btn").click()
        assert 'Successful creation.' in self.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div').text
        # 35 | click | css=#header_shopname > span |
        self.vars["window_handles"] = self.driver.window_handles
        # 36 | selectWindow | handle=${win6208} |
        self.driver.find_element(By.CSS_SELECTOR, "#header_shopname > span").click()
        # 37 | click | name=s |
        self.vars["win6208"] = self.wait_for_window(2000)
        # 38 | type | name=s | suburbia
        self.driver.switch_to.window(self.vars["win6208"])
        # 39 | sendKeys | name=s | ${KEY_ENTER}
        self.driver.find_element(By.NAME, "s").click()
        # 40 | click | css=.thumbnail > img |
        self.driver.find_element(By.NAME, "s").send_keys("suburbia")
        # 41 | click | css=#subtab-AdminCatalog > .link |
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        # 42 | click | linkText=Discounts |
        self.driver.find_element(By.CSS_SELECTOR, ".thumbnail > img").click()
        assert f'SAVE {discount_percentage}%' in self.driver.find_element(By.XPATH,
                                                                          '//*[@id="main"]/div[1]/div[2]/div[1]/div[2]/div/span[2]').text
        regular_price = self.driver.find_element(By.CLASS_NAME, "regular-price").text
        reduced_price = self.driver.find_element(By.CLASS_NAME, "current-price-value").text
        assert regular_price != reduced_price
        self.driver.get("http://34.118.122.203/administration")
        # 43 | click | id=subtab-AdminSpecificPriceRule |
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link").click()
        # 44 | click | css=.btn-default:nth-child(2) |
        self.driver.find_element(By.LINK_TEXT, "Discounts").click()
        # 45 | click | linkText=Delete |
        self.driver.find_element(By.ID, "subtab-AdminSpecificPriceRule").click()
        # 46 | click | id=popup_ok |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-default:nth-child(2)").click()
        # 47 | click | css=#header_shopname > span |
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        # 48 | selectWindow | handle=${win1665} |
        self.driver.find_element(By.ID, "popup_ok").click()
        assert 'Successful deletion.' in self.driver.find_element(By.ID, 'content').text
        # 49 | click | name=s |
        self.vars["window_handles"] = self.driver.window_handles
        # 50 | click | css=#ui-id-2 > .product |
        self.driver.find_element(By.CSS_SELECTOR, "#header_shopname > span").click()
        self.vars["win1665"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win1665"])
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").clear()
        self.driver.find_element(By.NAME, "s").send_keys("suburbia")
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div/article/div/div[1]/a/img').click()
        # assert self.driver.find_element(By.CLASS_NAME,'regular-price').size == 0
        assert len(self.driver.find_elements(By.XPATH, '//*[@id="main"]/div[1]/div[2]/div[1]/div[2]/div/span[1]')) < 1


if __name__ == '__main__':
    pytest.main()