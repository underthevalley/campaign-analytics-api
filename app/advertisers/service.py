from sqlalchemy.orm import Session
from sqlalchemy import func 
from .models import Advertiser
from .schemas import AdvertiserCreate

class AdvertiserAlreadyExists(Exception):
    """Raised when tryint to create an advertiser with same name"""
    pass

def create_advertiser(db: Session, data: AdvertiserCreate) -> Advertiser:
    # check if advertiser same name exists

    is_present = (
        db.query(Advertiser)
        .filter(func.lower(Advertiser.name) == data.name.lower())
        .first
    )

    if is_present: 
        raise AdvertiserAlreadyExists(f"Advertiser '{data.name}' already exists.")

    advertiser = Advertiser(name=data.name)
    db.add(advertiser)
    db.flush()   # assign ID without committing

    return advertiser

def list_advertisers(db: Session):
    return db.query(Advertiser).all()
