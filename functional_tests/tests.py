from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('saving_table')
        rows = table.find_elements_by_tag_name('td')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Somchai heard about money management web app.. he want to try. first
        #he go to it's homepage.
        self.browser.get(self.live_server_url)

        #First thing he saw is title.The title name is "Money management".
        title_home = self.browser.find_element_by_tag_name('title').text
        self.assertIn('Money Management', title_home)

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

        #He try to fill his income 17000$ about 'Money in banking' then he submit.
        sav_type = self.browser.find_element_by_id("id_type")
        sav_type.click()
        inputbox1 = self.browser.find_element_by_id('id_val')
        inputbox1.send_keys('5000')
        inputbox2 = self.browser.find_element_by_id('id_des')
        inputbox2.send_keys('Won a lottery')
        self.browser.find_element_by_id("id_sub").click()
        time.sleep(5)

        #He saw history about his saving.
        self.check_for_row_in_list_table('Money in banking')
        self.check_for_row_in_list_table('Won a lottery')

        #and he come back to home page.
        self.browser.find_element_by_partial_link_text('Back').click()
        time.sleep(5)
        self.fail('Finish the test!')

        #he look at the pie chart about his money.

        #Next,he found chart about gold price,stock price and Deposit interests.

        #He interest about gold price.then he go to see gold price history.

        #He think gold is a bad way to invest.then he come back.

        #Next,he go to stock price page.

        #That's good he think the stock is a best way to invest.he go back to home page.

        #He go to see bank interests it's not a way to rich.

        #He found the  best way he want to invest.

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')
