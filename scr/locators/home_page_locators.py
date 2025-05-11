from selenium.webdriver.common.by import By


class HomePageLocators:
    ORDER_FEED_FORM = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")
    CONSTRUCTOR_FORM = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']")
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    FLUORESCENT_BUN_BUTTON = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")
    CLOSE_POPUP_FORM = (By.XPATH, '//button[contains(@class,"close")]')
    COUNTER_INGREDIENT = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")
    ORDER_FORM = (By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']")
    ORDER_BASKET = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
    ORDER_NUM = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")
    POPUP_FORM_INGREDIENTS = (By.XPATH, "//h2[text()= 'Детали ингредиента']")
