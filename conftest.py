from datetime import datetime
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Импортируем ChromeOptions
import logging.config
from os import path, getenv      # path библиотека для поиска пути

# Настройка логирования
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini') # получаем абсолютный путь нашей директор
# print(log_file_path)                                            # и соединяем его с именем нашего файла = полный путь
logging.config.fileConfig(log_file_path)                         # применим в аргументе эту переменную с нашим путем




# Тестовое сообщение для проверки работы логирования
# logging.debug("Тестовое сообщение уровня DEBUG - файл conftest(25 december).py")
# logging.info("Тестовое сообщение уровня INFO - файл conftest(25 december).py")



# здесь будет хранится фикстура. Это такая функция - декоратор, а функция помещенная в нее является фикстур.
# ТО есть она позволяет выполнять что-либо до теста и после теста.
# Фикстура имеет некие свои свойства.




@pytest.fixture(scope="function")        # function т.к. поведение открытие-закрытие браузера
def driver():
    logging.debug('Prepare the browser')

    # Проверяем переменную окружения HEADLESS
    is_headless = getenv('HEADLESS', 'true').lower() == 'true'     # чтобы активировать поменяй на true

    # Настройки ChromeOptions
    chrome_options = Options()
    if is_headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Создание драйвера с опциями
    driver = webdriver.Chrome(options=chrome_options)
    mode = "headless" if is_headless else "non-headless"
    logging.debug(f'The browser has been started in {mode} mode')

    yield driver

    # Добавление скриншота в отчет
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot {datetime.today()}', attachment_type=allure.attachment_type.PNG)
    logging.debug('The browser has been closed')
    driver.quit()