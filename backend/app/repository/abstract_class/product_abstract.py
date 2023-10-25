from abc import ABC, abstractmethod
from typing import List
from app.database.models.product import Product
from app.domain.requests.product import create, update


class ProductAbstractRepository(ABC):
    @abstractmethod
    def get_all_product(self) -> List[Product]:
        """
        Dapatkan semua produk yang tersedia.

        Returns:
            List[Product]: Daftar objek produk.
        """
        pass

    @abstractmethod
    def create_product(self, request: create.CreateProductRequest):
        """
        Tambahkan produk baru ke dalam penyimpanan (repository).

        Args:
            product (Product): Objek produk yang akan ditambahkan.

        Returns:
            Product: Objek produk yang telah ditambahkan ke penyimpanan.
        """
        pass

    @abstractmethod
    def get_by_id(self, product_id: int):
        """
        Dapatkan produk berdasarkan ID produk.

        Args:
            product_id (int): ID produk yang akan dicari.

        Returns:
            Product: Objek produk yang sesuai dengan ID tersebut, atau None jika tidak ditemukan.
        """
        pass

    @abstractmethod
    def get_by_slug(self, slug: str):
        """
        Dapatkan produk berdasarkan ID produk.

        Args:
            slug (str): ID produk yang akan dicari.

        Returns:
            Product: Objek produk yang sesuai dengan slug tersebut, atau None jika tidak ditemukan.
        """
        pass

    @abstractmethod
    def my_update_quantity(self, product_id: int, quantity: int):
        """
        Perbarui jumlah (quantity) produk.

        Args:
            product_id (int): ID produk yang akan diperbarui.
            quantity (int): Jumlah produk yang akan diubah.

        Returns:
            bool: True jika perbaruan berhasil, False jika tidak.
        """
        pass

    @abstractmethod
    def update_product(self, product_id: int, request: update.UpdateProductRequest):
        """
        Perbarui informasi produk.

        Args:
            product_id (int): ID produk yang akan diperbarui.
            new_product (Product): Objek produk baru yang berisi informasi perbaruan.

        Returns:
            bool: True jika perbaruan berhasil, False jika tidak.
        """
        pass

    @abstractmethod
    def delete_product(self, product_id: int):
        """
        Hapus produk berdasarkan ID produk.

        Args:
            product_id (int): ID produk yang akan dihapus.

        Returns:
            bool: True jika penghapusan berhasil, False jika tidak.
        """
        pass
