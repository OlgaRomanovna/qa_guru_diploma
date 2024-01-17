import requests

from .user_api import UserApi


def register(first_name: str, last_name: str, password: str) -> requests:
    return UserApi().registration(first_name, last_name, password)


def get_profile(token: str):
    return UserApi().get_profile(token)


def auth(email: str, password: str) -> requests:
    return UserApi().log_in(email, password)


def log_out(token: str) -> requests:
    return UserApi().log_out(token)


def delete(token: str) -> requests:
    return UserApi().delete(token)
