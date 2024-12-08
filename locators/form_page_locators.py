import random

from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER = (By.CSS_SELECTOR, f"label[for='gender-radio-{random.randint(1,3)}']")
    MOBILE = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    SUBJECT_ID = (By.ID, "subjectsInput")
    SUBJECT_SELECTOR = (By.CSS_SELECTOR, "div[class='subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi subjects-auto-complete__value-container--has-value css-1hwfws3']")
    HOBBIES = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{random.randint(1,3)}']")
    FILE_INPUT = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    SELECT_STATE = (By.CSS_SELECTOR, "div[id='state']")
    STATE_INPUT = (By.ID, "react-select-3-input")
    SELECT_CITY = (By.ID, "city")
    CITY_INPUT = (By.ID, "react-select-4-input")
    SUBMIT = (By.ID, "submit")

    # table result
    TABLE = (By.CSS_SELECTOR, "table[class='table table-dark table-striped table-bordered table-hover']")
    TABLE_VALUES = (By.XPATH, "//div[@class='table-responsive']//td[2]")





