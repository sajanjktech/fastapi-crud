# 🛠️ FastAPI CRUD Application

A simple FastAPI-based CRUD API using in-memory storage. It provides endpoints to create, read, update, and delete items, with validation and descriptive docstrings.

---

## 👥 Team Name

**Team\_MCA**

## 👨‍💻 Team Members

* Sajan Jwala Ray
* Deoraj Gope

---

## 🚀 Features

* **Create Item (POST)** – Add an item with a name and optional description
* **Read Item (GET)** – Retrieve a specific item by ID
* **Update Item (PUT)** – Update an existing item by ID
* **Delete Item (DELETE)** – Remove an item by ID
* **List All Items (GET)** – Retrieve all stored items
* **Validation & Error Handling**:

  * Prevents duplicate item creation using the same ID
  * Ensures item exists before performing update/delete

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
    │       └── items.py      # Routes for item-related endpoints
    ├── db/                   # Database connection/config
    │   └── db.py             # Simple database
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

| Method | Endpoint           | Description         |
| ------ | ------------------ | ------------------- |
| GET    | `/`                | Check server status |
| POST   | `/items/{item_id}` | Create a new item   |
| GET    | `/items/{item_id}` | Retrieve item by ID |
| PUT    | `/items/{item_id}` | Update item by ID   |
| DELETE | `/items/{item_id}` | Delete item by ID   |
| GET    | `/items`           | Retrieve all items  |

---

## 📌 Example Payloads

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

---

## 📄 Requirements

### Python Dependencies

```
fastapi==0.115.12
uvicorn==0.34.3
```

> Install manually (if not using Docker):
>
> ```bash
> pip install -r requirements.txt
> ```

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

* Data is stored in-memory using a dictionary (`store = {}`).
* Data will reset on every server restart.
* Tested using Postman for API interaction.

---
