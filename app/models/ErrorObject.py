class ErrorObject:
    error = ""
    code = ""
    msg = ""

    def __init__(self, error, code, msg):
        self.error = error
        self.code = code
        self.msg = msg