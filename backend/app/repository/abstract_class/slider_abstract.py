from abc import ABC, abstractmethod
from app.domain.requests.slider.create import CreateSliderRequest
from app.domain.requests.slider.update import UpdateSliderRequest
from typing import List
from app.database.models.slider import Slider


class SliderAbstractRepository(ABC):
    @abstractmethod
    def get_all_sliders(self) -> List[Slider]:
        """
        Mengambil semua entitas slider dalam penyimpanan.
        """
        pass

    @abstractmethod
    def create_slider(self, slider_request: CreateSliderRequest):
        """
        Membuat entitas slider baru dan menyimpannya dalam penyimpanan.

        Parameters:
            slider_request (CreateSliderRequest): Data yang digunakan untuk membuat slider baru.
        """
        pass

    @abstractmethod
    def get_slider_by_id(self, slider_id: int) -> Slider:
        """
        Mengambil entitas slider berdasarkan ID.

        Parameters:
            slider_id: ID slider yang akan diambil.
        """
        pass

    @abstractmethod
    def update_slider_by_id(self, slider_id: int, updated_slider: UpdateSliderRequest):
        """
        Memperbarui entitas slider yang sudah ada dalam penyimpanan berdasarkan ID.

        Parameters:
            updated_slider (UpdateCategoryRequest): Data yang digunakan untuk memperbarui slider yang ada.
        """
        pass

    @abstractmethod
    def delete_slider_by_id(self, slider_id: int):
        """
        Menghapus entitas slider berdasarkan ID.

        Parameters:
            slider_id: ID slider yang akan dihapus.
        """
        pass
