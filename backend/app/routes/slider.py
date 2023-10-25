from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    UploadFile,
    File,
    Form,
    status,
    Response,
)
from app.database.models.user import User
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.service.slider_service import SliderService
from app.repository.slider_repository import SliderRepository
from app.core.token import get_currentUser
from cloudinary import uploader


sliderrouter = APIRouter(prefix="/slider", tags=["Slider"])

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


@sliderrouter.get("/")
async def get_all(db: Session = Depends(get_db)):
    try:
        slider_repository = SliderRepository(session=db)
        slider_service = SliderService(slider_repository=slider_repository)

        slider = slider_service.get_all_sliders()

        return slider
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}"
        )


@sliderrouter.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    try:
        slider_repository = SliderRepository(session=db)
        slider_service = SliderService(slider_repository=slider_repository)

        slider = slider_service.get_slider_by_id(slider_id=id)

        return slider

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}"
        )


@sliderrouter.post("/create")
async def create_slider(
    name: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user: User = Depends(get_currentUser),
):
    try:
        slider_repository = SliderRepository(session=db)
        slider_service = SliderService(slider_repository=slider_repository)

        file_extension = file.filename.split(".")[-1]
        if file_extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=400, detail="Jenis file tidak diizinkan")

        response = uploader.upload(file.file)

        slider = slider_service.create_slider(
            nama=name,
            file_path=response["secure_url"],
        )

        return slider
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Gagal mengunggah file: {e}",
        )


@sliderrouter.post("/update/{id}")
async def update_slider(
    id: int,
    name: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user: User = Depends(get_currentUser),
):
    try:
        slider_repository = SliderRepository(session=db)
        slider_service = SliderService(slider_repository=slider_repository)

        file_extension = file.filename.split(".")[-1]
        if file_extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=400, detail="Jenis file tidak diizinkan")

        response = uploader.upload(file.file)

        slider = slider_service.update_slider_by_id(
            slider_id=id,
            nama=name,
            file_path=response["secure_url"],
        )

        return slider
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Gagal mengunggah file: {e}",
        )


@sliderrouter.delete("/{id}")
async def delete_by_id(
    id: int, db: Session = Depends(get_db), user: User = Depends(get_currentUser)
):
    try:
        slider_repository = SliderRepository(session=db)
        slider_service = SliderService(slider_repository=slider_repository)

        slider = slider_service.delete_slider_by_id(slider_id=id)

        return Response(
            content={"message": "delete succefully"}, status_code=status.HTTP_200_OK
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}"
        )
