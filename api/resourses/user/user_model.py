class UserModel:
    def __init__(self, _id: str = None, first_name: str = None, last_name: str = None, email: str = None,
                 password: str = None, token: str = None):
        self.id = _id
        self.first_name = first_name if first_name else 'test'
        self.last_name = last_name if first_name else 'test'
        self.email = f'{self.first_name.lower()}_{self.last_name.lower()}@gmail.com' if not email else email
        self.password = password
        self.token = token
