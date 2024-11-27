import math
from datetime import datetime
from schemas import Receipt

def calculate_receipt_points(receipt: Receipt):
    """
    Calculates the total points earned based on a provided receipt.

    Args:
        receipt (Receipt): An object representing the receipt data.

    Returns:
        int: The total number of points earned for the receipt.
    """

    points = 0

    # One point for every alphanumeric character in the retailer name.
    points += sum(1 if c.isalnum() else 0 for c in receipt.retailer)

    total = round(float(receipt.total), 2)
    # 50 points if the total is a round dollar amount with no cents.
    points += 50 if int(total) == total else 0

    # 25 points if the total is a multiple of 0.25.
    points += 25 if round(total % 0.25, 2) == 0 else 0

    # 5 points for every two items on the receipt.
    points += 5 * (len(receipt.items) // 2)

    # If the trimmed length of the item description is a multiple of 3, 
    # multiply the price by 0.2 and round up to the nearest integer. 
    # The result is the number of points earned.
    for item in receipt.items:
        if len(item.shortDescription.strip()) % 3 == 0:
            price = round(float(item.price) * 0.2, 2)
            points += math.ceil(price)

    # 6 points if the day in the purchase date is odd.
    if int(receipt.purchaseDate.split('-')[-1]) % 2:
        points += 6

    # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    purchaseHour, purchaseMinute = receipt.purchaseTime.split(':')
    if purchaseHour == '14' and 1 <= int(purchaseMinute) <= 59:
        points += 10
    elif purchaseHour == '15':
        points += 10

    return points


def validate_total(receipt: Receipt):
    """
    Validate if the total is the sum of all items' price.

    Args:
        receipt (Receipt): An object representing the receipt data.

    Returns:
        bool: A boolean of whether the total is valid. 
    """

    total = round(float(receipt.total), 2)
    calculated_total = 0
    for item in receipt.items:
        calculated_total = round(calculated_total + float(item.price), 2)
    return calculated_total == total


def validate_date_time(receipt: Receipt):
    """
    Validate if the date and time are valid

    Args:
        receipt (Receipt): An object representing the receipt data.

    Returns:
        bool: A boolean of whether the date and time are valid. 
    """

    try:
        # Parse purchaseDate if it is in YYYY-MM-DD format.
        datetime.strptime(receipt.purchaseDate, "%Y-%m-%d")
        # Parse purchaseTime if it is in HH:MM 24-hour format.
        datetime.strptime(receipt.purchaseTime, "%H:%M")
        return True
    except ValueError:
        # Return False if any of the above parse failed.
        return False


def validate_receipt(receipt: Receipt):
    """
    Validate if the receipt is valid

    Args:
        receipt (Receipt): An object representing the receipt data.

    Returns:
        bool: A boolean of whether the receipt is valid. 
    """

    return validate_total(receipt) and validate_date_time(receipt)
    