import allure
from selene import browser, have

from api.resourses.user import UserModel
from .pages import ContactList, MainPage


class Login:
    def __init__(self, user: UserModel):
        self.b = browser
        self.user = user
        self.login_page = MainPage()
        self.contact_list_page = ContactList()
        self.url = '/login'

    @allure.step('Отрываем страницу страницу логина')
    def open(self):
        self.b.open(self.url)

    @allure.step('Заполняем форму логина')
    def fill_form(self):
        self.b.element(f'{self.login_page.email}').type(self.user.email)
        self.b.element(f'{self.login_page.password}').type(self.user.password)

    @allure.step('Подтверждаем введённые данные')
    def submit(self):
        self.b.element(self.login_page.submit).click()

    @allure.step('Проверяем результат после авторизации')
    def check_result_after_login(self, header: str, sub_header: str):
        self.b.element(self.contact_list_page.header_text).should(have.text(header))
        self.b.element(self.contact_list_page.sub_header_text).should(have.text(sub_header))
        self.b.element(self.contact_list_page.logout).should(have.text('Logout'))

    @allure.step('Проверяем результат после введения некорректных авторизационных данных')
    def check_result_after_incorrect_login_data(self, name_error: str):
        self.b.element(self.login_page.error_after_login).should(have.text(name_error))

    @allure.step('Проверяем ссылку на странице')
    def check_link(self):
        self.b.element(self.login_page.link_api_doc).click()


class Logout:
    def __init__(self):
        self.contact_list_page = ContactList()
        self.login_page = MainPage()
        self.b = browser

    @allure.step('Выполняем деавторизацию')
    def log_out(self):
        self.b.element(self.contact_list_page.logout).click()

    @allure.step('Проверяем результат после деавторизации')
    def check_result_after_log_out(self, header: str, sub_header: str, href: str):
        self.b.element(self.login_page.header).should(have.text(header))
        self.b.element(self.login_page.sub_header).should(have.text(sub_header))
        self.b.element(self.login_page.link_api_doc).should(have.text(href))
