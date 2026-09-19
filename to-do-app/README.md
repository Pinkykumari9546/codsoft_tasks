# 📝 Django To-Do App

A simple and user-friendly **To-Do List Web Application** built using **Python and Django**.
This application allows users to manage their daily tasks by adding, updating, completing, and deleting tasks.

## 🚀 Features

* User Registration / Signup
* User Login and Logout
* Add new tasks
* View all tasks
* Update tasks
* Delete tasks
* Mark tasks as completed
* User-specific tasks
* Responsive and simple UI
* Automatic browser reload during development

## 🛠️ Technologies Used

* **Python**
* **Django**
* **HTML5**
* **CSS3**
* **SQLite**
* **django-browser-reload**

## 📂 Project Structure

```text
Todo_App_using_Django/
│
├── manage.py
├── requirements.txt
│
├── todo/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── db.sqlite3
```


## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pinkykumari9546/Todo_App_using_Django.git
```


### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 📋 How to Use

1. Create a new account using the Signup page.
2. Login with your username and password.
3. Add your daily tasks.
4. Mark tasks as completed when finished.
5. Update tasks whenever required.
6. Delete tasks that are no longer needed.
7. Logout after completing your work.

## 🔐 Authentication

The application uses Django's built-in authentication system for:

* User registration
* Login
* Logout
* User authentication
* User-specific task management

Each logged-in user can manage their own tasks.

## 🗄️ Database

This project uses **SQLite** as the default database.

The database file is:

```text
db.sqlite3
```

Django ORM is used to interact with the database.


## 🖥️ Screens / Pages

The application contains pages such as:

* Signup
* Login
* Add Task
* Update Task
* Task List



## 🔮 Future Improvements

Some features that can be added in the future:

* Task due dates
* Task priority
* Search tasks
* Filter completed/pending tasks
* Task categories
* Email notifications
* User profile
* Dark mode
* REST API using Django REST Framework

## 👩‍💻 Author

**Pinky Kumari**

### ⭐ If you like this project

Give this repository a ⭐ on GitHub and feel free to improve the project!
