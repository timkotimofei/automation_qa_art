import time
import allure
import pytest
from faker.generator import random

from data.urls import Urls
from pages.widgets_page import AccordianPage, AutoCompletePage


@allure.suite("Widgets")
class TestWidgets:
    @allure.feature("Accordian")
    class TestAccordianPage:

        @pytest.mark.regression
        @allure.title("Check accordian first, second, third")
        def test_accordian(self, driver):
            """
            Steps:
            1. Open the page 'https://demoqa.com/accordian'
            2. Verify first title text
            3. Click the first title
            4. Verify first content text
            5. Verify second title text
            6. Click the second title
            7. Verify second content text
            8. Verify third title text
            9. Click the third title
            10. Verify third content text
            """
            accordian_page = AccordianPage(driver, Urls.Web.ACCORDIAN)
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?', 'The first title does not match'
            assert 'Lorem Ipsum' in first_content, 'The first content does not match'
            assert second_title == 'Where does it come from?', 'The second title does not match'
            assert 'Lorem Ipsum' in second_content, 'The second content does not match'
            assert third_title == 'Why do we use it?', 'The third title does not match'
            assert 'Lorem Ipsum' in third_content, 'The third content does not match'


        @pytest.mark.regression
        @allure.title("Check is accordian only one open at the time")
        def test_accordian_one_close_another_open(self, driver):
            """
            Steps:
            1. Open the page 'https://demoqa.com/accordian'
            2. Verify first accordian element is open
            3. Verify second and third accordian elements are close (True, False, False)
            4. Click first accordian element
            5. Verify first and second and third accordian elements are close (False, False, False)
            6. Click second accordian element
            7. Verify first and third accordian elements are close (False, True, False)
            8. Click third accordian element
            9. Verify first and third accordian elements are close (False, False, True)

            """
            accordian_page = AccordianPage(driver, Urls.Web.ACCORDIAN)
            accordian_page.open()
            first_opened = accordian_page.check_which_accordian_open_close()
            accordian_page.click_custom_accordian_element('first')
            time.sleep(1)
            after_click = accordian_page.check_which_accordian_open_close()
            assert first_opened == (True, False, False), 'First not open'
            assert after_click == (False, False, False), 'All not closed, someone is open'

            accordian_page.click_custom_accordian_element('second')
            time.sleep(1)
            after_click = accordian_page.check_which_accordian_open_close()
            assert after_click == (False, True, False), 'Second is not opened'

            accordian_page.click_custom_accordian_element('third')
            time.sleep(1)
            after_click = accordian_page.check_which_accordian_open_close()
            assert after_click == (False, False, True), 'Third is not opened'


    @allure.feature('Autocomplete page')
    class TestAutoCompletePage:

        @pytest.mark.regression
        @allure.title("Check autocomplete is filled_1")
        def test_fill_multi_autocomplete1(self, driver):
            autocomplete_page = AutoCompletePage(driver, Urls.Web.AUTO_COMPLETE)
            autocomplete_page.open()
            colors_send = autocomplete_page.send_data_in_autocomplete_field()
            colors_in_field = autocomplete_page.check_color_in_multi()
            # print(colors_send)
            # print(colors_in_field)
            assert  colors_in_field == colors_send, 'The colors in field does not match sended colors'
            time.sleep(3)


        @pytest.mark.regression
        @allure.title("Check autocomplete is filled_2")
        def test_fill_multi_autocomplete2(self, driver):
            autocomplete_page = AutoCompletePage(driver, Urls.Web.AUTO_COMPLETE)
            autocomplete_page.open()
            col_send = autocomplete_page.send_data_in_autocomplete_filed_2(random.randint(1,10))
            col_from_field = autocomplete_page.check_color_in_multi()
            # print(col_send)
            # print(col_from_field)
            assert col_send == col_from_field, 'The colors in field does not match sended colors'


        @pytest.mark.regression
        @allure.title("Check delete one item from autocomplete field")
        def test_delete_some_from_field(self, driver):
            autocomplete_page = AutoCompletePage(driver, Urls.Web.AUTO_COMPLETE)
            autocomplete_page.open()
            col_send = autocomplete_page.send_data_in_autocomplete_filed_2(random.randint(1, 10))
            before_col_from_field = autocomplete_page.check_color_in_multi()
            autocomplete_page.remove_value_from_multi()
            after_col_from_field = autocomplete_page.check_color_in_multi()
            # print(col_send)
            # print(before_col_from_field)
            # print(after_col_from_field)
            assert col_send == before_col_from_field , 'The send colors does not match with typed colors'
            assert len(col_send) - 1 == len(after_col_from_field), 'The color was not delete'

        @pytest.mark.regression
        @allure.title("Check delete all items from autocomplete field")
        def test_delete_all_items(self, driver):
            autocomplete_page = AutoCompletePage(driver, Urls.Web.AUTO_COMPLETE)
            autocomplete_page.open()
            col_send = autocomplete_page.send_data_in_autocomplete_filed_2(random.randint(1, 10))
            before_col_from_field = autocomplete_page.check_color_in_multi()
            autocomplete_page.remove_all_values_multu()
            after_col_form_field = autocomplete_page.check_the_color_multi_field_is_empty()
            print(col_send)
            print(before_col_from_field)
            print(after_col_form_field)
            assert col_send == before_col_from_field, 'The multi color field filled succes'
            assert after_col_form_field == True, 'The multi color field is not empty after delete'

















