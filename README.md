<pre>
````markdown
# 📦 URL Shortener (Monolith Version)

A simple, containerized URL shortener built with **FastAPI**, **PostgreSQL**, and **Redis**.

### ✨ Features

- ✅ Custom short aliases  
- ✅ Analytics tracking  
- ✅ Redis caching for fast redirects  
- ✅ Swagger UI for testing (`/docs`)  
- ✅ Fully Dockerized for local development  
⸻

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone git@github.com:your-username/url-shortener-monolith.git
cd url-shortener-monolith
```
### 2. Set up environment variables
Create a .env file in the root:
```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=url_shortener
DATABASE_URL=postgresql://postgres:postgres@db:5432/url_shortener
REDIS_HOST=redis
REDIS_PORT=6379
```
### 3. Build and run with docker compose
```bash
docker compose down --volumes --remove-orphans
docker compose up --build
```

⸻

## 🧪 API Documentation

📍 Visit: http://localhost:8000/docs — Swagger UI

⸻

## 📬 Example Usage

### ➕ Shorten a URL

POST /shorten
```json
{
  "long_url": "https://example.com",
  "custom_alias": "example",
  "expires_at": null
}
```

### 🔁 Redirect to long URL
GET /example
➡️ Redirects to https://example.com

### 📈 Get URL analytics
GET /stats/example
Returns:
```json
{
  "short_code": "example",
  "long_url": "https://example.com",
  "click_count": 3,
  "created_at": "2025-05-25T12:34:56",
  "expires_at": null
}
```
⸻

## 🧱 Tech Stack
- FastAPI – API framework
- SQLAlchemy – ORM
- PostgreSQL – Persistent database
- Redis – Cache for fast redirects
- Docker Compose – Local orchestration
- Pydantic v2 – Validation & serialization

⸻

## 💡 TODO / Improvements
- ⏳ Add link expiration logic
- 👤 User accounts & authentication
- 🧩 Break into microservices (next phase)
- ⚙️ Background task queue for analytics

⸻

👤 Author: Developed by Rebecca Heldt (Rebecca Bell)
````
</pre>
