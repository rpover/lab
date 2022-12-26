import uvicorn
import fastapi
from fastapi.responses import RedirectResponse
from routers import reader
from routers import book
from routers import staff
from sql_base.base import  BaseWorker

app = fastapi.FastAPI()
app.include_router(reader.router)
app.include_router(book.router)

if __name__ == '__main__':
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')

    if not base_worker.check_base():
        base_worker.create_base('sql_base/scripts/3.sql')

    uvicorn.run("start_server:app", reload=True)