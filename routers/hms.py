from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Doctor, Patient, Appointment, PharmacyInventory, Bill, LabTest, EHR, Prescription, Room
from typing import List, Optional
from pydantic import BaseModel
from datetime import date, time, datetime

router = APIRouter()

# Schemas
class DoctorSchema(BaseModel):
    doctor_id: int
    full_name: str
    specialization: str
    phone: str
    email: str
    availability_status: str

    class Config:
        from_attributes = True

class PatientSchema(BaseModel):
    patient_id: int
    full_name: str
    age: int
    gender: str
    phone: Optional[str] = None
    address: Optional[str] = None
    blood_group: Optional[str] = None
    insurance_provider: Optional[str] = None
    emergency_contact: Optional[str] = None

    class Config:
        from_attributes = True

class AppointmentSchema(BaseModel):
    appointment_id: int
    patient_id: int
    doctor_id: int
    appointment_date: date
    appointment_time: time
    status: str
    reason: Optional[str] = None
    patient_name: Optional[str] = None
    doctor_name: Optional[str] = None

    class Config:
        from_attributes = True

class PharmacySchema(BaseModel):
    medicine_id: int
    medicine_name: str
    stock_quantity: int
    unit_price: float
    minimum_stock: int

    class Config:
        from_attributes = True

class BillSchema(BaseModel):
    bill_id: int
    patient_id: int
    consultation_charge: float
    lab_charge: float
    medicine_charge: float
    room_charge: float
    total_amount: float
    payment_status: str
    bill_date: date
    patient_name: Optional[str] = None

    class Config:
        from_attributes = True

class LabTestSchema(BaseModel):
    test_id: int
    patient_id: int
    test_name: str
    result: Optional[str] = None
    status: str
    test_date: date
    patient_name: Optional[str] = None

    class Config:
        from_attributes = True

class EHRSchema(BaseModel):
    ehr_id: int
    patient_id: int
    allergies: Optional[str] = None
    diagnosis: Optional[str] = None
    treatment: Optional[str] = None
    doctor_notes: Optional[str] = None
    updated_at: Optional[datetime] = None
    patient_name: Optional[str] = None

    class Config:
        from_attributes = True

class PrescriptionSchema(BaseModel):
    prescription_id: int
    patient_id: int
    doctor_id: int
    medicine_name: str
    dosage: str
    duration: str
    instructions: Optional[str] = None
    prescribed_date: date
    doctor_name: Optional[str] = None

    class Config:
        from_attributes = True

class RoomSchema(BaseModel):
    room_id: int
    room_number: str
    room_type: str
    availability: str

    class Config:
        from_attributes = True

# Endpoints
@router.get("/doctors", response_model=List[DoctorSchema])
def get_doctors(db: Session = Depends(get_db)):
    return db.query(Doctor).all()

@router.get("/patients", response_model=List[PatientSchema])
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()

