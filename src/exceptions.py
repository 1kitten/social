class ApiKeyNotFoundError(Exception):
    """When no api-key found in headers"""
    pass


class NoUserFoundError(Exception):
    """When no user found"""
    pass

