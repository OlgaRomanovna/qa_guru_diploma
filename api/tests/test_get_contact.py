import json

import allure
import pytest
from jsonschema.validators import validate

from api.resourses.contact import get_contact, get_contacts
from api.resourses.json_schema import contact_json_path
from utils import Severity, StatusCode


@allure.severity(Severity.BLOCKER)
@allure.title('Валидация кода и ответа сервера после получения контакта')
@pytest.mark.api
@pytest.mark.contact
def test_get_contact(get_user_data_from_env, add_contact_fixture):
    with allure.step('Получаем контакт'):
        resp = get_contact(get_user_data_from_env.token, contact_id=add_contact_fixture.json()['_id'])
    with allure.step('Валидируем код ответа сервера'):
        assert resp.status_code == StatusCode.OK


@allure.severity(Severity.CRITICAL)
@allure.title('Валидация JSON_SCHEMA данных контакта после получения контакта')
@pytest.mark.api
@pytest.mark.contact
def test_validate_contact(get_user_data_from_env, add_contact_fixture):
    with allure.step('Читаем файл-образец с json_schema'):
        with open(contact_json_path) as file:
            schema = json.loads(file.read())
    with allure.step('Получаем контакт'):
        resp = get_contact(get_user_data_from_env.token, contact_id=add_contact_fixture.json()['_id'])
    with allure.step('Валидируем код ответа сервера'):
        assert resp.status_code == StatusCode.OK
    with allure.step('Валидируем json_schema'):
        validate(resp.json(), schema)


@allure.severity(Severity.CRITICAL)
@allure.title('Валидация кода и ответа сервера после получения списка контактов')
@pytest.mark.api
@pytest.mark.contact
def test_get_contacts(get_user_data_from_env, add_contact_fixture):
    with allure.step('Читаем файл-образец с json_schema'):
        with open(contact_json_path) as file:
            schema = json.loads(file.read())
    with allure.step('Получаем список контактов'):
        resp = get_contacts(get_user_data_from_env.token)
    with allure.step('Валидируем код ответа сервера'):
        assert resp.status_code == StatusCode.OK
    with allure.step('Валидируем json_schema'):
        for contact in resp.json():
            validate(contact, schema)
