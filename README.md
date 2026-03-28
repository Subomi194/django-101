# Task Manager

A simple Task Manager web application built with Django that allows users to create, manage, and track their tasks.
Users can register, log in, and manage their own tasks, while administrators have access to all tasks.

This project was built as part of my backend development learning.

### Features
- User registration and authentication
- Secure password hashing (handled by Django)
- Create, update, and delete tasks
- Tasks belong to individual users
- Role-based access control (RBAC)
    - Regular users can only manage their own tasks
    - Admin users can view and manage all tasks
- PostgreSQL database integration
- Basic HTML templates for task management

### Tech Stack
- Backend: Python, Django
- Database: PostgreSQL
- Frontend: HTML(basic templates)
- Authentication: Django built-in authentication system

### Installation
1. Clone the repo
```bash
git clone https://github.com/Subomi194/django-101.git
cd django-101
```

2. Create a virtual environment

3. Install dependencies
```bash
pip install django psycopg2-binary
```

4. Run the development server
```bash
python manage.py runserver
```

Built by Subomi as part of my backend development learning journey.