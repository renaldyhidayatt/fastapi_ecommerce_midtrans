from abc import ABC, abstractmethod
from app.domain.requests.review.create import ReviewRequest


class ReviewAbstractRepository(ABC):
    @abstractmethod
    def get_all(self):
        """
        Dapatkan semua ulasan (reviews) yang ada.

        Returns:
            List[Review]: Daftar objek ulasan (reviews).
        """
        pass

    @abstractmethod
    def get_by_id(self, review_id):
        """
        Dapatkan ulasan (review) berdasarkan ID ulasan.

        Args:
            review_id (int): ID ulasan yang akan dicari.

        Returns:
            Review: Objek ulasan (review) yang sesuai dengan ID tersebut, atau None jika tidak ditemukan.
        """
        pass

    @abstractmethod
    def create_review(
        self, name: str, comment: str, rating: int, user_id: int, product_id: int
    ):
        """
        Tambahkan ulasan baru ke dalam penyimpanan (repository).

        Args:
            review (Review): Objek ulasan yang akan ditambahkan.

        Returns:
            Review: Objek ulasan yang telah ditambahkan ke penyimpanan.
        """
        pass
