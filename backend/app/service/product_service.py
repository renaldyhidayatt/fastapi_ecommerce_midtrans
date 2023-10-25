from typing import List
from app.domain.requests.cart.create import CartRequest
from app.database.models.product import Product
from app.domain.requests.product import create, update
from app.repository.abstract_class.product_abstract import ProductAbstractRepository
from app.service.abstract_class.product_abstract import ProductAbstractService


class ProductService(ProductAbstractService):
    def __init__(self, product_repository: ProductAbstractRepository):
        self.product_repository = product_repository

    def get_all_product(self) -> List[Product]:
        return self.product_repository.get_all_product()

    def create_product(
        self,
        name: str,
        category_id: str,
        description: str,
        price: int,
        countInStock: int,
        weight: int,
        rating: int,
        file_path: str,
    ):
        request = create.CreateProductRequest(
            name=name,
            category_id=category_id,
            description=description,
            price=price,
            countInStock=countInStock,
            weight=weight,
            rating=rating,
            file_path=file_path,
        )

        return self.product_repository.create_product(request=request)

    def get_by_id(self, product_id: int) -> Product:
        product = self.product_repository.get_by_id(product_id=product_id)

        return product

    def get_by_slug(self, slug: str) -> Product:
        product = self.product_repository.get_by_slug(slug=slug)

        response = {
            "product_id": product.product_id,
            "name": product.name,
            "slug_product": product.slug_product,
            "image_product": product.image_product,
            "description": product.description,
            "price": product.price,
            "weight": product.weight,
            "brand": product.brand,
            "rating": product.rating,
            "countInStock": product.count_in_stock,
            "reviews": product.reviews_user,
        }

        return response

    def update_product(
        self,
        product_id: int,
        name: str,
        category_id: str,
        description: str,
        price: int,
        countInStock: int,
        weight: int,
        rating: int,
        brand: str,
        file_path: str,
    ) -> bool:
        try:
            request = update.UpdateProductRequest(
                name=name,
                category_id=category_id,
                description=description,
                price=price,
                countInStock=countInStock,
                weight=weight,
                rating=rating,
                brand=brand,
                file_path=file_path,
            )

            return self.product_repository.update_product(product_id, request=request)
        except Exception as e:
            return e

    def delete_product(self, product_id: int) -> bool:
        try:
            return self.product_repository.delete_product(product_id)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False

    def update_quantity(self, cart: List[CartRequest]) -> bool:
        if not cart or len(cart) == 0:
            raise ValueError("No cart data received")

        try:
            for item in cart:
                product_id = item.product_id
                quantity = item.quantity

                product = self.get_by_id(product_id=product_id)
                current_stock = product.countInStock

                new_stock = current_stock - quantity

                result = self.product_repository.my_update_quantity(
                    product_id=product_id, quantity=new_stock
                )

                return result
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False
