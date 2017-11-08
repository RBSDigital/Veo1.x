import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
from time import sleep

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators for the RetailerID
    _login_link = "//*[@id='content']/div[2]/div[3]/ul/li[1]/a"
    # _login_link = "Login do varejista"
    _retailerID_field = "retailer-store-number"
    _password_field = "retailer-password"
    _terms_conditions = "ageCheckboxRetailer"
    # _terms_conditions = 'html/body/div[2]/div[1]/div[1]/div[3]/section/div[2]/div[4]/div[1]/form/div[4]/div/label/input'
    _login_button = "//*[@id='retailer-login-button']"
    _user_settings_icon = "my-account-menu"
    _user_settings_icon_menu = "//div[2]/nav/ul/li[3]/a"


    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, retailerID):
        self.sendKeys(retailerID, self._retailerID_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def setTermsandConditions(self):
        self.elementClick(self._terms_conditions, locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, retailerID="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(retailerID)
        self.enterPassword(password)
        # sleep(3)
        self.setTermsandConditions()
        tandc = self.getElement(locator=self._terms_conditions)
        if(not tandc.is_selected()):
            tandc.click()

        # sleep(3)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.waitForElement("//*[@id='main-search']",
                            locatorType="xpath")
        result = self.isElementPresent(locator='//*[@id="main-search"]',
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator="//*[@id='retailer-login-button']",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Página Inicial")

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="//div[2]/nav/ul/li[3]/a",
                          locatorType="xpath", pollFrequency=1)
        self.elementClick(locator="//div[2]/nav/ul/li[3]/a",
                          locatorType="xpath")

    def clearFields(self):
        retailerIDField = self.getElement(locator=self._retailerID_field)
        retailerIDField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()
        tandc = self.getElement(locator=self._terms_conditions)
        if(tandc.is_selected()):
            tandc.click()