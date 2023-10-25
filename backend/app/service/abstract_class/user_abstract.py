from abc import ABC, abstractmethod
from typing import List, Optional
from app.database.models.user import User
from app.domain.requests.user.create import CreateUserRequest
from app.domain.requests.user.update import UpdateUserRequest


class UserAbstractService(ABC):
    @abstractmethod
    def get_all_users(self) -> List[User]:
        """
        Mengambil semua entitas pengguna dalam penyimpanan.
        :return: Daftar entitas pengguna.
        """
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Mengambil entitas pengguna berdasarkan alamat email.
        :param email: Alamat email pengguna yang ingin diambil.
        :return: Entitas pengguna jika ditemukan, atau None jika tidak ada.
        """
        pass

    @abstractmethod
    def create_user(
        self, firstname: str, lastname: str, email: str, password: str, role: str
    ) -> User:
        """
        Membuat entitas pengguna baru dan menyimpannya dalam penyimpanan.
        :param request: Data permintaan untuk membuat pengguna baru.
        :return: Entitas pengguna yang baru dibuat.
        """
        pass

    @abstractmethod
    def update_user(
        self,
        user_id: int,
        firstname: str,
        lastname: str,
        email: str,
        password: str,
        role: str,
    ) -> User:
        """
        Memperbarui entitas pengguna yang sudah ada dalam penyimpanan.
        :param request: Data permintaan untuk pembaruan pengguna.
        :return: Entitas pengguna yang sudah diperbarui.
        """
        pass

    @abstractmethod
    def delete_user(self, user_id: int):
        """
        Menghapus entitas pengguna dari penyimpanan.
        :param user_id: ID pengguna yang akan dihapus.
        """
        pass
