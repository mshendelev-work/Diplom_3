import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        with allure.step('Получить текущий URL'):
            return self.driver.current_url

    def wait_element_clickable(self, locator):
        with allure.step('Подождать кликабельности элемента'):
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    def wait_for_load_element(self, locator):
        with allure.step('Ожидание загрузки элемента'):
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))

    def click_button(self, locator):
        with allure.step('Клик по кнопке'):
            self.wait_element_clickable(locator)
            self.driver.find_element(*locator).click()

    def send_keys_to_field(self, locator, text):
        with allure.step('Заполнение формы'):
            self.wait_element_clickable(locator)
            self.driver.find_element(*locator).send_keys(text)

    def get_text_locator(self, locator):
        with allure.step('Получить текст элемента'):
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator).text

    def get_text_locators(self, locator):
        with allure.step('Получить текст элементов'):
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
            return self.driver.find_elements(*locator)

    def check_element(self, locator):
        with allure.step('Проверка отображения элемента'):
            self.wait_for_load_element(locator)
            return self.driver.find_element(*locator)

    def check_element_is_not_visible(self, locator):
        with allure.step('Проверка элемента, что он больше не отображается'):
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
            return self.driver.find_element(*locator)

    def drag_and_drop(self, element_one, element_two):
        with allure.step('Перетаскивание элемента'):
            element = self.driver.find_element(*element_one)
            target = self.driver.find_element(*element_two)
            action_chains = ActionChains(self.driver)
            action_chains.drag_and_drop(element, target).perform()

    def move_to_element_and_click(self, locator):
        with allure.step('Переход к элементу и клик на него'):
            element = self.driver.find_element(*locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
