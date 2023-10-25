from abc import ABC, abstractmethod
from typing import List
from app.database.models.order import Order
from app.database.models.user import User
from app.domain.requests.order.create import CreateOrderRequest


class OrderAbstractRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Order]:
        """
        Metode abstrak untuk mengambil daftar semua pesanan yang ada dalam repositori.

        Returns:
            List[Order]: Daftar semua pesanan dalam repositori.
        """
        pass

    @abstractmethod
    def create_order(self, request: CreateOrderRequest, current_user: User) -> Order:
        """
        Metode abstrak untuk membuat pesanan baru dan menyimpannya dalam repositori.

        Args:
            order (Order): Objek Order yang akan dibuat dan disimpan dalam repositori.

        Returns:
            Order: Objek Order yang telah dibuat dan disimpan dalam repositori.
        """
        pass

    @abstractmethod
    def order_by_user(self, user_id: int) -> List[Order]:
        """
        Metode abstrak untuk mengambil daftar pesanan berdasarkan ID pengguna.

        Args:
            user_id (int): ID pengguna yang digunakan sebagai kriteria pencarian pesanan.

        Returns:
            List[Order]: Daftar pesanan yang sesuai dengan ID pengguna yang diberikan.
        """
        pass

    @abstractmethod
    def order_by_id(self, order_id: int) -> Order:
        """
        Metode abstrak untuk mengambil pesanan berdasarkan ID pesanan.

        Args:
            order_id (int): ID pesanan yang digunakan sebagai kriteria pencarian pesanan.

        Returns:
            Order: Objek Order yang sesuai dengan ID pesanan yang diberikan.
        """
        pass
