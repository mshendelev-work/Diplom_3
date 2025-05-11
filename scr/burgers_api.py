import allure
import requests

from scr.constants import Url


class StellarBurgersAPI:
    @staticmethod
    @allure.step('Запрос авторизации пользователя')
    def login_user(email, password):
        url = f"{Url.BASE_URL}/auth/login"
        payload = {"email": email, "password": password}
        return requests.post(url, json=payload)

    @staticmethod
    @allure.step("Запрос удаления пользователя")
    def delete_user(token, email, password, name):
        url = f"{Url.BASE_URL}/auth/register"
        headers = {"Authorization": token}
        payload = {"email": email, "password": password, "name": name}
        return requests.delete(url, json=payload, headers=headers)
