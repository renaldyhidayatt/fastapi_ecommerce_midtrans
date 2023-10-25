from typing import List
from sqlalchemy.orm import Session
from app.repository.abstract_class.slider_abstract import SliderAbstractRepository
from app.database.models.slider import Slider
from app.domain.requests.slider.create import CreateSliderRequest
from app.domain.requests.slider.update import UpdateSliderRequest


class SliderRepository(SliderAbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all_sliders(self) -> List[Slider]:
        try:
            return self.session.query(Slider).all()
        except Exception as e:
            raise e

    def get_slider_by_id(self, slider_id) -> Slider:
        try:
            return self.session.query(Slider).filter_by(slider_id=slider_id).first()
        except Exception as e:
            raise e

    def create_slider(self, slider_request: CreateSliderRequest):
        try:
            my_slider = Slider(nama=slider_request.nama, image=slider_request.file_path)

            self.session.add(my_slider)

            self.session.commit()

            self.session.refresh(my_slider)

            return my_slider
        except Exception as e:
            raise e

    def update_slider_by_id(self, slider_id: int, updated_slider: UpdateSliderRequest):
        try:
            my_slider = self.get_slider_by_id(slider_id=slider_id)

            my_slider.nama = updated_slider.nama
            my_slider.image = updated_slider.file_path

            self.session.commit()
            self.session.refresh(my_slider)

            return my_slider

        except Exception as e:
            raise e

    def delete_slider_by_id(self, slider_id: int):
        try:
            my_slider = self.get_slider_by_id(slider_id=slider_id)

            self.session.delete(my_slider)
            self.session.commit()
        except Exception as e:
            raise e
