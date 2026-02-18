from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.advertiser import Advertiser
from app.schemas.advertiser import AdvertiserCreate, AdvertiserRead

router = APIRouter(prefix="/advertisers", tags=["Advertisers"])


@router.post("/", response_model=AdvertiserRead)
def create_advertiser(
    advertiser: AdvertiserCreate,
    db: Session = Depends(get_db),
):
    db_advertiser = Advertiser(name=advertiser.name)
    db.add(db_advertiser)
    db.commit()
    db.refresh(db_advertiser)
    return db_advertiser


@router.get("/", response_model=list[AdvertiserRead])
def list_advertisers(db: Session = Depends(get_db)):
    return db.query(Advertiser).all()
