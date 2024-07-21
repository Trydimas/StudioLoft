from fastapi import FastAPI, HTTPException, APIRouter
from typing import List
from pydantic import BaseModel
from models.queries.core import *


router = APIRouter(
    prefix="/api",
    tags=["api"]
)

# Модели данных
class Client(BaseModel):
    id: int
    fio: str
    region: str
    size: str
    email: str
    phone: str

class Staff(BaseModel):
    id: int
    first_name: str
    last_name: str
    patronymic: str
    photo: str
    description: str
    phrase: str

class Portfolio(BaseModel):
    id: int
    storage_name: str
    size: str
    location: str
    description: str
    images: str


def get_user_normal():
    fix_users = []

    for users_tuple in select_user():
            users_dict = {
                "id": users_tuple[0],
                "FIO": users_tuple[1],
                "location": users_tuple[2],
                "size_apartment": users_tuple[3],
                "email": users_tuple[4],
                "phone_number": users_tuple[5]
            }
            fix_users.append(users_dict)
    return fix_users

def get_project_normal():
    projects = []

    for project_tuple in select_project():
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
    return projects

def get_staff_normal():
    fix_staff = []
    print(select_staff())
    for staff_tuple in select_staff():
            staff_dict = {
                "id": staff_tuple[0],
                "Name": staff_tuple[1],
                "Last_name": staff_tuple[2],
                "Father_name": staff_tuple[3],
                "Description": staff_tuple[4],
                "Phrase": staff_tuple[5],
                "IMG": staff_tuple[6]
            }
            fix_staff.append(staff_dict)
    return fix_staff



# Define routes to work with clients
@router.get("/clients")
async def get_clients():
    return get_user_normal()

@router.post("/clients", response_model=Client)
async def add_client(client: Client):
    insert_user(client.fio, client.region, client.size, client.email, client.phone)
    return client

@router.put("/clients/{client_id}")
async def update_client(client_id: int, user: Client):
    update_user(
        user_id=client_id,
        fio_u=user.fio,
        size_apartment=user.size,
        location=user.region,
        email=user.email,
        phone_number=user.phone
    )
    return user



@router.delete("/clients/{client_id}")
async def delete_client(client_id: int):
    delete_user(client_id)
    return {"message": "Клиент удален"}

# Define routes to work with staff
@router.get("/staff")
async def get_staff():
    return get_staff_normal()

@router.post("/staff", response_model=Staffs)
async def add_staff(member: Staffs):
    insert_staff(member)
    return member

@router.put("/staff/{member_id}", response_model=Staffs)
async def update_staff(member_id: int, member: Staffs):
    update_staff(member_id, member.Name, member.Last_name, member.Father_name, member.Image, member.Description, member.Phrase)
    return member

@router.delete("/staff/{member_id}")
async def delete_staff(member_id: int):
    delete_staff(member_id)
    return {"message": "Сотрудник удален"}

# Define routes to work with portfolio
@router.get("/portfolio")
async def get_portfolio():
    return get_project_normal()

@router.post("/portfolio", response_model=Project)
async def add_portfolio(item: Project):
    insert_project(item)
    return item

@router.put("/portfolio/{item_id}", response_model=Project)
async def update_portfolio(project_id: int,
                   name_project: Optional[str] = None,
                   size_apartment: Optional[str] = None,
                   description: Optional[str] = None,
                   name_ru: Optional[str] = None,
                   images: Optional[List[str]] = None):
    item = {project_id,  name_project, size_apartment, description, name_ru, images}
    update_portfolio(**item)
    return item

@router.delete("/portfolio/{item_id}")
async def delete_portfolio(item_id: int):
    delete_project(item_id)
    return {"message": "Элемент портфолио удален"}


