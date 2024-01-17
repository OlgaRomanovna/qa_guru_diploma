import json

import allure
import requests
from allure_commons.types import AttachmentType
from curlify import to_curl
from requests import sessions


def do_request(method: str, base_url: str, url: str, **kwargs) -> requests:
    current_url = base_url + url
    with allure.step(f'{method.upper()} {base_url}{url}'):
        with sessions.Session() as session:
            resp = session.request(method=method, url=current_url, **kwargs)
            message = to_curl(resp.request)
            allure.attach(body=message.encode('utf8'), name='Curl',
                          attachment_type=AttachmentType.TEXT, extension='txt')
            if resp.text == '' or resp.text == 'Contact deleted':  # в случае ответа, когда тело пустое, то падаем на json.dumps()
                allure.attach(body=resp.text.encode('utf8'), name='empty_response',
                              attachment_type=AttachmentType.JSON, extension='json')
                return resp
            allure.attach(body=json.dumps(resp.json(), indent=4).encode('utf8'), name='response',
                          attachment_type=AttachmentType.JSON, extension='json')
    return resp


def headers(token: str) -> dict:
    return {'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'}
