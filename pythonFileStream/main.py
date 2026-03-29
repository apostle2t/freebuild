from fastapi import FastAPI
from pythonFileStream.router import routePics, routeVids


app = FastAPI()
app.include_router(routePics.router)
app.include_router(routeVids.router)

@app.get("/")
async def getHome():
    return {"Message: This is the default route"}




