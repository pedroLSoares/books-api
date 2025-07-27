from sqlmodel import Session, SQLModel, create_engine
from typing import Annotated
from fastapi import Depends
import os
import logging

logger = logging.getLogger(__name__)

class DatabaseConfig:
    def __init__(self):
        self.sqlite_file_name = os.path.join('/tmp', 'database.db')
        self.sqlite_url = f"sqlite:///{self.sqlite_file_name}"
        self.connect_args = {"check_same_thread": False}
        self.engine = create_engine(self.sqlite_url, connect_args=self.connect_args)

    def init_db(self):
        SQLModel.metadata.create_all(self.engine)
        logger.info(f"Database initialized at {self.sqlite_file_name}")


    
    def get_session(self):
        with Session(self.engine) as session:
            yield session

SessionDep = Annotated[Session, Depends(DatabaseConfig().get_session)]