class ContactModel:
    def __init__(self, _id: str = None, first_name: str = None, last_name: str = None, birthdate: str = None,
                 email: str = None, phone: str = None, street1: str = None, street2: str = None, city: str = None,
                 state_province: str = None, postal_code: str = None, country: str = None, owner: str = None):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.owner = owner
