from fastapi import FastAPI, HTTPException
from app.models import Staff
from app.database import InMemoryDB
import uuid

app = FastAPI(title="Best Buy Staff Service")
db = InMemoryDB()

@app.post("/api/staff")
def create_staff(staff: Staff):
    staff.id = str(uuid.uuid4())
    return db.create(staff)

@app.get("/api/staff/{staff_id}")
def get_staff(staff_id: str):
    staff = db.get(staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff

@app.get("/api/staff")
def get_all_staff():
    return list(db.get_all().values())

@app.put("/api/staff/{staff_id}")
def update_staff(staff_id: str, staff: Staff):
    if not db.get(staff_id):
        raise HTTPException(status_code=404, detail="Staff not found")
    staff.id = staff_id
    return db.update(staff_id, staff)

@app.delete("/api/staff/{staff_id}")
def delete_staff(staff_id: str):
    if not db.delete(staff_id):
        raise HTTPException(status_code=404, detail="Staff not found")
    return {"message": "Staff deleted successfully"}