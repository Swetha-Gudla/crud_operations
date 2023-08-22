# from typing import Union

# from fastapi import APIRouter

# router = APIRouter()


# @router.get("/")
# def read_root():
#     return {"Hello": "World"}


# @router.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# if __name__ == '__main__':
#     router.run()

from fastapi import APIRouter, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates

from fastapi.responses import RedirectResponse

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@router.post("/add")
async def add(request: Request, name: str = Form(...)):
    print(name)
    return RedirectResponse(url=router.url_path_for("home"),status_code = status.HTTP_303_SEE_OTHER)


@router.get("/addnew")
async def addnew(request:Request):
    return templates.TemplateResponse("addnew.html",{"request":request})