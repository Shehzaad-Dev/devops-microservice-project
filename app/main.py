from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/users")
def users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
