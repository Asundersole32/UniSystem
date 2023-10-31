from pydantic import BaseModel
from datetime import date


class Academic(BaseModel):
    registration: str
    name: str
    registration_date: date | None = None
    institutional_email: str
    password: str


class Student(Academic):
    course: str


class Professor(Academic):
    academic_formation: str
    academic_status: str
    salary: float
    academic_training_place: str


class Principal(BaseModel):
    registration: str
    entry_board_date: date
    exit_board_date: date
    salary: float
    vice_principal: str


class Dean(Academic):
    rectory_entry_date: date
    rectory_exit_date: date | None = None
    academic_training_place: date


class Subject(BaseModel):
    id: str
    professor_registration: str
    course: str
    subject_name: str
    workload: int


class SubjectNote(BaseModel):
    subject_id: str
    student_registration: str
    professor_registration: str
    note: float | None = None
    note_date: date | None = None
