import os
import uvicorn
from mangum import Mangum
from fastapi import FastAPI, Body
from feed_urls import feed_urls
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()
from feed import feed_starter


app = FastAPI()
handler = Mangum(app)


@app.get("/")
def home():
    return {"api_version": "1.0"}


@app.get("/sources")
def sources():
    news = list(feed_urls.keys())
    return {"sources": news}


@app.get("/ingest")
def start_feed(
    data_dict: dict = Body(..., example={"sources": ["genres"]})
):
    try:
        feed_starter(data_dict)
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
