import pytest
from selenium import webdriver
from pagesObjects.HomePage import Home
from pagesObjects import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Home:
    baseURL = ReadConfig.getAppURL()
    input = ReadConfig.variable()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("******Test_001_Home******")
        self.logger.info("******Verify url functionality******")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)
        self.driver.close()
        if act_title == "Google Finance - Stock Market Prices, Real-time Quotes & Business News":
            assert True
        else:
            assert False

    def test_search_follow(self, setup):
        self.logger.info("******Test_001_Home******")
        self.logger.info("******Verify search string functionality******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.follow = Home(self.driver)
        self.follow.searchInput(self.input)
        self.follow.search_stock_follow()
        self.follow.verify_gmail_page()
        self.driver.close()

    def test_search_share(self, setup):
        self.logger.info("******Test_001_Home******")
        self.logger.info("******Verify search string functionality******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.share = Home(self.driver)
        self.share.searchInput(self.input)
        self.share.search_stock_share()
        self.share.click_facebook()
        self.driver.close()

    """""
    def test_localMarket(self, setup):
        self.logger.info("******Test_001_Home******")
        self.logger.info("******Verify local markets functionality******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.market = Home(self.driver)
        self.market.localMarket()
        self.driver.close()   

    def test_signIn_Click(self,setup):
        self.logger.info("******Test_001_Home******")
        self.logger.info("******Verify signin click functionality******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.signin = Home(self.driver)
        self.signin.signIn()
        act_title_gmail= self.driver.title
        self.driver.close()
        if act_title_gmail == "Sign in - Google Accounts":
            assert True
        else:
            assert False 

    def test_compare_markets(self,setup):
        self.logger.info("******Test_001_Home******")
        self.logger.info("******Verify compare markets functionality******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.compare_market = Home(self.driver)
        self.compare_market.compareMarkets()
        self.driver.close()   

    def test_list_index(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.index = Home(self.driver)
        self.index.you_may_be_interested_in()   """""
