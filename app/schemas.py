from pydantic import BaseModel, Field
class OrderCreate(BaseModel):
    item: str = Field(min_length=1)
    quantity: int = Field(ge=1)
class OrderRead(BaseModel):
    id: int
    item: str
    quantity: int
    status: str
    class Config:
        from_attributes = True
