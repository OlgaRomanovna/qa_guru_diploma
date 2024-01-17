class Method:
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    PATCH = 'patch'
    DELETE = 'delete'


class StatusCode:
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    UNAUTHORIZED = 401
    NOT_FOUND = 404


class Severity:
    BLOCKER = 'Blocker'
    CRITICAL = 'Critical'
    MAJOR = 'Major'
    MINOR = 'Minor'
    TRIVIAL = 'Trivial'


BASE_URL = 'https://thinking-tester-contact-list.herokuapp.com'
