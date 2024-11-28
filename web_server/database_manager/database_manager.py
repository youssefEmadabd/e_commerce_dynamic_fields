from uuid import uuid4
from typing import Tuple
from helper import validate_fields
from database_manager.constants import *

class DatabaseManager:
    """ a database manager for an in-memory dictionary acting as a database
    """
    database_dict: dict
    
    def __init__(self):
        self.database_dict = {
            TableNames.USERS.value: 
                {
                    "generic_id": 
                    {
                        "name": "generic_name",
                        "username": "generic_username",
                        "password": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
                    }
                },
            TableNames.PRODUCTS.value: {
                "generic_id": {
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
            }
        }

    def get_products(self) -> Tuple[list, bool]:
        """
        Retrieves all products from the in-memory database.

        Returns:
            Tuple[list, bool]: A tuple of the list of products and a boolean indicating if retrieval was successful.
        """
        products = self.database_dict.get(TableNames.PRODUCTS.value)
        if not products:
            return [], False

        return list(products.values()), True

    def get_product(self, product_id: str) -> Tuple[dict, bool]:
        """
        Retrieves a product from the in-memory database based on the product id.

        Args:
            product_id (str): The unique id of the product.

        Returns:
            Tuple[dict, bool]: A tuple of the product dictionary and a boolean indicating if retrieval was successful.
        """
        products = self.database_dict.get(TableNames.PRODUCTS.value)
        if not products:
            return {}, False

        product = products.get(product_id)
        if not product:
            return {}, False

        product = product | {ProductKeys.ID.value: product_id}

        return product, True
    
    def create_product(self, product: dict) -> Tuple[dict, bool]:
        """
        Creates a new product in the database.

        Args:
            product (dict): The new product.

        Returns:
            Tuple[dict, bool]: A tuple of the new product and a boolean indicating if creation was successful.
        """
        product_id = str(uuid4())
        if not product.get(ProductKeys.TYPE.value):
            return {}, False
        
        type = product.get(ProductKeys.TYPE.value)
        list_of_available_attributes = [key.value for key in ProductKeys]
        
        if type == "laptop":
            list_of_available_attributes += [key.value for key in Laptops]
        
        elif type == "chair":
            list_of_available_attributes += [key.value for key in Chairs]
        
        else:
            return {}, False
        
        if not validate_fields(product, list_of_available_attributes):
            return {}, False

        self.database_dict[TableNames.PRODUCTS.value][product_id] = product

        return product, True
    
    def update_product(self, product_id: str, update_object: dict) -> Tuple[dict, bool]:
        """
        Updates an existing product in the database with the provided update object.

        Args:
            product_id (str): The unique id of the product to be updated.
            update_object (dict): A dictionary containing the fields to update and their new values.

        Returns:
            Tuple[dict, bool]: A tuple containing the updated product dictionary and a boolean indicating if the update was successful.
        """
        products = self.database_dict.get(TableNames.PRODUCTS.value)

        if not products:
            return {}, False

        product = products.get(product_id)
        if not product:
            return {}, False
        
        type = product.get(ProductKeys.TYPE.value)
        list_of_available_attributes = [key.value for key in ProductKeys]
        
        if type == "laptop":
            list_of_available_attributes += [key.value for key in Laptops]
        
        elif type == "chair":
            list_of_available_attributes += [key.value for key in Chairs]
        
        else:
            return {}, False
        
        if not validate_fields(update_object, list_of_available_attributes):
            return {}, False

        self.database_dict[TableNames.PRODUCTS.value][product_id] = {**product, **update_object}

        return self.database_dict[TableNames.PRODUCTS.value][product_id], True
    
    def delete_product(self, product_id: str) -> bool:
        """
        Deletes a product from the database based on the product id.

        Args:
            product_id (str): The unique id of the product to be deleted.

        Returns:
            bool: A boolean indicating if the deletion was successful.
        """
        products = self.database_dict.get(TableNames.PRODUCTS.value)
        if not products:
            return False

        product = products.get(product_id)
        if not product:
            return False
        
        del products[product_id]
        return True
    
    def get_user(self, username: str) -> Tuple[dict, bool]:
        """
        Retrieves a user from the in-memory database based on the user id.

        Args:
            username (str): The unique username of the user.

        Returns:
            Tuple[dict, bool]: A tuple of the user dictionary and a boolean indicating if retrieval was successful.
        """
        users: dict = self.database_dict.get(TableNames.USERS.value)

        if not users:
            return {}, False

        for _, user in users.items():
            if user[UserKeys.USERNAME.value] == username:
                return user, True

        return {}, False