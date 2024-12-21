import time
import allure
import pytest
from selenium.webdriver.support.expected_conditions import alert_is_present

from conftest import driver
from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramePage
import logging

@allure.suite("Alert Frame Window")
class TestAlertsFrameWindow:
    @allure.feature("Browser Window")
    class TestBrowserWindow:

        @pytest.mark.regression
        @allure.title("New Tab")
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            logging.debug('Start click to alert button')
            text_new_tab_title, current_url = new_tab_page.check_opened_new_tab()
            logging.debug('The alert button has been clicked')
            time.sleep(1)
            assert text_new_tab_title == 'This is a sample page', 'The title text from new tab does not match'
            assert current_url == 'https://demoqa.com/sample', 'The current tab url does not match'

        @pytest.mark.regression
        @allure.title("New Window")
        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            text_new_tab_title, current_url = new_window_page.check_opened_new_tab()
            time.sleep(1)
            assert text_new_tab_title == 'This is a sample page', 'The title text from new tab does not match'
            assert current_url == 'https://demoqa.com/sample', 'The current tab url does not match'

    @allure.feature("Alert Page")
    class TestAlertPage:

        @pytest.mark.regression
        @allure.title("See Alert")
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text_alert = alert_page.check_see_alert()
            assert text_alert == 'You clicked a button', 'The message does not match'

        @pytest.mark.regression
        @allure.title("See Alert")
        def test_see_afet_5sec_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text_alert = alert_page.check_see_after_5sec()
            print(text_alert)
            assert text_alert == 'This alert appeared after 5 seconds', 'The message does not match'

        @pytest.mark.regression
        @allure.title("Confirm Alert")
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text_alert, text_answer  = alert_page.check_confirm_alert()
            assert text_answer == 'You selected Ok' or 'You selected Cancel'


        @pytest.mark.regression
        @allure.title("Prompt Alert")
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text_input, answer_prompt_alert = alert_page.check_prompt_alert()
            assert text_input in answer_prompt_alert


    @allure.feature("Frame Page")
    class TestFramePage:

        def test_frames(self, driver):
            frame_page = FramePage(driver, 'https://demoqa.com/frames')
            frame_page.open()

