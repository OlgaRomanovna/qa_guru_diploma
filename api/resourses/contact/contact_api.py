import requests

from api.resourses.contact.contact_model import ContactModel
from api.resourses.contact.contact_view import ContactView
from utils import BASE_URL, Method, do_request, headers


class ContactApi:
    def __init__(self) -> None:
        self.base_url = BASE_URL
        self.endpoint = '/contacts'

    def create(self, token: str, contact: ContactModel):
        resp = do_request(
            method=Method.POST,
            base_url=self.base_url,
            url=self.endpoint,
            headers=headers(token),
            json=ContactView(contact).create()
        )
        return resp

    def get_contacts(self, token: str) -> list:
        resp = do_request(
            method=Method.GET,
            base_url=self.base_url,
            url=self.endpoint,
            headers=headers(token))
        return resp

    def get_contact(self, token: str, contact_id: str) -> requests:
        resp = do_request(
            method=Method.GET,
            base_url=self.base_url,
            url=f'{self.endpoint}/{contact_id}',
            headers=headers(token)
        )
        return resp

    def full_update_contact(self, token: str, contact_id: str, contact: ContactModel):
        resp = do_request(
            method=Method.PUT,
            base_url=self.base_url,
            url=f'{self.endpoint}/{contact_id}',
            headers=headers(token),
            json=ContactView(contact).create()
        )
        return resp

    def put_contact(self, token: str, contact_id: str, part_object: dict):
        resp = do_request(
            method=Method.PATCH,
            base_url=self.base_url,
            url=f'{self.endpoint}/{contact_id}',
            headers=headers(token),
            json=part_object
        )
        return resp

    def delete_contact(self, token: str, contact_id: str):
        resp = do_request(
            method=Method.DELETE,
            base_url=self.base_url,
            url=f'{self.endpoint}/{contact_id}',
            headers=headers(token)
        )
        return resp
