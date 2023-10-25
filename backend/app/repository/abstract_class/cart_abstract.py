from abc import ABC, abstractmethod


class CartAbstractRepository(ABC):
    @abstractmethod
    def find_all_by_user_id(self, user_id):
        """
        Temukan semua item dalam keranjang berdasarkan ID pengguna.

        Args:
            user_id (int): ID pengguna.

        Returns:
            List[Cart]: Daftar objek Cart yang terkait dengan pengguna.
        """
        pass

    @abstractmethod
    def create(self, cart_item):
        """
        Tambahkan item ke keranjang.

        Args:
            cart_item (Cart): Objek Cart yang akan ditambahkan ke keranjang.

        Returns:
            Cart: Objek Cart yang telah ditambahkan ke keranjang.
        """
        pass

    @abstractmethod
    def delete(self, cart_id):
        """
        Hapus item dari keranjang berdasarkan ID item.

        Args:
            cart_id (int): ID item yang akan dihapus dari keranjang.

        Returns:
            bool: True jika penghapusan berhasil, False jika tidak.
        """
        pass

    @abstractmethod
    def delete_many(self, cart_ids):
        """
        Hapus beberapa item dari keranjang berdasarkan ID item.

        Args:
            cart_ids (List[int]): Daftar ID item yang akan dihapus dari keranjang.

        Returns:
            int: Jumlah item yang berhasil dihapus.
        """
        pass
