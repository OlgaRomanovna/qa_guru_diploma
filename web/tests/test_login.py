import allure
import pytest

from api.resourses.user import UserModel
from utils import Severity
from web.resourses import Login, Logout


@allure.severity(Severity.BLOCKER)
@allure.title('Авторизация пользователя')
@pytest.mark.web
@pytest.mark.user
def test_login(open_browser, web_user_for_auth):
    page = Login(web_user_for_auth)
    page.open()
    page.fill_form()
    page.submit()
    page.check_result_after_login(header='Contact List', sub_header='Click on any contact to view the Contact Details')


@allure.severity(Severity.BLOCKER)
@allure.title('Деавторизация пользователя')
@pytest.mark.web
@pytest.mark.user
def test_logout(open_browser, web_user_for_auth):
    login_page = Login(web_user_for_auth)
    login_page.open()
    login_page.fill_form()
    login_page.submit()
    logout_page = Logout()
    logout_page.log_out()
    logout_page.check_result_after_log_out(
        header='Contact List App',
        sub_header='Welcome! This application is for testing purposes only. '
                   'The database will be purged as needed to keep costs down.',
        href='here'
    )


@allure.severity(Severity.BLOCKER)
@allure.title('Авторизация пользователя с некорректными данными')
@pytest.mark.web
@pytest.mark.user
def test_incorrect_login(open_browser):
    login_page = Login(
        user=UserModel(email='incorrect@mail.ru', password='incorrect_password')
    )
    login_page.open()
    login_page.fill_form()
    login_page.submit()
    login_page.check_result_after_incorrect_login_data('Incorrect username or password')


@allure.severity(Severity.MINOR)
@allure.title('Проверка ссылки на главной странице')
@pytest.mark.web
def test_check_api_documentation(open_browser, web_user_for_auth):
    login_page = Login(web_user_for_auth)
    login_page.open()
    login_page.check_link()
