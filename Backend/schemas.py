from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    phoneNumber: Optional[str] = None
    
class UserLogin(BaseModel):
    email: str
    password: str
    
class UserInDB(BaseModel):
    id: str = Field(..., alias = 'id')
    name: str
    email: str
    phoneNumber: Optional[str] = None
    role: str = "student"
    class Config:
        allowPopulationByFieldname = True
        jsonEncoders = {
            str: lambda v: str(v)
        }
        
class HostelCreate(BaseModel):
    name: str
    location:str
    price: float
    vacancies: int

class HistelInDB(HostelCreate):
    id: str = Field(..., alias = 'id')
    ownerId = Optional[str] = None
    
    class Config:
        allowPopulationByFieldName = True
        
class BookingCreate(BaseModel):
    userId: str
    hotelId: str
    amount: float
    status: str = "pending"
    
class BookingDB(BookingCreate):
    id: str = Field(..., alias = 'id')
    
    class Config:
        allowPopulationByFielName = True