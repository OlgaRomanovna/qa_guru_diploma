
import allure
import pytest

from api.resourses.contact import full_update_contact
from api.resourses.contact.contact_model import ContactModel
from utils.handbook import Severity, StatusCode


@allure.severity(Severity.BLOCKER)
@allure.title('Валидация кода и ответа сервера после частичной замены данных контакта')
@pytest.mark.api
@pytest.mark.contact
def test_full_update_contact(get_user_data_from_env, add_contact_fixture, data_contact):
    contact = ContactModel()
    contact.first_name = 'new_Alexander'
    contact.last_name = 'new_Pushkin'
    contact.birthdate = '1799-07-07'
    contact.email = 'new_alexander_pushkin@gmail.com'
    contact.phone = '8005555556'
    contact.street1 = 'new_street Glinka'
    contact.street2 = 'new_house 5, flat 17'
    contact.city = 'new_Moscow'
    contact.state_province = 'newRU'
    contact.postal_code = '1234567'
    contact.country = 'new_Russia'
    with allure.step('Меняем данные контакта'):
        resp = full_update_contact(get_user_data_from_env.token, add_contact_fixture.json()['_id'], contact)
    with allure.step('Валидируем код ответа сервера'):
        assert resp.status_code == StatusCode.OK
    with allure.step('Валидируем данные контакта'):
        assert resp.json()['firstName'] == contact.first_name
        assert resp.json()['lastName'] == contact.last_name
        assert resp.json()['birthdate'] == contact.birthdate
        assert resp.json()['email'] == contact.email
        assert resp.json()['phone'] == contact.phone
        assert resp.json()['street1'] == contact.street1
        assert resp.json()['street2'] == contact.street2
        assert resp.json()['city'] == contact.city
        assert resp.json()['stateProvince'] == contact.state_province
        assert resp.json()['postalCode'] == contact.postal_code
        assert resp.json()['country'] == contact.country
