# FastAPI-based E-Commerce CRUD API using MySQL and SQLAlchemy.

A simple Shopping API built using **FastAPI** that performs CRUD (Create, Read, Update, Delete) operations.

##  Features

- Create products
- Get all products
- Get a product by ID
- Update product details
- Delete a product
- MySQL database integration
- SQLAlchemy ORM
- Pydantic validation

## Technologies Used

- Python 3
- FastAPI
- SQLAlchemy
- Pydantic
- MySQL
- Uvicorn

## Project Structure

```
shopping-api-fastapi/
│── main.py
│── crud.py
│── database.py
│── models.py
│── schemas.py
│── README.md
```

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/Jhansi-123762/shopping-api-fastapi.git
```

2. Navigate to the project

```bash
cd shopping-api-fastapi
```

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

5. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy pymysql
```

##  Run the Project

```bash
uvicorn main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

to access the Swagger UI.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /products | Create a product |
| GET | /products | Get all products |
| GET | /products/{id} | Get product by ID |
| PUT | /products/{id} | Update product |
| DELETE | /products/{id} | Delete product |

##  Author

**Jhansi Rani Kuchika**
