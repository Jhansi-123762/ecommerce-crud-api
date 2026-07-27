from pydantic import BaseModel
from typing import Optional


# CATEGORY SCHEMAS
# ==========================

class CategoryBase(BaseModel):
    category_name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True



# PRODUCT SCHEMAS
# ==========================

class ProductBase(BaseModel):
    name: str
    category_id: int
    price: float
    quantity: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None
    price: Optional[float] = None
    quantity: Optional[int] = None


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True