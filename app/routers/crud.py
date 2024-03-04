from fastapi import APIRouter,HTTPException,Depends
from typing import List
from ..models import Todo
from app.schemas import TodoCreate,TodoResponse,TodoUpdate
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/todo",
    tags=['To-do-List']
)


       
#CRUD operations
@router.post("/",response_model=TodoResponse)
def create_todo(todo:TodoCreate,db: Session = Depends(get_db)):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
    
    
@router.get("/", response_model=List[TodoResponse])
def read_todo(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    todos = db.query(Todo).offset(skip).limit(limit).all()
    return todos


@router.get("/{id}",response_model=TodoResponse)
def read_single_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{id}",response_model=TodoResponse)
def update_todo(id:int,todo:TodoUpdate,db: Session = Depends(get_db)):
    # Retrieve the existing Todo item from the database
    db_todo = db.query(Todo).filter(Todo.id == id).first()
    
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
     
    # Update the Todo item attributes with the values from the TodoUpdate model
    for key,value in todo.dict().items():
        setattr(db_todo,key,value)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.delete("/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
     # Retrieve the existing Todo item from the database
    db_todo = db.query(Todo).filter(Todo.id == id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")      
    
    db.delete(db_todo)
    db.commit()
    return {'todo':db_todo,'msg':f'todo of id_no:{id} is deleted successfully'}


