# URL Shortener - FastAPI Project

This project is a simple, efficient URL shortener built with FastAPI, SQLAlchemy, and SQLite. It allows users to create short URLs, redirect to the original URLs, and delete short URLs when no longer needed.

---

## Challenge: [URL Shortener Challenge](https://codingchallenges.fyi/challenges/challenge-url-shortener)

### Objective
Create a system that takes long URLs, generates a shorter version, and manages URL redirection.

### Key Requirements
- Shorten long URLs
- Redirect users to long URLs from short links
- Delete URLs from the system

---

## Features
- **Shorten URLs**: Generate unique short links for long URLs.
- **Redirection**: Visiting the short link redirects the user to the original URL.
- **URL Deletion**: Remove short URLs from the database if no longer needed.

---

## Tech Stack
- **Backend**: FastAPI
- **Database**: SQLite with SQLAlchemy ORM
- **Validation**: Pydantic for request/response validation
- **Web Server**: Uvicorn

---

## Project Structure
```
app/
├── crud/
│   └── url.py             # Business logic for URL shortening, redirection, and deletion
├── models/
│   └── url_mapping.py     # SQLAlchemy model for URL storage
├── schemas/
│   ├── request.py         # Pydantic model for request validation
│   └── response.py        # Pydantic model for response structure
├── dependencies.py        # Database connection dependency
├── main.py                # Entry point for FastAPI app
├── database.py            # Database setup and initialization
└── README.md              # Project documentation
```

---

## Installation and Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### 1. Clone the Repository
```bash
git clone https://github.com/dagmawitensay/Codding-challenges.git
cd url_shortener
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create the database
```bash
python initialize_db.py
```

### 3. Run the Application
```bash
uvicorn app.main:app --reload
```
The application will be available at: `http://127.0.0.1:8000`

---

## API Endpoints

### 1. Shorten a URL
- **Method**: POST  
- **Endpoint**: `/shorten`  
- **Request Body**:
  ```json
  {
    "long_url": "https://www.example.com"
  }
  ```
- **Response**:
  ```json
  {
    "key": "abc123",
    "long_url": "https://www.example.com",
    "short_url": "http://127.0.0.1:8000/abc123"
  }
  ```

### 2. Redirect to Long URL
- **Method**: GET  
- **Endpoint**: `/{short_url_key}`  
- **Example**: `GET http://127.0.0.1:8000/abc123`  
- **Response**: Redirect to `https://www.example.com`

### 3. Delete a Shortened URL
- **Method**: DELETE  
- **Endpoint**: `/{short_url_key}`  
- **Example**: `DELETE http://127.0.0.1:8000/abc123`  
- **Response**: HTTP 204 No Content

---

## Database Schema

**Table**: `urls`

| Column        | Type       | Description                   |
|---------------|------------|-------------------------------|
| `key`         | `STRING`   | Unique identifier for short URL (primary key) |
| `short_url`   | `STRING`   | The shortened URL            |
| `long_url`    | `STRING`   | Original long URL            |
| `creation_date`| `TIMESTAMP`| Timestamp of URL creation    |

---

## Example Walkthrough

1. **Shorten a URL**  
Request:
```json
{
  "long_url": "https://www.example.com"
}
```
Response:
```json
{
  "key": "abc123",
  "long_url": "https://www.example.com",
  "short_url": "http://127.0.0.1:8000/abc123"
}
```

2. **Access the Shortened URL**  
Visiting `http://127.0.0.1:8000/abc123` redirects to `https://www.example.com`.

3. **Delete the URL**  
```bash
DELETE http://127.0.0.1:8000/abc123
```
Response: HTTP 204 No Content

---

## Notes
- Redirects use HTTP 302 status.
- A 404 error is returned if the short URL does not exist.
- URL keys are unique and case-sensitive.


