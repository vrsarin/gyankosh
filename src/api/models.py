from pydantic import BaseModel

class Bookmark(BaseModel):
    uid: str | None = None
    title: str | None = None
    uri: str 
    selectedtext: str | None = None