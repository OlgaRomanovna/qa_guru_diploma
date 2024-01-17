import json

import allure
import pytest
from jsonschema.validators import validate

from api.resourses.contact import add_contact
from api.resourses.json_schema import contact_json_path
from utils import Severity, StatusCode


@allure.severity(Severity.BLOCKER)
@allure.title('Валидация кода и ответа сервера после добавления контакта')
@pytest.mark.api
@pytest.mark.contact
def test_add_contact(get_user_data_from_env, data_contact):
    with allure.step('Добавляем контакт'):
        resp = add_contact(get_user_data_from_env.token, data_contact)
    with allure.step('Проверяем код ответа сервера'):
        assert resp.status_code == StatusCode.CREATED
    json = resp.json()
    with allure.step('Проверяем ответ сервера'):
        assert data_contact.first_name == json['firstName']
        assert data_contact.last_name == json['lastName']
        assert data_contact.birthdate == json['birthdate']
        assert data_contact.email == json['email']
        assert data_contact.phone == json['phone']
        assert data_contact.street1 == json['street1']
        assert data_contact.street2 == json['street2']
        assert data_contact.city == json['city']
        assert data_contact.state_province == json['stateProvince']
        assert data_contact.postal_code == json['postalCode']
        assert data_contact.country == json['country']


@allure.severity(Severity.CRITICAL)
@allure.title('Валидация JSON_SCHEMA данных контакта')
@pytest.mark.api
@pytest.mark.contact
def test_add_contact_validate_json_schema(get_user_data_from_env, data_contact):
    with allure.step('Читаем файл-образец с json_schema'):
        with open(contact_json_path) as file:
            schema = json.loads(file.read())
    with allure.step('Добавляем контакт'):
        resp = add_contact(get_user_data_from_env.token, data_contact)
    with allure.step('Валидируем json_schema'):
        validate(resp.json(), schema)
