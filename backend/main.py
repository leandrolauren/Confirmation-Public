import logging, uvicorn, datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as confirmation_router
from zoneinfo import ZoneInfo


sp_timezone = ZoneInfo("America/Sao_Paulo")


logging.Formatter.converter = lambda *args: datetime.datetime.now(
    sp_timezone
).timetuple()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - origin: %(name)s - message: %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    force=True,
)

logging.info("Starting the API")


app = FastAPI(title="Birthday Party Confirmation API", version="1.0.0")

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
    logging.info("Starting the API2")

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
