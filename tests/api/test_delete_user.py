import os
import allure
import pytest
from tests.api.conftest import post_request, delete_request, check_status_code
from utils.const import CREATED, OK, CRITICAL


@allure.id("29417")
@allure.severity(CRITICAL)
@allure.title('Проверка кода ответа от сервера после удаления пользователя')
@pytest.mark.test_api
@pytest.mark.user
@pytest.mark.skip
def test_delete_user(load_env):
    with allure.step('Регистрируем пользователя'):
        json = {
            "firstName": f"{os.getenv('FIRST_NAME')}",
            "lastName": f"{os.getenv('LAST_NAME')}",
            "email": f"{os.getenv('EMAIL')}",
            "password": f"{os.getenv('PASSWORD_USER')}"
        }
        response = post_request('/users', json)
        check_status_code(response, CREATED)
    with allure.step('Удаляем пользователя'):
        response = delete_request('/users/me')
        check_status_code(response, OK)
