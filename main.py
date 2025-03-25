# from fastapi import FastAPI, HTTPException
# from enum import Enum
# from pydantic import BaseModel

# app = FastAPI()

# class Category(Enum):
#     TOOLS = 'tools'
#     CONSUMABLES = 'consumables'

# class Item(BaseModel):
#     name: str
#     price: float
#     count: int
#     id: int
#     category: Category

# items ={
#     0 : Item(name="Kratos", price=8.99, count=20,id=0, category=Category.TOOLS),
#     1 : Item(name="God", price=7.99, count=18,id=1, category=Category.TOOLS),
#     2 : Item(name="Candy", price=4.99, count=10,id=2, category=Category.CONSUMABLES),
# }

# @app.get("/")
# def read_root() -> dict[str,dict[int,Item]]:
#     return {"items": items}

# @app.get("/items/{item_id}")
# def query_item_by_id(item_id : int) -> Item:
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")
    
#     return items(item_id)


    