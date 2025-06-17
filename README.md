# 🛠️ FastAPI CRUD Application with JWT Authentication

A secure FastAPI-based CRUD API using in-memory storage and JWT authentication. It provides endpoints to create, read, update, and delete items, along with secure login and token-based access control.

---

## 👥 Team Name

**Team_MCA**

## 👨‍💻 Team Members

* Sajan Jwala Ray
* Deoraj Gope

---

## 🚀 Features

* **JWT Authentication** with login and access token
* **Create Item (POST)** – Add an item with a name and optional description
* **Read Item (GET)** – Retrieve a specific item by ID
* **Update Item (PUT)** – Update an existing item by ID
* **Delete Item (DELETE)** – Remove an item by ID
* **List All Items (GET)** – Retrieve all stored items
* **Validation & Error Handling**:
  * Prevents duplicate item creation using the same ID
  * Ensures item exists before performing update/delete
  * JWT-protected access to all item operations

---

## 📁 Project Structure

```
fastapi-crud/
├── venv/                     # Virtual environment (optional if using Docker)
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── .gitignore                # Git ignored files
├── Dockerfile                # Docker image configuration
├── docker-compose.yml        # Docker Compose configuration
└── app/                      # Main application package
    ├── main.py               # Entry point for FastAPI
    ├── api/                  # API-related logic
    │   └── routes/           # Route handlers
    │       ├── items.py      # Routes for item-related endpoints
    │       └── auth.py       # Routes for authentication
    ├── db/                   # Database connection/config
    │   └── db.py             # Simple in-memory database
    ├── models/               # Models
    │   └── items.py          # Item model definition
```

---

## 🐳 Running with Docker (Recommended)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd fastapi-crud
```

### 2. Build and Run with Docker Compose

```bash
docker compose up --build
```

### 3. Open in Browser

* Server: [http://localhost:8000](http://localhost:8000)
* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

### 4. Stop the Containers

```bash
docker compose down
```

---

## ⚙️ Running without Docker (Manual Setup)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd fastapi-crud
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

* **Windows**:

  ```bash
  venv\Scripts\activate
  ```

* **Linux/macOS**:

  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the App

```bash
uvicorn app.main:app --reload
```

* Server: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📡 API Endpoints

| Method | Endpoint           | Description                        |
| ------ | ------------------ | ---------------------------------- |
| GET    | `/`                | Check server status                |
| POST   | `/token`           | Generate JWT access token          |
| POST   | `/items/{item_id}` | Create a new item (requires JWT)   |
| GET    | `/items/{item_id}` | Retrieve item by ID (requires JWT) |
| PUT    | `/items/{item_id}` | Update item by ID (requires JWT)   |
| DELETE | `/items/{item_id}` | Delete item by ID (requires JWT)   |
| GET    | `/items`           | Retrieve all items (requires JWT)  |

---

## 📌 Example Payloads

### Login to Get Token – `POST /token`

```bash
curl -X POST "http://127.0.0.1:8000/token" -H "Content-Type: application/x-www-form-urlencoded" -d "username=sajan&password=secret"
```

### Create Item – `POST /items/1`

```json
{
  "name": "Notebook",
  "description": "200 pages"
}
```

### Update Item – `PUT /items/1`

```json
{
  "name": "Notebook",
  "description": "300 pages"
}
```

### Use Token in Header

```http
Authorization: Bearer <your-token-here>
```

---

## 🧪 API Testing (Swagger & Postman)

### 🔍 Using Swagger UI

1. Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Click `POST /token`, input `username` and `password`, and execute
3. Copy the returned `access_token`
4. Click on the 🔐 "Authorize" button
5. Paste `Bearer <your-token>` and authorize
6. Use other `/items` endpoints as authenticated user

---

### 🧪 Using Postman

1. **Get JWT Token**
   - Method: `POST`
   - URL: `http://127.0.0.1:8000/token`
   - Body: `x-www-form-urlencoded`
     ```
     username=sajan
     password=secret
     ```

2. **Use Token in Auth Header**
   - Authorization Type: `Bearer Token`
   - Token: `<access-token>`

3. **Test Authenticated Routes**
   - Create Item: `POST /items/1`
   - Get Item: `GET /items/1`
   - Update Item: `PUT /items/1`
   - Delete Item: `DELETE /items/1`
   - List Items: `GET /items`

---

## 📄 Requirements

### Python Dependencies

```
fastapi==0.115.12
uvicorn==0.34.3
python-jose
passlib[bcrypt]
python-dotenv
```

> Install manually:
>
> ```bash
> pip install -r requirements.txt
> ```

---

### Required Tools for Docker Setup

* Docker Engine
* Docker Compose (v2+ recommended)

> To verify installation:
>
> ```bash
> docker --version
> docker compose version
> ```

---

## 📦 Notes

* User credentials are hardcoded for testing (see `auth.py`)
* Data is stored in memory using a dictionary (`store = {}`)
* JWT tokens and data reset on server restart
* Fully tested using Swagger UI and Postman

---