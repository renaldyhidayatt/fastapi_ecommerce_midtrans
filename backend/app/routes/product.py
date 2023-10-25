from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from app.core.database import get_db
from sqlalchemy.orm import Session
from cloudinary import uploader
from app.database.models.user import User
from app.service.product_service import ProductService
from app.core.token import get_currentUser
from app.repository.product_repository import ProductRepository


productrouter = APIRouter(prefix="/product", tags=["Product"])

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


@productrouter.get("/hello")
def hello():
    return "Hello"


@productrouter.get("/")
async def get_all(db: Session = Depends(get_db)):
    try:
        product_repository = ProductRepository(session=db)

        product_service = ProductService(product_repository=product_repository)

        product_all = product_service.get_all_product()

        return product_all
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@productrouter.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    try:
        product_repository = ProductRepository(session=db)

        product_service = ProductService(product_repository=product_repository)

        product_by_id = product_service.get_by_id(product_id=id)

        return product_by_id

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@productrouter.get("/slug/{slug}")
async def get_by_slug(slug: str, db: Session = Depends(get_db)):
    try:
        product_repository = ProductRepository(session=db)

        product_service = ProductService(product_repository=product_repository)

        product_by_slug = product_service.get_by_slug(slug=slug)

        return product_by_slug

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@productrouter.post("/create")
async def create_product(
    name: str = Form(...),
    category_id: str = Form(...),
    description: str = Form(...),
    price: int = Form(...),
    countInStock: int = Form(...),
    weight: int = Form(...),
    rating: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    try:
        product_repository = ProductRepository(db)
        product_service = ProductService(product_repository=product_repository)

        file_extension = file.filename.split(".")[-1]
        if file_extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=400, detail="Jenis file tidak diizinkan")

        response_file = uploader.upload(file.file)

        my_product = product_service.create_product(
            name=name,
            category_id=category_id,
            description=description,
            price=price,
            countInStock=countInStock,
            weight=weight,
            rating=rating,
            file_path=response_file["secure_url"],
        )

        return my_product
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gagal mengunggah file: {e}")


@productrouter.put("/update/{id}")
async def update_product(
    id: int,
    name: str = Form(...),
    category_id: str = Form(...),
    description: str = Form(...),
    price: int = Form(...),
    countInStock: int = Form(...),
    weight: int = Form(...),
    rating: int = Form(...),
    brand: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    try:
        product_repository = ProductRepository(db)
        product_service = ProductService(product_repository=product_repository)

        file_extension = file.filename.split(".")[-1]
        if file_extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=400, detail="Jenis file tidak diizinkan")

        response_file = uploader.upload(file.file)

        my_product = product_service.update_product(
            product_id=id,
            name=name,
            category_id=category_id,
            description=description,
            price=price,
            countInStock=countInStock,
            weight=weight,
            rating=rating,
            brand=brand,
            file_path=response_file["secure_url"],
        )

        return my_product
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gagal mengunggah file: {e}")


@productrouter.delete("/{id}")
async def delete_byId(
    id: int, db: Session = Depends(get_db), user: User = Depends(get_currentUser)
):
    try:
        product_repository = ProductRepository(db)
        product_service = ProductService(product_repository=product_repository)

        product = product_service.delete_product(product_id=id)

        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
