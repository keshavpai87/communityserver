from sqlalchemy.orm import Session

from models.temple_model import Temples
from repositories.temple_repository import TempleRepository


class TempleRepositoryImpl(TempleRepository):

    def __init__(self, db: Session):

        self.db = db

    def get_all_temples(self):

        return self.db.query(Temples).all()
    
    # NOTE: Repository should ONLY communicate with database.