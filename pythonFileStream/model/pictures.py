from typing import Annotated
from fastapi import File

class pictures:
    idPic: int
    pic: Annotated[bytes, File()]



