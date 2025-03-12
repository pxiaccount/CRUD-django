# CRUD Django

CRUD (Create, Read, Update, Delete) App created with Django.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/pxiaccount/CRUD-django.git
    cd CRUD-django
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a `.env` file in the root directory of the project and add the following environment variables:
    ````plaintext
    DJANGO_SECRET_KEY=your-secret-key
    ````
    Replace `your-secret-key` with a secure, random string. You can generate a secret key using the following Python code:
    ```python
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```
5. Apply the migrations:
    ```bash
    python manage.py migrate
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```
