import pytest
from selenium import webdriver
import requests

from scr.constants import BaseUrl, Endpoints, Ingredients
from scr.helpers import User
from scr.pages.home_page import HomePage
from scr.pages.home_page_header import HeaderPage
from scr.pages.login_page import LoginPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(BaseUrl.BASE_URL)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(BaseUrl.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_new_user():
    payload = User.create_user()
    response = requests.post(BaseUrl.BASE_URL + Endpoints.CREATE_USER, data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(BaseUrl.BASE_URL + Endpoints.DELETE_USER, headers={"Authorization": token})


@pytest.fixture
def login(driver, create_new_user):
        create_user_data = create_new_user[0]
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)
        header_page.click_profile_area_button()
        login_page.login(create_user_data["email"], create_user_data["password"])
        home_page = HomePage(driver)
        home_page.wait_load_home_page()


@pytest.fixture
def create_order(create_new_user):
    token = create_new_user[1].json()["accessToken"]
    headers = {'Authorization': token}
    response = requests.post(BaseUrl.BASE_URL + Endpoints.CREATE_ORDER, headers=headers, data=Ingredients.CORRECT_INGREDIENTS_DATA)
    return response.json()["order"]["number"]
