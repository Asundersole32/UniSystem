from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Date, DECIMAL
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class AcademicTypes(Base):
    __tablename__ = 'academic_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)


class Students(Base):
    __tablename__ = 'students'
    registration = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    registration_date = Column(Date, nullable=False)
    institutional_email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    academic_type_id = Column(Integer, ForeignKey('academic_types.id'), nullable=False)
    coefficient = Column(DECIMAL(2,2))
    academic_period = Column(Integer, nullable=False)
    course = Column(String, nullable=False)
    student_altPK = UniqueConstraint(registration, academic_type_id)


class Professors(Base):
    __tablename__ = 'professors'
    registration = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    registration_date = Column(Date, nullable=False)
    institutional_email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    academic_type_id = Column(Integer, ForeignKey('academic_types.id'), nullable=False)
    academic_formation = Column(String, nullable=False)
    academic_status = Column(String, nullable=False)
    professional_status = Column(String, nullable=False)
    salary = (DECIMAL(10, 2))
    academic_training_place = Column(String, nullable=False)
    professor_altPK = UniqueConstraint(registration, academic_type_id)


class Principals(Base):
    __tablename__ = 'principals'
    registration = Column(None, ForeignKey('professors.registration'), primary_key=True)
    academic_type_id = Column(Integer, ForeignKey('academic_types.id'), nullable=False)
    entry_board_date = Column(Date, nullable=False)
    exit_board_date = Column(Date)
    vice_principal = Column(String, ForeignKey('professors.registration'))
    principal_altPK = UniqueConstraint(registration, academic_type_id)


class Deans(Base):
    __tablename__ = 'deans'
    registration = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    registration_date = Column(Date, nullable=False)
    institutional_email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    academic_type_id = Column(Integer, ForeignKey('academic_types.id'), nullable=False)
    rectory_entry_date = Column(Date, nullable=False)
    rectory_exit_date = Column(Date)
    salary = Column(DECIMAL(10,2))
    academic_training_place = Column(String, nullable=False)


class Subjects(Base):
    __tablename__ = 'subjects'
    id = Column(String, primary_key=True)
    professor_registration = Column(String, ForeignKey('professors.registration'))
    course = Column(String, nullable=False)
    subject_name = Column(String, nullable=False)
    workload = Column(String, nullable=False)
    subject_altPK = UniqueConstraint(id, professor_registration, course)


class SubjectsNotes(Base):
    __tablename__ = 'subjects_notes'
    subjects_id = Column(String, ForeignKey('subjects.id'), nullable=False)
    student_registration = Column(String, ForeignKey('students.registration'), primary_key=True)
    professor_registration = Column(String, ForeignKey("professors.registration"))
    note = Column(DECIMAL(2,2))
    note_date = Column(Date)
    note_PK = UniqueConstraint(subjects_id, student_registration, professor_registration)


new_academic_type1 = AcademicTypes(type='student')
new_academic_type2 = AcademicTypes(type='professor')
new_academic_type3 = AcademicTypes(type='dean')
