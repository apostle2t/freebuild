from fastapi import APIRouter, Depends
from typing import Annotated
from pythonFileStream.dependencies import index

router = APIRouter(prefix="/pictures", tags=["pictures"])

"""
Things to look into later
1. The indexing of items
solution: After uploading the picture, we want to generate an id and store the picture 
with this id 

We then kind of need a global function which will maintain states. 


2. The way to get the items from the request body 
"""

@router.post("/")
async def postPictures():
    """
    So basically we want to create the path so that it accepts file (Images etc)

    We also want to pass the dependency which saves the ID of all the post made.
    we will use the ID to save our file in the database. This will help in queries.

    We want to create some type of database which helps us to store our file.
    In the database, we should be able to pass the file and the ID

    """
    return {"This route is meant for sending pictures"}

@router.get("/")
async def getPictures(id: Annotated[int, Depends(index.getID)]):
    return {"This is your Picture ID": id}

