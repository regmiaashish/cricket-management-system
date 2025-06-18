
# 🏏 Cricket Management System

A Django-based web application designed to manage and streamline cricket-related activities such as player registration, match scheduling, team management, and an e-commerce section where users can purchase team jerseys, kits, bats, and more.

---

## 📌 Project Overview

The **Cricket Management System** aims to simplify the operations of cricket tournaments, clubs, and teams. It provides a user-friendly interface to manage players, coaches, teams, matches, tasks, and basic e-commerce in one place.

---

## 🚀 Features

- 🔐 User Authentication & Role Management (Admin, Coach, Player)  
- 🧑‍💼 Player & Coach Profile Management  
- 🏏 Team Creation and Assignment  
- 🗓️ Match Scheduling & Result Management  
- 📊 Match Statistics Tracking  
- 📝 Task & Comment System  
- 📋 Admin Dashboard Panel  
- 🛍️ E-commerce Section for Kits and Jerseys

---

## 🔧 Tech Stack

| Layer         | Technology             |
|---------------|-------------------------|
| Backend       | Django                  |
| Frontend      | HTML, CSS, JavaScript   |
| Database      | PostgreSQL              |
| Authentication| Django’s built-in auth  |

---

## 📷 Screenshots

> *(Add screenshots of your UI in this section)*

Example:
```
📸 dashboard.png       - Admin dashboard  
📸 schedule_form.png   - Match scheduling form  
📸 ecommerce_page.png  - Kit purchase section  
```

---

## 🔑 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/regmiaashish/cricket-management-system.git
cd cricket-management-system
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure PostgreSQL Database

1. Open PostgreSQL and create a database:
   ```sql
   CREATE DATABASE cricket_management;
   ```

2. Update the `DATABASES` section in `cricketmgmt/settings.py`:

```python
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
```

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser.

---

## 📂 Project Structure

```
cricket-management-system/
├── cricketmgmt/       # Django settings and URLs
├── accounts/          # User roles and profiles
├── teams/             # Teams and player management
├── matches/           # Match scheduling and tracking
├── store/             # E-commerce functionality
├── comments/          # Task and comment module
├── templates/         # HTML templates
└── static/            # CSS, JS, and image files
```

---

## 🤝 Contributing

Contributions are welcome and appreciated!

### Steps to Contribute

```bash
# 1. Fork the repository
# 2. Clone your fork
git clone https://github.com/your-username/cricket-management-system.git

# 3. Create a new branch
git checkout -b feature/your-feature-name

# 4. Make your changes and commit
git add .
git commit -m "Added new feature"

# 5. Push to your branch
git push origin feature/your-feature-name

# 6. Create a Pull Request on GitHub
```

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

**Author:** Aashish Regmi  
🔗 GitHub: [@regmiaashish](https://github.com/regmiaashish)

---

> Built with ❤️ using Django and PostgreSQL.
