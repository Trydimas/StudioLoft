from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from models.queries.core import *
from pages.Email import send_email

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="../../Front/html")

images_data = select_project()

@router.get("/", response_class=HTMLResponse)
def get_home_page(request: Request):
    our_project = select_project()
    staff = select_staff()
    if select_project():
        imgs = select_project()[0]
    return templates.TemplateResponse("home.html", {"request": request,
                                                    "page_title": "Домашняя",
                                                    "ex_carousel_items": imgs,
                                                    "staff_carousel_items": staff,
                                                    "our_project": our_project})

@router.post("/")
async def post_contacts_page(request: Request,
                             f_FIO: str = Form(...),
                             f_phone_number: str = Form(...),
                             f_email: str = Form(...),
                             f_location: str = Form(...),
                             f_size: str = Form(...)):
    print(f_FIO,f_email,f_phone_number,f_size,f_location)
    insert_user(FIO=f_FIO, Phone_number=f_phone_number, Email=f_email, Location=f_location, Size_apartment=f_size)
    message = f"ФИО: {f_FIO}\nНомер телефона: {f_phone_number}\nEmail: {f_email}\nС какой целью письмо: оценка\nРайон: {f_location}\nКвадратура: {f_size}м²"
    subject = "Поступила заявка!"
    to_email = "akentev.dima@bk.ru"
    send_email(subject, message, to_email)
    return RedirectResponse(url=request.url_for('get_home_page'), status_code=303)


@router.get("/portfolio", response_class=HTMLResponse)
def get_portfolio_page(request: Request):
    print(images_data)
    return templates.TemplateResponse("portfolio.html", {"request": request, "page_title": "Портфолио",
                                                         "images": images_data[:9]})

@router.get("/portfolio/more")
async def load_more_images(request: Request, offset: int = 0):
    start = offset * 9
    end = start + 9
    more_images = images_data[start:end]
    projects = []

    for project_tuple in more_images:
        project_dict = {
            "id": project_tuple[0],
            "name": project_tuple[1],
            "size": project_tuple[2],
            "name_ru": project_tuple[3],
            "description": project_tuple[4],
            "images": [str(image) for image in project_tuple[5]] if project_tuple[5] else []
        }
        if project_dict["description"] is None:
            project_dict["description"] = ""  # Если описание None, заменяем на пустую строку
        projects.append(project_dict)

    return {"images": projects}

@router.get("/portfolio/project/{project_id}")
async def read_image(request: Request, project_id: int):
    projects = []
    for project_tuple in images_data:
        project_dict = {
            "id": project_tuple[0],
            "name": project_tuple[1],
            "size": project_tuple[2],
            "name_ru": project_tuple[3],
            "description": project_tuple[4],
            "images": [str(image) for image in project_tuple[5]] if project_tuple[5] else []
        }
        if project_dict["description"] is None:
            project_dict["description"] = ""  # Если описание None, заменяем на пустую строку
        projects.append(project_dict)

    image = next((img for img in projects if img["id"] == project_id), None)
    if image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return templates.TemplateResponse("project.html", {"request": request, "image": image, "page_title": "Проект"})


@router.get("/contacts")
def get_contacts_page(request: Request):
    return templates.TemplateResponse("contacts.html", {"request": request, "page_title": "Контакты"})

@router.post("/contacts")
async def post_contacts_page(request: Request,
                             f_FIO: str = Form(...),
                             f_phone_number: str = Form(...),
                             f_email: str = Form(...),
                             f_type_send_form: str = Form(...),
                             f_message_form: str = Form(...)):
    #print(f_FIO,f_email,f_phone_number,f_message_form,f_type_send_form)
    insert_user(FIO=f_FIO, Phone_number=f_phone_number, Email=f_email, Location="", Size_apartment=0)
    message = f"ФИО: {f_FIO}\nНомер телефона: {f_phone_number}\nEmail: {f_email}\nС какой целью письмо: {f_type_send_form}\nсообщение: {f_message_form}"
    subject = "Поступила заявка!"
    to_email = "akentev.dima@bk.ru"
    send_email(subject, message, to_email)
    return RedirectResponse(url=request.url_for('get_contacts_page'), status_code=303)

