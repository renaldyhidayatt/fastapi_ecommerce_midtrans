from typing import List
from sqlalchemy.orm import Session
from app.database.models.product import Product
from app.domain.requests.product import create, update
from app.repository.abstract_class.product_abstract import ProductAbstractRepository
from slugify import slugify


class ProductRepository(ProductAbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all_product(self):
        try:
            product = self.session.query(Product).all()

            return product
        except Exception as e:
            return e

    def get_by_slug(self, slug: str):
        try:
            product = (
                self.session.query(Product).filter(Product.slug_product == slug).first()
            )

            return product
        except Exception as e:
            return e

    def create_product(self, request: create.CreateProductRequest):
        try:
            slug_product = slugify(request.name)

            new_product = Product(
                name=request.name,
                slug_product=slug_product,
                image_product=request.file_path,
                description=request.description,
                price=request.price,
                weight=request.weight,
                category_id=request.category_id,
                count_in_stock=request.countInStock,
                rating=request.rating,
            )

            self.session.add(new_product)

            self.session.commit()

            self.session.refresh(new_product)

            return new_product
        except Exception as e:
            return e

    def get_by_id(self, product_id: int) -> Product:
        try:
            return (
                self.session.query(Product)
                .filter(Product.product_id == product_id)
                .first()
            )
        except Exception as e:
            return e

    def my_update_quantity(self, product_id: int, quantity: int) -> bool:
        try:
            db_product = self.get_by_id(product_id)
            if db_product:
                db_product.quantity = quantity
                self.session.commit()
                return True
            return False
        except Exception as e:
            return e

    def update_product(
        self, product_id: int, request: update.UpdateProductRequest
    ) -> Product:
        try:
            slug_product = slugify(request.name)

            db_product = self.get_by_id(product_id)
            if db_product:
                db_product.name = request.name
                db_product.slug_product = slug_product
                db_product.image_product = request.file_path
                db_product.description = request.description
                db_product.price = request.price
                db_product.weight = request.weight
                db_product.category_id = request.category_id
                db_product.brand = request.brand
                db_product.count_in_stock = request.countInStock
                db_product.rating = request.rating

                self.session.commit()
                self.session.refresh(db_product)

                return db_product
            return False
        except Exception as e:
            return False

    def delete_product(self, product_id: int) -> bool:
        try:
            db_product = self.get_by_id(product_id)
            if db_product:
                self.session.delete(db_product)
                self.session.commit()
                return True
            return False
        except Exception as e:
            return e
