from typing import Annotated
from fastapi import File

class pictures:
    pic: Annotated[bytes, File()]



