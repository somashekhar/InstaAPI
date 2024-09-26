from fastapi import FastAPI
from fastapi import Body
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Som!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/posts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title: {payLoad['title']} content: {payLoad['content']}"}
