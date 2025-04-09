# Quora Clone

A simple Quora-like website built with Django that allows users to:
- Create an account and login
- Post questions
- View questions posted by others
- Answer questions
- Like answers
- Logout

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Features
- User authentication (signup, login, logout)
- Question creation and viewing
- Answer posting
- Like functionality for answers
- Simple and functional UI 