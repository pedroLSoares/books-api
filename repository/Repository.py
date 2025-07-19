from config.database_config import SessionDep
from sqlmodel import SQLModel, select

class Repository:

    def __init__(self, model: SQLModel, session: SessionDep):
        self.model = model
        self.session = session

    def get_all(self):
        return self.session.exec(select(self.model)).all()
    
    def create(self, data: SQLModel):
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        return data
