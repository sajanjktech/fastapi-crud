from pydantic import BaseModel

class Item(BaseModel):
    """
    Data model for an item.
    Attributes:
        name (str): Name of the item (required).
        description (str, optional): Optional description of the item.
    """
    name: str
    description: str = None

class ItemInDb(Item):
    username:str