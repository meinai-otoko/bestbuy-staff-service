from pydantic import BaseModel
from typing import Optional

class Staff(BaseModel):
    id: Optional[str] = None
    name: str
    position: str
    department: str
    email: str
    phone: str