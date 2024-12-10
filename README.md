# To-Do List Application

This is a Django-based to-do list application designed to manage tasks and profiles. It supports features like user authentication, JWT-based authentication, filtering, and profile creation. This project is containerized using Docker for easy deployment.

## Features

- **User Profiles**: Create and manage user profiles.
- **Task Management**: Add, edit, delete, and view tasks.
- **JWT Authentication**: Secure access with JSON Web Tokens (JWT).
- **RESTful API**: Expose the application functionality through a REST API.

## Requirements

- Python 3.10 or higher (for development outside Docker)
- Docker (for containerized setup)
- PostgreSQL (via Docker or locally installed)

## Installation

Follow these steps to set up the project on your local machine, either with Docker or manually.

### Option 1: Running with Docker

To run the project using Docker, follow these steps:

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/to-do-list.git
   cd to-do-list
   ```

2. **Build and start the containers**

   Run the following command to build the Docker image and start the containers:

   ```bash
   docker-compose up --build
   ```

   This will build the application container, set up the database container, and start them both. It will also apply any migrations and start the Django server.

3. **Create a superuser (optional)**

   Once the containers are running, you can access the application in the browser. If you need to create a superuser, run the following command:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

4. **Access the application**

   You can access the Django application at `http://localhost:8000/`.

5. **Stop the containers**

   To stop the Docker containers, run:

   ```bash
   docker-compose down
   ```

### Option 2: Running Without Docker (Manual Setup)

If you prefer to run the project without Docker, follow these steps:

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/to-do-list.git
   cd to-do-list
   ```

2. **Set up a virtual environment**

   For Python 3.10 and above:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**

   Make sure you have PostgreSQL installed and running. Create a new database for the application and update the `.env` file (or directly in `settings.py`) with your database credentials.

   Then, run the following command to apply migrations:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**

   You can create a superuser to access the Django admin:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   The server will start at `http://127.0.0.1:8000/`.

### 7. Access the API

You can access the REST API at the following endpoints:

- **Login**: `/iam/login/`
- **Signup**: `/iam/signup/`
- **Profile**: `/iam/me/`
- **Tasks**: `/tasks/`

Use JWT for authentication by logging in and including the token in the Authorization header for further requests.

## Docker Setup

If you’re using Docker, here are the configurations for the containers.

### `docker-compose.yml`

This file is used to define the services for the Django app and PostgreSQL database.

```yaml
version: "3.8"

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db

  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: todo
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password

volumes:
  postgres_data:
```
