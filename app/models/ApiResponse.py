from .ErrorObject import ErrorObject

class ApiResponse:
    response: ""
    status: ""

    def __init__(self, response, status):
        self.response = response
        self.status = status