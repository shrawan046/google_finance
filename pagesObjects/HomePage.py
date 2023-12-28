import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Home:
    search_input_field_xpath = "//div[@class='L6J0Pc ZB3Ebc nz7KN']//div[@class='d1dlne']"
    local_market_tab_css = "c-wiz[class='zQTmif SSPGKf ccEnac'] div[class='Y4Oy5e'] div:nth-child(2)"
    world_markets_tab_css = "c-wiz[class='zQTmif SSPGKf ccEnac'] div[class='Y4Oy5e'] div:nth-child(3)"
    compare_markets_tab_xpath = "//span[@id='market-rundown-heading']"
    compare_markets_grid_xpath = "//c-wiz[@jsrenderer='FfFYBb']"
    home_page_grid_xpath = "//div[@class='UJweIb']//div[@role='tablist']"
    signin_button_xpath = "//span[@class='VfPpkd-vQzf8d'][normalize-space()='Sign in']"
    redirection_gmail_logo_xpath = "//div[@id='logo']"
    follow_button_xpath = "//div[@class='ibi25b']"
    share_button_xpath = "//span[normalize-space()='Share']"
    compare_grid_1d_xpath = "//button[@id='1dayTab']//span[@class='VfPpkd-YVzG2b']"
    compare_grid_max_xpath = "//button[@id='maxTab']//span[@class='VfPpkd-YVzG2b']"
    list_of_index_xpath = "//ul[@class='sbnBtf']"
    sbin_xpath = "(//div[contains(@class,'SxcTic')])[2]"
    itc_text_xpath = "//div[@role='heading'][normalize-space()='ITC Ltd']"
    airtel_text_xpath = "//div[normalize - space() = 'Airtel Africa PLC']"
    email_input_xpath= "//input[@id='identifierId']"
    create_account_xpath= "//span[normalize-space()='Create account']"
    share_popup_xpath= "//div[@class='VfPpkd-cnG4Wd']//section"
    facebook_button_xpath= "//button[@aria-label='Share to Facebook']"

    def __init__(self, driver):
        self.driver = driver

    def searchInput(self, search_input):
        search_string = self.driver.find_element(By.XPATH, self.search_input_field_xpath)
        time.sleep(5)
        act = ActionChains(self.driver).move_to_element(search_string).click(search_string)
        act.send_keys(search_input)
        act.send_keys(Keys.ENTER).perform()
        time.sleep(5)

    def search_stock_follow(self):
        click_follow = self.driver.find_element(By.XPATH, self.follow_button_xpath)
        ActionChains(self.driver).move_to_element(click_follow).click(click_follow).perform()

    def search_stock_share(self):
        click_share= self.driver.find_element(By.XPATH, self.share_button_xpath)
        ActionChains(self.driver).move_to_element(click_share).click(click_share).perform()
        #share_popup = self.driver.find_element(By.XPATH, self.share_popup_xpath)
       # ActionChains(self.driver).move_to_element(share_popup).perform()

    def click_facebook(self):
        click_on_facebook=self.driver.find_element(By.XPATH, self.share_button_xpath)
        ActionChains(self.driver).move_to_element(click_on_facebook).click(click_on_facebook).perform()
        time.sleep(5)

    def verify_gmail_page(self):
        email_input = self.driver.find_element(By.XPATH, self.email_input_xpath)
        create_button= self.driver.find_element(By.XPATH, self.create_account_xpath)
        assert email_input.is_displayed()
        assert create_button.is_displayed()


    def localMarket(self):
        self.driver.find_element(By.CSS_SELECTOR, self.local_market_tab_css).click()


    def signIn(self):
        self.driver.find_element(By.XPATH, self.signin_button_xpath).click()

    def compareMarkets(self):
        self.driver.find_element(By.XPATH, self.compare_markets_tab_xpath).click()
        grid = self.driver.find_element(By.XPATH, self.compare_markets_grid_xpath)
        assert grid.is_displayed()
        compare_days_1d = self.driver.find_element(By.XPATH, self.compare_grid_1d_xpath)
        assert compare_days_1d.is_displayed()
        self.driver.find_element(By.XPATH, self.compare_grid_max_xpath).click()

    def you_may_be_interested_in(self):
        index_list = self.driver.find_element(By.XPATH, self.list_of_index_xpath).text
        if "ITC Ltd" in index_list:
            self.driver.find_element(By.XPATH, self.list_of_index_xpath).click()
            itc_text = self.driver.find_element(By.XPATH, self.itc_text_xpath)
            assert itc_text.is_displayed()
