import json
import os

import allure
import pytest
from jsonschema.validators import validate

from api.resourses.json_schema import data_user_json_path
from api.resourses.user import get_profile
from utils import Severity, StatusCode


@allure.severity(Severity.BLOCKER)
@allure.title('Валидация данных пользователя после авторизации')
@pytest.mark.api
@pytest.mark.user
def test_get_user_profile(get_user_data_from_env):
    with allure.step('Получаем информацию по профилю пользователя'):
        response = get_profile(get_user_data_from_env.token)
    with allure.step('Валидируем код ответа сервера'):
        assert response.status_code == StatusCode.OK
    with allure.step('Валидируем ответ сервера'):
        assert response.json()['firstName'] == os.getenv('FIRST_NAME')
        assert response.json()['lastName'] == os.getenv('LAST_NAME')
        assert response.json()['email'] == os.getenv('EMAIL')


@allure.severity(Severity.CRITICAL)
@allure.title('Валидация JSON_SCHEMA данных пользователя')
@pytest.mark.user
def test_validate_json_schema_user_profile(get_user_data_from_env):
    with allure.step('Читаем файл-образец с json_schema'):
        with open(data_user_json_path) as file:
            schema = json.loads(file.read())
    with allure.step('Получаем информацию по профилю пользователя'):
        response = get_profile(get_user_data_from_env.token)
    assert response.status_code == StatusCode.OK  # надо ли?
    with allure.step('Валидируем json_schema'):
        validate(response.json(), schema)
