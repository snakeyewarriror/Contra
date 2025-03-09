# Contra

**Contra** is a subscription platform where investors can get access to articles and reports on all topics related to investment and trading.

## Development

Contra is a Django app with a MySQL backend DB.

### Project Structure

📦 project-root/
├── 📄 .gitignore               # Ignore files for Git
├── 📄 LICENSE                  # Project license(consider using .env instead)
├── 📄 README.md                # Project documentation
├── 📄 requirements.txt         # Python dependencies
├── 📁 .vscode/                 # VS Code settings
│   ├── 📄 Contra.code-workspace   # Workspace settings
│   ├── ...
├── 📁 docs/                    # Documentation folder
│   ├── ...
├── 📄 db.sqlite3               # SQLite database (local development)
├── 🐍 manage.py                # Django management script
├── 📁 src/                     # (Optional) Source code folder
│   ├── 📁 account/             # User authentication & account management
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 admin.py
│   │   ├── 🐍 apps.py
│   │   ├── 🐍 forms.py
│   │   ├── 🐍 managers.py
│   │   ├── 🐍 models.py
│   │   ├── 🐍 tests.py
│   │   ├── 🐍 urls.py
│   │   ├── 🐍 views.py
│   │   ├── 📁 migrations/      # Django database migrations
│   │   ├── 📁 templates/       # Account-related templates
│   │   ├── 📁 __pycache__/     # Python cache
│   │   ├── ...
│   ├── 📁 client/              # Client-related functionality
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 admin.py
│   │   ├── 🐍 apps.py
│   │   ├── 🐍 forms.py
│   │   ├── 🐍 models.py
│   │   ├── 🐍 paypal.py        # PayPal-related logic
│   │   ├── 🐍 tests.py
│   │   ├── 🐍 urls.py
│   │   ├── 🐍 views.py
│   │   ├── 📁 migrations/
│   │   ├── 📁 templates/       # Client-related templates
│   │   ├── 📁 __pycache__/
│   │   ├── ...
│   ├── 📁 common/              # Shared resources (e.g., base templates, utilities)
│   │   ├── ...
│   ├── 📁 contra/              # Django project settings
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 settings.py      # Main Django settings
│   │   ├── 🐍 urls.py          # Project-level URLs
│   │   ├── 🐍 wsgi.py          # WSGI configuration
│   │   ├── 🐍 asgi.py          # ASGI configuration (if needed)
│   │   ├── ...
│   ├── 📁 static/              # Static assets (CSS, JS, images)
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   │   ├── ...
│   ├── 📁 writer/              # Writer-related functionality
│   │   ├── ...

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
