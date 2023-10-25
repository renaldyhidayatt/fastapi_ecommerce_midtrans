from abc import ABC, abstractmethod
from typing import List


class CartServiceAbstract(ABC):
    @abstractmethod
    def get_cart_items(self, user_id):
        """
        Dapatkan daftar item dalam keranjang untuk seorang pengguna.

        Args:
            user_id (int): ID pengguna yang akan mengambil item keranjangnya.

        Returns:
            List[Cart]: Daftar objek Cart yang mewakili item keranjang pengguna.
        """
        pass

    @abstractmethod
    def add_to_cart(self, user_id, product_id, quantity):
        """
        Tambahkan item ke keranjang pengguna.

        Args:
            user_id (int): ID pengguna yang akan menambahkan item ke keranjang.
            product_id (int): ID produk yang akan ditambahkan ke keranjang.
            quantity (int): Jumlah item yang akan ditambahkan.

        Returns:
            Cart: Objek Cart yang telah ditambahkan ke keranjang pengguna.
        """
        pass

    @abstractmethod
    def remove_from_cart(self, cart_id):
        """
        Hapus item dari keranjang pengguna berdasarkan ID item.

        Args:
            cart_id (int): ID item yang akan dihapus dari keranjang pengguna.

        Returns:
            bool: True jika penghapusan berhasil, False jika tidak.
        """
        pass

    @abstractmethod
    def remove_items_from_cart(self, cart_ids):
        """
        Hapus beberapa item dari keranjang pengguna berdasarkan ID item.

        Args:
            cart_ids (List[int]): Daftar ID item yang akan dihapus dari keranjang pengguna.

        Returns:
            int: Jumlah item yang berhasil dihapus dari keranjang pengguna.
        """
        pass
