from faker import Faker
import requests
import allure

from scr.constants import BaseUrl, Endpoints, Ingredients


class Order:
    @allure.step('Создание нового заказа пользователя')
    def create_order(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        requests.post(BaseUrl.BASE_URL + Endpoints.CREATE_ORDER, headers=headers, data=Ingredients.CORRECT_INGREDIENTS_DATA)

    @allure.step('Получение заказов пользователя')
    def get_user_orders(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        response = requests.get(BaseUrl.BASE_URL + Endpoints.GET_ORDERS, headers=headers)
        return response.json()["orders"][0]["number"]


class User:
    @staticmethod
    @allure.step('Генерация email, password, name пользователя')
    def create_user():
        faker = Faker('ru_RU')
        data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name()
        }
        return data
