# Template Project: Django + Django Ninja

Quick implementation of two instances of Django Ninja with basic CRUD operations. 

---

## Initialization

1. Clone the repository:
    ```bash
    git clone https://github.com/Cybernetic-Ransomware/template_Django_Ninja_CRUD_API.git
    ```
2. Install Python >= 3.12.
3. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
4. Activate the virtual environment:
    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source .venv/bin/activate
      ```
5. Install dependencies using Poetry:
    ```bash
    pip install poetry
    poetry install
    ```
6. Apply migrations and run the server:
    ```bash
    cd .\iamaninja\
    poetry run python manage.py makemigrations
    poetry run python manage.py migrate
    poetry run python manage.py runserver
    ```

---

## Default Checkups

- Basic API: [http://localhost:8000/crud/api/docs](http://localhost:8000/crud/api/docs)
- CRUD API: [http://localhost:8000/crud/crudapi/docs](http://localhost:8000/crud/crudapi/docs)

---

## Useful Links and Documentation

- Django Ninja CRUD example: [https://django-ninja.dev/tutorial/other/crud/)
  - Schemas need to be updated to work with partial data, as applied in this template.
