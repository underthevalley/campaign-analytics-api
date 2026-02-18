from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine
from app.advertisers.router import router as advertiser_router

from app.advertisers import models  # important for table registration

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Campaign Analytics API"}


app.include_router(advertiser_router)

Base.metadata.create_all(bind=engine)
