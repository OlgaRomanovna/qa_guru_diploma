from .login import Login


def auth_web(web_user_for_auth):
    page = Login(web_user_for_auth)
    page.open()
    page.fill_form()
    page.submit()
