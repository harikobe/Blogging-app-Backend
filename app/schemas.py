from pydantic import BaseModel,Field,EmailStr
from datetime import datetime

class TodoCreate(BaseModel):
    title:str
    description:str
    
    
class TodoUpdate(BaseModel):
    title: str
    description: str
    completed: bool
    
    
    

class TodoResponse(TodoCreate):
    id: int
    
    class Config:
        orm_mode=True
    
 
    
 