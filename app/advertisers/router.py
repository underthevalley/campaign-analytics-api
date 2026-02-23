from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from . import service, schemas

router = APIRouter(prefix="/advertisers", tags=["Advertisers"])


@router.post("/", response_model=schemas.AdvertiserResponse)
def create_advertiser(
    data: schemas.AdvertiserCreate,
    db: Session = Depends(get_db),
):
    try:
        return service.create_advertiser(db, data)
    except service.AdvertiserAlreadyExists as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[schemas.AdvertiserResponse])
def list_advertisers(db: Session = Depends(get_db)):
    return service.list_advertisers(db)
