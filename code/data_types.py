from typing import Optional, Union
from pydantic import BaseModel
from datetime import date 

class User(BaseModel):
    uid: int
    pwd: str

class RegistrationDate(BaseModel):
    reg_date: date
    desc: str
