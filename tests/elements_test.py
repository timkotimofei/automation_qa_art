import time
from faulthandler import is_enabled
from random import randint

from conftest import driver
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadDownloadPage, DynamicPropertiesPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, 'The fullname does not match'
            assert email == output_email, 'The email does not match'
            assert current_address == output_cur_addr, 'The current address does not match'
            assert permanent_address == output_per_addr, 'The permanent address does not match'


    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver,'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_info()
            assert input_checkbox == output_result, 'Checkboxes have not been selected'


    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == "Yes", "'Yes' have not been selected"
            assert output_impressive == "Impressive", "'Impressive' have not been selected"
            assert output_no == "No", "'No' have not been selected"

    class  TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            # print(new_person)
            # print(table_result)
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[randint(0,5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            # print(key_word)
            # print(table_result)
            assert key_word in table_result, "the person was not found in the table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            # print(age)
            # print(row)
            assert  age in row, "the person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            time.sleep(3)
            text = web_table_page.check_deleted()
            # print(text)
            assert text == "No rows found"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], ("The numbers of rows in the table has not been changed or"
                                                       " has changed incorrectly")



    class TestButtonsPage:

        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            # print(double)
            # print(right)
            # print(click)
            assert double == 'You have done a double click', "The double click button was not pressed"
            assert right == 'You have done a right click', "The right click button was not pressed"
            assert click == 'You have done a dynamic click', "The dynamic click button was not pressed"


    class TestLinksPage:

        def test_simple_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_links('simple')
            print(href_link)
            print(current_url)
            assert href_link == current_url , 'The link is broken or URL is incorrect'

        def test_dynamic_link(self,driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_links('dynamic')
            # print(href_link)
            # print(current_url)
            assert href_link == current_url

        def test_created_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            text, code = links_page.created_link('https://demoqa.com/created')
            # print(text)
            # print(code)
            assert '201' in text
            assert 201 == code


        def test_bad_request_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            text, code = links_page.bad_request_link('https://demoqa.com/bad-request')
            # print(text)
            # print(code)
            assert '400' in text
            assert 400 == code




    class TestUploadDownload:

        def test_upload_file(self,driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, file_name_result = upload_download_page.upload_file()
            assert file_name == file_name_result, 'The file has not been upload'


        def test_download_file(self, driver):
            download_file_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            download_file_page.open()
            check = download_file_page .download_file()
            assert check is True, 'The file has not been download'

    class TestDynamicPropertiesPage:

        def test_enable_button_after_5_second(self, driver):
            enable_button_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            enable_button_page.open()
            is_enabled = enable_button_page.check_enable_button()
            assert is_enabled is True, 'The button does not enabled after 5 sec'

        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_color()
            assert  color_before != color_after , 'The color does not changed'

        def test_the_button_is_appear(self, driver):
            appear_button = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            appear_button.open()
            is_appear = appear_button.check_appear_of_button()
            assert is_appear is True, 'The button does not appear after 5 seconds'















