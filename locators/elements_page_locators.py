from ast import Bytes

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




