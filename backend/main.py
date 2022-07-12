from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)

@app.get("/")
def hello_api():
    return {"detail", "Hello sysmoon!"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)