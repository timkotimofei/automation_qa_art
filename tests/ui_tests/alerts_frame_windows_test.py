import time
import allure
import pytest
from data.urls import Urls
from conftest import driver
from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramePage, NestedFramePage, ModalDialogsPage
import logging

@allure.suite("Alert Frame Window")
class TestAlertsFrameWindow:
    @allure.feature("Browser Window")
    class TestBrowserWindow:

        @pytest.mark.regression
        @allure.title("New Tab")
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, f'{Urls.Web.BROWSER_WINDOWS}')
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
            new_window_page = BrowserWindowsPage(driver, f'{Urls.Web.BROWSER_WINDOWS}')
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
            alert_page = AlertsPage(driver, f'{Urls.Web.ALERTS}')
            alert_page.open()
            text_alert = alert_page.check_see_alert()
            assert text_alert == 'You clicked a button', 'The message does not match'

        @pytest.mark.regression
        @allure.title("See Alert")
        def test_see_afet_5sec_alert(self, driver):
            alert_page = AlertsPage(driver, f'{Urls.Web.ALERTS}')
            alert_page.open()
            text_alert = alert_page.check_see_after_5sec()
            print(text_alert)
            assert text_alert == 'This alert appeared after 5 seconds', 'The message does not match'

        @pytest.mark.regression
        @allure.title("Confirm Alert")
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, f'{Urls.Web.ALERTS}')
            alert_page.open()
            text_alert, text_answer  = alert_page.check_confirm_alert()
            assert text_answer == 'You selected Ok' or 'You selected Cancel'


        @pytest.mark.regression
        @allure.title("Prompt Alert")
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, f'{Urls.Web.ALERTS}')
            alert_page.open()
            text_input, answer_prompt_alert = alert_page.check_prompt_alert()
            assert text_input in answer_prompt_alert


    @allure.feature("Frame Page")
    class TestFramePage:

        @pytest.mark.regression
        @allure.title("Test First Big Frame")
        def test_big_frame(self, driver):
            frame_page = FramePage(driver, f'{Urls.Web.FRAMES}')
            frame_page.open()
            width, height, text_frame = frame_page.check_frame1()
            assert width == '500px', 'The value of width does not match'
            assert height == '350px', 'The value of height does not match'
            assert text_frame == 'This is a sample page', 'The text message does not match'

        @pytest.mark.regression
        @allure.title("Test Second Little Frame")
        def test_little_frame(self, driver):
            frame_page = FramePage(driver, f'{Urls.Web.FRAMES}')
            frame_page.open()
            width, height, text_frame = frame_page.check_frame2()
            assert width == '100px', 'The value of width does not match'
            assert height == '100px', 'The value of height does not match'
            assert text_frame == 'This is a sample page', 'The text message does not match'

    @allure.feature("Nested Page")
    class TestNestedPage:

        @pytest.mark.regression
        @allure.title("Test Nested Frames")
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramePage(driver, f'{Urls.Web.NESTED_FRAMES}')
            nested_frame_page.open()
            text_parent, text_child = nested_frame_page.check_nested_frames()
            assert text_parent == 'Parent frame', 'Parent frame text does not exist'
            assert  text_child == 'Child Iframe', 'Child frame text does not exist'

    @allure.feature("Modal Dialogs")
    class TestModalDialogsPage:

        @pytest.mark.regression
        @allure.title("Test Small Modal Dialogs")
        def test_small_modal_dialogs(self, driver):
            """
            Steps:
            1. Open the page 'https://demoqa.com/modal-dialogs'
            2. Click the button "Small Modal"
            3. Verify title text
            4. Verify content modal text
            5. Click the exit "x" button
            6. Repeat step 2
            7. Click the "Close" button
            8. Repeat step 2
            9. Click outside the modal (modal-overlay)
            """
            modal_dialogs_page = ModalDialogsPage(driver, f"{Urls.Web.MODAL_DIALOGS}")
            modal_dialogs_page.open()
            title_small_text, body_small_text = modal_dialogs_page.check_small_modal_dialogs()
            assert title_small_text == 'Small Modal', 'Title does not match'
            assert body_small_text == 'This is a small modal. It has very less content', 'Text content Small Modal does not match'


        @pytest.mark.regression
        @allure.title("Test Large Modal Dialogs")
        def test_large_modal_dialogs(self, driver):
            """
            Steps:
            1. Open the page 'https://demoqa.com/modal-dialogs'
            2. Click the button "Large Modal"
            3. Verify title text
            4. Verify content modal text
            5. Click the exit "x" button
            6. Repeat step 2
            7. Click the "Close" button
            8. Repeat step 2
            9. Click outside the modal (modal-overlay)
            """
            modal_dialogs_page = ModalDialogsPage(driver, f"{Urls.Web.MODAL_DIALOGS}")
            modal_dialogs_page.open()
            title_large_text, body_large_text = modal_dialogs_page.check_large_modal_dialogs()
            assert title_large_text == 'Large Modal', 'Title does not match'
            assert len(body_large_text) == 574, 'Text content Large Modal does not match'







