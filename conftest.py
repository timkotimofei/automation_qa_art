from datetime import datetime

import allure
import pytest
from selenium import webdriver
import logging.config
from os import path                         # библиотека для поиска пути

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini') # получаем абсолютный путь нашей директор
# print(log_file_path)                                             # и соединяем его с именем нашего файла = полный путь
logging.config.fileConfig(log_file_path)    # применим в аргументе эту переменную с нашим путем

# Тестовое сообщение для проверки работы логирования
# logging.debug("Тестовое сообщение уровня DEBUG - файл conftest.py")
# logging.info("Тестовое сообщение уровня INFO - файл conftest.py")



# здесь будет хранится фикстура. Это такая функция - декоратор, а функция помещенная в нее является фикстур
# ТО есть она позволяет выполнять что-либо до теста и после теста.
# Фикстура имеет некие свои свойства.

@pytest.fixture(scope="function")   # function т.к. поведение открытие-закрытие юраузера
def driver():
    logging.debug('Prepare the browser')
    driver = webdriver.Chrome()
    driver.maximize_window()
    logging.debug('The browser has been started')
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot {datetime.today()}', attachment_type=allure.attachment_type.PNG)
    logging.debug('The browser has been close')
    driver.quit()




