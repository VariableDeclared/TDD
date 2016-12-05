from selenium import webdriver
import unittest

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'To-Do' in browser.title

browser.quit()

class NewVisitorTEst(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start__a_list_and_retrieve_it_later(self):
        #editth has heard about a cool new online t-do app She Goes
        # to check out it's homepage
        self.browser.get('http://localhost:8000')

        # She notices the page tutle and heard ention to-do lists
        self.assertIn('To-Do', self.brwoser.title)
        self.fail('Finish the test!')

        #She is invited to enter a to-do item straight away

if __name__ == '__main__':
    unittest.main(warnings='ignore')