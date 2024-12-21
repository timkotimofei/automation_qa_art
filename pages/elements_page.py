import base64
import os
import random
import time
import allure
import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBookPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadDownloadPageLocators, \
    DynamicPropertiesPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBookPageLocators()

    @allure.step('Fill all fields')
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.remove_footer()
        with allure.step('filling fields'):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step('click submit button'):
            self.elements_is_clickable(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step('Check filled form')
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address

class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    @allure.step('Open full list')
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('Click random items')
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)  #здесь будет храниться список всех элементов
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step('Get checked checkbox')
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)    # выбрали только с актив чекбоксом
        data = []
        for box in checked_list:
            title_item = box.find_element("xpath",self.locators.TITLE_ITEM) # внутри выбраных чекбоксов смотрим это
            data.append(title_item.text)
        return str(data).replace(' ','').replace('.doc','').lower()

    @allure.step('Get output result')
    def get_output_info(self):
        output_list = self.elements_are_present(self.locators.OUTPUT_ITEMS)
        data_output = []
        for item in output_list:
            data_output.append(item.text)
        return str(data_output).replace(' ','').lower()

class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step('Click on the radio button')
    def click_on_the_radio_button(self, choice):    #реализую с помощью словаря
        choices = {
            'yes': self.locators.YES_BUTTON,
            'impressive': self.locators.IMPRESSIVE_BUTTON,
            'no': self.locators.NO_BUTTON
        }
        with allure.step('Click the button'):
            self.element_is_visible(choices[choice]).click()

    @allure.step('Get output result')
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.step('Add new person')
    def add_new_person(self):
        count = random.randint(1,3) # чтобы всегда можно было менять кол-во добавляемых людей
        while count != 0:
            with allure.step('Generating testing data'):
                person_info = next(generated_person())
                first_name = person_info.first_name
                last_name = person_info.last_name
                email = person_info.email
                age = person_info.age
                salary = person_info.salary
                department = person_info.department
            with allure.step('Filling all field of testing data'):
                self.element_is_visible(self.locators.ADD_BUTTON).click()
                self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
                self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
                self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
                self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
                self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
                self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
                self.element_is_visible(self.locators.SUBMIT).click()
            time.sleep(1)
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step('Check added people')
    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for i in people_list:
            data.append(i.text.splitlines())
        return data

    @allure.step('Find some person')
    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('Check found person')
    def check_search_person(self):
        # Моя задача здесь найти строку, но их всего 10 в таблице отображается и есть пустые строки
        # Как найти непустые строки? Они содержат кнопку delete и значит по кнопке delete и находим
        # ищем ее а потом переходим к родительскому элементу т е  к строке
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath",self.locators.ROW_PARENT)
        return row.text.splitlines()


    @allure.step('Update person information')
    def update_person_info(self):
        with allure.step('Generate testing data'):
            person_info = next(generated_person())
            age = person_info.age
        with allure.step('Filling updates field'):
            self.remove_footer()
            self.element_is_visible(self.locators.UPDATE_BUTTON).click()
            self.element_is_visible(self.locators.AGE_INPUT).clear()
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    @allure.step('Delete person')
    def delete_person(self):
        self.remove_footer()
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('Check deleted person')
    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step('Select up to some row')
    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR,f"option[value='{x}']")).click()
            data.append(self.check_count_rows())
        return data

    @allure.step('Check count rows')
    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)




class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step('Check on different buttons')
    def click_on_different_button(self, type_click):
        if type_click == "double":
            with allure.step('Double click button'):
                self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)

        if type_click == "right":
            with allure.step('Right click button'):
                self.remove_footer()
                self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)

        if type_click == "click":
            with allure.step('Simple click button'):
                self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    @allure.step('Check clicked on the button')
    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text

class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step('Check link')
    def check_new_tab_links(self, type_link):
        self.remove_footer()
        if type_link == 'simple':
            with allure.step('Simple click link'):
                simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
            link_href = simple_link.get_attribute('href')
            request = requests.get(link_href)
            if request.status_code == 200:
                simple_link.click()
                self.driver.switch_to.window(self.driver.window_handles[1])
                url = self.driver.current_url
                return link_href, url
            else:
                return link_href, request.status_code

        if type_link == 'dynamic':
            with allure.step('Dynamic click link'):
                dynamic_link = self.element_is_visible(self.locators.DYNAMIC_LINK)
            link_href = dynamic_link.get_attribute('href')
            request = requests.get(link_href)
            if request.status_code == 200:
                dynamic_link.click()
                self.driver.switch_to.window(self.driver.window_handles[1])
                url = self.driver.current_url
                return link_href, url
            else:
                return link_href, request.status_code

    @allure.step('Created link')
    def created_link(self, url):
        self.remove_footer()
        with allure.step('Click created link'):
            created_link = self.element_is_present(self.locators.CREATED_LINK)
            created_link.click()
        with allure.step('Parse status code'):
            response_text = self.element_is_present(self.locators.RESPONSE_TEXT).text
            response_code = requests.get(url).status_code
        return response_text, response_code

    @allure.step('Bad requested link')
    def bad_request_link(self, url):
        self.remove_footer()
        with allure.step('Bad request link click'):
            bad_request_link = self.element_is_present(self.locators.BAD_REQUEST_LINK)
            bad_request_link.click()
        with allure.step('Bad request link response parse test'):
            response_text = self.element_is_present(self.locators.RESPONSE_TEXT).text
            response_code = requests.get(url).status_code
        return response_text, response_code


class UploadDownloadPage(BasePage):
    locators = UploadDownloadPageLocators()

    @allure.step('Upload file')
    def upload_file(self):
        with allure.step('Generate file and path data'):
            file_name, path = generated_file()
        with allure.step('Upload file with generated path and file'):
            self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)   # удаляем сразу же файл, чтобы не скапливался мусор
        text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        file_name = path.split('/')[-1]
        file_name_result = text.split('\\')[-1]
        return file_name, file_name_result

    @allure.step('Download file')
    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE_BUTTON).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'/Users/timofeitimko/PycharmProjects/automation_qa_art/filetest{random.randint(1,999)}.jpg'
        with open(path_name_file, 'wb+') as f:
           offset__= link_b.find(b'\xff\xd8')
           f.write(link_b[offset__:])
           check_file = os.path.exists(path_name_file)
        os.remove(path_name_file)
        return check_file



class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    @allure.step('Check enable button')
    def check_enable_button(self):
        try:
            enable_after_button = self.elements_is_clickable(self.locators.WILL_ENABLE_5_SECONDS_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step('Check changed color')
    def check_changed_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_before = color_button.value_of_css_property('color')
        time.sleep(6)
        color_after = color_button.value_of_css_property('color')
        return color_before, color_after

    @allure.step('Check appear of button')
    def check_appear_of_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_5_SECOND_BUTTON) # в basepage стоит 5 сек таймаут по дефолту
        except TimeoutException:
            return False
        return True











