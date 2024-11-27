from pydantic import BaseModel, Field
from typing import List


class Item(BaseModel):
    """
    Represents an item.

    Attributes:
        shortDescription (str): A short description of the item.
        price (str): The price of the item.
    """

    shortDescription: str = Field(
        ..., 
        pattern=r"^[\w\s\-]+$", 
        example="Mountain Dew 12PK"
    )
    price: str = Field(
        ..., 
        pattern=r"^\d+\.\d{2}$", 
        example="6.49"
    )


class Receipt(BaseModel):
    """
    Represents a receipt.

    Attributes:
        retailer (str): The name of the retailer.
        purchaseDate (str): The purchase date in the format YYYY-MM-DD.
        purchaseTime (str): The purchase time in the 24-hour format.
        items (List): A list of items on the receipt.
        total (str): The total of the receipt.
    """

    retailer: str = Field(
        ..., 
        pattern=r"^[\w\s\-&]+$", 
        example="M&M Corner Market"
    )
    purchaseDate: str = Field(
        ..., 
        example="2022-01-01"
    )
    purchaseTime: str = Field(
        ..., 
        example="13:01"
    )
    items: List[Item] = Field(
        ..., 
        example=[
            {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6.49"
            }
        ]
    )
    total: str = Field(
        ..., 
        pattern=r"^\d+\.\d{2}$", 
        example="6.49"
    )


class ReceiptResponse(BaseModel):
    """
    Represent a response object for the receipt.

    Attributes:
        id (str): The unique identifier of the receipt.
    """

    id: str = Field(
        ..., 
        pattern=r"^\S+$"
        )


class PointsResponse(BaseModel):
    """
    Represent a response object for the points.

    Attributes:
        points (int): The points received for a receipt.
    """
    
    points: int
