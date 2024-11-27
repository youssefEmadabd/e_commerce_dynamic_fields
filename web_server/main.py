from fastapi import FastAPI, HTTPException, Request

from helper import create_access_token, is_valid_password
from database_manager.constants import UserKeys
from database_manager.database_manager import DatabaseManager
from decorators.authentication_decorator import protected

# FastAPI Initialization
app = FastAPI()
database_manager = DatabaseManager()

@app.post("/product/")
@protected
async def create_product(request: Request):
    """
    Add a new product
    
    Test payload: {
        "price": 50,
        "quantity": 10,
        "type": "chair",
        "description": "description",
        "image": "https://picsum.photos/200/300",
        "name": "test",
        "model_number": 1,
        "brand_name": "dell",
        "dimensions": "4x5",
        "color": "white",
        "size": "49"
    }
    """
    data = await request.json()
    product, create_status = database_manager.create_product(data)
    if not create_status:
        raise HTTPException(status_code=400, detail="failed to create product")

    return {"message": "Product created successfully", "product": product}

@app.get("/product/{product_id}")
@protected
async def get_product(product_id: str, request: Request):
    """
    Get the product.
    
    example id: generic_id
    """
    product, status = database_manager.get_product(product_id)
    if not status:
        raise HTTPException(status_code=404, detail="Product not found.")

    return product

@app.patch("/product/{product_id}")
@protected
async def update_product(product_id: str, request: Request):
    """
    Update the attributes of a model type.
    
    example payload: 
        {
        "quantity": 20
    }
    example id: generic_id
    """
    data = await request.json()
    product, status = database_manager.update_product(product_id=product_id, update_object=data)
    if not status:
        raise HTTPException(status_code=404, detail="Product not found.")

    return product

@app.delete("/product/{product_id}")
@protected
async def delete_product(product_id: str, request: Request):
    """
    Delete a product by id.
    """
    status = database_manager.delete_product(product_id)
    if not status:
        raise HTTPException(status_code=404, detail="Cannot delete product.")

    return {"message": "Model deleted successfully."}

@app.post("/login")
async def login(data: dict):
    """
    Login endpoint to get a jwt token.
    => Test payload: {
            "username": "generic_username",
            "password": "test"
        }
    Args:
        data (dict): Dictionary with username and password.

    Returns:
        dict: A dictionary with the jwt token.

    Raises:
        HTTPException: 401 if username or password is invalid.
    """
    username = data.get("username")
    password = data.get("password")
    user, status = database_manager.get_user(username)
    if not status or not user:
        raise HTTPException(status_code=401, detail="Invalid username")
    
    if is_valid_password(user[UserKeys.PASSWORD.value], password):
        token = create_access_token({"sub": username})
        return {"access_token": token}

    raise HTTPException(status_code=401, detail="Invalid password")
