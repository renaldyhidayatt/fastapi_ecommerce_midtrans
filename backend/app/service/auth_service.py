from .abstract_class.auth_abstract import AuthAbstractService
from app.repository.abstract_class.user_abstract import UserAbstractRepository
from app.domain.requests.user.create import CreateUserRequest
from app.database.models.user import User


class AuthService(AuthAbstractService):
    def __init__(self, user_repository: UserAbstractRepository) -> None:
        self.user_repository = user_repository

    def register_user(self, firstname, lastname, email, password) -> User:
        user = CreateUserRequest(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
        )

        return self.user_repository.create(request=user)

    def login_user(self, email) -> User:
        user = self.user_repository.get_user_by_email(email=email)

        return user
