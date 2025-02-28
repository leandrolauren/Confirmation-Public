import logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as confirmation_router
import datetime

utc_now = datetime.datetime.now(datetime.timezone.utc)
utc_now = utc_now.replace(tzinfo=datetime.timezone.utc)
utc_now = utc_now.astimezone(datetime.timezone(datetime.timedelta(hours=-3)))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt=utc_now.strftime("%d-%m-%Y %H:%M:%S"),
)

app = FastAPI(title="Birthday Party Confirmation API")

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(confirmation_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
