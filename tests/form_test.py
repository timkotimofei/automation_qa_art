import time

from pages.form_page import FormPage
from conftest import driver

class TestForm:

    class TestFormPage:

        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            file_name, subject, address, person_info = form_page.fill_form_fields()
            result = form_page.form_result()
            print(person_info)
            print(result)
            assert result[7] in file_name, 'The file name does not match'
            assert person_info.email in result, 'The mail does not match'
            assert subject in result, 'The subject does not match'
            assert person_info.current_address in result, 'Current address does not match'
            assert person_info.mobile[0:10] in result, 'The telephone number does not match'


