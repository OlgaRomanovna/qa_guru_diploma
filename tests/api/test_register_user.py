import allure
import pytest
from data.data import first_name_for_register, last_name_for_register, password, email_for_register
from schemas.schema_create_user import CreateUser
from tests.api.conftest import check_response_list_schema, post_request_without_token
from utils.const import CREATED, BLOCKER, CRITICAL


@allure.id("29427")
@allure.severity(BLOCKER)
@allure.title('Валидация кода и ответа сервера после регистрации пользователя')
@pytest.mark.test_api
@pytest.mark.user
def test_register():
    with allure.step(f'Регистрируем пользователя. Имя {first_name_for_register}, фамилия {last_name_for_register}'):
        json = {
            "firstName": f"{first_name_for_register}",
            "lastName": f"{last_name_for_register}",
            "email": f"{email_for_register}",
            "password": f"{password}"
        }
        response = post_request_without_token('/users', json)
    with allure.step('Валидируем код ответа сервера'):
        assert response.status_code == CREATED, f'{response.status_code} is not {CREATED}'
    resp_json = response.json()['user']
    with allure.step('Валидируем ответ сервера'):
        assert resp_json['firstName'] == first_name_for_register
        assert resp_json['lastName'] == last_name_for_register
        assert resp_json['email'] == email_for_register


@allure.id("29428")
@allure.severity(CRITICAL)
@allure.title('Валидация JSON_SCHEMA после регистрации пользователя')
@pytest.mark.test_api
@pytest.mark.user
def test_register_validate_json_schema():
    with allure.step(
            f'Регистрируем пользователя. Имя {first_name_for_register}, фамилия {last_name_for_register}'):
        json = {
            "firstName": f"{first_name_for_register}",
            "lastName": f"{last_name_for_register}",
            "email": f"{email_for_register}",
            "password": f"{password}"
        }
        response = post_request_without_token('/users', json)
    assert response.status_code == CREATED, f'{response.status_code} is not {CREATED}'
    with allure.step('Валидируем json_schema'):
        check_response_list_schema(CreateUser, response.json())
