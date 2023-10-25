from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    UploadFile,
    File,
    Form,
    Response,
    status,
)
from app.core.database import get_db
from sqlalchemy.orm import Session
from cloudinary import uploader
from app.database.models.user import User
from app.service.category_service import CategoryService
from app.core.token import get_currentUser, role_permission_middleware
from app.repository.category_repository import CategoryRepository

categoryrouter = APIRouter(prefix="/category", tags=["Category"])

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


@categoryrouter.get(
    "/hello",
)
def hello():
    return "Hello"


@categoryrouter.get("/admin_only", response_model=str)
async def admin_only(current_user: User = Depends(role_permission_middleware)):
    return "Welcome, Admin!"


@categoryrouter.get("/")
async def get_all(db: Session = Depends(get_db)):
    try:
        category_repository = CategoryRepository(db)
        category_service = CategoryService(category_repository=category_repository)

        categories = category_service.get_all_categories()

        return categories

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}"
        )


@categoryrouter.get("/slug/{slug}")
async def get_by_slug(slug: str, db: Session = Depends(get_db)):
    try:
        category_repository = CategoryRepository(db)
        category_service = CategoryService(category_repository=category_repository)

        category = category_service.get_category_by_slug(slug=slug)

        return category
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}"
        )


@categoryrouter.get("/{id}")
async def get_by_id(
    id: int, db: Session = Depends(get_db), user: User = Depends(get_currentUser)
):
    try:
        category_repository = CategoryRepository(db)
        category_service = CategoryService(category_repository=category_repository)

        category = category_service.get_category_by_id(category_id=id)

        return category
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}"
        )


@categoryrouter.post("/create")
async def create_category(
    name: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user: User = Depends(get_currentUser),
):
    try:
        category_repository = CategoryRepository(db)
        category_service = CategoryService(category_repository=category_repository)

        file_extension = file.filename.split(".")[-1]
        if file_extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=400, detail="Jenis file tidak diizinkan")

        response = uploader.upload(file.file)

        my_category = category_service.create_category(
            name=name, file_path=response["secure_url"]
        )

        return my_category
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Gagal mengunggah file: {e}",
        )


@categoryrouter.put("/update/{id}")
async def update_category(
    id: int,
    name: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user: User = Depends(get_currentUser),
):
    try:
        category_repository = CategoryRepository(db)
        category_service = CategoryService(category_repository=category_repository)

        file_extension = file.filename.split(".")[-1]
        if file_extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=400, detail="Jenis file tidak diizinkan")

        response = uploader.upload(file.file)

        my_category = category_service.update_category_by_id(
            category_id=id, name=name, file_path=response["secure_url"]
        )

        return my_category
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Gagal mengunggah file: {e}",
        )


@categoryrouter.delete("/{id}")
async def delete_byId(
    id: int, db: Session = Depends(get_db), user: User = Depends(get_currentUser)
):
    try:
        category_repository = CategoryRepository(db)
        category_service = CategoryService(category_repository=category_repository)

        category = category_service.delete_category_by_id(category_id=id)

        return {"message": "delete succefully"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}"
        )
