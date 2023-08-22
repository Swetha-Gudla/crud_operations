from fastapi import APIRouter
from pydantic import BaseModel
app=APIRouter()

db={}

class Items(BaseModel):
    name: str
    desc : str

# @app.get("/")
# async def root(name: str):
#     return{"message":"Welcome "+name}

@app.get("/")
def get_all_data():
    return db

@app.post("/items")
def Create_Item(item:Items):
    db[item.name]=item.desc
    return {"items":item}

@app.get("/")
def get_all_data():
    return db

@app.delete("/")
def delete_data(name:str):
    del db[name]
    return db

@app.put("/")
def update_data(item:Items):
    db[item.name]=item.desc
    return db


if __name__ == '__main__':
    app.run()
    


