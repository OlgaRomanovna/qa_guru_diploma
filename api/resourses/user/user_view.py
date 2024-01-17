from .user_model import UserModel


class UserView:
    def __init__(self, user: UserModel):
        self.user = user

    def full(self) -> dict:
        d = {
            "firstName": self.user.first_name,
            "lastName": self.user.last_name,
            "email": self.user.email,
            "password": self.user.password
        }
        return d

    def for_auth(self) -> dict:
        d = {
            "email": self.user.email,
            "password": self.user.password
        }
        return d

    def from_response(self, json: dict) -> UserModel:
        self.user.id = json['user']['id']
        self.user.token = json['token']
        return self.user
