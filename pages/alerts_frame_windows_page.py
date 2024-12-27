import time
import allure
from faker.generator import random
from websocket import frame_buffer

from generator.generator import generated_person
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertPageLocators, FramePageLocators, \
    NestedFramesPageLocators
from pages.base_page import BasePage
import logging


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step('Check opened new tab')
    def check_opened_new_tab(self):
        logging.debug('Start searching elements on the page')
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        logging.debug('The allert button has been clicked')
        self.switch_to_window_custom_tab(1)  # написал свой метод в BasePage 0 = первая вкладка, 1 = вторая вкладка итд
        text_title = self.element_is_present(self.locators.TITLE_NEW_TAB).text
        logging.debug('The allert tab text has been pased')
        current_url = self.get_url_current_page()
        print(current_url)
        return text_title, current_url

    @allure.step('Check opened new window')
    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.switch_to_window_custom_tab(1)
        text_title = self.element_is_present(self.locators.TITLE_NEW_TAB).text
        current_url = self.get_url_current_page()
        print(current_url)
        return text_title, current_url

class AlertsPage(BasePage):
    locators = AlertPageLocators()

    @allure.step('Check see alert')
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        # alert = self.driver.switch_to.alert   # это голая функция ниже написал через BasePage
        alert = self.switch_to_alert_window()
        text = alert.text
        alert.accept()    # это метода для закрытия окна аллерта, так как скрин шот не делается и дает ошибку
        return text

    @allure.step('Check see alert after 5 second')
    def check_see_after_5sec(self):
        self.remove_footer()
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(6)
        alert = self.switch_to_alert_window()
        text = alert.text
        alert.accept()    # это метода для закрытия окна аллерта, так как скрин шот не делается и дает ошибку
        return text

    @allure.step('Check confirm alert')
    def check_confirm_alert(self):
        self.remove_footer()
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert_window()
        text_alert = alert_window.text
        random_choice_from_methods = [alert_window.accept,alert_window.dismiss]
        random.choice(random_choice_from_methods)()
        text_answer = self.element_is_visible(self.locators.CONFIRM_RESULT).text
        # print(text_alert)
        # print(text_answer)
        return text_alert, text_answer

    @allure.step('Check prompt alert')
    def check_prompt_alert(self):
        generator = next(generated_person())
        generate_text = generator.first_name
        self.remove_footer()
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert_window()
        alert_window.send_keys(generate_text)
        alert_window.accept()
        text_answer = self.element_is_visible(self.locators.PROMPT_RESULT).text
        return  generate_text, text_answer

class FramePage(BasePage):
    locators = FramePageLocators()

    @allure.step('Check Frame 1')
    def check_frame1(self):
        self.remove_footer()
        frame = self.element_is_present(self.locators.FIRST_FRAME)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.switch_to_frame(frame)
        text_frame = self.element_is_present(self.locators.TEXT_FIRST_FRAME).text
        return width, height, text_frame

    @allure.step('Check Frame 2')
    def check_frame2(self):
        self.remove_footer()
        frame = self.element_is_present(self.locators.SECOND_FRAME)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.switch_to_frame(frame)
        text_frame = self.element_is_present(self.locators.TEXT_SECOND_FRAME).text
        return width, height, text_frame

class NestedFramePage(BasePage):
    locators = NestedFramesPageLocators()

    @allure.step('Check Nested Frames')
    def check_nested_frames(self):
        self.remove_footer()
        frame_1 = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_to_frame(frame_1)
        text_frame_1 = self.element_is_present(self.locators.PARENT_TEXT).text
        frame_2 = self.element_is_present(self.locators.CHILD_FRAME)
        self.switch_to_frame(frame_2)
        text_frame_2 = self.element_is_present(self.locators.CHILD_TEXT).text
        return text_frame_1, text_frame_2












