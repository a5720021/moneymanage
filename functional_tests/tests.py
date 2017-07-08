from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import unittest
import time
from django.contrib.auth.models import User
from moneymanage.models import Sav_list,Gold_price,Stock,Bank

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        Gold_price.objects.create(buy_price=25000,sell_price='24000')
        Gold_price.objects.create(buy_price=24000,sell_price='23000')
        Stock.objects.create(name='TES',value=2400,change=5.2)
        Stock.objects.create(name='CPA',value=1500,change=-2.5)
        Bank.objects.create(name='Kasikorn',fixed_min=0.6,fixed_max=1.2,saving=0.5)
        Bank.objects.create(name='Krungsri',fixed_min=0.5,fixed_max=1.4,saving=0.6)
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,table_id,row_text):
        table = self.browser.find_element_by_id(table_id)
        rows = table.find_elements_by_tag_name('td')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Somchai heard about money management web app.. he want to try. first
        #he go to it's homepage.
        self.browser.get(self.live_server_url)
        time.sleep(2)

        #He register before log-in
        self.browser.find_element_by_partial_link_text('Create').click()
        time.sleep(2)
        login_name_create = self.browser.find_element_by_id('id_usr_reg')
        login_name_create.send_keys('test')
        password_login_create = self.browser.find_element_by_id('id_pw_reg')
        password_login_create.send_keys('Munggy44101')
        email = self.browser.find_element_by_id('id_email_reg')
        email.send_keys('mung@test.com')
        self.browser.find_element_by_id("id_sub_reg").click()
        time.sleep(2)
        self.browser.find_element_by_partial_link_text('Back').click()
        time.sleep(2)

        #He is logging in to moneymanagement homepage.
        login_name = self.browser.find_element_by_id('id_usr')
        login_name.send_keys('test')
        password_login = self.browser.find_element_by_id('id_pw')
        password_login.send_keys('Munggy44101')
        time.sleep(2)
        self.browser.find_element_by_id("id_sub").click()
        time.sleep(3)

        #First thing he saw is title.The title name is "Money management".
        title_home = self.browser.find_element_by_tag_name('title')
        self.assertIn('Money Management', title_home.text)

        #He interest about "Manage your saving" and he try to click this.
        link = self.browser.find_element_by_partial_link_text('Manage')
        self.assertIn('Manage your saving', link.text)
        link.click()
        time.sleep(3)

        #He go to new url. This is "Saving Management"
        title_sav = self.browser.find_element_by_tag_name('title').text
        self.assertIn('Saving Management', title_sav)

        #He try to fill his income 17000$ about 'Money in banking' then he submit.
        sav_type = self.browser.find_element_by_id("id_type")
        sav_type.click()
        inputbox1 = self.browser.find_element_by_id('id_val')
        inputbox1.send_keys('17000')
        inputbox2 = self.browser.find_element_by_id('id_des')
        inputbox2.send_keys('Money in banking')
        self.browser.find_element_by_id("id_sub").click()
        time.sleep(2)

        #He fill his outcome 10000$ about 'Buy a new mobile' then he submit.Again..
        sav_type = self.browser.find_element_by_id("id_type2")
        sav_type.click()
        inputbox1 = self.browser.find_element_by_id('id_val')
        inputbox1.send_keys('10000')
        inputbox2 = self.browser.find_element_by_id('id_des')
        inputbox2.send_keys('Buy a new mobile')
        self.browser.find_element_by_id("id_sub").click()
        time.sleep(2)

        #He think he won lottery amount 30000$
        sav_type = self.browser.find_element_by_id("id_type")
        sav_type.click()
        inputbox1 = self.browser.find_element_by_id('id_val')
        inputbox1.send_keys('30000')
        inputbox2 = self.browser.find_element_by_id('id_des')
        inputbox2.send_keys('Won lottery')
        self.browser.find_element_by_id("id_sub").click()
        time.sleep(2)

        #But he misunderstand and He's going to remove his saving about "won lottery"
        self.browser.find_element_by_id('3').click()
        time.sleep(2)

        #He saw history about his saving.
        self.check_for_row_in_list_table('saving_table','Money in banking')
        self.check_for_row_in_list_table('saving_table','Buy a new mobile')

        #and he come back to home page.
        self.browser.find_element_by_partial_link_text('Back').click()
        time.sleep(2)

        #he look at statistical(pie chart) about his money.
        #Next,he found chart about gold price,stock price and Deposit interests.
        #He interest about gold price.then he go to see gold price history.
        gold_page = self.browser.find_element_by_partial_link_text('View Gold')
        gold_page.click()
        time.sleep(2)

        #He's now in a Gold Price History Page.
        #He think gold is a bad way to invest.then he come back.
        table = self.browser.find_element_by_id('id_gold')
        rows = table.find_elements_by_tag_name('th')
        self.assertIn('Buy Price', [row.text for row in rows])
        self.browser.find_element_by_partial_link_text('Back').click()
        time.sleep(2)

        #Next,he go to stock price page.
        stock_page = self.browser.find_element_by_partial_link_text('View All Stock')
        stock_page.click()
        time.sleep(2)

        #That's good he think the stock is a best way to invest.he go back to home page.
        self.check_for_row_in_list_table('id_stock','TES')
        self.check_for_row_in_list_table('id_stock','CPA')
        self.browser.find_element_by_partial_link_text('Back').click()
        time.sleep(2)

        #He go to see bank interests it's not a way to rich.
        bank_page = self.browser.find_element_by_partial_link_text('View Bank')
        bank_page.click()

        #He found the  best way he want to invest and He close this app.
        time.sleep(5)
        self.fail('Finish the test!')


