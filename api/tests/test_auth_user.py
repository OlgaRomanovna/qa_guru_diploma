import os

import allure
import pytest

from api.resourses.user import auth
from utils import Severity, StatusCode


@allure.severity(Severity.BLOCKER)
@allure.title('Валидация данных пользователя после авторизации')
@pytest.mark.api
@pytest.mark.user
def test_auth():
    with allure.step('Выполняем авторизацию'):
        resp = auth(email=os.getenv('EMAIL'),
                    password=os.getenv('PASSWORD_USER'))
    with allure.step('Валидируем код ответа сервера'):
        assert resp.status_code == StatusCode.OK, f'{resp.status_code} is not {StatusCode.OK}'
