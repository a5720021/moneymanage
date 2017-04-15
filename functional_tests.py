from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Somchai heard about money management web app.. he want to try. first
        #he go to it's homepage.
        self.browser.get('http://localhost:8000')

        #First thing he saw is title.The title name is "Money management".
        title_text = self.browser.find_element_by_tag_name('title').text
        self.assertIn('Money Management', title_text)
        self.fail('Finish the test!')

        #He interest about "Manage your saving" and he try to click this.

        #He go to new url. This is "Saving Management"

        #He try to fill his income and outcome then he submit.

        #He saw history about his saving. an he come back to home page.

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
