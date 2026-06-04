from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates=Jinja2Templates(directory="templates")

posts:list[dict]=[
{
    "id":1,
    "title":"FastApi Awesome!",
    "author":"Corey Schaler",
    "content":"This Framework is really easy to use and super fast",
    "date_posted":"April 20,2025"
    },{
        "id":2,
        "title":"Python is great for web development",
        "author":"Jane Doe",
        "content":"Python is great language for web develomnet, and FastApi makes it even better",
        "date_posted":"April 21, 2025"
    }
] 

@app.get("/",include_in_schema=False,name="home")
@app.get("/post",include_in_schema=False,name="post")
def home(request:Request):
    return templates.TemplateResponse(request,"home.html",{"posts":posts,"title":"Home"})

@app.get("/api/post")
def get_posts():
    return posts

