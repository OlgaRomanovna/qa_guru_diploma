class MainPage:
    def __init__(self):
        self.url = '/login'
        self.email = '#email'
        self.password = '#password'
        self.submit = '#submit'
        self.link_api_doc = 'body > div:nth-child(3) > a'
        self.header = 'body > h1'
        self.sub_header = 'body > div:nth-child(2)'
        self.error_after_login = '#error'
        self.sign_up = '#signup'


class ContactList:
    def __init__(self):
        self.url = '/contactList'
        self.header_text = 'body > div > header > h1'
        self.sub_header_text = 'body > div > p:nth-child(2)'
        self.add_new_contact = '#add-contact'
        self.logout = '#logout'
        self.name = '#myTable > tr:nth-child(3) > td:nth-child(2)'
        self.birthdate = '#myTable > tr:nth-child(3) > td:nth-child(3)'
        self.email = '#myTable > tr:nth-child(3) > td:nth-child(4)'
        self.phone = '#myTable > tr:nth-child(3) > td:nth-child(5)'
        self.address = '#myTable > tr:nth-child(3) > td:nth-child(6)'
        self.city_state_province_postal_code = '#myTable > tr:nth-child(3) > td:nth-child(7)'
        self.country = '#myTable > tr:nth-child(7) > td:nth-child(8)'


class ContactWeb:
    def __init__(self):
        self.first_name = '#firstName'
        self.last_name = '#lastName'
        self.birthdate = '#birthdate'
        self.email = '#email'
        self.phone = '#phone'
        self.street1 = '#street1'
        self.street2 = '#street2'
        self.city = '#city'
        self.state_province = '#stateProvince'
        self.postal_code = '#postalCode'
        self.country = '#country'
        self.submit = '#submit'
        self.cancel = '#cancel'


class AddUser:
    def __init__(self):
        self.url = '/addUser'
        self.first_name = '#firstName'
        self.last_name = '#lastName'
        self.email = '#email'
        self.password = '#password'
        self.submit = '#submit'
        self.cancel = '#cancel'
        self.error = '#error'
