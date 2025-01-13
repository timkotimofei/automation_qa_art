import allure
from locators.widgets_page_locators import AccordianPageLocators
from pages.base_page import BasePage


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



