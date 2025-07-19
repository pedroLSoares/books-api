from repository.users_repository import UsersRepository, SessionDep
from models.User import User
from dto.RegisterUser import RegisterUser
from dto.LoginUser import LoginUser
from fastapi import HTTPException
from config.auth_config import verify_password, get_password_hash, create_access_token, decode_jwt, create_refresh_token

class UsersService:
    def __init__(self, session: SessionDep):
        self.users_repository = UsersRepository(session)

    def register_user(self, user: RegisterUser):
        existingUser = self.get_user_by_email(user.email)
        if existingUser is not None:
            raise HTTPException(status_code=400, detail="User already exists")
        hashed_password = get_password_hash(user.password)
        newUser = User(name=user.name, email=user.email, password=hashed_password)
        self.users_repository.create(newUser)

    def get_user_by_email(self, email: str):
        return self.users_repository.get_by_email(email)


    def login_user(self, user: LoginUser):
        foundUser = self.get_user_by_email(user.email)
        if foundUser is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        if not verify_password(user.password, foundUser.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {
            "access_token": create_access_token(data={"sub": foundUser.email}),
            "refresh_token": create_refresh_token(data={"sub": foundUser.email})
        }
    
    def refresh_token(self, token: str):
        decoded_token = decode_jwt(token)
        if decoded_token is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return create_access_token(data={"sub": decoded_token["sub"]})