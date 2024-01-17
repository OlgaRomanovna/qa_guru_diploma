import allure
import pytest

from api.resourses.user import delete, register
from utils import Severity, StatusCode


@allure.severity(Severity.CRITICAL)
@allure.title('Проверка кода ответа от сервера после удаления пользователя')
@pytest.mark.api
@pytest.mark.user
def test_delete_user(user_data_for_register):
    with allure.step('Регистрируем пользователя'):
        resp = register(first_name=user_data_for_register.first_name,
                        last_name=user_data_for_register.last_name,
                        password=user_data_for_register.password)
        assert resp.status_code == StatusCode.CREATED
    token = resp.json()['token']  # read token from response
    with allure.step('Удаляем пользователя'):
        assert delete(token).status_code == StatusCode.OK, f'{delete(token).status_code} is not {StatusCode.OK}'
