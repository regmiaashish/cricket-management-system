# 🏏 Cricket Management System

A Django-based web application designed to manage and streamline cricket-related activities such as player registration, match scheduling, team management, and e-commerce section where user can purchase team based jerseys, kit, bats etc.

## 📌 Project Overview

The Cricket Management System aims to simplify and digitalize the operations of cricket tournaments, clubs, and teams. It provides a user-friendly interface to manage players, coaches, matches, teams, and statistics efficiently.

## 🚀 Features

- User Authentication & Role Management (Admin, Coach, Player)  
- Player & Coach Profile Management  
- Team Creation and Assignment  
- Match Scheduling & Management  
- Match Statistics Tracking  
- Task & Comment System  
- Admin Dashboard Panel  
- JWT-based Secure Authentication  

## 🔧 Tech Stack

- Backend: Django, Django REST Framework  
- Frontend: HTML, CSS, JavaScript (Basic Template)  
- Database: PostgreSQL  
- Authentication: JWT (djangorestframework-simplejwt)


## 🔑 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/regmiaashish/cricket-management-system.git
cd cricket-management-system

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up PostgreSQL database
# Create database in PostgreSQL:
# CREATE DATABASE cricket_management;

# In cricketmgmt/settings.py update:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cricket_management',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver


