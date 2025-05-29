from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
app = FastAPI()

abs_path = os.path.dirname(os.path.realpath(__file__))
print(f"Absolute path: {abs_path}")
# html 템플릿을 사용하기 위한 설정
templates = Jinja2Templates(directory=f"{abs_path}/templates")

# static 파일을 사용하기 위한 설정
app.mount("/static", StaticFiles(directory=f"{abs_path}/static"), name="static")


@app.get("/")
async def home(request: Request):
    todo = 20
    # html 템플릿을 렌더링하여 데이터를 리턴
    return templates.TemplateResponse("index.html",
                                      {"request": request,
                                       "todo": todo})