from selenium.webdriver.common.by import By


class OrderFeedLocators:
    TITLE_ORDERS_LIST = (By.XPATH, '//h1[text()="Лента заказов"]')
    ORDERS_INFO = (By.XPATH, '//p[text()="Cостав"]')
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    NUMBER_ORDER_IN_JOB = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")
    ORDER_INFO_WINDOW = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")
    ORDER_HISTORY = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')
