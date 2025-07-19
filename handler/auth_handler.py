from fastapi import APIRouter, HTTPException
import logging
from services.users_service import UsersService
from dto.RegisterUser import RegisterUser
from dto.LoginUser import LoginUser
from config.database_config import SessionDep

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["auth"]
)

@router.post('/register')
def register_user_handler(req: RegisterUser, session: SessionDep):
    """
        Register a new user
    """
    try:
        logger.info("Registering user")
        users_service = UsersService(session)
        users_service.register_user(req)
        return {"status": "created"}
    except Exception as e:
        logger.error(f"Error registering user: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/login')
def login_user_handler(req: LoginUser, session: SessionDep):
    """ 
        Login a user
    """
    try:
        logger.info("Logging in user")
        users_service = UsersService(session)
        token = users_service.login_user(req)
        return {"status": "logged in", "token": token}
    except Exception as e:
        logger.error(f"Error on auth: {e}")
        raise HTTPException(status_code=500, detail=str(e))



