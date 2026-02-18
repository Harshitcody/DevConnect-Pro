from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str

class ProjectCreate(BaseModel):
    title: str
    description: str
    skills: str
    budget: int

