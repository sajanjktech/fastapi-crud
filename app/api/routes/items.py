"""
items management , here the user needs not to be authorised to just see the products but for uploading or to change a product 
he must be

"""



from fastapi import APIRouter, HTTPException, Depends
from app.db.db import store
from app.models.items import Item,ItemInDb
from app.api.routes.auth import verify_token

router = APIRouter()

@router.post("/{item_id}")
def create_item(item_id: str, item: Item, username: str = Depends(verify_token)):
    """
    Create a new item with a given ID.

    Args:
        item_id (int): ID to assign to the new item.
        item (Item): Item data sent in the request body.
        username (str): Username from the JWT token.

    Returns:
        dict: Success message.

    Raises:
        HTTPException: 400 if item already exists.
    """
    if item_id in store:
        raise HTTPException(status_code=400, detail="Item exists")
    store[item_id] = ItemInDb(**item.dict(),username=username)
    return {"message": f"Item created by {username}"}

@router.get("/{item_id}")
def read_item(item_id: str, username: str = Depends(verify_token)):
    """
    Retrieve an item by its ID.

    Args:
        item_id (int): ID of the item to retrieve.
        username (str): Username from the JWT token.

    Returns:
        Item: The item data.

    Raises:
        HTTPException: 404 if item not found.
    """
    if item_id not in store:
        raise HTTPException(status_code=404, detail="Item not found")
    print(type(store[item_id]))
    return store[item_id]

@router.put("/{item_id}")
def update_item(item_id: str, item: Item, username: str = Depends(verify_token)):
    """
    Update an existing item by its ID.

    Args:
        item_id (int): ID of the item to update.
        item (Item): Updated item data.
        username (str): Username from the JWT token.

    Returns:
        dict: Success message.

    Raises:
        HTTPException: 404 if item not found.
    """
    if item_id not in store:
        raise HTTPException(status_code=404, detail="Item not found")
    item_data = store[item_id]
    print(type(item_data))
    if item_data.username != username:
        raise HTTPException(status_code=401,detail = "You are not authorized")
    store[item_id] = ItemInDb(**item.dict(),username=username)
    return {"message": f"Item updated by {username}"}

@router.delete("/{item_id}")
def delete_item(item_id: str, username: str = Depends(verify_token)):
    """
    Delete an item by its ID.

    Args:
        item_id (int): ID of the item to delete.
        username (str): Username from the JWT token.

    Returns:
        dict: Success message.

    Raises:
        HTTPException: 404 if item not found.
    """
    if item_id not in store:
        raise HTTPException(status_code=404, detail="Item not found")
    item_data = store[item_id]
    if item_data.username!=username:
        raise HTTPException(status_code=401,detail = "You are not authorized")
    del store[item_id]
    return {"message": f"Item deleted by {username}"}

@router.get("/")
def get_all_items():
    """
    Retrieve all items in the store.

    Args:
        username (str): Username from the JWT token.

    Returns:
        dict: All items in the in-memory store.
    """

    return store
