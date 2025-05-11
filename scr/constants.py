class BaseUrl:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'


class Urls:
    URL_FEED = 'feed'
    URL_LOGIN = 'login'
    URL_RECOVERY = 'forgot-password'
    URL_REGISTER = 'register'
    URL_PROFILE = 'account/profile'
    URL_HISTORY_ORDER = 'account/order-history'
    URL_RESET_PASSWORD = 'reset-password'


class Endpoints:
    CREATE_USER = 'api/auth/register'
    LOGIN = 'api/auth/login'
    DELETE_USER = 'api/auth/user'
    CREATE_ORDER = 'api/orders'
    GET_ORDERS = 'api/orders'


class Ingredients:
    CORRECT_INGREDIENTS_DATA = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }
