from pydantic import BaseModel, Field
from typing import Optional, List

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity > 0")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity > 0")

class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., gt=0, description="Quantity > 0")
    subtotal: float = Field(..., description="Subtotal (price * quantity)")
    image_url: Optional[str] = Field(None, description="Image URL")

class CartResponse(BaseModel):
    items: List[CartItem] = Field(..., description="CartItems")
    total: float = Field(..., description="Total cart price")
    items_count: int = Field(..., description="Total cart count")

    
