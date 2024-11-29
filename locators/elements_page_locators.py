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

    #table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT =  ".//ancestor::div[@class='rt-tr-group']"
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label='rows per page']")

    #update
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")


class ButtonsPageLocators:
    # buttons
    DOUBLE_BUTTON = (By.ID, 'doubleClickBtn')
    RIGHT_CLICK_BUTTON = (By.ID, 'rightClickBtn')
    CLICK_ME_BUTTON = (By.XPATH, "//button[normalize-space(.)='Click Me']")

    #result text
    SUCCESS_DOUBLE = (By.ID, 'doubleClickMessage')
    SUCCESS_RIGHT = (By.ID, 'rightClickMessage')
    SUCCESS_CLICK_ME = (By.ID, 'dynamicClickMessage')


class LinksPageLocators:

    # new tab links
    SIMPLE_LINK = (By.XPATH, "//a[@id='simpleLink']")
    DYNAMIC_LINK = (By.XPATH, "//a[@id='dynamicLink']")

    # api calls links
    CREATED_LINK = (By.XPATH, "//a[@id='created']")
    NO_CONTENT_LINK = (By.XPATH, "//a[@id='no-content']")
    MOVED_LINK = (By.XPATH, "//a[@id='moved']")
    BAD_REQUEST_LINK = (By.XPATH, "//a[@id='bad-request']")
    UNAUTHORIZED_LINK = (By.XPATH, "//a[@id='unauthorized']")
    FORBIDDEN_LINK = (By.XPATH, "//a[@id='forbidden']")
    NOT_FOUND_LINK = (By.XPATH, "//a[@id='invalid-url']")

    #response text
    RESPONSE_TEXT = (By.ID, 'linkResponse')

class UploadDownloadPageLocators:

    UPLOAD_FILE = (By.CSS_SELECTOR,"input[id='uploadFile']")
    UPLOADED_RESULT = (By.ID, 'uploadedFilePath')

    DOWNLOAD_FILE_BUTTON = (By.ID, 'downloadButton')

class DynamicPropertiesPageLocators:

    WILL_ENABLE_5_SECONDS_BUTTON = (By.CSS_SELECTOR, 'button[id=enableAfter]')
    COLOR_CHANGE_BUTTON = (By.XPATH, "//button[contains(text(), 'Color Change')]")
    VISIBLE_AFTER_5_SECOND_BUTTON = (By.XPATH, "//button[contains(text(), 'Visible After 5 Seconds')]")
















