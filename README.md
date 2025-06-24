# SOCIAL_MEDIA_APPLICATION-BLOG-APPLICATION-USING-REACT-JS-AND-FASTAPI


# 📝 Blog & Social Media Platform using FastAPI and React

A full-stack **social blogging platform** where users can **register, authenticate using JWT, create, read, update, and delete blogs.** This project simulates a basic **social media system** with secure access and user-specific content management.

> 🔐 Powered by FastAPI + React + JWT Authentication

---

## 📖 Project Overview

This Blog Application serves as a minimal social media platform that allows:

- 🧑‍💻 **Users** to register and log in securely.
- 📝 **Authenticated users** to post, view, edit, and delete blogs.
- 📚 **All users** to view publicly available blogs.
- 🔐 **JWT Authentication** for secure access to protected endpoints.
- 🎨 **React Frontend** for a clean, dynamic, and user-friendly interface.

---

## 🚀 Core Features

### ✅ User Management
- User **Signup** and **Login**
- JWT-based authentication
- Profile viewing

### ✅ Blog Management
- Create new blogs (only after login)
- View all blogs
- View your own blogs separately
- Update and delete only your blogs

### ✅ Authentication
- Secure login via OAuth2PasswordBearer
- Passwords are hashed using Bcrypt before storing in DB
- Tokens are stored on client side (localStorage)

---

## 🛠 Tech Stack

| Layer        | Technology              |
|--------------|--------------------------|
| **Frontend** | React, Axios, React Router DOM |
| **Backend**  | FastAPI, SQLAlchemy, Pydantic |
| **Database** | SQLite (can switch to PostgreSQL) |
| **Security** | JWT, Bcrypt |
| **Deployment** | Localhost (`uvicorn` + `npm start`) |

**---requirements.txt**

fastapi
uvicorn
sqlalchemy
pydantic
passlib[bcrypt]
python-jose


**Run with specific host and port**
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

**Run the FastAPI Server (development mode)**
uvicorn main:app --reload



