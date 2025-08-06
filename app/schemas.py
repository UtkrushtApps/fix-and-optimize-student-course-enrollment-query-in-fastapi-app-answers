from pydantic import BaseModel
from typing import Optional

class StudentOut(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class CourseOut(BaseModel):
    id: int
    title: str
    class Config:
        orm_mode = True

class EnrollmentStatusOption(BaseModel):
    status: str
