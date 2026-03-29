from fastapi import APIRouter

router = APIRouter(prefix="/videos", tags=["videos"])

"""
Things to look into later
1. The indexing of items
2. The way to get the items from the request body 
"""


@router.put("/")
async def putVideos():
    return {"This route is meant for sending videos"}


@router.get("/")
async def getVideos():
    return {"This route is meant for getting the videos"}


