# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestWishlist():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_wishlist(self):
        # Test name: wishlist
        # Step # | name | target | value
        # 1 | open | http://34.118.122.203/en/ |
        self.driver.get("http://34.118.122.203/en/")
        # 2 | setWindowSize | 1936x1056 |
        self.driver.set_window_size(1936, 1056)
        # 3 | click | css=a > .hidden-sm-down |
        self.driver.find_element(By.CSS_SELECTOR, "a > .hidden-sm-down").click()
        # 4 | click | id=field-email |
        self.driver.find_element(By.ID, "field-email").click()
        # 5 | type | id=field-email | user@example.com
        self.driver.find_element(By.ID, "field-email").send_keys("user@example.com")
        # 6 | click | id=field-password |
        self.driver.find_element(By.ID, "field-password").click()
        # 7 | type | id=field-password | 123456789
        self.driver.find_element(By.ID, "field-password").send_keys("123456789")
        # 8 | click | id=submit-login |
        self.driver.find_element(By.ID, "submit-login").click()
        # 9 | click | name=s |
        self.driver.find_element(By.NAME, "s").click()
        # 10 | type | name=s | empire
        self.driver.find_element(By.NAME, "s").send_keys("empire")
        # 11 | sendKeys | name=s | ${KEY_ENTER}
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        # 12 | click | css=.wishlist-button-add > .material-icons |
        self.driver.find_element(By.CSS_SELECTOR, ".wishlist-button-add > .material-icons").click()
        self.driver.implicitly_wait(1)
        # 13 | click | css=.wishlist-list-item > p |
        self.driver.find_element(By.CSS_SELECTOR, ".wishlist-list-item > p").click()
        # 14 | click | name=s |
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").clear()
        # 15 | type | name=s | humming
        self.driver.find_element(By.NAME, "s").send_keys("humming")
        # 16 | sendKeys | name=s | ${KEY_ENTER}
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        # 17 | click | css=.js-product:nth-child(1) img |
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(1) img").click()
        # 18 | click | css=.js-product:nth-child(1) .wishlist-button-add > .material-icons |
        self.driver.find_element(By.XPATH,'//*[@id="add-to-cart-or-refresh"]/div[2]/div/button').click()
        # 19 | click | css=.wishlist-list-item > p |
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.CSS_SELECTOR, ".wishlist-list-item > p").click()
        # 20 | mouseDownAt | css=.account > .hidden-sm-down | 36.9375,4.5
        element = self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        # 21 | mouseMoveAt | css=.account > .hidden-sm-down | 36.9375,4.5
        element = self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 22 | mouseUpAt | css=.account > .hidden-sm-down | 36.9375,4.5
        element = self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        # 23 | click | css=.account > .hidden-sm-down |
        self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down").click()
        self.driver.implicitly_wait(1)
        # 24 | click | css=#wishlist-link .material-icons |
        self.driver.find_element(By.CSS_SELECTOR, "#wishlist-link .material-icons").click()
        self.driver.implicitly_wait(1)
        # 25 | click | css=.wishlist-list-item-link |
        self.driver.find_element(By.CSS_SELECTOR, ".wishlist-list-item-link").click()
        assert 'After The Empire (Kickstarter Deluxe Edition)' in self.driver.find_element(By.XPATH,
                                                                                           '//*[@id="content"]/ul/li[1]/div/a/div[2]/p[1]').text
        assert 'Hummingbird printed t-shirt' in self.driver.find_element(By.XPATH,
                                                                         '//*[@id="content"]/ul/li[2]/div/a/div[2]/p[1]').text
        # 26 | click | css=.wishlist-products-item:nth-child(2) .wishlist-button-add > .material-icons |
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".wishlist-products-item:nth-child(2) .wishlist-button-add > .material-icons").click()
        # 27 | click | css=.show .btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".show .btn-primary").click()
        time.sleep(0.5)
        assert 'Hummingbird printed t-shirt' not in self.driver.page_source
        # 28 | click | css=.wishlist-product-image > img |
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".wishlist-products-item:nth-child(1) .wishlist-button-add > .material-icons").click()
        self.driver.find_element(By.CSS_SELECTOR, ".show .btn-primary").click()
        assert 'No products found' in self.driver.find_element(By.CLASS_NAME, "wishlist-list-empty").text


if __name__ == '__main__':
    pytest.main()
