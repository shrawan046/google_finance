import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Market:
    main_menu_xpath = "//div[@aria-label='Main menu']//*[name()='svg']"
    market_trends_xpath = "//div[@class='jjm4k'][normalize-space()='Market trends']"
    market_indexes_tab_xpath = ("//c-wiz[@class='zQTmif SSPGKf rU0AKc']//div//a[@class='GqNdIe GqNdIe-YySNWc']"
                                "[normalize-space()='Market indexes']")
    most_active_tab_xpath = ("//c-wiz[@class='zQTmif SSPGKf rU0AKc']//div//a[contains(@class,'GqNdIe')]"
                             "[normalize-space()='Most active']")
    most_active_text_xpath = ("//c-wiz[@class='zQTmif SSPGKf rU0AKc']//span[@class='LzRWEc']"
                              "[normalize-space()='Most active']")
    gainers_tab_xpath = ("//c-wiz[@class='zQTmif SSPGKf rU0AKc']//div//a[contains(@class,'GqNdIe')]"
                         "[normalize-space()='Gainers']")
    gainers_text_xpath = ("//c-wiz[@class='zQTmif SSPGKf rU0AKc']//span[@class='LzRWEc']"
                          "[normalize-space()='Gainers']")
    losers_tab_xpath = ("//c-wiz[@class='zQTmif SSPGKf rU0AKc']//div//a[contains(@class,'GqNdIe')]"
                        "[normalize-space()='Losers']")
    losers_text_xpath = "//span[normalize-space()='Losers']"
    climate_leaders_tab_xpath = ("//c-wiz[@class='zQTmif SSPGKf rU0AKc']//div//a[contains(@class,'GqNdIe')]"
                                 "[normalize-space()='Climate leaders']")
    climate_leaders_text_xpath = "//span[normalize-space()='Climate leaders']"
    crypto_tab_xpath = ("//c-wiz[@class='zQTmif SSPGKf rU0AKc']//div//a[contains(@class,'GqNdIe')]"
                        "[normalize-space()='Crypto']")
    crypto_text_xpath = "//span[normalize-space()='Cryptocurrency']"
    currencies_tab_xpath = ("//c-wiz[@class='zQTmif SSPGKf rU0AKc']//div//a[contains(@class,'GqNdIe')]"
                            "[normalize-space()='Currencies']")
    local_currencies_text_xpath = "//span[normalize-space()='Local']"
    global_currencies_text_xpath = "//span[normalize-space()='Global']"
    market_trends_grid_xpath = "//c-wiz[@class='zQTmif SSPGKf rU0AKc']//div[@class='ZuWnOb']//div//div[@role='tablist']"
    share_button_xpath = "//span[normalize-space()='Share']"
    Americas_title_xpath = "//span[@class='r6XbWb']"
    local_currency_grid_xpath = "//div[@role='main']//div[1]//ul[1]//li[1]//a[1]//div[1]//div[1]//div[1]//div[2]//div[1]"
    local_currency_list_xpath = "//div[2]//ul[1]"
    inr_currency_Xpath = "//div[contains(text(),'INR / JPY')]"
    inr_chat_text_xpath = "//div[@class='zzDege']"
    compare_to_search_xpath = "//span[normalize-space()='Compare to']"
    follow_button_xpath = "(//div[@class='ibi25b'])[1]"
    gmail_logo_xpath = "//div[@id='logo']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_mainMenu(self):
        self.driver.find_element(By.XPATH, self.main_menu_xpath).click()
        self.driver.find_element(By.XPATH, self.market_trends_xpath).click()
        americas_text = self.driver.find_element(By.XPATH, self.Americas_title_xpath)
        # print(americas_text.text)
        assert americas_text.is_displayed()

    def explore_market_trends(self):
        var = self.driver.find_element(By.XPATH, self.market_trends_grid_xpath).text
        for i in var:
            if i == "Gainers":
                self.driver.find_element(By.XPATH, self.gainers_tab_xpath).click()

    def verify_mostActive(self):
        self.driver.find_element(By.XPATH, self.most_active_tab_xpath).click()
        most_active_text = self.driver.find_element(By.XPATH, self.most_active_text_xpath)
        assert most_active_text.is_displayed()
        assert most_active_text.text == "Most active"

    def verify_gainers(self):
        self.driver.find_element(By.XPATH, self.gainers_tab_xpath).click()
        gainer_text = self.driver.find_element(By.XPATH, self.gainers_text_xpath)
        assert gainer_text.is_displayed()
        assert gainer_text.text == "Gainers"

    def verify_losers(self):
        self.driver.find_element(By.XPATH, self.losers_tab_xpath).click()
        losers_text = self.driver.find_element(By.XPATH, self.losers_text_xpath)
        assert losers_text.text == "Losers"

    def verify_climateLeader(self):
        self.driver.find_element(By.XPATH, self.climate_leaders_tab_xpath).click()
        climate_leaders_text = self.driver.find_element(By.XPATH, self.climate_leaders_text_xpath)
        assert climate_leaders_text.is_displayed()
        assert climate_leaders_text.text == "Climate leaders"

    def verify_crypto(self):
        self.driver.find_element(By.XPATH, self.crypto_tab_xpath).click()
        crypto_text = self.driver.find_element(By.XPATH, self.crypto_text_xpath)
        assert crypto_text.is_displayed()
        assert crypto_text.text == "Cryptocurrency"

    def verify_currencies(self):
        global inr_text, compare_to
        self.driver.find_element(By.XPATH, self.currencies_tab_xpath).click()
        currencies_local_text = self.driver.find_element(By.XPATH, self.local_currencies_text_xpath)
        currencies_global_text = self.driver.find_element(By.XPATH, self.global_currencies_text_xpath)
        assert currencies_local_text.is_displayed()
        assert currencies_global_text.is_displayed()
        assert currencies_local_text.text == "Local"
        if currencies_local_text.is_displayed():
            local_list = self.driver.find_element(By.XPATH, self.local_currency_list_xpath).text
            for currency in local_list:
                if currency == "INR / JPY":
                    self.driver.find_element(By.XPATH, self.inr_currency_Xpath).click()
                    inr_text = self.driver.find_element(By.XPATH, self.inr_chat_text_xpath)
                    compare_to = self.driver.find_element(By.XPATH, self.compare_to_search_xpath)
                assert inr_text.is_displayed()
                assert compare_to.is_displayed()

    def verify_follow(self):
        follow_button = self.driver.find_element(By.XPATH, self.follow_button_xpath)
        assert follow_button.is_displayed()
        gmail_logo = self.driver.find_element(By.XPATH, self.gmail_logo_xpath)
        gmail_get_url = self.driver.current_url
        print(gmail_get_url)
        assert gmail_logo.is_displayed()
