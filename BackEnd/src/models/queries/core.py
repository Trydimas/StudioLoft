from database import sync_engine
from sqlalchemy import text, insert, select, update, delete
from models.models import *
from models.scheme import *






def create_tables():
    metadata.drop_all(sync_engine)
    metadata.create_all(sync_engine)


# user
def insert_user(FIO: str, Location: str, Size_apartment: int, Email: str, Phone_number: str):
    with sync_engine.connect() as conn:
        stmt = insert(tbl_users).values(
            [{
            "FIO": FIO,
            "location": Location,
            "size_apartment": Size_apartment,
            "email": Email,
            "phone_number": Phone_number
            }]
        )
        conn.execute(stmt)
        conn.commit()


def select_user():
    with sync_engine.connect() as conn:
        query = select(tbl_users)
        result = conn.execute(query)
        return result.all()

def delete_user(user_id: int):
    with sync_engine.connect() as conn:
        stmt = tbl_users.delete().where(tbl_users.c.id == user_id)
        conn.execute(stmt)
        conn.commit()


# Функция для обновления проекта в базе данных
def update_user(user_id: int,
                fio_u: Optional[str] = None,
                size_apartment: Optional[str] = None,
                location: Optional[str] = None,
                email: Optional[str] = None,
                phone_number: Optional[str] = None):
    with sync_engine.connect() as conn:
        stmt = update(tbl_projects).where(tbl_projects.c.id == user_id)
        values = {}
        if fio_u is not None:
            values['FIO'] = fio_u
        if size_apartment is not None:
            values['size_apartment'] = size_apartment
        if location is not None:
            values['location'] = location
        if email is not None:
            values['email'] = email
        if phone_number is not None:
            values['phone_number'] = phone_number
        if values:
            stmt = stmt.values(**values)
            conn.execute(stmt)
            conn.commit()




#project
def insert_project(project:Project):
    with sync_engine.connect() as conn:
        stmt = tbl_projects.insert().values(
            Name_project=project.Name_project,
            Size=project.Size_apartment,
            Description=project.Description,
            Name_ru=project.Name_ru,
            Images=project.Images

        )
        conn.execute(stmt)
        conn.commit()

def select_project():
    with sync_engine.connect() as conn:
        query = select(tbl_projects)
        result = conn.execute(query)
        return result.all()

# Функция для обновления проекта в базе данных
def update_project(project_id: int,
                   name_project: Optional[str] = None,
                   size_apartment: Optional[str] = None,
                   description: Optional[str] = None,
                   name_ru: Optional[str] = None,
                   images: Optional[List[str]] = None):
    with sync_engine.connect() as conn:
        stmt = update(tbl_projects).where(tbl_projects.c.id == project_id)
        values = {}
        if name_project is not None:
            values['Name_project'] = name_project
        if size_apartment is not None:
            values['Size_apartment'] = size_apartment
        if description is not None:
            values['Description'] = description
        if name_ru is not None:
            values['Name_ru'] = name_ru
        if images is not None:
            values['Images'] = images
        if values:
            stmt = stmt.values(**values)
            conn.execute(stmt)
            conn.commit()

def delete_project(staff_id: int):
    with sync_engine.connect() as conn:
        stmt = tbl_projects.delete().where(tbl_projects.c.id == staff_id)
        conn.execute(stmt)
        conn.commit()


#staff
def insert_staff(staff:Staffs):
    with sync_engine.connect() as conn:
        stmt = tbl_staff.insert().values(
            Name=staff.Name,
            Last_name=staff.Last_name,
            Father_name=staff.Father_name,
            Description=staff.Description,
            Phrase=staff.Phrase,
            Image=staff.Image
        )
        conn.execute(stmt)
        conn.commit()

def select_staff():
    with sync_engine.connect() as conn:
        query = select(tbl_staff)
        result = conn.execute(query)
        return result.all()

def update_staff(staff_id: int,
                 Name_staff: Optional[str] = None,
                 Last_name_staff: Optional[str] = None,
                 Father_name_staff: Optional[str] = None,
                 Description_staff: Optional[str] = None,
                 Phrase_staff: Optional[str] = None,
                 Image_staff: Optional[str] = None):
    with sync_engine.connect() as conn:
        stmt = update(tbl_staff).where(tbl_staff.c.id == staff_id)
        values = {}
        if Name_staff is not None:
            values['Name'] = Name_staff
        if Last_name_staff is not None:
            values['Last_name'] = Last_name_staff
        if Father_name_staff is not None:
            values['Father_name'] = Father_name_staff
        if Description_staff is not None:
            values['Description'] = Description_staff
        if Phrase_staff is not None:
            values['Phrase'] = Phrase_staff
        if Image_staff is not None:
            values['Image'] = Image_staff
        if values:
            stmt = stmt.values(**values)
            conn.execute(stmt)
            conn.commit()

def delete_staff(staff_id: int):
    with sync_engine.connect() as conn:
        stmt = tbl_staff.delete().where(tbl_staff.c.id == staff_id)
        conn.execute(stmt)
        conn.commit()
