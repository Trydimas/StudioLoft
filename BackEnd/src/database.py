from sqlalchemy import URL, create_engine, text
from config import settings_asyncpg, settings_psycopg

sync_engine = create_engine(
    url=settings_psycopg,
    echo=False,
    # pool_size=5,
    # max_overflow=10
)




