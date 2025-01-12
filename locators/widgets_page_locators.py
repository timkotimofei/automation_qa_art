from selenium.webdriver.common.by import By


class AccordianPageLocators:

    SECTION_FIRST =  (By.XPATH, '//div[contains(text(), "What is Lorem Ipsum?")]')
    SECTION_CONTENT_FIRST = (By.CSS_SELECTOR, "div[id='section1Content']")

    SECTION_SECOND = (By.XPATH, "//div[contains(text(), 'Where does it come from?')]")
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, "div[id='section2Content']")

    SECTION_THIRD = (By.XPATH, "//div[contains(text(), 'Why do we use it?')]")
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, "div[id='section3Content']")

