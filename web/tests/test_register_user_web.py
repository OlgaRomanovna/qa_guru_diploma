import random

import allure
import pytest

from api.resourses.user import UserModel
from utils import Severity
from web.resourses import Login, Logout, WebRegisterUser


@allure.severity(Severity.BLOCKER)
@allure.title('Успешная регистрация пользователя')
@pytest.mark.web
@pytest.mark.user
def test_positive_register(open_browser):
    login_page = Login(user=UserModel())
    login_page.open()
    register_page = WebRegisterUser(user=UserModel(
        first_name='Alexey',
        last_name='Ivanov',
        email=f'alexey_ivanov{random.randint(1, 1000)}@mail.ru',
        password='1234567'
    ))
    register_page.open()
    register_page.fill_form()
    register_page.submit()
    register_page.check_after_positive_register('Contact List')


@allure.severity(Severity.BLOCKER)
@allure.title('Безуспешная регистрация пользователя')
@pytest.mark.web
@pytest.mark.user
def test_negative_register(open_browser):
    login_page = Login(user=UserModel())
    login_page.open()
    register_page = WebRegisterUser(user=UserModel(
        first_name=None,
        last_name=None,
        email=None,
        password=None
    ))
    register_page.open()
    register_page.submit()
    register_page.check_after_negative_register('User validation failed: firstName: Path `firstName` is required., '
                                                'lastName: Path `lastName` is required., email: Email is invalid, '
                                                'password: Path `password` is required.')


@allure.severity(Severity.MINOR)
@allure.title('Отмена регистрации пользователя')
@pytest.mark.web
@pytest.mark.user
def test_cancel_register(open_browser):
    login_page = Login(user=UserModel())
    login_page.open()
    register_page = WebRegisterUser(user=UserModel(
        first_name=None,
        last_name=None,
        email=None,
        password=None
    ))
    register_page.open()
    register_page.cancel()
    logout_page = Logout()
    logout_page.check_result_after_log_out(
        header='Contact List App',
        sub_header='Welcome! This application is for testing purposes only. '
                   'The database will be purged as needed to keep costs down.',
        href='here'
    )
