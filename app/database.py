from typing import Dict
from app.models import Staff

class InMemoryDB:
    def __init__(self):
        self.staff_db: Dict[str, Staff] = {}

    def create(self, staff: Staff) -> Staff:
        self.staff_db[staff.id] = staff
        return staff

    def get(self, staff_id: str) -> Staff:
        return self.staff_db.get(staff_id)

    def get_all(self) -> Dict[str, Staff]:
        return self.staff_db

    def update(self, staff_id: str, staff: Staff) -> Staff:
        self.staff_db[staff_id] = staff
        return staff

    def delete(self, staff_id: str) -> bool:
        if staff_id in self.staff_db:
            del self.staff_db[staff_id]
            return True
        return False