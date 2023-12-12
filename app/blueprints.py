from mangum import Mangum
from fastapi import FastAPI
from fastapi import Body
from app.utils.feed_urls import feed_urls
from app.feed_blc import feed_starter
from fastapi.responses import JSONResponse

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
    data_dict: dict = Body(..., example={"sources": [], "genres": []})
):
    try:
        if not data_dict.get("sources", None):
            return JSONResponse(
                {"status": "failed", "Error": "Please provide valid sources."},
            )
        feed_starter(data_dict)
        return JSONResponse(
            {"status": "success"},
        )
    except Exception as ex:
        return JSONResponse(
            {"status": "failed", "Error": str(ex)},
        )