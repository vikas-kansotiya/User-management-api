# User Management API

A simple API for managing user data using Flask and SQLAlchemy. This API supports CRUD operations and includes pagination, searching, and sorting functionalities. The data is stored in a PostgreSQL database.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete users.
- **Pagination**: Get paginated user data.
- **Search**: Search users by first name or last name.
- **Sorting**: Sort users by specified fields.
- **Logging**: Application logs are maintained in `app.log` with a rotating file handler.

## Requirements

- Python 3.x
- PostgreSQL
- Flask
- Flask-SQLAlchemy
- psycopg2
- black (for code formatting)

## Installation

1. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    ```

2. **Activate the Virtual Environment**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

3. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Set Up PostgreSQL**

    Ensure you have PostgreSQL installed and running. Create a database named `User_management_db` and update your `config.py` with the correct database URI. 

    ```python
    class Config:
        SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:5432/User_management_db"
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    ```

2. **Update Database Configuration**

    Update the `SQLALCHEMY_DATABASE_URI` in `config.py` with your PostgreSQL credentials:

    ```python
    class Config:
        SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Vikasdatabase@localhost:5432/User_management_db"
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    ```

## Running the Application

1. **Initialize the Database**

    Run the following command to create the necessary tables in your PostgreSQL database:

    ```bash
    python app.py
    ```

2. **Run the Application**

    Start the Flask application using:

    ```bash
    python app.py
    ```

    The application will run on `http://127.0.0.1:5000/`.

## API Endpoints

- **`GET /api/users`**: Retrieve a list of users with optional pagination, search, and sorting.
    - **Query Parameters**:
        - `page`: Page number for pagination (default: 1).
        - `limit`: Number of users per page (default: 5).
        - `search`: Search term for filtering users by first or last name.
        - `sort`: Field to sort by (prefix with `-` for descending order).

    - **Response**: 
        ```json
        {
            "users": [
                {
                    "id": 1,
                    "first_name": "John",
                    "last_name": "Doe",
                    "company_name": "Company Inc.",
                    "age": 30,
                    "city": "New York",
                    "state": "NY",
                    "zip": 10001,
                    "email": "john.doe@example.com",
                    "web": "http://example.com"
                }
            ],
            "total": 10,
            "pages": 2,
            "current_page": 1
        }
        ```

- **`POST /api/user`**: Create a new user or a list of users.
    - **Request Body**: JSON object or list of user objects.
    
    - **Response**:
        ```json
        {
            "message": "Users created successfully"
        }
        ```

- **`GET /api/users/<int:id>`**: Retrieve a user by ID.
    - **Response**:
        ```json
        {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "company_name": "Company Inc.",
            "age": 30,
            "city": "New York",
            "state": "NY",
            "zip": 10001,
            "email": "john.doe@example.com",
            "web": "http://example.com"
        }
        ```

- **`PUT /api/users/<int:id>`**: Update a user by ID.
    - **Request Body**: JSON object with fields to update.
    
    - **Response**:
        ```json
        {
            "message": "User updated successfully"
        }
        ```

- **`DELETE /api/users/<int:id>`**: Delete a user by ID.
    
    - **Response**: HTTP Status 204 (No Content)

## Logging

The application uses a rotating file handler to log events to `app.log`. Logs include information about successful operations and any errors encountered.

## Code Formatting

Use `black` to format the code. To format the codebase, run:

```bash
black .
