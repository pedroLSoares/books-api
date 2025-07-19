from repository.users_repository import UsersRepository, SessionDep
from models.User import User
from dto.RegisterUser import RegisterUser
from dto.LoginUser import LoginUser
from fastapi import HTTPException


class UsersService:
    def __init__(self, session: SessionDep):
        self.users_repository = UsersRepository(session)

    def register_user(self, user: RegisterUser):
        newUser = User(name=user.name, email=user.email, password=user.password)
        self.users_repository.create(newUser)

    def get_user_by_email(self, email: str):
        return self.users_repository.get_by_email(email)


    def login_user(self, user: LoginUser):
        user = self.get_user_by_email(user.email)
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        if user.password != user.password:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return user.email