from sqlalchemy.orm import Session
from . import models, schemas

def get_tasks(db: Session):
    return db.query(models.Task).all()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, updated_task: schemas.TaskCreate):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        task.title = updated_task.title
        task.completed = updated_task.completed
        db.commit()
        db.refresh(task)
        return task
    return None

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return task
    return None
