from fastapi import APIRouter, HTTPException, Depends, status
import logging, os, datetime
from models import ConfirmationResponse, ConfirmationCreate
from database import insert_confirmation, read_confirmation, validate_email
from fastapi.security import APIKeyHeader

utc_now = datetime.datetime.now(datetime.timezone.utc)
utc_now = utc_now.replace(tzinfo=datetime.timezone.utc)
utc_now = utc_now.astimezone(datetime.timezone(datetime.timedelta(hours=-3)))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt=utc_now.strftime("%d-%m-%Y %H:%M:%S"),
)


router = APIRouter()


# Endpoint to confirm presence
@router.post("/confirm", response_model=ConfirmationResponse)
def create_confirmation(confirmation: ConfirmationCreate):
    logging.info(f"New confirmation received from: {confirmation.email}")

    # Check if the email is already in the database
    existing = validate_email(confirmation.email)

    if existing:
        return {
            "success": False,
            "message": f"Presence already confirmed for this email {confirmation.email}",
        }

    try:
        # Insert the confirmation into the database
        insert_confirmation(
            confirmation.name,
            confirmation.email,
            confirmation.phone,
            confirmation.confirmation,
        )

        # Return the confirmation
        return ConfirmationResponse(
            success=True,
            name=confirmation.name,
            email=confirmation.email,
            phone=confirmation.phone,
            confirmation=confirmation.confirmation,
        )
    except Exception as e:
        logging.error(f"Error creating confirmation: {e}")
        raise HTTPException(status_code=500, detail="Error creating confirmation", message=str(e))


api_key_scheme = APIKeyHeader(name="Authorization")

def validate_token(token: str = Depends(api_key_scheme)) -> str:
    expec_token = os.getenv("API_TOKEN")

    if token != f"Bearer {expec_token}":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return token


@router.get("/confirmations", response_model=list)
async def get_all_confirmations(token: str = Depends(validate_token)):

    logging.info({"message": "Access granted with token", "token": token})
    logging.info("Start reading all confirmations")

    confirmations = read_confirmation()

    if confirmations.get("success") is False:
        raise HTTPException(status_code=500, detail="Error reading confirmations")
    
    result = []
    for confirmation in confirmations["data"]:
        result.append(
            {
                "name": confirmation.get("name"),
                "email": confirmation.get("email"),
                "phone": confirmation.get("phone"),
                "confirmation": confirmation.get("confirmation"),
            }
        )
    logging.info("Retrieved all confirmations")
    
    return result
