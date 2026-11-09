from fastapi import FastAPI

app = FastAPI(title="Task Tracker API")


@app.get("/")
def read_root():
    return {"message": "Task Tracker API is running"}