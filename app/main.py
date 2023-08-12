from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello from fastapi_template"}


@app.get("/ping")
def ping():
    return {"ping": "pong"}
