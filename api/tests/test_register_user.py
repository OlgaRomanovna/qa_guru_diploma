import json

import allure
import pytest
from jsonschema.validators import validate

from api.resourses.json_schema import register_json_path
from api.resourses.user import register
from utils.handbook import Severity, StatusCode


@allure.severity(Severity.BLOCKER)
@allure.title('Валидация кода и ответа сервера после регистрации пользователя')
@pytest.mark.api
@pytest.mark.user
def test_register(user_data_for_register):
    with allure.step(f'Регистрируем пользователя. Имя {user_data_for_register.first_name}, '
                     f'фамилия {user_data_for_register.last_name}'):
        resp = register(first_name=user_data_for_register.first_name,
                        last_name=user_data_for_register.last_name,
                        password=user_data_for_register.password)
    with allure.step('Валидируем код ответа сервера'):
        assert resp.status_code == StatusCode.CREATED, f'{resp.status_code} is not {StatusCode.CREATED}'
    resp_json = resp.json()['user']
    with allure.step('Валидируем ответ сервера'):
        assert resp_json['firstName'] == user_data_for_register.first_name
        assert resp_json['lastName'] == user_data_for_register.last_name
        assert resp_json['email'] == user_data_for_register.email


@allure.severity(Severity.CRITICAL)
@allure.title('Валидация JSON_SCHEMA после регистрации пользователя')
@pytest.mark.api
@pytest.mark.user
def test_register_validate_json_schema(user_data_for_register):
    with allure.step('Читаем файл-образец с json_schema'):
        with open(register_json_path) as file:
            schema = json.loads(file.read())
    with allure.step(f'Регистрируем пользователя. Имя {user_data_for_register.first_name}, '
                     f'фамилия {user_data_for_register.last_name}'):
        resp = register(first_name=user_data_for_register.first_name,
                        last_name=user_data_for_register.last_name,
                        password=user_data_for_register.password)
    assert resp.status_code == StatusCode.CREATED, f'{resp.status_code} is not {StatusCode.CREATED}'
    with allure.step('Валидируем json_schema'):
        validate(resp.json(), schema)
