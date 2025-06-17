from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.db.db import store
from app.models.items import Item

router = APIRouter()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str = Depends(oauth2_scheme)) -> str:
    """
    Verify JWT token and extract the username (subject).

    Args:
        token (str): JWT token passed through the Authorization header.

    Returns:
        str: Username extracted from the token payload.

    Raises:
        HTTPException: 401 error if token is invalid or expired.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/{item_id}")
def create_item(item_id: int, item: Item, username: str = Depends(verify_token)):
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
    store[item_id] = item
    return {"message": f"Item created by {username}"}

@router.get("/{item_id}")
def read_item(item_id: int, username: str = Depends(verify_token)):
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
    return store[item_id]

@router.put("/{item_id}")
def update_item(item_id: int, item: Item, username: str = Depends(verify_token)):
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
    store[item_id] = item
    return {"message": f"Item updated by {username}"}

@router.delete("/{item_id}")
def delete_item(item_id: int, username: str = Depends(verify_token)):
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
    del store[item_id]
    return {"message": f"Item deleted by {username}"}

@router.get("/")
def get_all_items(username: str = Depends(verify_token)):
    """
    Retrieve all items in the store.

    Args:
        username (str): Username from the JWT token.

    Returns:
        dict: All items in the in-memory store.
    """
    return store
