from abc import ABC, abstractmethod


class PasswordService(ABC):
    @staticmethod
    @abstractmethod
    def hash_utf8_password_to_hex(password: str) -> str:
        pass

    @staticmethod
    @abstractmethod
    def check_utf8_password(password: str, hashed_password_hex: str) -> bool:
        pass
