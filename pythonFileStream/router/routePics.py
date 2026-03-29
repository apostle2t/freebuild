from fastapi import APIRouter

router = APIRouter(prefix="/pictures", tags=["pictures"])

"""
Things to look into later
1. The indexing of items
2. The way to get the items from the request body 
"""

@router.put("/")
async def putPictures():
    return {"This route is meant for sending pictures"}

@router.get("/")
async def getPictures():
    return {"This route is meant for getting pictures"}

