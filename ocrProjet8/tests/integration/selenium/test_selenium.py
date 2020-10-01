from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


class SeleniumBasedTestCase(LiveServerTestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='test1',
            password='test1@1234'
        )
        caps = DesiredCapabilities().FIREFOX.copy()
        caps['marionette'] = True
        self.driver = webdriver.Firefox(
            capabilities=caps,
            firefox_binary='/Applications/Applications/Firefox.app/Contents'
                           '/MacOS/firefox-bin',

        )

    def test_save_favorite(self):

        self.driver.get('http://127.0.0.1:8000/accounts/login')

        # login
        self.driver.find_element_by_id('id_login').send_keys('test1')
        self.driver.find_element_by_id('id_password').send_keys('test1@1234')
        self.driver.find_element_by_id('login-button').click()

        # go to home page
        self.driver.find_element_by_id('pur-beurre').click()

        self.assertEqual(self.driver.title, 'Pur beurre')
        # select search form
        self.driver.find_element_by_class_name('select2-selection').click()

        # search for a product
        self.driver.find_element_by_class_name(
            'select2-search__field'
        ).send_keys(Keys.ENTER)

        # click on "chercher" button
        self.driver.find_element_by_id('search-button').click()

        self.assertEqual(self.driver.title, 'Résultats')

        # save first product
        self.driver.find_element_by_xpath('//figure/form/button').click()

        # go to favorites
        self.driver.find_element_by_id('carrot-logo').click()

        self.assertEqual(self.driver.title, 'Favoris')

        self.driver.close()
