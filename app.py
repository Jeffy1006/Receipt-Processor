from fastapi import FastAPI, HTTPException, Path, Request
from typing import Dict
from uuid import uuid4
from schemas import *
from business_logics import *
from fastapi.exceptions import RequestValidationError


app = FastAPI(
    title="Receipt Processor",
    description="A simple receipt processor",
    version="1.0.0"
)


receipts_db: Dict[str, Receipt] = {}
points_db: Dict[str, int] = {}


@app.post("/receipts/process", response_model=ReceiptResponse, tags=['receipt-processor'])
def process_receipt(receipt: Receipt):
    """
    Processes a new receipt and returns its unique identifier.

    Args:
        receipt (Receipt): An object representing the receipt data.

    Returns:
        ReceiptResponse: A response object containing the generated receipt ID.

    Raises:
        HTTPException: A 400 response for invalid receipt.
    """

    if not validate_receipt(receipt):
        raise HTTPException(status_code=400, detail="The receipt is invalid")

    receipt_id = str(uuid4())
    receipts_db[receipt_id] = receipt

    # Business logic to calculate points.
    points = calculate_receipt_points(receipt)

    points_db[receipt_id] = points
    return {"id": receipt_id}


@app.get("/receipts/{id}/points", response_model=PointsResponse, tags=['receipt-processor'])
def get_points(id: str = Path(..., pattern=r"^\S+$")):
    """
    Retrieves the points associated with a specific receipt ID.

    Args:
        id (str): The unique identifier of the receipt.

    Returns:
        PointsResponse: A response object containing the calculated points.

    Raises:
        HTTPException: A 404 response for no receipt found for that id.
    """

    if id not in receipts_db:
        raise HTTPException(status_code=404, detail="No receipt found for that id")
    return {"points": points_db[id]}


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Handles validation errors based on the request path.
    Change the status code of /receipts/process from the default 422 to 400 if the receipt is invalid

    Args:
        id (str): The unique identifier of the receipt.

    Raises:
        HTTPException: A 400 response with detail added to /receipts/process.
    """

    if request.url.path == "/receipts/process":
        raise HTTPException(status_code=400, detail="The receipt is invalid")
    else:
        raise HTTPException(status_code=400)
