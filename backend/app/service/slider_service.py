from typing import List
from app.database.models.slider import Slider
from app.repository.abstract_class.slider_abstract import SliderAbstractRepository
from .abstract_class.slider_abstract import SliderAbstractService
from app.domain.requests.slider.create import CreateSliderRequest
from app.domain.requests.slider.update import UpdateSliderRequest


class SliderService(SliderAbstractService):
    def __init__(self, slider_repository: SliderAbstractRepository) -> None:
        self.slider_repository = slider_repository

    def get_all_sliders(self) -> List[Slider]:
        return self.slider_repository.get_all_sliders()

    def get_slider_by_id(self, slider_id) -> Slider:
        return self.slider_repository.get_slider_by_id(slider_id=slider_id)

    def create_slider(self, nama: str, file_path: str):
        request = CreateSliderRequest(nama=nama, file_path=file_path)

        return self.slider_repository.create_slider(slider_request=request)

    def update_slider_by_id(self, slider_id: int, nama: str, file_path: str):
        request = UpdateSliderRequest(nama=nama, file_path=file_path)

        return self.slider_repository(slider_id=slider_id, updated_slider=request)

    def delete_slider_by_id(self, slider_id: int):
        return self.slider_repository.delete_slider_by_id(slider_id=slider_id)
