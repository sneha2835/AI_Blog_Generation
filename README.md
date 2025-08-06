# 📝 AI Blog Generator

🚀 Generate AI-powered blogs with Django, Streamlit, and LLaMA 2!

## 🎯 Project Overview

This project is an AI-powered Blog Generator that allows users to:
- ✅ Generate AI-written blogs based on Title, Word Count & Target Audience
- ✅ Save & View generated blogs in MySQL database
- ✅ User authentication (Register/Login with JWT authentication)
- ✅ View saved blogs in the sidebar
- ✅ Optimized AI model (LLaMA 2) for fast & efficient blog generation

## 🛠 Tech Stack

| Component               | Technology                          |
|-------------------------|-------------------------------------|
| Frontend                | Streamlit                           |
| Backend                 | Django, Django REST Framework (DRF) |
| Database                | MySQL                               |
| AI Model                | LLaMA 2 (Local execution)           |
| Authentication          | JWT (JSON Web Tokens)               |
| Deployment              | Local (VS Code)                     |

## 📂 Project Structure
Blog_Gen/
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── exceptions.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── utils/
│   │   │   ├── __pycache__/
│   │   │   └── model_loader.py
│   │   └── views.py
│   ├── BlogGen/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── wsgi.py
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── app.py
│   └── requirements.txt
├── models/
│   └── llama-2-7b-chat.Q4_K_M.gguf
├── venv/
├── GenBlogapi.txt
├── push_sequential.sh
└── README.md




## 📥 Installation Guide

### 🔹 1️⃣ Clone the Repository

git clone https://github.com/sneha2835/AI_Blog_Generation.git
cd AI_Blog_Generation

### 🔹 2️⃣ Set Up Virtual Environment

python -m venv venv
venv\Scripts\activate

### 🔹 3️⃣ Install Dependencies

pip install -r requirements.txt

### 🔹 4️⃣ Install MySQL & Create Database

mysql -u root -p
CREATE DATABASE blog_db;
EXIT;

### 🔹 5️⃣ Configure MySQL in Django (.env file)

Create a .env file in the root directory and add:
SECRET_KEY="your-secret-key"
DEBUG=True
MYSQL_DB_NAME="blog_db"
MYSQL_USER="root"
MYSQL_PASSWORD="root"
MYSQL_HOST="localhost"
MYSQL_PORT="3306"

### 🔹 6️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate

### 🔹 7️⃣ Create Superuser (Admin)

python manage.py createsuperuser


## 📌 Download & Add LLaMA 2 Model
The LLaMA 2 model file is NOT included in this repository due to its large size. You must manually download it and place it inside a models/ folder.

### 1️⃣ Create the models folder:

mkdir models

### 2️⃣ Download the model file:
Download LLaMA 2 (7B Chat - GGUF format) from:

🔗 Meta AI (Official)

🔗 TheBloke (Optimized GGUF)

### 3️⃣ Move the downloaded model to the models/ folder:

mv /path/to/llama-2-7b-chat.Q4_K_M.gguf models/
(Replace /path/to/ with the actual file location.)


## 🏃 Run the Project

### 🔹 8️⃣ Start the Django Backend

python manage.py runserver
The backend runs at http://127.0.0.1:8000/

### 🔹 9️⃣ Start the Streamlit Frontend

cd frontend
streamlit run app.py

The frontend runs at http://localhost:8501/


## 🔑 User Authentication (Login/Register)
1️⃣ Register using the sidebar  
2️⃣ Login with username & password  
3️⃣ Generate blogs using AI model  
4️⃣ Save & view generated blogs in history  

## ⚡ Optimizations for Faster Model Inference
✅ Reduced max_new_tokens for faster output  
✅ Used streaming for real-time blog generation  
✅ Increased batch_size to process more tokens at once  
✅ Lowered temperature for more stable responses  

## 🎯 Project Features
✅ User Registration & Login (JWT Auth)  
✅ Generate AI Blogs (LLaMA 2 Model)  
✅ Save Generated Blogs to MySQL  
✅ View Saved Blogs in Sidebar  
✅ Clean & Minimal UI  

## 🤝 Contributing
Feel free to fork, improve, and submit pull requests! 🚀

## 📞 Contact
📧 Email: snehakamatam28@example.com
🌐 GitHub: github.com/sneha2835


## 📌 .gitignore
To avoid pushing unnecessary files, create a .gitignore file:
venv/
__pycache__/
*.pyc
.env
models/llama-2-7b-chat.Q4_K_M.gguf

### ✅ Final Checklist Before Pushing to GitHub
🔲 All project files are present
🔲 Database setup instructions are correct
🔲 Git ignore file is added (.gitignore)
🔲 Project runs successfully before pushing


This README.md provides:
1. Clear project overview and features
2. Detailed installation instructions
3. Project structure visualization
4. Configuration guidance
5. Usage instructions
6. Contribution guidelines
7. Contact information
