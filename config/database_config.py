from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated
from fastapi import Depends

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

class DatabaseConfig:
    def __init__(self):
        self.sqlite_file_name = "database.db"
        self.sqlite_url = f"sqlite:///{self.sqlite_file_name}"
        self.connect_args = {"check_same_thread": False}
        self.engine = create_engine(self.sqlite_url, connect_args=self.connect_args)

    def init_db(self):
        SQLModel.metadata.create_all(self.engine)

    
    def get_session(self):
        with Session(self.engine) as session:
            yield session

SessionDep = Annotated[Session, Depends(DatabaseConfig().get_session)]