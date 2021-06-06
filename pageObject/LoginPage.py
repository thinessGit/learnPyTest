class LoginPage:
    txtUsernameId = "//input[@id='Email']"
    txtPasswordId = "//input[@id='Password']"
    btnSubmit = "//button[@type='submit' and contains(text(),'Log in')]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.txtUsernameId).clear()
        self.driver.find_element_by_xpath(self.txtUsernameId).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPasswordId).clear()
        self.driver.find_element_by_xpath(self.txtPasswordId).send_keys(password)

    def clickSubmit(self):
        self.driver.find_element_by_xpath(self.btnSubmit).click()

