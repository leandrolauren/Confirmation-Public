from fastapi import HTTPException
from models import Connection
import logging, datetime

utc_now = datetime.datetime.now(datetime.timezone.utc)
utc_now = utc_now.replace(tzinfo=datetime.timezone.utc)
utc_now = utc_now.astimezone(datetime.timezone(datetime.timedelta(hours=-3)))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt=utc_now.strftime("%d-%m-%Y %H:%M:%S"),
)


# Function to create the table
def create_table():
    try:
        
        with Connection() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS confirmations (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT,
                    confirmation BOOLEAN DEFAULT TRUE,
                    confirmation_date DATE NOT NULL DEFAULT CURRENT_DATE
                );
            """
            )

        return {f"success": True, "message": "Table created successfully"}
    
    except Exception as e:
        logging.error(f"Error creating table: {e}")
        raise

# Function to insert a new confirmation
def insert_confirmation(name: str, email: str, phone: str, confirmation: bool) -> dict:
    try:
        with Connection() as conn:
            conn.execute(
                "INSERT INTO confirmations (name, email, phone, confirmation) VALUES (%s, %s, %s, %s)",
                (name, email, phone, confirmation),
            )

        return {
            f"success": True,
            "message": "Confirmation inserted successfully",
            "data_entered": 
                {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "confirmation": confirmation,
                },
        }

    except Exception as e:
        logging.error(f"Error inserting confirmation: {e}")
        raise HTTPException(
            status_code=400,
            detail=f"Error inserting confirmation: {e}",
        )


# Function to read all confirmations
def read_confirmation() -> dict:
    try:
        with Connection() as conn:
            confirmations = conn.execute(
                "SELECT name, email, phone, confirmation FROM confirmations", None
            )

        result = []
        for row in confirmations:
            result.append({
                "name": row[0],
                "email": row[1],
                "phone": row[2],
                "confirmation": row[3]
            })
        
        return {f"success": True, "message": "Confirmations read successfully", "data": result}
    
    except Exception as e:
        logging.error(f"Error reading confirmations: {e}")
        return {f"success": False, "message": f"Error reading confirmations: {e}", "data": []}


# This function will be used to check if the email is already in the database before inserting a new confirmation
def validate_email(email):

    with Connection() as conn:
        existing = conn.execute(
            "SELECT email FROM confirmations WHERE email = %s", (email,)
        )

    return existing 
    
