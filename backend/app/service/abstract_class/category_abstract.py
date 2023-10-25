from abc import ABC, abstractmethod
from typing import List
from app.database.models.category import Category
from app.domain.requests.category import create


class CategoryAbstractService(ABC):
    @abstractmethod
    def get_all_categories(self) -> List[Category]:
        """Mengambil semua kategori."""
        pass

    @abstractmethod
    def get_category_by_id(self, category_id: int) -> Category:
        """Mengambil kategori berdasarkan ID."""
        pass

    @abstractmethod
    def get_category_by_slug(self, slug: str) -> Category:
        """Mengambil kategori berdasarkan slug."""
        pass

    @abstractmethod
    def create_category(self, name: str, file_path: str):
        """
        Membuat kategori
        """

        pass

    @abstractmethod
    def update_category_by_id(self, category_id: int, name: str, file_path: str):
        """Memperbarui kategori berdasarkan ID."""
        pass

    @abstractmethod
    def delete_category_by_id(self, category_id):
        """Menghapus kategori berdasarkan ID."""
        pass
