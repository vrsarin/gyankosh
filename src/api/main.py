from fastapi import FastAPI

from models import Bookmark


app = FastAPI()

# ----------------------------------------------------------
# Bookmarks
# ----------------------------------------------------------


@app.get("/bookmarks", tags=["Bookmarks"])
async def get_all_bookmarks():
    return {"Hello": "World"}


@app.post("/bookmarks", tags=["Bookmarks"])
async def add_bookmarks(bookmark: Bookmark):
    return {"item_id": uri}


@app.delete("/bookmarks", tags=["Bookmarks"])
async def delete_bookmark(uri: str):
    return {"item_id": uri}


@app.post("/bookmarks/search", tags=["Bookmarks"])
async def search_bookmarks(uri: str):
    return {"Hello": "World"}

# ----------------------------------------------------------
# Keywords
# ----------------------------------------------------------


@app.get("/keywords", tags=["Keywords"])
async def get_all_keywordss():
    return {"Hello": "World"}


@app.post("/keywords", tags=["Keywords"])
async def add_keywords(keyword: str):
    return {"item_id": keyword}


@app.post("/keywords", tags=["Keywords"])
async def delete_keywords(keyword: str):
    return {"item_id": keyword}
