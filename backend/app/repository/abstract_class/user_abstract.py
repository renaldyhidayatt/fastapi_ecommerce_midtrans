from abc import ABC, abstractmethod
from typing import List, Optional
from app.database.models.user import User
from app.domain.requests.user import create, update


class UserAbstractRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[User]:
        """
        Mengambil semua entitas pengguna dalam penyimpanan.
        """
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Mengambil entitas pengguna berdasarkan alamat email.

        Parameters:
            email (str): Alamat email pengguna yang akan diambil.
        """
        pass

    @abstractmethod
    def create(self, request: create.CreateUserRequest):
        """
        Membuat entitas pengguna baru dan menyimpannya dalam penyimpanan.

        Parameters:
            request (CreateUserRequest): Data yang digunakan untuk membuat pengguna baru.
        """
        pass

    @abstractmethod
    def update(self, request: update.UpdateUserRequest):
        """
        Memperbarui entitas pengguna yang sudah ada dalam penyimpanan.

        Parameters:
            request (UpdateUserRequest): Data yang digunakan untuk memperbarui pengguna yang ada.
        """
        pass

    @abstractmethod
    def delete(self, user_id: int):
        """
        Menghapus entitas pengguna dari penyimpanan.

        Parameters:
            user_id (int): ID pengguna yang akan dihapus.
        """
        pass
