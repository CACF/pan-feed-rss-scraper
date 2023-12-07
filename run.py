import os
import uvicorn
from mangum import Mangum
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()
from feed import feed_starter


app = FastAPI()
handler = Mangum(app)


@app.get("/")
def home():
    return {"api_version": "1.0"}


@app.get("/ingest")
def start_feed():
    try:
        feed_starter()
        return JSONResponse(
            {"status": "success"},
        )
    except Exception as ex:
        return JSONResponse(
            {"status": "failed", "Error": str(ex)},
        )


if __name__ == "__main__":
    uvicorn.run(
        "run:app",
        host=os.environ.get("HOST"),
        port=int(os.environ.get("PORT")),
        reload=True if os.environ.get("ENVIRONMENT") == "development" else False,
    )
