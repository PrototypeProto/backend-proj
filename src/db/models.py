from sqlmodel import SQLModel, Field, Column
from datetime import date, datetime
import uuid
import sqlalchemy.dialects.postgresql as postgres



class Product(SQLModel, table=True):
    '''
        the ORM for products
    '''
    __tablename__ = "Products"

    uid: uuid.UUID = Field(
        sa_column= Column(
            postgres.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    product_name: str
    product_description: str = Field(
        sa_column=Column(
            postgres.TEXT, default=""
        )
    )
    revision_number: int
    date_introduced: date = Field(
        sa_column=Column(
            postgres.DATE, default=date.today
        )
    )
    time_modified: datetime = Field(
        sa_column=Column(
            postgres.TIMESTAMP, default=datetime.now
        )
    )

    def __repr__(self):
        return f"<User {self.product_name} + {self.uid}>"


# 3:15