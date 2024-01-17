from .contact_model import ContactModel


class ContactView:
    def __init__(self, contact: ContactModel) -> None:
        self.data = contact

    def create(self) -> dict:
        d = {
            "firstName": self.data.first_name,
            "lastName": self.data.last_name,
            "birthdate": self.data.birthdate,
            "email": self.data.email,
            "phone": self.data.phone,
            "street1": self.data.street1,
            "street2": self.data.street2,
            "city": self.data.city,
            "stateProvince": self.data.state_province,
            "postalCode": self.data.postal_code,
            "country": self.data.country
        }
        return d

    def from_response(self, contact: dict) -> ContactModel:
        self.data.id = contact['_id']
        self.data.first_name = contact['firstName']
        self.data.last_name = contact['lastName']
        self.data.birthdate = contact['birthdate']
        self.data.email = contact['email']
        self.data.phone = contact['phone']
        self.data.street1 = contact['street1']
        self.data.street2 = contact['street2']
        self.data.city = contact['city']
        self.data.state_province = contact['stateProvince']
        self.data.postal_code = contact['postalCode']
        self.data.country = contact['country']
        self.data.owner = contact['owner']
        return self.data
