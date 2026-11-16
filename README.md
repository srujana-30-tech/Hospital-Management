# 🏥 OmniCare Pro — Hospital Management System

A full-stack **Hospital Management System (HMS)** built with **FastAPI** and **MySQL**, featuring a modular frontend for each department. OmniCare Pro covers everything from patient registration and doctor management to pharmacy inventory, billing, lab results, and clinical reporting — all accessible from a unified web interface.

---

## 📸 Modules Overview

| Module | Description |
|--------|-------------|
| 🔐 HMS Login | Secure role-based login for hospital staff |
| 👤 Patient Management | Register, update, and manage patient records |
| 📋 Electronic Health Records (EHR) | View patient diagnoses, treatments & doctor notes |
| 👨‍⚕️ Doctor Directory | Manage doctor profiles and availability |
| 📅 Appointment Scheduling | Book and track patient-doctor appointments |
| 🧾 Billing & Insurance | Generate bills, track charges and payment status |
| 💊 Pharmacy & Stock Inventory | Monitor medicine stock levels and pricing |
| 🧪 Laboratory Services | Record and manage lab test orders and results |
| 🛏️ Facility & Bed Management | Track room types and availability |
| 📊 Clinical Reporting Dashboard | Visualize hospital-wide clinical data |
| 🛡️ Admin & User Access Control | Manage users and their role-based permissions |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | FastAPI (Python) |
| **Database** | MySQL via SQLAlchemy ORM |
| **Authentication** | JWT (JSON Web Tokens) with `python-jose` |
| **Password Hashing** | `passlib[bcrypt]` |
| **Frontend** | HTML, CSS, JavaScript (served as static files) |
| **Server** | Uvicorn (ASGI) |

---

## 📁 Project Structure

```
stitch_omnicare_pro_hospital_system/
│
├── main.py                          # FastAPI app entry point
├── database.py                      # DB connection & session setup
├── models.py                        # SQLAlchemy ORM models
├── auth.py                          # JWT token creation & password utils
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variable template
│
├── routers/
│   ├── auth.py                      # Login / authentication endpoint
│   └── hms.py                       # All HMS CRUD API endpoints
│
├── hms_login/                       # Login page UI
├── patient_management/              # Patient management UI
├── patient_electronic_health_records/  # EHR UI
├── doctor_directory_management/     # Doctor directory UI
├── appointment_scheduling_view/     # Appointment scheduling UI
├── billing_insurance_management/    # Billing & insurance UI
├── pharmacy_stock_inventory/        # Pharmacy inventory UI
├── laboratory_services_results/     # Lab services UI
├── facility_bed_management/         # Facility & bed management UI
├── clinical_reporting_dashboard/    # Clinical reporting UI
├── admin_user_access_control/       # Admin panel UI
└── clinical_precision/              # Clinical precision design spec
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- MySQL Server running locally
- `pip` package manager

### 1. Clone the repository

```bash
git clone https://github.com/srujana-30-tech/Hospital-Management.git
cd Hospital-Management
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` with your actual values:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_db_password
DB_NAME=hospital
JWT_SECRET_KEY=your_super_secret_jwt_key
ACCESS_TOKEN_EXPIRE_MINUTES=60
GOOGLE_API_KEY=your_google_api_key
```

### 4. Set up the database

Create the MySQL database:

```sql
CREATE DATABASE hospital;
```

The tables are auto-created by SQLAlchemy on first run.

### 5. Run the server

```bash
python main.py
```

The server starts at **http://localhost:8000**

---

## 🌐 Application URLs

| URL | Description |
|-----|-------------|
| `http://localhost:8000` | HMS Login page (app entry point) |
| `http://localhost:8000/docs` | Interactive Swagger API docs |
| `http://localhost:8000/redoc` | ReDoc API documentation |

---

## 🔐 Authentication

The app uses **JWT-based role-based access control**.

### Default Admin Login
| Field | Value |
|-------|-------|
| Username | `admin` |
| Password | `admin123` |
| Role | `Admin` |

### User Roles
| Role | Access Level |
|------|-------------|
| `Admin` | Full system access |
| `Doctor` | Patient records, EHR, prescriptions |
| `Nurse` | Patient and appointment management |
| `Staff` | General access |

---

## 📡 API Endpoints

All endpoints are prefixed with `/api`

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/login` | Login and receive JWT token |

### Patients
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/patients` | List all patients |
| `POST` | `/api/patients` | Register a new patient |
| `PUT` | `/api/patients/{id}` | Update patient details |
| `DELETE` | `/api/patients/{id}` | Remove a patient |

### Doctors
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/doctors` | List all doctors |
| `POST` | `/api/doctors` | Add a new doctor |
| `PUT` | `/api/doctors/{id}` | Update doctor profile |
| `DELETE` | `/api/doctors/{id}` | Remove a doctor |

### Appointments
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/appointments` | List all appointments |
| `POST` | `/api/appointments` | Book an appointment |

### Electronic Health Records
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/ehr/{patient_id}` | Get EHR for a patient |

### Billing
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/bills` | List all bills |
| `POST` | `/api/bills` | Create a bill |

### Pharmacy
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/pharmacy` | View medicine inventory |
| `POST` | `/api/pharmacy` | Add medicine stock |

### Laboratory
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/lab-tests` | List all lab tests |
| `POST` | `/api/lab-tests` | Order a lab test |

### Prescriptions
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/prescriptions/{patient_id}` | Get prescriptions for a patient |

### Rooms
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/rooms` | View all rooms and availability |
| `POST` | `/api/rooms` | Add a new room |

---

## 🗄️ Database Models

| Table | Key Fields |
|-------|-----------|
| `patient` | name, age, gender, blood group, insurance, emergency contact |
| `doctor` | name, specialization, phone, email, availability |
| `users` | username, password (hashed), role |
| `appointment` | patient, doctor, date, time, status, reason |
| `ehr` | patient, allergies, diagnosis, treatment, doctor notes |
| `bills` | charges (consultation, lab, medicine, room), payment status |
| `pharmacy_inventory` | medicine name, stock quantity, unit price, minimum stock |
| `lab_test` | patient, test name, result, status, date |
| `prescription` | patient, doctor, medicine, dosage, duration, instructions |
| `room` | room number, type, availability |

---

## 🔒 Security Notes

- `.env` is excluded from version control via `.gitignore`
- Passwords are hashed using `bcrypt`
- All protected routes require a valid JWT Bearer token
- Never commit real credentials — use `.env.example` as a reference

---

## 📦 Dependencies

```
fastapi
uvicorn
sqlalchemy
pymysql
python-dotenv
python-multipart
python-jose[cryptography]
passlib[bcrypt]
bcrypt
```

---

## 👩‍💻 Author

**Srujana R Pujar**  
📧 srujanarpujar1930@gmail.com  
🔗 [GitHub](https://github.com/srujana-30-tech)
