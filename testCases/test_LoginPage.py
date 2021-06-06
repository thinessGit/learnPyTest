import pytest
from selenium import webdriver

from pageObject.LoginPage import LoginPage


class Test_001WebPageLogin:
    driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe")
    baseURL = "https://admin-demo.nopcommerce.com/"
    userName = "admin@yourstore.com"
    passWord = "admin"

    @pytest.mark.seleniumTest
    def test_Login(self):
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.admin)
        self.lp.btnSubmit()
        self.driver.quit()
