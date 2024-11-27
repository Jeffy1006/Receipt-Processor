# Receipt Processor API
A **FastAPI-based web service** for processing receipts and calculating points based on receipt details. The API includes endpoints to submit receipts and retrieve their associated points.
<br>
<br>
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

