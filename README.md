# User Authentication API (JWT)

## 👤 Student Details

* Name: Tirth Makwana
* Enrollment No: 2403031240050

---

## 📌 Project Description

This project implements a secure User Authentication System using JWT (JSON Web Tokens).
Users can register, log in, and access protected APIs using authentication tokens.

---

## 🚀 Features

* User Registration API
* User Login API (JWT Token)
* Token Refresh API
* Protected Route (Authentication Required)
* Secure Password Hashing

---

## 🛠️ Technologies Used

* Django
* Django REST Framework
* SimpleJWT
* SQLite

---

## 🔗 API Endpoints

| Method | Endpoint        | Description     |
| ------ | --------------- | --------------- |
| POST   | /api/register/  | Register user   |
| POST   | /api/login/     | Get JWT token   |
| POST   | /api/refresh/   | Refresh token   |
| GET    | /api/protected/ | Protected route |

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python manage.py runserver
```

---

## 🧪 Testing

Use Thunder Client / Postman:

1. Register user
2. Login → get access token
3. Use token in Authorization header
4. Access protected API

---

## 🔐 Example Header

```
Authorization: Bearer <your_access_token>
```

---

## ✅ Output

```
{
  "message": "You are authenticated!",
  "user": "username"
}
```
