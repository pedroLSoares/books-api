from repository.Repository import Repository
from config.database_config import SessionDep
from sqlmodel import select
from models.User import User

class UsersRepository(Repository):

    def __init__(self, session: SessionDep):
        super().__init__(User, session)

    def get_by_email(self, email: str):
        return self.session.exec(select(self.model).where(self.model.email == email)).first()
