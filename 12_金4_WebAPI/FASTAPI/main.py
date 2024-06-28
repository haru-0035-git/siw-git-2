from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
# FastAPI本体を生成
app = FastAPI()

class Item(BaseModel):
    name : str
    price : float
    is_offer:bool = None

def read_root():
    return {'Hello':'World'}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/sum/")
def sum_num(num1:float,num2:float):
    ans = num1 + num2
    return {"ans":ans}

@app.get("/div/")
def div_num(num1:int,num2:int):
    if num2 == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    ans = num1 / num2
    return {"ans":ans}