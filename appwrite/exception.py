class AppwriteException(Exception):
    def __init__(self, message, code=0, error_type=None, response=None):
        self.message = message
        self.code = code
        self.error_type = error_type
        self.response = response
        super().__init__(message)
