from fastapi import FastAPI, Request
from pages.router import router as router_pages
from starlette.staticfiles import StaticFiles
from auth.router import router as router_auth
from auth.admin import router as router_api
import logging
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = request.headers.get("X-Request-Id")
    logger.info(f"rid={idem} start request path={request.url.path}")
    response = await call_next(request)
    logger.info(f"rid={idem} completed_in={response.headers.get('X-Process-Time')} status_code={response.status_code}")
    return response

app.include_router(router_pages)
app.include_router(router_auth)
app.include_router(router_api)
app.mount('/Front', StaticFiles(directory="../../Front"), name='static')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)