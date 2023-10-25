from abc import ABC, abstractmethod
from app.database.models.user import User


class AuthAbstractService(ABC):
    @abstractmethod
    def register_user(self, firstname, lastname, email, password) -> User:
        """
        Mendaftarkan pengguna baru.

        Args:
            firstname (str): Nama depan pengguna yang akan didaftarkan.
            lastname (str): Nama belakang pengguna yang akan didaftarkan.
            email (str): Alamat surel pengguna.
            password (str): Kata sandi pengguna.

        Returns:
            User: Objek pengguna yang telah didaftarkan.
        """
        pass

    @abstractmethod
    def login_user(self, email, password) -> User:
        """
        Melakukan proses masuk (login) pengguna.

        Args:
            email (str): Alamat surel pengguna.
            password (str): Kata sandi pengguna.

        Returns:
            User: Objek pengguna yang berhasil masuk, atau None jika gagal.
        """
        pass
