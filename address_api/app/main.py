from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/addresses/', response_model=schemas.Address)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db=db, address=address)


@app.get('/address/{address_id}', response_model=schemas.Address)
def get_address(address_id:int ,db : Session= Depends(get_db)):
    db_address = crud.get_address(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code = 404, detail='address not found')
    return db_address

@app.get('/addresses/', response_model= list[schemas.Address])
def get_addresses(skip: int=0, limit : int=10 ,db :Session = Depends(get_db)):
    return crud.get_addresses(db, skip=skip ,limit=limit)

@app.put('/addresses/{address_id}', response_model= schemas.Address)
def update_adddress(address_id:int, db :Session = Depends(get_db), address = schemas.AddressUpdate):
    db_address = crud.update_address(db=db , address_id=address_id,address=address)
    if db_address is None:
        raise HTTPException(status_code=404, detail='Address not found')
    return db_address


@app.delete('/address/{address_id}', response_model=schemas.Address)
def delete_address(address_id : int, db: Session = Depends(get_db)):
    db_address = crud.delete_address(db=db , address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail='Address not found')
    return db_address