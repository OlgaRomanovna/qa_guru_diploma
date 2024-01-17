import allure
import pytest

from api.resourses.contact import delete_contact, get_contact
from utils.handbook import Severity, StatusCode


@allure.severity(Severity.BLOCKER)
@allure.title('Удаление контакта пользователя')
@pytest.mark.api
@pytest.mark.contact
def test_delete_contact(get_user_data_from_env, add_contact_fixture):
    with allure.step('Удаляем контакт'):
        resp = delete_contact(get_user_data_from_env.token, add_contact_fixture.json()['_id'])
    with allure.step('Валидируем код ответа сервера'):
        assert resp.status_code == StatusCode.OK


@allure.severity(Severity.BLOCKER)
@allure.title('Удаление контакта пользователя')
@pytest.mark.api
@pytest.mark.contact
def test_delete_contact_and_get_deleted_contact(get_user_data_from_env, add_contact_fixture):
    with allure.step('Удаляем контакт'):
        delete_contact(get_user_data_from_env.token, add_contact_fixture.json()['_id'])
    with allure.step('Получение удалённого контакта'):
        assert get_contact(get_user_data_from_env.token,add_contact_fixture.json()['_id']).status_code == StatusCode.NOT_FOUND
