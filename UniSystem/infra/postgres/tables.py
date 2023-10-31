from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Date, DECIMAL, ForeignKeyConstraint, Boolean
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class AcademicTypes(Base):
    __tablename__ = 'academic_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)


class AcademicInstitutionalData(Base):
    __tablename__ = 'academic_institutional_datas'
    registration = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    academic_type_id = Column(Integer, ForeignKey('academic_types.id'))
    institutional_email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    academic_data_PK = UniqueConstraint(registration, academic_type_id)


class Students(Base):
    __tablename__ = 'students'
    registration = Column(String, ForeignKey('academic_institutional_datas.registration'), primary_key=True)
    registration_date = Column(Date, nullable=False)
    coefficient = Column(DECIMAL(2,2), nullable=False)
    academic_period = Column(Integer, nullable=False)
    course = Column(String, nullable=False)


class Professors(Base):
    __tablename__ = 'professors'
    registration = Column(String, ForeignKey('academic_institutional_datas.registration'),primary_key=True)
    registration_date = Column(Date, nullable=False)
    academic_formation = Column(String, nullable=False)
    academic_status = Column(String, nullable=False)
    salary = Column(DECIMAL(10, 2), nullable=False)
    academic_training_place = Column(String, nullable=False)


class Principals(Base):
    __tablename__ = 'principals'
    registration = Column(None, ForeignKey('professors.registration'), primary_key=True)
    entry_board_date = Column(Date, nullable=False)
    exit_board_date = Column(Date, nullable=False)
    salary = Column(DECIMAL(10, 2), nullable=False)
    vice_principal = Column(String, ForeignKey('professors.registration'))


class Deans(Base):
    __tablename__ = 'deans'
    registration = Column(String, ForeignKey('academic_institutional_datas.registration'),primary_key=True)
    registration_date = Column(Date, nullable=False)
    rectory_entry_date = Column(Date, nullable=False)
    rectory_exit_date = Column(Date)
    salary = Column(DECIMAL(10, 2), nullable=False)
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
    subject_start_date = Column(Date, nullable=False)
    note = Column(DECIMAL(2, 2))
    note_date = Column(Date)
    approved = Column(Boolean, nullable=False)
    note_PK = UniqueConstraint(subjects_id, student_registration, professor_registration)


new_academic_type1 = AcademicTypes(type='Student')
new_academic_type2 = AcademicTypes(type='Professor')
new_academic_type3 = AcademicTypes(type='Principal')
new_academic_type4 = AcademicTypes(type='Dean')
new_academic_type5 = AcademicTypes(type='Administrator')
