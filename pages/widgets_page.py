import allure
from locators.widgets_page_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):

    locators = AccordianPageLocators()

    @allure.step('Check Small Modal Dialogs')
    def check_accordian(self, accordian_num):
        accordian = { 'first':
                          { 'title' : self.locators.SECTION_FIRST,
                            'content': self.locators.SECTION_CONTENT_FIRST},
                      'second':
                          {'title': self.locators.SECTION_SECOND,
                           'content': self.locators.SECTION_CONTENT_SECOND},
                      'third':
                          {'title': self.locators.SECTION_THIRD,
                           'content': self.locators.SECTION_CONTENT_THIRD}
                    }
        # self.remove_footer()
        section_title = self.element_is_visible_with_go_to_element(accordian[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return section_title.text, section_content

