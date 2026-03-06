from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from .category import CategoryResponse


class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=200, description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., gt=0, description='Product price > 0')

    category_id: int = Field(..., description="Category id")
    image_url: Optional[str] = Field(None, description="Product image url")

class ProductCreate(ProductBase):
    pass

class ProductResponse(BaseModel):
    id: int = Field(..., description="Product id")
    name: str
    description: Optional[str] = Field(None, description="Product description")
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponse = Field(..., description="Product category details")

    class Config:
        form_attributes = True

class ProductListResponse(BaseModel):
    products: List[ProductResponse]
    total: int = Field(..., description="Total product count")


