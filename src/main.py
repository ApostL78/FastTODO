from fastapi import FastAPI

app = FastAPI(
    title="Task manager"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


