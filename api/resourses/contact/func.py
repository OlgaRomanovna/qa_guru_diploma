import requests

from .contact_api import ContactApi
from .contact_model import ContactModel


def add_contact(token: str, contact: ContactModel) -> requests:
    return ContactApi().create(token, contact)


def get_contacts(token: str) -> requests:
    return ContactApi().get_contacts(token)


def get_contact(token: str, contact_id: str) -> requests:
    return ContactApi().get_contact(token, contact_id)


def full_update_contact(token: str, contact_id: str, contact: ContactModel) -> requests:
    return ContactApi().full_update_contact(token, contact_id, contact)


def put_contact(token: str, contact_id: str, part_object: dict) -> requests:
    return ContactApi().put_contact(token, contact_id, part_object)


def delete_contact(token: str, contact_id: str) -> requests:
    return ContactApi().delete_contact(token, contact_id)
