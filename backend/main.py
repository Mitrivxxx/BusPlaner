from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model danych dla post request
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}

