from sqlalchemy import MetaData, Integer, String, Table, Column, JSON

metadata = MetaData()


tbl_projects = Table(
    "projects",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("Name_project", String, nullable=False),
    Column("Size", Integer, nullable=False),
    Column("Name_ru", String),
    Column("Description", String),
    Column("Images", JSON, nullable=False)
)

tbl_staff = Table(
        'staff',
        metadata,
        Column("id", Integer, primary_key=True),
        Column("Name", String, nullable=False),
        Column("Last_name", String, nullable=False),
        Column("Father_name", String, nullable=False),
        Column("Description", String, nullable=False),
        Column("Phrase", String, nullable=False),
        Column("Image", String, nullable=False)
)

tbl_users = Table(
    'users',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("FIO", String, nullable=False),
    Column("location", String, nullable=False),
    Column("size_apartment", Integer, nullable=False),
    Column("email", String, nullable=False),
    Column("phone_number", String, nullable=False)
)

























