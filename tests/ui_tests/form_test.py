import time
import allure
import pytest
from pages.form_page import FormPage
from conftest import driver

@allure.suite("Test Form")
class TestForm:
    @allure.feature("Test Form Page")
    class TestFormPage:

        @pytest.mark.regression
        @allure.title("Test form")
        def test_form(self, driver):
            """
            Шаги:
            1. Open the page 'https://demoqa.com/automation-practice-form'
            2. Wait until page loading
            3. Generate testing data
            4. Fill the fields by the generated test data
            5. Click the button Submit
            6. Validate result table by parse text
            """
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


