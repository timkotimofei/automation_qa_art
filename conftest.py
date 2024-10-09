import pytest
from selenium import webdriver



# здесь будет хранится фикстура. Это такая функция - декоратор, а функция помещенная в нее является фикстур
# ТО есть она позволяет выполнять что-либо до теста и после теста.
# Фикстура имеет некие свои свойства.

@pytest.fixture(scope="function")   # function т.к. поведение открытие-закрытие юраузера
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()



