from selenium.webdriver.common.by import By


class PersonalPageLocators:
    PROFILE_FORM = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")
    PROFILE_BUTTON = (By.XPATH, ".//a[text() = 'Профиль']")
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[text() = 'История заказов']")
    HISTORY_ORDER_FORM = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")
    NUMBER_ORDER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")
    CANCEL_BUTTON = (By.XPATH, ".//button[text() = 'Отмена']")
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
    EXIT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")
