from app.domain.requests.user import create, update
from .abstract_class.user_abstract import UserAbstractService
from app.repository.abstract_class.user_abstract import UserAbstractRepository


class UserService(UserAbstractService):
    def __init__(self, user_repository: UserAbstractRepository):
        self.user_repository = user_repository

    def get_all_users(self):
        try:
            return self.user_repository.get_all()
        except Exception as e:
            raise e

    def get_user_by_email(self, email: str):
        try:
            return self.user_repository.get_user_by_email(email)
        except Exception as e:
            raise e

    def create_user(self, firstname: str, lastname: str, email: str, password: str):
        try:
            user = create.CreateUserRequest(
                firstname=firstname,
                lastname=lastname,
                email=email,
                password=password,
            )

            return self.user_repository.create(request=user)
        except Exception as e:
            raise e

    def update_user(
        self,
        user_id: int,
        firstname: str,
        lastname: str,
        role: str,
        email: str,
        password: str,
    ):
        try:
            user = update.UpdateUserRequest(
                id=user_id,
                firstname=firstname,
                lastname=lastname,
                email=email,
                role=role,
                password=password,
            )

            return self.user_repository.update(request=user)
        except Exception as e:
            raise e

    def delete_user(self, user_id: int):
        try:
            self.user_repository.delete(user_id)
        except Exception as e:
            raise e
