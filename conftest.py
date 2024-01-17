import os

import allure
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from api.resourses.contact import add_contact
from api.resourses.contact.contact_model import ContactModel
from api.resourses.user import UserModel, auth
from config import browser
from utils import BASE_URL, StatusCode, add_html, add_logs, add_screenshot, add_video, generate_random_string

DEFAULT_BROWSER_VERSION = '100'


@pytest.fixture
def user_data_for_register():
    """
    The first and last name must be unique
    """
    first_name = f'Ivan_{generate_random_string(4)}'
    last_name = f'Ivanov_{generate_random_string(4)}'
    password = '1234567'
    return UserModel(first_name=first_name, last_name=last_name, password=password)


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session')
def get_user_data_from_env():
    with allure.step('Получаем данные по пользователю'):
        resp = auth(email=os.getenv('EMAIL'),
                    password=os.getenv('PASSWORD_USER'))
        assert resp.status_code == StatusCode.OK
        return UserModel(token=resp.json()['token'], _id=resp.json()['user']['_id'])


@pytest.fixture()
def data_contact():
    contact = ContactModel()
    contact.first_name = 'Alexander'
    contact.last_name = 'Pushkin'
    contact.birthdate = '1799-06-06'
    contact.email = 'alexander_pushkin@gmail.com'
    contact.phone = '8005555555'
    contact.street1 = 'street Glinka'
    contact.street2 = 'house 5, flat 17'
    contact.city = 'Moscow'
    contact.state_province = 'RU'
    contact.postal_code = '12345'
    contact.country = 'Russia'
    return contact


@pytest.fixture()
def add_contact_fixture(get_user_data_from_env, data_contact):
    with allure.step('Создаём контакт'):
        resp = add_contact(get_user_data_from_env.token, data_contact)
        assert resp.status_code == StatusCode.CREATED
        return resp


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--browser_version', action='store', default="99.0")


@pytest.fixture(scope='function')
def open_browser(request):
    browser_name = request.config.getoption('browser_name')
    browser_version = request.config.getoption('browser_version')
    options = Options()
    selenoid_capabilities = {
        "browserName": f"{browser_name}",
        "browserVersion": f"{browser_version}",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )
    browser.config.driver = driver
    browser.config.base_url = BASE_URL
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    add_html(browser)
    add_screenshot(browser)
    add_video(browser)
    if browser_name == 'chrome':
        add_logs(browser)
    browser.quit()


@pytest.fixture()
def web_user_for_auth():
    return UserModel(email=os.getenv('EMAIL'), password=os.getenv('PASSWORD_USER'))