@router.post("/doctors", response_model=DoctorSchema)
def create_doctor(doctor: DoctorSchema, db: Session = Depends(get_db)):
    db_doctor = Doctor(
        full_name=doctor.full_name,
        specialization=doctor.specialization,
        phone=doctor.phone,
        email=doctor.email,
        availability_status=doctor.availability_status
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

@router.put("/doctors/{doctor_id}", response_model=DoctorSchema)
def update_doctor(doctor_id: int, doctor: DoctorSchema, db: Session = Depends(get_db)):
    db_doctor = db.query(Doctor).filter(Doctor.doctor_id == doctor_id).first()
    if not db_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    db_doctor.full_name = doctor.full_name
    db_doctor.specialization = doctor.specialization
    db_doctor.phone = doctor.phone
    db_doctor.email = doctor.email
    db_doctor.availability_status = doctor.availability_status
    
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

@router.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = db.query(Doctor).filter(Doctor.doctor_id == doctor_id).first()
    if not db_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    db.delete(db_doctor)
    db.commit()
    return {"message": "Doctor deleted successfully"}

@router.post("/patients", response_model=PatientSchema)
def create_patient(patient: PatientSchema, db: Session = Depends(get_db)):
    db_patient = Patient(
        full_name=patient.full_name,
        age=patient.age,
        gender=patient.gender,
        phone=patient.phone,
        address=patient.address,
        blood_group=patient.blood_group,
        insurance_provider=patient.insurance_provider,
        emergency_contact=patient.emergency_contact
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.put("/patients/{patient_id}", response_model=PatientSchema)
def update_patient(patient_id: int, patient: PatientSchema, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    db_patient.full_name = patient.full_name
    db_patient.age = patient.age
    db_patient.gender = patient.gender
    db_patient.phone = patient.phone
    db_patient.address = patient.address
    db_patient.blood_group = patient.blood_group
    db_patient.insurance_provider = patient.insurance_provider
    db_patient.emergency_contact = patient.emergency_contact
    
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    db.delete(db_patient)
    db.commit()
    return {"message": "Patient deleted successfully"}
@router.get("/appointments", response_model=List[AppointmentSchema])
def get_appointments(db: Session = Depends(get_db)):
    appointments = db.query(Appointment).all()
    result = []
    for appt in appointments:
        appt_dict = AppointmentSchema.from_orm(appt).dict()
        appt_dict['patient_name'] = appt.patient.full_name if appt.patient else "Unknown"
        appt_dict['doctor_name'] = appt.doctor.full_name if appt.doctor else "Unknown"
        result.append(appt_dict)
    return result

@router.post("/appointments", response_model=AppointmentSchema)
def create_appointment(appt: AppointmentSchema, db: Session = Depends(get_db)):
    db_appt = Appointment(
        patient_id=appt.patient_id,
        doctor_id=appt.doctor_id,
        appointment_date=appt.appointment_date,
        appointment_time=appt.appointment_time,
        status=appt.status,
        reason=appt.reason
    )
    db.add(db_appt)
    db.commit()
    db.refresh(db_appt)
    return db_appt

@router.get("/pharmacy", response_model=List[PharmacySchema])
def get_pharmacy(db: Session = Depends(get_db)):
    return db.query(PharmacyInventory).all()

@router.post("/pharmacy", response_model=PharmacySchema)
def create_pharmacy_item(item: PharmacySchema, db: Session = Depends(get_db)):
    db_item = PharmacyInventory(
        medicine_name=item.medicine_name,
        stock_quantity=item.stock_quantity,
        unit_price=item.unit_price,
        minimum_stock=item.minimum_stock
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/bills", response_model=List[BillSchema])
def get_bills(db: Session = Depends(get_db)):
    bills = db.query(Bill).all()
    result = []
    for bill in bills:
        bill_dict = BillSchema.from_orm(bill).dict()
        patient = db.query(Patient).filter(Patient.patient_id == bill.patient_id).first()
        bill_dict['patient_name'] = patient.full_name if patient else "Unknown"
        result.append(bill_dict)
    return result

@router.post("/bills", response_model=BillSchema)
def create_bill(bill: BillSchema, db: Session = Depends(get_db)):
    db_bill = Bill(
        patient_id=bill.patient_id,
        consultation_charge=bill.consultation_charge,
        lab_charge=bill.lab_charge,
        medicine_charge=bill.medicine_charge,
        room_charge=bill.room_charge,
        total_amount=bill.total_amount,
        payment_status=bill.payment_status,
        bill_date=bill.bill_date
    )
    db.add(db_bill)
    db.commit()
    db.refresh(db_bill)
    return db_bill

@router.get("/lab-tests", response_model=List[LabTestSchema])
def get_lab_tests(db: Session = Depends(get_db)):
    tests = db.query(LabTest).all()
    result = []
    for test in tests:
        test_dict = LabTestSchema.from_orm(test).dict()
        patient = db.query(Patient).filter(Patient.patient_id == test.patient_id).first()
        test_dict['patient_name'] = patient.full_name if patient else "Unknown"
        result.append(test_dict)
    return result

@router.post("/lab-tests", response_model=LabTestSchema)
def create_lab_test(test: LabTestSchema, db: Session = Depends(get_db)):
    db_test = LabTest(
        patient_id=test.patient_id,
        test_name=test.test_name,
        result=test.result,
        status=test.status,
        test_date=test.test_date
    )
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

@router.get("/ehr/{patient_id}", response_model=List[EHRSchema])
def get_ehr(patient_id: int, db: Session = Depends(get_db)):
    records = db.query(EHR).filter(EHR.patient_id == patient_id).all()
    result = []
    for rec in records:
        rec_dict = EHRSchema.from_orm(rec).dict()
        patient = db.query(Patient).filter(Patient.patient_id == rec.patient_id).first()
        rec_dict['patient_name'] = patient.full_name if patient else "Unknown"
        result.append(rec_dict)
    return result

@router.get("/prescriptions/{patient_id}", response_model=List[PrescriptionSchema])
def get_prescriptions(patient_id: int, db: Session = Depends(get_db)):
    prescriptions = db.query(Prescription).filter(Prescription.patient_id == patient_id).all()
    result = []
    for p in prescriptions:
        p_dict = PrescriptionSchema.from_orm(p).dict()
        doctor = db.query(Doctor).filter(Doctor.doctor_id == p.doctor_id).first()
        p_dict['doctor_name'] = doctor.full_name if doctor else "Unknown"
        result.append(p_dict)
    return result

@router.get("/rooms", response_model=List[RoomSchema])
def get_rooms(db: Session = Depends(get_db)):
    return db.query(Room).all()

@router.post("/rooms", response_model=RoomSchema)
def create_room(room: RoomSchema, db: Session = Depends(get_db)):
    db_room = Room(
        room_number=room.room_number,
        room_type=room.room_type,
        availability=room.availability
    )
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room
