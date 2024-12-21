from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver


# Здесь будут методы для работы со страницей, выносим описание и создание этих методов сюда, чтобы потом упоминая их
# мы могли бы просто вызвать название этого метода ив аргументе указать driver, locator


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

# Этот код будет часто повторяться и нам потом достаточно просто вызвать element_is_visible(self, locator, timeout=5)
    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def elements_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def elements_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').style.display='none';")

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def switch_to_window_custom_tab(self,number):
        self.driver.switch_to.window(self.driver.window_handles[number])


    def switch_to_alert_window(self):
        return self.driver.switch_to.alert


    def get_url_current_page(self):
        return self.driver.current_url

    '''
    Метод go_to_element выполняет прокрутку страницы до указанного элемента на веб-странице с помощью JavaScript. 
    Вот подробное объяснение:
    Как работает "arguments[0].scrollIntoView();":

	1.	arguments[0]:
	•	В JavaScript, при использовании метода execute_script в Selenium, можно передавать аргументы из Python-кода в 
	JavaScript-код. Эти аргументы доступны через специальный массив arguments.
	•	arguments[0] означает первый переданный аргумент. В данном случае, это будет элемент, который вы передаете 
	в метод execute_script через Selenium.
	2.	.scrollIntoView();:
	•	Это стандартный метод JavaScript, который доступен для любого DOM-элемента (элемента на веб-странице). 
	Он автоматически прокручивает страницу, чтобы сделать элемент видимым в области просмотра.
	•	Когда вы вызываете element.scrollIntoView(), браузер перемещает страницу таким образом, чтобы элемент, 
	который соответствует переменной element, оказался в видимой части экрана.

    '''
