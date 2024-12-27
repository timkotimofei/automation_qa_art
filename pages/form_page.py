import os
import time
from time import sleep
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from generator.generator import generated_person, generated_file, generate_subject, generate_state, generate_city
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    @allure.step('Fill form fields')
    def fill_form_fields(self):
        with allure.step('Generate data'):
            person = next(generated_person())
            file_name, path = generated_file()
            subject = generate_subject()
            first_name = person.first_name
            last_name = person.last_name
            email = person.email
            mobile = person.mobile
            address = person.current_address
            state = generate_state()
            city = generate_city(state)
        with allure.step('Remove footer'):
            self.remove_footer()
        with allure.step('Filling all fields'):
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.GENDER).click()
            self.element_is_visible(self.locators.MOBILE).send_keys(mobile)
            self.element_is_visible(self.locators.DATE_OF_BIRTH).click()
            self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(Keys.RETURN)
        # # #--------------------------------------------------------
        # ActionChains(self.driver).send_keys(subject).perform()       # смог взаимодействовать с полем subject только
        # ActionChains(self.driver).send_keys(Keys.RETURN).perform()   # через ActionChains (это через экран)
        # # 	1.	ActionChains: Эта библиотека отправляет действия напрямую в окно браузера, а не на конкретный элемент,
        # # 	что позволяет обойти некоторые ограничения.
        # # 	2.	Независимость от элемента: Вы сначала кликаете, чтобы активировать элемент, а затем используете
        # # 	ActionChains, чтобы отправить текст как последовательность клавиш.
        # # --------------------------------------------------------
            self.go_to_element(self.element_is_present(self.locators.SUBJECT_ID))
            self.element_is_visible(self.locators.SUBJECT_ID).send_keys(f'{subject}')
            self.element_is_visible(self.locators.SUBJECT_ID).send_keys(Keys.RETURN)
            self.element_is_present(self.locators.HOBBIES).click()
            self.element_is_visible(self.locators.FILE_INPUT).send_keys(path)
            os.remove(path)  # удаляю, только что созданный файл
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(address)
            self.go_to_element(self.element_is_present(self.locators.STATE_INPUT))
            self.element_is_visible(self.locators.STATE_INPUT).send_keys(state)
            self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
            self.go_to_element(self.element_is_present(self.locators.CITY_INPUT))
            self.element_is_visible(self.locators.CITY_INPUT).send_keys(city)
            self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
            self.element_is_visible(self.locators.SUBMIT).click()
        return (file_name.split('/')), subject, address, person

    @allure.step('Form result')
    def form_result(self):
        with allure.step('Looking for table by locator'):
            table = self.elements_are_present(self.locators.TABLE_VALUES)
        data = []
        with allure.step('Parse text from result table'):
            for item in table:
                time.sleep(0.1)
                self.go_to_element(item)
                data.append(item.text)
        return data




