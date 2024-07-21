from typing import List, Optional

from pydantic import BaseModel

class User(BaseModel):
    FIO: str
    Location: str
    Size_apartment: int
    Email: str
    Phone_number: str


class Project(BaseModel):
    Name_project: str
    Size_apartment: int
    Description: Optional[str] = None
    Name_ru: Optional[str] = None
    Images: List[str]

class Staffs(BaseModel):
    Name: str
    Last_name: str
    Father_name: str
    Description: str
    Phrase: str
    Image: str

class Client(BaseModel):
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


class ProjectData(BaseModel):
        id: int
        name: str
        size: int
        address: str
        task_description: Optional[str] = None
        images: List[str]