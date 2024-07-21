from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Depends, HTTPException, Request, Response, APIRouter, Form
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_302_FOUND

security = HTTPBasic()

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

templates = Jinja2Templates(directory="../../Front/html")

def get_current_username(request: Request):
    username = request.cookies.get("username")
    if not username:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return username

# Роут для отображения страницы входа
@router.get("/login", response_class=HTMLResponse)
def get_login(request: Request, error: bool = False):
    return templates.TemplateResponse("auth.html", {"request": request, "error": error})

# Роут для обработки входа
@router.post("/login/submit")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    correct_username = "admin"
    correct_password = "password"
    if username == correct_username and password == correct_password:
        response = RedirectResponse(url=("/docs"), status_code=HTTP_302_FOUND)
        response.set_cookie(key="username", value=username)
        return response
    else:
        return templates.TemplateResponse("auth.html", {"request": request, "error": True})
        #raise HTTPException(status_code=401, detail="Incorrect username or password")

# Роут для админ панели
@router.get("/admin", response_class=HTMLResponse)
def get_admin_panel(request: Request, username: str = Depends(get_current_username)):
    return templates.TemplateResponse("admin.html", {"request": request, "username": username})
