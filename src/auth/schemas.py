from pydantic import BaseModel
import uuid
from datetime import date, datetime
from sqlmodel import SQLModel

'''
    What we use to enforce data input
'''


class User(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    pwd: str
    user_description: str
    is_male: bool
    role: str
    date_created: date
    time_modified: datetime

class UserCreateModel(BaseModel):
    username: str
    email: str
    pwd: str
    user_description: str
    is_male: bool
    role: str

class UserUpdateModel(BaseModel):
    email: str
    pwd: str
    user_description: str
    is_male: bool
    role: str