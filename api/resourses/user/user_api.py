import requests

from utils import BASE_URL, Method, do_request, headers
from .user_model import UserModel
from .user_view import UserView


class UserApi:
    def __init__(self) -> None:
        self.base_url = BASE_URL
        self.endpoint = '/users'

    def registration(self, first_name: str, last_name: str, password: str) -> requests:
        data = UserView(UserModel(first_name=first_name, last_name=last_name, password=password)).full()
        resp = do_request(
            method=Method.POST,
            base_url=self.base_url,
            url=f'{self.endpoint}',
            json=data
        )
        return resp

    def get_profile(self, token: str) -> requests:
        resp = do_request(
            method=Method.GET,
            base_url=self.base_url,
            url=f'{self.endpoint}/me',
            headers=headers(token)
        )
        return resp

    def log_in(self, email: str, password: str) -> requests:
        resp = do_request(
            method=Method.POST,
            base_url=self.base_url,
            url=f'{self.endpoint}/login',
            json=UserView(UserModel(email=email, password=password)).for_auth()

        )
        return resp

    def log_out(self, token):
        resp = do_request(
            method=Method.POST,
            base_url=self.base_url,
            url=f'{self.endpoint}/logout',
            headers=headers(token)
        )
        return resp

    def delete(self, token):
        resp = do_request(
            method=Method.DELETE,
            base_url=self.base_url,
            url=f'{self.endpoint}/me',
            headers=headers(token)
        )
        return resp
