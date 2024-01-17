import allure
import pytest

from utils import Severity
from web.resourses import AddContact, auth_web


@allure.severity(Severity.BLOCKER)
@allure.title('Добавление контакта')
@pytest.mark.web
@pytest.mark.contact
def test_add_contact(open_browser, web_user_for_auth, data_contact):
    auth_web(web_user_for_auth)
    page = AddContact(data_contact)
    page.open()
    page.fill_form()
    page.submit()
    page.check_result()
