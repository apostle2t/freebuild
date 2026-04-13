from fastapi import APIRouter, Depends
from typing import Annotated
from pythonFileStream.dependencies import index


router = APIRouter(prefix="/videos", tags=["videos"])

"""
Things to look into later
1. The indexing of items
2. The way to get the items from the request body 
"""

# print(index.getID())
# print(index.getID())
# print(index.getID())
# print(index.getID())

@router.put("/")
async def putVideos():
    return {"This route is meant for sending videos"}


@router.get("/")
async def getVideos(id: Annotated[int, Depends(index.getID)]):
    return {"Hello world this is your ID": id}


