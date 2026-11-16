from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="OmniCare Pro Hospital System")

# Serve static files
# We will serve each module's code.html at a specific route
MODULES = [
    "admin_user_access_control",
    "appointment_scheduling_view",
    "billing_insurance_management",
    "clinical_precision",
    "clinical_reporting_dashboard",
    "doctor_directory_management",
    "facility_bed_management",
    "hms_login",
    "laboratory_services_results",
    "patient_electronic_health_records",
    "patient_management",
    "pharmacy_stock_inventory"
]

for module in MODULES:
    app.mount(f"/static/{module}", StaticFiles(directory=f"{module}"), name=module)

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open(os.path.join("hms_login", "code.html"), "r") as f:
        return f.read()

from routers import auth, hms

app.include_router(auth.router, prefix="/api")
app.include_router(hms.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
