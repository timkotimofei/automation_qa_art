from selenium.webdriver.common.by import By


class TextBookPageLocators:

    #form fields
    FULL_NAME = (By.CSS_SELECTOR, "[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "[id='permanentAddress']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    #created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")   # CSS  сначала ищет output а потом name
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")     # CSS  сначала ищет output а потом email
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")  #

class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']") # здесь 17 элементов и я буду работать с циклом
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']") # только отмеченные элементы
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")
    OUTPUT_ITEMS = (By.XPATH, "//span[@class='text-success']")

class RadioButtonPageLocators:
    YES_BUTTON = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_BUTTON = (By.CSS_SELECTOR, "label[for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")

class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.XPATH, "//button[contains(text(),'Add')]")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")














