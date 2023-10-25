from sqlalchemy.orm import Session
from app.repository.abstract_class.category_abstract import CategoryAbstractRepository
from app.database.models.category import Category
from app.domain.requests.category import create, update
from slugify import slugify


class CategoryRepository(CategoryAbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        """
        Mengambil semua entitas kategori dalam penyimpanan.
        """
        try:
            return self.session.query(Category).all()
        except Exception as e:
            raise e

    def get_by_id(self, category_id: int):
        """
        Mengambil entitas kategori berdasarkan ID.

        Parameters:
            id (int): ID kategori yang akan diambil.
        """
        try:
            return (
                self.session.query(Category).filter_by(category_id=category_id).first()
            )
        except Exception as e:
            raise e

    def get_by_slug(self, slug: str):
        try:
            category = (
                self.session.query(Category).filter_by(slug_category=slug).first()
            )

            return category
        except Exception as e:
            raise e

    def create(self, request: create.CreateCategoryRequest):
        try:
            slug_category = slugify(request.name)

            my_category = Category(
                name_category=request.name,
                slug_category=slug_category,
                image_category=request.file_path,
            )
            self.session.add(my_category)

            self.session.commit()

            self.session.refresh(my_category)

            return my_category
        except Exception as e:
            raise e

    def update_by_id(self, updated_category: update.UpdateCategoryRequest):
        try:
            category = self.get_by_id(updated_category.id)

            category.name_category = updated_category.name
            category.slug_category = slugify(updated_category.name)
            category.image_category = updated_category.file_path

            self.session.commit()
            self.session.refresh(category)

            return category
        except Exception as e:
            raise e

    def delete_by_id(self, category_id):
        try:
            category = self.get_by_id(category_id)
            if category:
                self.session.delete(category)
                self.session.commit()
        except Exception as e:
            raise e
