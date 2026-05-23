# TODO: Step 1 - Import FastAPI and set up the first test route. DONE TEST
# Day 1 - Learned Python Decorators and Virtual Environments

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"active_threats": 5, "Welcome TO": "Cyber Threat API"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
