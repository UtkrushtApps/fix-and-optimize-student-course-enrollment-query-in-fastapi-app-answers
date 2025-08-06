from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import select, join
from app.database import SessionLocal, init_db
from app.models import Student, Course, Enrollment, EnrollmentStatusEnum
from app.schemas import StudentOut

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/courses/{course_id}/students", response_model=List[StudentOut])
def get_students_by_course(
    course_id: int,
    status: Optional[EnrollmentStatusEnum] = Query(None, description="Filter by enrollment status"),
    db: Session = Depends(get_db)
):
    # Check course exists (optional, for errors)
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    query = db.query(Student).join(
        Enrollment, (Enrollment.student_id == Student.id)
    ).filter(
        Enrollment.course_id == course_id
    )
    if status:
        query = query.filter(Enrollment.status == status)

    students = query.all()
    return students
