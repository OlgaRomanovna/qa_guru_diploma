import allure
from selene import browser, have

from api.resourses.user import UserModel
from .login import ContactList, MainPage
from .pages import AddUser


class WebRegisterUser:
    def __init__(self, user: UserModel):
        self.register_page = AddUser()
        self.b = browser
        self.user = user
        self.contact_list_page = ContactList()
        self.login_page = MainPage()

    @allure.step('Кликаем по кнопке регистрации')
    def open(self):
        self.b.element(self.login_page.sign_up).click()

    @allure.step('Заполняем форму регистрации')
    def fill_form(self):
        self.b.element(self.register_page.first_name).type(self.user.first_name)
        self.b.element(self.register_page.last_name).type(self.user.last_name)
        self.b.element(self.register_page.email).type(self.user.email)
        self.b.element(self.register_page.password).type(self.user.password)

    @allure.step('Подтверждаем данные')
    def submit(self):
        self.b.element(self.register_page.submit).click()

    @allure.step('Нажимаем кнопку Cancel')
    def cancel(self):
        self.b.element(self.register_page.cancel).click()

    @allure.step('Проверяем результат успешной регистрации')
    def check_after_positive_register(self, header: str):
        self.b.element(self.contact_list_page.header_text).should(have.text(header))

    @allure.step('Проверяем результат, когда форма регистрации не заполнена')
    def check_after_negative_register(self, name_error: str):
        self.b.element(self.register_page.error).should(have.text(name_error))
