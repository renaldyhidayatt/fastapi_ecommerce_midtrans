from abc import ABC, abstractmethod
from typing import List

from app.domain.requests.slider.create import CreateSliderRequest
from app.domain.requests.slider.update import UpdateSliderRequest
from app.database.models.slider import Slider


class SliderAbstractService(ABC):
    @abstractmethod
    def get_all_sliders(self) -> List[Slider]:
        """
        Get a list of all sliders.

        Returns:
        List[Slider]: A list of Slider objects.
        """
        pass

    @abstractmethod
    def get_slider_by_id(self, slider_id) -> Slider:
        """
        Get a slider by its ID.

        Args:
        slider_id: int - The ID of the slider to retrieve.

        Returns:
        Slider: The Slider object with the specified ID.
        """
        pass

    @abstractmethod
    def create_slider(self, slider_request: CreateSliderRequest):
        """
        Create a new slider.

        Args:
        slider_request: CreateSliderRequest - Data for creating a new slider.

        Returns:
        Slider: The created Slider object.
        """
        pass

    @abstractmethod
    def update_slider_by_id(self, slider_id: int, updated_slider: UpdateSliderRequest):
        """
        Update a slider by its ID.

        Args:
        slider_id: int - The ID of the slider to update.
        updated_slider: UpdateSliderRequest - Data for updating the slider.

        Returns:
        Slider: The updated Slider object.
        """
        pass

    @abstractmethod
    def delete_slider_by_id(self, slider_id: int):
        """
        Delete a slider by its ID.

        Args:
        slider_id: int - The ID of the slider to delete.
        """
        pass
