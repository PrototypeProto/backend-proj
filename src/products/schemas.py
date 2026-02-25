from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime
from sqlmodel import SQLModel

'''
    What we use to enforce data input
'''


# class User(BaseModel):
#     uid: UUID
#     username: str
#     email: str
#     pwd: str
#     user_description: str
#     is_male: bool
#     role: str
#     date_created: date
#     time_modified: datetime

# class UserCreateModel(BaseModel):
#     username: str
#     email: str
#     pwd: str
#     user_description: str
#     is_male: bool
#     role: str

# class UserUpdateModel(BaseModel):
#     email: str
#     pwd: str
#     user_description: str
#     is_male: bool
#     role: str


class Product(BaseModel):
    uid: UUID
    product_name: str
    revision_number: int
    product_description: str
    date_introduced: date
    time_modified: datetime

class ProductCreateModel(BaseModel):
    product_name: str
    revision_number: int
    date_introduced: date
    product_description: str

class ProductUpdateModel(BaseModel):
    revision_number: int
    date_introduced: date
    product_description: str


