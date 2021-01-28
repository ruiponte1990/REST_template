"""
Use custom exceptions to determine API response
"""

class BadRequestException(Exception):
    """
    Raise this for 400
    """
    pass

class UnauthorizedException(Exception):
    """
    Raise this for 401
    """
    pass

class MethodNotAllowedException(Exception):
    """
    Raise this for 405
    """
    pass

class ConflictException(Exception):
    """
    Raise this for 409
    """
    pass

class NoContentException(Exception):
    """
    Raise this for 204
    """
    pass