from sqlmodel import Session, SQLModel, create_engine
from typing import Annotated
from fastapi import Depends
import os
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()


class DatabaseConfig:
    def __init__(self):
        self.engine = create_engine(os.getenv('DATABASE_URL'))

    def init_db(self):
        SQLModel.metadata.create_all(self.engine)
    
    def get_session(self):
        with Session(self.engine) as session:
            yield session

SessionDep = Annotated[Session, Depends(DatabaseConfig().get_session)]