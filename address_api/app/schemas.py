from pydantic import BaseModel

class AddressBase(BaseModel):
    name : str
    flatnum : int
    address : str
    city : str
    state : str

class AddressCreate(AddressBase):
    pass

class AddressUpdate(BaseModel):
    name : str = None
    flatnum : int = None
    address : str = None
    city : str = None
    state : str = None

class Address(AddressBase):
    id : int
     
    class Config:
        orm_mode = True