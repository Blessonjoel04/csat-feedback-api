# CSAT Feedback & Analytics System

A production-style Customer Satisfaction (CSAT) feedback and analytics platform built using FastAPI, MySQL, Docker, AWS EC2, S3, Nginx, and GitHub Actions CI/CD.

This system allows public users to submit feedback (with optional screenshot upload) and provides a secure admin dashboard with real-time analytics.

---

## Live Application

Application:
https://blessoncsat.duckdns.org

Swagger Docs:
https://blessoncsat.duckdns.org/docs

---

## Features

- Public feedback submission
- Screenshot upload to AWS S3
- Client IP capture
- JWT-based admin authentication
- Protected analytics endpoints
- Rating distribution chart (Chart.js)
- Dockerized backend & database
- Nginx reverse proxy
- HTTPS via Let’s Encrypt
- CI/CD auto deployment

---

## Tech Stack

Backend:
- FastAPI
- SQLAlchemy
- MySQL
- python-jose (JWT)
- passlib (bcrypt)
- boto3 (AWS S3)
- Pydantic

Frontend:
- HTML
- JavaScript
- Chart.js

Infrastructure:
- Docker & Docker Compose
- AWS EC2 (Ubuntu)
- AWS S3
- IAM (Restricted User)
- Nginx
- Let’s Encrypt
- GitHub Actions

---

## Installation (Docker - Recommended)

Clone the repository:

```bash
git clone https://github.com/Blessonjoel04/csat-feedback-api.git
cd csat-feedback-api
```

Create a `.env` file in the project root:

```
DATABASE_URL=mysql+pymysql://csat_user:csat_password@db:3306/csat_db
JWT_SECRET=your_secret_key
ALGORITHM=HS256
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=ap-south-1
S3_BUCKET_NAME=your_bucket_name
```

Start the application:

```bash
docker compose up -d --build
```

Access Swagger locally:

```
http://localhost:8000/docs
```

---

## Running Without Docker (Development)

Install Poetry:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Install dependencies:

```bash
poetry install
```

Configure `.env` (use localhost for DB):

```
DATABASE_URL=mysql+pymysql://csat_user:csat_password@localhost:3306/csat_db
```

Run server:

```bash
poetry run uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

Public:

```
POST /api/submit-feedback
```

Admin:

```
POST /api/admin/login
```

Protected (JWT required):

```
GET /api/report/summary
GET /api/report/distribution
```

Authorization header format:

```
Authorization: Bearer <token>
```

---

## CI/CD

GitHub Actions pipeline automatically:

- Connects to EC2
- Pulls latest code
- Rebuilds Docker containers
- Restarts services

Deployment is automated on push to `main`.

---

## Security

- JWT authentication
- Password hashing (bcrypt)
- HTTPS enforced
- Port 8000 not publicly exposed
- IAM user for S3 (not root)
- Environment variables stored in `.env`

---

## Postman Collection

Includes:
- Feedback submission
- Admin login
- Protected reporting endpoints

Base URL used:

```
{{base_url}} = https://blessoncsat.duckdns.org
```

---

## Author

Blesson Joel
