from fastapi import APIRouter, HTTPException
import logging
from services.users_service import UsersService
from dto.RegisterUser import RegisterUser
from dto.LoginUser import LoginUser
from config.database_config import SessionDep
from config.auth_config import oauth2_scheme, verify_jwt_refresh, decode_jwt_refresh, create_access_token
from fastapi import Depends
from dto.LoginResponse import LoginResponse
from dto.RefreshResponse import RefreshResponse

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
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error registering user: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/login', response_model=LoginResponse)
def login_user_handler(req: LoginUser, session: SessionDep):
    """ 
        Login a user returning access and refresh tokens
    """
    try:
        logger.info("Logging in user")
        users_service = UsersService(session)
        tokens = users_service.login_user(req)
        return LoginResponse(access_token=tokens["access_token"], refresh_token=tokens["refresh_token"])
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error on auth: {e.with_traceback()}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/refresh-token', response_model=RefreshResponse)
def refresh_token_handler(refresh_token: str = Depends(oauth2_scheme)):
    """
        Refresh a token returning a new access token
        The refresh token is sent in the authorization header
    """
    try:
        isValid = verify_jwt_refresh(refresh_token)
        if not isValid:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        decoded_token = decode_jwt_refresh(refresh_token)
        token = create_access_token(data={"sub": decoded_token["sub"]})
        return RefreshResponse(token=token)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error on refresh token: {e.with_traceback()}")
        raise HTTPException(status_code=500, detail=str(e))

