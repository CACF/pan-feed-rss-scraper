import os
import uvicorn
from fastapi import Body
from mangum import Mangum
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.responses import JSONResponse

load_dotenv()
from app.utils.feed_urls import feed_urls
from app.feed_blc import feed_starter

app = FastAPI()
handler = Mangum(app)


@app.get("/")
def home():
    return {"api_version": "1.0"}


@app.get("/sources")
def get_sources():
    sources = list(feed_urls.keys())
    return {"sources": sources}


@app.get("/genres")
def get_genres():
    all_genres = set()
    for single_source in feed_urls.values():
        urls_list = single_source.get("urls")
        for single_url in urls_list:
            all_genres.add(single_url.get("genre"))

    return {"genres": list(all_genres)}


@app.post("/ingest")
def start_feed(data_dict: dict = Body(..., example={"sources": [], "genres": []})):
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


if __name__ == "__main__":
    uvicorn.run(
        "run:app",
        host=os.environ.get("HOST"),
        port=int(os.environ.get("PORT")),
        reload=True if os.environ.get("ENVIRONMENT") == "development" else False,
    )
