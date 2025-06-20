Newsflow Backend
------------------
Flask Backend API for Newsflow Capstone Project — includes user authentication, token-based API security, SQLAlchemy database models, and stateful CRUD endpoints.

Project Overview
------------------
This repository contains the backend portion of the Newsflow Capstone Project. The backend was built using Flask, Flask-SQLAlchemy, and PostgreSQL. It provides user authentication, token-based API authorization, and CRUD functionality for user posts.

The backend is designed to integrate with a separate frontend React/Vite application (hosted at: https://github.com/karinaquenta/NewsFlow_Front_JSScript), but it can also function independently as a secure REST API.

Tech Stack
------------------
Language: Python 3

Framework: Flask

ORM: SQLAlchemy

Database: PostgreSQL

Migrations: Flask-Migrate (Alembic)

Authentication: Flask-Login (session-based) & custom token-based authentication for API endpoints

Forms (browser views): Flask-WTF

Project Features
------------------

Authentication

—User registration & login using hashed passwords

—Session-based authentication for browser views (Flask-Login)

—Token-based authentication for secure API endpoints (custom decorator token_required)

CRUD API Endpoints

—Create, read, and retrieve user posts via REST API

—Protected API routes that require valid user token

—JSON responses with appropriate error handling

State Management

—Secure session and token state handling

—Persistent database state managed via SQLAlchemy ORM

—Schema migrations managed with Alembic

Database Models

—User model: stores user credentials, hashed passwords, and tokens

—Post model: stores user posts linked via foreign key relationships

Environment Variables
------------------
Before running the application, create a .env file in the project root with the following structure:

FLASK_APP=app

FLASK_DEBUG=1

SECRET_KEY=your_secret_key

DATABASE_URL=your_postgres_database_url

*Note: For security reasons, actual secret keys and database URLs are excluded from this public repository.*

Contact
------------------
Developed by Karina Quenta as part of full-stack capstone project for LinkedIn REACH Backend Apprenticeship submission.
