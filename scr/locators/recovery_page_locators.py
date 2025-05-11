from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")
    RECOVERY_BUTTON = (By.XPATH, ".//button[text() = 'Восстановить']")
    LOGIN_BUTTON = (By.XPATH, ".//a[text() = 'Войти']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Введите новый пароль']")
    CODE_FROM_MAIL = (By.XPATH, ".//label[text() = 'Введите код из письма']")
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
    RECOVERY_TEXT_FORM = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")
    SHOW_BUTTON = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")
    INPUT_FIELD_ACTIVE = (By.CSS_SELECTOR, ".input.input_status_active")
