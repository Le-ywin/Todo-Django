# 📝 Django Todo WebApp

A simple and productive Todo WebApp built with Django. Users can register, log in, manage tasks by category, and securely reset their passwords.

## 🚀 Features

- ✅ User Registration & Login  
- 🔐 Forgot Password (Password Reset via Email)  
- 🗂️ Task Categorization  
- 📝 Create, Read, Update, Delete (CRUD) Todos  
- 🎯 Clean and responsive UI to boost productivity  

## 🔧 Tech Stack

- Backend: Django (Python)  
- Frontend: HTML, CSS (Bootstrap)  
- Database: SQLite (default Django DB)  
- Authentication: Django's built-in auth system

## 🛠️ Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/your-username/todo-webapp.git
cd todo-webapp

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver

# 6. Visit in browser
http://127.0.0.1:8000/






📧 Forgot Password Configuration
Configure your email settings in settings.py to enable password reset via email:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'

⚠️ Use an app password for Gmail or your preferred SMTP provider. Never commit sensitive info to source control.

Just replace `your-username` and `your_email@gmail.com` as needed.
