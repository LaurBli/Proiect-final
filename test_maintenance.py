# Generated by Selenium IDE
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class TestMaintenance():
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

    def test_maintenance(self):
        # Test name: Maintenance
        # Step # | name | target | value
        # 1 | open | http://34.118.122.203/administration/index.php?controller=AdminLogin&logout=1&token=def97ab7614757538fe964e40fd3c155 |
        self.driver.get(
            "http://34.118.122.203/administration/index.php?controller=AdminLogin&logout=1&token=def97ab7614757538fe964e40fd3c155")
        # 2 | setWindowSize | 1920x1040 |
        self.driver.set_window_size(1920, 1040)
        # 3 | click | id=email |
        self.driver.find_element(By.ID, "email").click()
        # 4 | type | id=email | user@example.com
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        # 5 | click | id=passwd |
        self.driver.find_element(By.ID, "passwd").click()
        # 6 | type | id=passwd | VTR6WmtBCvnZ
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        # 7 | click | id=submit_login |
        self.driver.find_element(By.ID, "submit_login").click()
        self.driver.implicitly_wait(3)
        # 8 | click | css=#subtab-ShopParameters .sub-tabs-arrow |
        self.driver.find_element(By.XPATH, '//*[@id="subtab-ShopParameters"]/a').click()
        # 9 | click | linkText=General |
        self.driver.find_element(By.XPATH, '//*[@id="subtab-AdminParentPreferences"]/a').click()
        # 10 | click | id=subtab-AdminMaintenance |
        self.driver.find_element(By.ID, "subtab-AdminMaintenance").click()
        self.driver.implicitly_wait(2)
        text = self.driver.find_element(By.XPATH, '//*[@id="form_maintenance_text_1_ifr"]').text
        text_bun = text.replace('"', '')
        # 11 | click | id=form_enable_shop_0 |
        self.driver.find_element(By.ID, "form_enable_shop_0").click()
        # 12 | click | id=form-maintenance-save-button |
        self.driver.find_element(By.ID, "form-maintenance-save-button").click()
        self.driver.implicitly_wait(2)
        # 13 | mouseOver | id=mceu_6-button |
        element = self.driver.find_element(By.ID, "mceu_6-button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 14 | mouseOut | id=mceu_6-button |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, 0, 0).perform()
        # 15 | mouseOver | id=mceu_6-button |
        element = self.driver.find_element(By.ID, "mceu_6-button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 16 | mouseOut | id=mceu_6-button |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, 0, 0).perform()
        # 17 | click | css=#header_shopname > span |
        self.vars["window_handles"] = self.driver.window_handles
        # 18 | selectWindow | handle=${win194} |
        self.driver.find_element(By.CSS_SELECTOR, "#header_shopname > span").click()
        self.vars["win194"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win194"])
        assert text_bun in self.driver.page_source
        self.driver.get(
            "http://34.118.122.203/administration/index.php?controller=AdminLogin&logout=1&token=def97ab7614757538fe964e40fd3c155")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        self.driver.find_element(By.ID, "passwd").click()
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        self.driver.find_element(By.ID, "submit_login").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//*[@id="subtab-ShopParameters"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="subtab-AdminParentPreferences"]/a').click()
        self.driver.find_element(By.ID, "subtab-AdminMaintenance").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, '//*[@id="form_enable_shop_1"]').click()
        self.driver.find_element(By.ID, "form-maintenance-save-button").click()
        assert 'Successful update' in self.driver.find_element(By.CLASS_NAME,"alert-text").text
        self.driver.get('http://34.118.122.203/')
        assert 'popular products' in self.driver.find_element(By.ID,'main').text.lower()



if __name__ == '__main__':
    pytest.main()