from fastapi import FastAPI
app = FastAPI()
@app.get("/")

def read_root():
    return {"message": "Hello, Natalie! Your server is running."}
