from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None

class ItemInDb(Item):
    username: str