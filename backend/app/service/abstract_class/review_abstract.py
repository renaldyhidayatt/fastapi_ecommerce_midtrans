from abc import ABC, abstractmethod
from app.domain.requests.review.create import ReviewRequest
from app.database.models.user import User

class ReviewAbstractService(ABC):
    @abstractmethod
    def get_all_reviews(self):
        """
        Dapatkan semua ulasan (reviews) yang ada.

        Returns:
            List[Review]: Daftar objek ulasan (reviews).
        """
        pass

    @abstractmethod
    def get_review_by_id(self, review_id):
        """
        Dapatkan ulasan (review) berdasarkan ID ulasan.

        Args:
            review_id (int): ID ulasan yang akan dicari.

        Returns:
            Review: Objek ulasan (review) yang sesuai dengan ID tersebut, atau None jika tidak ditemukan.
        """
        pass

    @abstractmethod
    def create_review(self, product_id: int, request: ReviewRequest, current_user: User):
        """
        Tambahkan ulasan baru ke dalam penyimpanan (repository).

        Args:
            name (str): Nama pengguna yang memberikan ulasan.
            comment (str): Komentar atau isi ulasan.
            rating (int): Rating ulasan.
            user_id (int): ID pengguna yang memberikan ulasan.
            product_id (int): ID produk yang diulas.

        Returns:
            Review: Objek ulasan yang telah ditambahkan ke penyimpanan.
        """
        pass
