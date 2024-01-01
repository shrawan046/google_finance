import time

import pytest
from selenium import webdriver
from pagesObjects.MarketsPage import Market
from pagesObjects import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_002_Market:
    baseURL = ReadConfig.getAppURL()
    input = ReadConfig.variable()
    logger = LogGen.loggen()

    @pytest.mark.smoke
    def test_click_on_mainMenu(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.market_obj = Market(self.driver)
        self.market_obj.click_on_mainMenu()
        act_title = self.driver.title
        print(act_title)
        self.driver.close()

    @pytest.mark.smoke
    def test_click_on_most_active(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.most_active_obj = Market(self.driver)
        self.most_active_obj.click_on_mainMenu()
        self.most_active_obj.verify_mostActive()
        self.driver.close()

    def test_currencies(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.currency_obj = Market(self.driver)
        self.currency_obj.click_on_mainMenu()
        self.currency_obj.verify_currencies()
        self.driver.close()

    def test_gainers(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.gainers_obj = Market(self.driver)
        self.gainers_obj.click_on_mainMenu()
        self.gainers_obj.verify_gainers()
        self.driver.close()

    def test_crypto(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.crypto_obj = Market(self.driver)
        self.crypto_obj.click_on_mainMenu()
        self.crypto_obj.verify_crypto()
        self.driver.close()
