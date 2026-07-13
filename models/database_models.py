from asyncio.windows_events import NULL

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Role(Base) : 
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String)

class Countries(Base) :
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, index=True)
    shortname = Column(String)
    name = Column(String)
    phonecode = Column(Integer)

class States(Base) :
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    country_id = Column(Integer)

class Cities(Base) :
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    state_id = Column(Integer)

class Users(Base) :
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    email = Column(String)
    user_password = Column(String)
    role_id = Column(Integer)
    p_address = Column(String)
    c_address = Column(String)
    mobile_number = Column(String)
    p_country_id = Column(Integer)
    p_state_id = Column(Integer)
    p_city_id = Column(Integer)
    p_pincode = Column(String)
    c_country_id = Column(Integer)
    c_state_id = Column(Integer)
    c_city_id = Column(Integer)
    c_pincode = Column(String)
    temple_id = Column(String)  # Assuming INT[] can be represented as a comma-separated string
    disp_phone = Column(Integer)  # Assuming BOOLEAN can be represented as Integer 0/1
    disp_bday = Column(Integer)
    marital_status = Column(Integer)
    disp_anniversary = Column(Integer)
    dob = Column(String)  # Assuming DATE can be represented as String
    doa = Column(String)
    profile_image = Column(String)  # Assuming BYTEA can be represented as 
    
class Temples(Base) :
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

