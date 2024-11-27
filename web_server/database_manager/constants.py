from enum import Enum

class TableNames(Enum):
    PRODUCTS = "products"
    CATALOGS = "catalogs"
    USERS = "users"
    
    def __str__(self):
        return self.value

class ProductKeys(Enum):
    PRODUCT = "product"
    PRICE = "price"
    QUANTITY = "quantity"
    TYPE = "type"
    DESCRIPTION = "description"
    IMAGE = "image"
    ID = "id"
    NAME = "name"
    MODEL_NUMBER = "model_number"
    BRAND_NAME = "brand_name"
    
    def __str__(self):
        return self.value
    
class Chairs(Enum):
    DIMENSIONS = "dimensions"
    COLOR = "color"
    SIZE = "size"
    
    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

class Laptops(Enum):
    RAM = "ram"
    CPU = "cpu"
    
    def __str__(self):
        return self.value

class CatalogKeys(Enum):
    DESCRIPTION = "description"
    NAME = "name"
    OWNER = "owner"
    ID = "id"
    
    def __str__(self):
        return self.value
    
class UserKeys(Enum):
    NAME = "name"
    USERNAME = "username"
    PASSWORD = "password"
    ID = "id"
    
    def __str__(self):
        return self.value