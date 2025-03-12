# Contra

**Contra** is a subscription platform where investors can get access to articles and reports on all topics related to investment and trading.

## Development

Contra is a Django app with a SQLite backend DB.

### Project Structure

```
project-root/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── .vscode/
│   ├── Contra.code-workspace
│   ├── ...
├── docs/
│   ├── ...
├── db.sqlite3
├── manage.py
├── src/
│   ├── account/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── managers.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── __pycache__/
│   │   ├── ...
│   ├── client/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── paypal.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── __pycache__/
│   │   ├── ...
│   ├── common/
│   │   ├── ...
│   ├── contra/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── asgi.py
│   │   ├── ...
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   │   ├── ...
│   ├── writer/
│   │   ├── ...

```
### Requirements

- Python 3.8+
- Django
- crispy-bootstrap5
- uvicorn[standard]
- ptpython
- docopt
- httpx
- python-decouple

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/contra.git
    cd contra
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    python src/manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python src/manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python src/manage.py runserver
    ```

### Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage users and content.
- Register and log in to access subscription-based content.

### Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

### License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
