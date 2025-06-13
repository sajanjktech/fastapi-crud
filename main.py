from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

store = {}  # Simple in-memory key-value store for items

class Item(BaseModel):
    """
    Data model for an item.
    Attributes:
        name (str): Name of the item (required).
        description (str, optional): Optional description of the item.
    """
    name: str
    description: str = None

@app.get("/")
def root():
    """
    Home route to confirm server is running.
    """
    return {"message": "✅ Server running at http://127.0.0.1:8000/"}



@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    """
    Create a new item with a given ID.

    Args:
        item_id (int): Unique ID for the item.
        item (Item): Item data parsed from the request body.

    Raises:
        HTTPException: If an item with the given ID already exists.

    Returns:
        dict: Message indicating successful creation.
    """
    if item_id in store:
        raise HTTPException(status_code=400, detail="Item exists")
    store[item_id] = item
    return {"message": "Item created"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Retrieve an item by its ID.

    Args:
        item_id (int): ID of the item to retrieve.

    Raises:
        HTTPException: If the item does not exist.

    Returns:
        Item: The requested item.
    """
    if item_id not in store:
        raise HTTPException(status_code=404, detail="Item not found")
    return store[item_id]


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """
    Update an existing item by its ID.

    Args:
        item_id (int): ID of the item to update.
        item (Item): New item data from the request body.

    Raises:
        HTTPException: If the item does not exist.

    Returns:
        dict: Message indicating successful update.
    """
    if item_id not in store:
        raise HTTPException(status_code=404, detail="Item not found")
    store[item_id] = item
    return {"message": "Item updated"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """
    Delete an item by its ID.

    Args:
        item_id (int): ID of the item to delete.

    Raises:
        HTTPException: If the item does not exist.

    Returns:
        dict: Message indicating successful deletion.
    """
    if item_id not in store:
        raise HTTPException(status_code=404, detail="Item not found")
    del store[item_id]
    return {"message": "Item deleted"}

@app.get("/items")
def get_all_items():
    """
    Return all items in the store.
    """
    return store

