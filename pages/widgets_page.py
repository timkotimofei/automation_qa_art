import time
import random
from os import remove

import allure
from selenium.webdriver import Keys

from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage
from generator.generator import generate_color, true_generator_color


class AccordianPage(BasePage):

    locators = AccordianPageLocators()

    accordian = {'first':
                     {'title': locators.SECTION_FIRST,
                      'content': locators.SECTION_CONTENT_FIRST},
                 'second':
                     {'title': locators.SECTION_SECOND,
                      'content': locators.SECTION_CONTENT_SECOND},
                 'third':
                     {'title': locators.SECTION_THIRD,
                      'content': locators.SECTION_CONTENT_THIRD}
                 }

    @allure.step('Check Accordian Elements')
    def check_accordian(self, accordian_num):
        section_title = self.element_is_visible_with_go_to_element(self.accordian[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(self.accordian[accordian_num]['content']).text
        return section_title.text, section_content

    @allure.step('Is accordian only one open at the time')
    def check_which_accordian_open_close(self):
        first = self.element_is_present(self.accordian['first']['content']).is_displayed()
        second = self.element_is_present(self.accordian['second']['content']).is_displayed()
        third = self.element_is_present(self.accordian['third']['content']).is_displayed()
        return first, second, third

    @allure.step('Click custom accordian element')
    def click_custom_accordian_element(self, accordian_num):
        self.element_is_visible_with_go_to_element(self.accordian[accordian_num]['title']).click()


class AutoCompletePage(BasePage):

    locators = AutoCompletePageLocators()

    def send_data_in_autocomplete_field(self):
        autocomplete = self.element_is_visible(self.locators.MULTI_INPUT)
        colors = {generate_color() for i in range(random.randint(1,8))}
        for i in colors:
            autocomplete.send_keys(i)
            time.sleep(1)
            autocomplete.send_keys(Keys.ENTER)
        return list(colors)

    def send_data_in_autocomplete_filed_2(self, n):
        autocomplete = self.element_is_visible(self.locators.MULTI_INPUT)
        colors = true_generator_color(n)
        list_for_check_in = []
        for i in range(1, n+1):
            value_color = next(colors)
            autocomplete.send_keys(value_color)
            list_for_check_in.append(value_color)
            time.sleep(1)
            autocomplete.send_keys(Keys.ENTER)
        return list_for_check_in

    def remove_value_from_multi(self):
        remove_buttons = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        remove_buttons[1].click()

    def check_color_in_multi(self):
        multi_value = self.elements_are_visible(self.locators.MULTI_VALUE)
        multi_value_text = [i.text for i in multi_value]
        return multi_value_text

    def remove_all_values_multu(self):
        remove_all = self.element_is_visible(self.locators.MULTI_VALUE_REMOVE_ALL)
        remove_all.click()




