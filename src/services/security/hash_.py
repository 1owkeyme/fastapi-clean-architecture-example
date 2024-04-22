import bcrypt

from domain.interfaces import security as security_interfaces


class BCryptHashService(security_interfaces.HashService):
    _UTF8 = "utf-8"

    @staticmethod
    def hash_utf8_password_to_hex(password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(
            password=password.encode(BCryptHashService._UTF8),
            salt=salt,
        ).hex()

    @staticmethod
    def check_utf8_password(password: str, hashed_password_hex: str) -> bool:
        hashed_password = bytes.fromhex(hashed_password_hex)
        return bcrypt.checkpw(
            password=password.encode(BCryptHashService._UTF8),
            hashed_password=hashed_password,
        )
