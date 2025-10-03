from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import Base, engine, get_db
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Order Management API")
@app.post("/orders", response_model=schemas.OrderRead, status_code=201)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    obj = models.Order(item=order.item, quantity=order.quantity, status="pending")
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
@app.get("/orders/{order_id}", response_model=schemas.OrderRead)
def get_order(order_id: int, db: Session = Depends(get_db)):
    obj = db.get(models.Order, order_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Order not found")
    return obj
@app.get("/orders")
def list_orders(db: Session = Depends(get_db)):
    items = db.query(models.Order).order_by(models.Order.id.desc()).all()
    return [{
        "id": o.id, "item": o.item, "quantity": o.quantity, "status": o.status
    } for o in items]
