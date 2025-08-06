from sqlalchemy import Column, Integer, String, ForeignKey, Enum, UniqueConstraint, Index
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()

class EnrollmentStatusEnum(enum.Enum):
    enrolled = 'enrolled'
    dropped = 'dropped'
    completed = 'completed'

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    enrollments = relationship('Enrollment', back_populates='student')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)

    enrollments = relationship('Enrollment', back_populates='course')

class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False, index=True)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False, index=True)
    status = Column(Enum(EnrollmentStatusEnum), nullable=False, index=True)

    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')

    __table_args__ = (
        UniqueConstraint('student_id', 'course_id', name='uniq_student_course'),
        Index('idx_enrollments_course_status', 'course_id', 'status'),
        Index('idx_enrollments_student_id', 'student_id'),
    )
