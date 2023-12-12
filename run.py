import os
import uvicorn
from dotenv import load_dotenv
load_dotenv()



if __name__ == "__main__":
    uvicorn.run(
        "app.v1.blueprints:app",
        host=os.environ.get("HOST"),
        port=int(os.environ.get("PORT")),
        reload=True if os.environ.get("ENVIRONMENT") == "development" else False,
    )
