from pydantic import BaseModel

class TempleResponse(BaseModel):

    id: int
    temple_name: str
    address: str
    city_id: int
    state_id: int
    country_id: int
    pincode : str
    phone_number : str
    temple_image : str

    class Config:
        from_attributes = True

# NOTE : 
# i. Never expose SQLAlchemy model directly. Create DTO.
# ii. from_attributes = True - This is required in Pydantic V2.