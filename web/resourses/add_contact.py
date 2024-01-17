import allure
from selene import have

from api.resourses.contact import ContactModel
from config import browser
from .pages import ContactList, ContactWeb


class AddContact:
    def __init__(self, contact: ContactModel):
        self.b = browser
        self.contact_list_page = ContactList()
        self.url = '/addContact'
        self.data_contact = contact
        self.add_contact_page = ContactWeb()

    @allure.step('Кликаем по кнопке "Add a New Contact" ')
    def open(self):
        self.b.element(self.contact_list_page.add_new_contact).click()

    @allure.step('Заполняем форму контакта')
    def fill_form(self):
        self.b.element(f'{self.add_contact_page.first_name}').type(self.data_contact.first_name)
        self.b.element(f'{self.add_contact_page.last_name}').type(self.data_contact.last_name)
        self.b.element(f'{self.add_contact_page.birthdate}').type(self.data_contact.birthdate)
        self.b.element(f'{self.add_contact_page.email}').type(self.data_contact.email)
        self.b.element(f'{self.add_contact_page.phone}').type(self.data_contact.phone)
        self.b.element(f'{self.add_contact_page.street1}').type(self.data_contact.street1)
        self.b.element(f'{self.add_contact_page.street2}').type(self.data_contact.street2)
        self.b.element(f'{self.add_contact_page.city}').type(self.data_contact.city)
        self.b.element(f'{self.add_contact_page.state_province}').type(self.data_contact.state_province)
        self.b.element(f'{self.add_contact_page.postal_code}').type(self.data_contact.postal_code)
        self.b.element(f'{self.add_contact_page.country}').type(self.data_contact.country)

    @allure.step('Подтверждаем введённые данные')
    def submit(self):
        self.b.element(self.add_contact_page.submit).click()

    @allure.step('Проверяем результат в общем списке контактов')
    def check_result(self):
        self.b.element(self.contact_list_page.name).should(have.text(
            f'{self.data_contact.first_name}'))
        self.b.element(self.contact_list_page.birthdate).should(have.text(f'{self.data_contact.birthdate}'))
        self.b.element(self.contact_list_page.email).should(have.text(f'{self.data_contact.email}'))
        self.b.element(self.contact_list_page.address).should(have.text(
            f'{self.data_contact.street1} {self.data_contact.street2}'))
        self.b.element(self.contact_list_page.city_state_province_postal_code).should(have.text(
            f'{self.data_contact.city} {self.data_contact.state_province} {self.data_contact.postal_code}'
        ))
        self.b.element(self.contact_list_page.country).should(have.text(self.data_contact.country))
