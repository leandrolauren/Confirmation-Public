from typing import Optional
from pydantic import BaseModel, EmailStr, Field
import psycopg2 as pg
import os
from dotenv import load_dotenv


# ConfirmationCreate class to handle the request of the confirmation endpoint
class ConfirmationCreate(BaseModel):
    name: str = Field(max_length=100, description="The name of the person confirming")
    email: EmailStr = Field(
        max_length=150, description="The email of the person confirming"
    )
    phone: Optional[str] = Field(
        max_length=15, description="The phone number of the person confirming"
    )
    confirmation: bool = Field(
        ..., description="When the person confirms their presence"
    )
    qtt_adult: int = Field(
        ...,
        max_length=10,
        ge=1,
        description="Number of adults in invite",
        title="Number of Adults",
    )
    qtt_child: int = Field(
        ...,
        max_length=10,
        ge=0,
        description="Number of children in invite",
        title="Number of Children",
    )


# ConfirmationResponse class to handle the response of the confirmation endpoint
class ConfirmationResponse(BaseModel):
    success: bool = Field(..., description="Whether the confirmation was successful")
    name: str = Field(..., description="The name of the person confirming")
    email: EmailStr = Field(..., description="The email of the person confirming")
    phone: Optional[str] = Field(
        None, description="The phone number of the person confirming"
    )
    confirmation: bool = Field(
        ..., description="Whether the person confirmed their presence"
    )


# Load environment variables
load_dotenv()


# Connection class to handle database connections
class Connection(object):

    def __init__(self):

        required_vars = ["DB_NAME", "DB_USER", "DB_PASSWORD", "DB_HOST", "DB_PORT"]
        for var in required_vars:
            if not os.getenv(var):
                raise ValueError(f"Environment variable {var} is not set")

        self.conn = pg.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    # Close the connection and commit transaction if no exception was raised
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.conn.rollback()
        else:
            self.conn.commit()

        if hasattr(self, "cursor") and self.cursor:
            self.cursor.close()
        if hasattr(self, "conn") and self.conn:
            self.conn.close()

    # Execute the query, if it is a Select query, return the results, otherwise returns the number of rows affected
    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        if query.strip().lower().startswith("select"):
            return self.cursor.fetchall()
        else:
            return self.cursor.rowcount

    # Commit transaction
    def commit(self):
        self.conn.commit()

    # Rollback transaction
    def rollback(self):
        self.conn.rollback()
