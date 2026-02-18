from sqlalchemy.orm import Session
import models
import auth

def create_user(db: Session, user):
    hashed = auth.hash_password(user.password)
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_project(db: Session, project):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_projects(db: Session):
    return db.query(models.Project).all()
