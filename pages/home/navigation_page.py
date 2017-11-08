import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Veo Locators & methods
    _leftHandMainMenu = "//*[@id='my-account-menu']"
    _leftHandMenuItemMyaccout = "//div[2]/nav/ul/li[1]/a"
    _leftHandMenuItemOrderhistory = "//div[2]/nav/ul/li[2]/a"
    _logout = "//div[2]/nav/ul/li[3]/a"

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._leftHandMainMenu,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(locator=self._leftHandMainMenu,
                          locatorType="xpath")

    def navigateToUserLmainMenuLogout(self):
        userSettingsElement = self.waitForElement(locator=self._leftHandMainMenu,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(locator=self._logout,
                          locatorType="xpath")

    def navigateToUserLmainMenuMyaccount(self):
        userSettingsElement = self.waitForElement(locator=self._leftHandMainMenu,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(locator=self._leftHandMenuItemMyaccout,
                          locatorType="xpath")

    def navigateToUserLmainMenuOrderhistory(self):
        userSettingsElement = self.waitForElement(locator=self._leftHandMainMenu,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(locator=self._leftHandMenuItemOrderhistory,
                          locatorType="xpath")