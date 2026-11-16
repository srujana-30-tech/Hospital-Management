from sqlalchemy import Column, Integer, String, Enum, Date, Time, Text, Numeric, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import enum

class UserRole(str, enum.Enum):
    Admin = "Admin"
    Doctor = "Doctor"
    Nurse = "Nurse"
    Staff = "Staff"

class Patient(Base):
    __tablename__ = "patient"
    patient_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100))
    age = Column(Integer)
    gender = Column(String(10))
    phone = Column(String(15))
    address = Column(String(255))
    blood_group = Column(String(5))
    insurance_provider = Column(String(100))
    emergency_contact = Column(String(15))
    registered_at = Column(TIMESTAMP)

class Doctor(Base):
    __tablename__ = "doctor"
    doctor_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100))
    specialization = Column(String(100))
    phone = Column(String(15))
    email = Column(String(100))
    availability_status = Column(String(50))

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(255))
    role = Column(Enum(UserRole))
    created_at = Column(TIMESTAMP)

class Appointment(Base):
    __tablename__ = "appointment"
    appointment_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patient.patient_id"))
    doctor_id = Column(Integer, ForeignKey("doctor.doctor_id"))
    appointment_date = Column(Date)
    appointment_time = Column(Time)
    status = Column(String(50))
    reason = Column(Text)

    patient = relationship("Patient")
    doctor = relationship("Doctor")

class EHR(Base):
    __tablename__ = "ehr"
    ehr_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patient.patient_id"))
    allergies = Column(Text)
    diagnosis = Column(Text)
    treatment = Column(Text)
    doctor_notes = Column(Text)
    updated_at = Column(TIMESTAMP)

class Bill(Base):
    __tablename__ = "bills"
    bill_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patient.patient_id"))
    consultation_charge = Column(Numeric(10, 2))
    lab_charge = Column(Numeric(10, 2))
    medicine_charge = Column(Numeric(10, 2))
    room_charge = Column(Numeric(10, 2))
    total_amount = Column(Numeric(10, 2))
    payment_status = Column(Enum("Paid", "Unpaid", "Partial", "Pending", name="bill_status"))
    bill_date = Column(Date)

class PharmacyInventory(Base):
    __tablename__ = "pharmacy_inventory"
    medicine_id = Column(Integer, primary_key=True, index=True)
    medicine_name = Column(String(100))
    stock_quantity = Column(Integer)
    unit_price = Column(Numeric(10, 2))
    minimum_stock = Column(Integer)

class LabTest(Base):
    __tablename__ = "lab_test"
    test_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patient.patient_id"))
    test_name = Column(String(100))
    result = Column(Text)
    status = Column(Enum("Pending", "Completed", name="lab_status"))
    test_date = Column(Date)

class Prescription(Base):
    __tablename__ = "prescription"
    prescription_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patient.patient_id"))
    doctor_id = Column(Integer, ForeignKey("doctor.doctor_id"))
    medicine_name = Column(String(100))
    dosage = Column(String(50))
    duration = Column(String(50))
    instructions = Column(Text)
    prescribed_date = Column(Date)

class Room(Base):
    __tablename__ = "room"
    room_id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String(50))
    room_type = Column(String(50))
    availability = Column(String(50))
