from configuration import ALLOWED_USERS


def check_access(email: str) -> bool:
    return email in ALLOWED_USERS
