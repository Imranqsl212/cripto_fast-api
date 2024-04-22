from fastapi import FastAPI
from uvicorn import run
from router import router as crypto_router


app = FastAPI()
app.include_router(crypto_router)


if __name__ == "__main__":
    run("main:app", port=5000, reload=True, host="127.0.0.1")
