from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates



router = APIRouter()

templates = Jinja2Templates(directory="src/templates")

@router.get("/", response_class=HTMLResponse)
async def get_info_page(request: Request):

    return templates.TemplateResponse("getinfo.html", {"request": request})

