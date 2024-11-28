# Receipt Processor
A **FastAPI-based web service** for processing receipts and calculating points based on receipt details. The API includes endpoints to submit receipts and retrieve their associated points.

---

## Getting Started
### Prerequisites
- Python 3.9+
- Docker

### Python Installation
1. Clone the repository:
```bash
git clone https://github.com/Jeffy1006/Receipt-Processor.git
cd Receipt-Processor
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the server:
```bash
uvicorn app:app --reload
```
4. Access the API documentation at http://127.0.0.1:8000/docs

### Docker
1. Pull the docker container:
```bash
docker pull jeffy1006/receipt-processor:latest
```
2. Run the container:
```bash
docker run -d -p 8000:8000 jeffy1006/receipt-processor
```
3. Access the API documentation at http://127.0.0.1:8000/docs

---

## Endpoints

### 1. **Submit a Receipt**
- **Method**: `POST`
- **Endpoint**: `/receipts/process`
- **Request Body (Example)**:
  ```json
  {
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
      {
        "shortDescription": "Mountain Dew 12PK",
        "price": "6.49"
      },{
        "shortDescription": "Emils Cheese Pizza",
        "price": "12.25"
      },{
        "shortDescription": "Knorr Creamy Chicken",
        "price": "1.26"
      },{
        "shortDescription": "Doritos Nacho Cheese",
        "price": "3.35"
      },{
        "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
        "price": "12.00"
      }
    ],
    "total": "35.35"
  }
- **Response (Example)**:
  ```json
  {
    "id": "cb016f4b-1b74-4dbc-8ea2-91e7913d583a"
  }

### 2. **Get Points for a Receipt**
- **Method**: `GET`
- **Endpoint**: `/receipts/{id}/points`
- **Path Parameter (Example)**:
  - `id`: "cb016f4b-1b74-4dbc-8ea2-91e7913d583a"
- **Response (Example)**:
  ```json
  {
    "points": 28 
  }
---
## Example cURL Requests
### 1. **Submit a Receipt**
```bash
curl -X POST "http://127.0.0.1:8000/receipts/process" \
-H "Content-Type: application/json" \
-d '{
    "retailer": "M&M Corner Market",
    "purchaseDate": "2022-03-20",
    "purchaseTime": "14:33",
    "items": [
      {
        "shortDescription": "Gatorade",
        "price": "2.25"
      },{
        "shortDescription": "Gatorade",
        "price": "2.25"
      },{
        "shortDescription": "Gatorade",
        "price": "2.25"
      },{
        "shortDescription": "Gatorade",
        "price": "2.25"
      }
    ],
    "total": "9.00"
  }'
```
### 2. **Get Points for a Receipt**
```bash
curl -X GET "http://127.0.0.1:8000/receipts/de947efd-14c5-4ff2-af34-8f973c3bd653/points"
```
---
