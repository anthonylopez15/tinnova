import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import constants
from app.endpoints.veiculos import router

app = FastAPI(swagger_static={"favicon": constants.FAVICON})

app.include_router(router, tags=["Api"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Index"], summary="Routes base")
async def index():
    return "Tinnova Software on demand version " + constants.API_VERSION


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
