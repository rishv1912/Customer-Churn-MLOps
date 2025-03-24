from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message" : "Welcome to Customer Churn Prediction"}

# @app.get("/items/{item_id}")
# def read_item(item_id : int , q : str = None):
#     return {"item_id": item_id, "q":q}
@app.get("/")
def read_root():
    return {"message":"Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id : int, query_param: str = None):
    return{"item_id" : item_id, "query_param" : query_param}