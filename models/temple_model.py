from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from core.database import Base


class Temples(Base):
    __tablename__ = "temples"
    id = Column(Integer, primary_key=True, index=True)
    temple_name = Column(String)
    address = Column(String)
    city_id = Column(Integer)
    state_id = Column(Integer)
    country_id = Column(Integer)
    pincode = Column(String)
    phone_number = Column(String)
    temple_image = Column(String)