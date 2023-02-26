from fastapi import FastAPI

from api.routers import calc, done, item, task, token, user

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)
app.include_router(item.router)
app.include_router(token.router)
app.include_router(calc.router)
app.include_router(user.router)


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}
