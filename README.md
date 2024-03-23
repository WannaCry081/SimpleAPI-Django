# SimpleAPI-Django

## Overview

SimpleAPI-Django is a straightforward note API implemented in the Django framework, designed to showcase REST API principles for CRUD operations, authentication, and more. It leverages various Django packages, including Djoser for authentication, djangorestframework-simplejwt, djangorestframework-xml, drf-yasg for Swagger documentation (accessible via /swagger or /redoc), and pipenv for dependency management.

## Features

- Django 3.x and Django Rest Framework
- RESTful API supporting CRUD operations
- Authentication powered by Djoser
- Token-based authentication with djangorestframework-simplejwt
- Swagger documentation available at /swagger or /redoc
- Utilizes pipenv for dependency management

## Best Practices Implemented

SimpleAPI-Django embodies best practices for creating a comprehensive REST API, including:

- Versioning to manage API changes gracefully
- Throttling mechanisms for controlling the rate of API requests
- Flexible rendering options (json, text/html, and xml)
- Pagination for handling large datasets
- Search capabilities for efficient data retrieval
- Ordering for sorting results based on specific criteria

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/WannaCry081/SimpleAPI-Django.git
   ```

2. **Create a virtual environment:**

   ```bash
   cd SimpleAPI-Django
   virtualenv venv
   ```

3. **Activate the virtual environment:**

    ```bash
    source venv/Scripts/activate
    ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

   Access the API at `http://localhost:8000/`.

## Testing

Execute unit tests with:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.