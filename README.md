# Osmeña Colleges

A Django-based web application for managing Osmeña Colleges, featuring:

- Department and Program Management
- Faculty Directory
- News and Events
- Student Applications
- Admin Interface

## Requirements

- Python 3.8+
- Django 5.2
- Other dependencies in requirements.txt

## Local Development

1. Clone the repository
```bash
git clone https://github.com/yesirpls/osmenacolleges.git
cd osmenacolleges
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create superuser
```bash
python manage.py createsuperuser
```

6. Run development server
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to view the site.

## Features

- Responsive design
- User authentication
- CRUD operations for departments, programs, faculty, news, and events
- Student application system
- Admin dashboard
- Media file handling

## License

MIT License

## Authors

- @yesirpls
