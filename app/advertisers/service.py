from sqlalchemy.orm import Session
from .models import Advertiser
from .schemas import AdvertiserCreate

def create_advertiser(db: Session, data: AdvertiserCreate) -> Advertiser:
    advertiser = Advertiser(name=data.name)

    db.add(advertiser)
    db.flush()   # get ID without committing

    return advertiser


def list_advertisers(db: Session):
    return db.query(Advertiser).all()
