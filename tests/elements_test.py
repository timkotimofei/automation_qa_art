import time
from conftest import driver
from pages.base_page import BasePage




def test(driver):
    page =BasePage(driver, 'https://demoqa.com/elements')
    page.open()
    time.sleep(5)