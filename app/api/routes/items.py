from fastapi import APIRouter , HTTPException
from app.db.db import store
from app.models.items import Item

router = APIRouter()

@router.post("/{item_id}")
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


@router.get("/{item_id}")
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


@router.put("/{item_id}")
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


@router.delete("/{item_id}")
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

@router.get("/")
def get_all_items():
    """
    Return all items in the store.
    """
    return store

