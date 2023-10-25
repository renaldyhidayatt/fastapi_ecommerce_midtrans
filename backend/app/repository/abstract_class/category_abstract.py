from abc import ABC, abstractmethod
from typing import List
from app.database.models.category import Category
from app.domain.requests.category import create, update


class CategoryAbstractRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Category]:
        """
        Mengambil semua entitas kategori dalam penyimpanan.
        """
        pass

    @abstractmethod
    def create(self, request: create.CreateCategoryRequest):
        """
        Membuat entitas kategori baru dan menyimpannya dalam penyimpanan.

        Parameters:
            request (CreateCategoryRequest): Data yang digunakan untuk membuat kategori baru.
        """
        pass

    @abstractmethod
    def get_by_id(self, category_id) -> Category:
        """
        Mengambil entitas kategori berdasarkan ID.

        Parameters:
            category_id: ID kategori yang akan diambil.
        """
        pass

    @abstractmethod
    def get_by_slug(self, slug: str) -> Category:
        """
        Mengambil entitas kategori berdasarkan ID.

        Parameters:
            slug : slug  yang akan diambil.
        """
        pass

    @abstractmethod
    def update_by_id(self, updated_category: update.UpdateCategoryRequest):
        """
        Memperbarui entitas kategori yang sudah ada dalam penyimpanan berdasarkan ID.

        Parameters:
            updated_category (UpdateCategoryRequest): Data yang digunakan untuk memperbarui kategori yang ada.
        """
        pass

    @abstractmethod
    def delete_by_id(self, category_id):
        """
        Menghapus entitas kategori berdasarkan ID.

        Parameters:
            category_id: ID kategori yang akan dihapus.
        """
        pass
