from abc import ABC, abstractmethod

from typing import List
from app.domain.requests.cart.create import CartRequest
from app.database.models.product import Product


class ProductAbstractService(ABC):
    @abstractmethod
    def get_all_product(self):
        """
        Dapatkan semua produk yang tersedia.

        Returns:
            List[Product]: Daftar objek produk.
        """
        pass

    @abstractmethod
    def create_product(
        self,
        name: str,
        category_id: str,
        description: str,
        price: int,
        countInStock: int,
        weight: int,
        rating: int,
        file_path: str,
    ):
        """
        Tambahkan produk baru ke dalam penyimpanan (repository).

        Args:
            name (str): Nama produk.
            category_id (str): ID kategori produk.
            description (str): Deskripsi produk.
            price (int): Harga produk.
            countInStock (int): Jumlah produk dalam stok.
            weight (int): Berat produk.
            file_path (str): Path ke gambar produk.

        Returns:
            Product: Objek produk yang telah ditambahkan ke penyimpanan.
        """
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        """
        Dapatkan produk berdasarkan ID produk.

        Args:
            product_id (int): ID produk yang akan dicari.

        Returns:
            Product: Objek produk yang sesuai dengan ID tersebut, atau None jika tidak ditemukan.
        """
        pass

    @abstractmethod
    def get_by_slug(self, slug: str) -> Product:
        """
        Dapatkan produk berdasarkan ID produk.

        Args:
            slug (str): ID produk yang akan dicari.

        Returns:
            Product: Objek produk yang sesuai dengan str tersebut, atau None jika tidak ditemukan.
        """
        pass

    @abstractmethod
    def update_product(
        self,
        product_id: int,
        name: str,
        category_id: str,
        description: str,
        price: int,
        countInStock: int,
        weight: int,
        rating: int,
        file_path: str,
    ) -> bool:
        """
        Perbarui informasi produk.

        Args:
            product_id (int): ID produk yang akan diperbarui.
            name (str): Nama produk.
            category_id (str): ID kategori produk.
            description (str): Deskripsi produk.
            price (int): Harga produk.
            countInStock (int): Jumlah produk dalam stok.
            weight (int): Berat produk.
            file_path (str): Path ke gambar produk.

        Returns:
            bool: True jika perbaruan berhasil, False jika tidak.
        """
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> bool:
        """
        Hapus produk berdasarkan ID produk.

        Args:
            product_id (int): ID produk yang akan dihapus.

        Returns:
            bool: True jika penghapusan berhasil, False jika tidak.
        """
        pass

    @abstractmethod
    def update_quantity(self, cart: List[CartRequest]) -> bool:
        """
        Perbarui jumlah (quantity) produk.

        Args:
            cart (List[CartRequest]): Daftar item keranjang yang akan mempengaruhi stok produk.

        Returns:
            bool: True jika perbaruan berhasil, False jika tidak.
        """
        pass
