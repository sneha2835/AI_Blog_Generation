# 📝 **AI Blog Generator** 🚀  
Generate AI-powered blogs with **Django, Streamlit, and LLaMA 2!**

## 🎯 **Project Overview**  
This project is an **AI-powered Blog Generator** that allows users to:  
✅ **Generate AI-written blogs** based on **Title, Word Count & Target Audience**  
✅ **Save & View generated blogs** in **MySQL database**  
✅ **User authentication** (Register/Login with **JWT authentication**)  
✅ **View saved blogs in the sidebar**  
✅ **Optimized AI model** (**LLaMA 2**) for **faster** and **efficient** blog generation  

---

## 🛠 **Tech Stack Used**  

| **Component**  | **Technology**  |
|--------------- |---------------|
| **Frontend**   |  Streamlit, Tailwind CSS (optional) |
| **Backend**    | Django, Django REST Framework (DRF) |
| **Database**   | MySQL |
| **AI Model**   | LLaMA 2 (Local execution) |
| **Authentication** | JWT (JSON Web Tokens) |
| **Deployment** | Local (VS Code) |

---

## 📥 **Installation Guide**  

### 🔹 **1️⃣ Clone the Repository**  

git clone https://github.com/sneha2835/AI_Blog_Generation.git
cd AI_Blog_Generation


---

### 🔹 **2️⃣ Set Up Virtual Environment**  

#### **For Windows**  

python -m venv venv
venv\Scripts\activate


#### **For macOS/Linux**  

python3 -m venv venv
source venv/bin/activate


---

### 🔹 **3️⃣ Install Dependencies**  

pip install -r requirements.txt


---

## 🗄️ **Database Setup (MySQL)**  

### **4️⃣ Install MySQL & Create Database**  

mysql -u root -p


CREATE DATABASE blog_db;
EXIT;


### **5️⃣ Configure MySQL in Django (`.env` file)**  
Create a **`.env`** file in the **root directory** and add:  

SECRET_KEY="your-secret-key"
DEBUG=True
MYSQL_DB_NAME="blog_db"
MYSQL_USER="root"
MYSQL_PASSWORD="root"
MYSQL_HOST="localhost"
MYSQL_PORT="3306"


---

### **6️⃣ Apply Migrations**  

python manage.py makemigrations
python manage.py migrate


---

### **7️⃣ Create Superuser (Admin)**  

python manage.py createsuperuser


---

## 🏃 **Run the Project**  

### 🔹 **8️⃣ Start the Django Backend**  

python manage.py runserver

🚀 The backend runs at **http://127.0.0.1:8000/**  

### 🔹 **9️⃣ Start the Streamlit Frontend**  

cd streamlit_app
streamlit run app.py

🚀 The frontend runs at **http://localhost:8501/**  

---

## 🔑 **User Authentication (Login/Register)**  
1️⃣ **Register using the sidebar**  
2️⃣ **Login** with username & password  
3️⃣ **Generate blogs** using AI model  
4️⃣ **Save & view generated blogs** in history  

---

## ⚡ **Optimizations for Faster Model Inference**  
✅ **Reduced `max_new_tokens`** for **faster output**  
✅ **Used `streaming`** for **real-time blog generation**  
✅ **Increased `batch_size`** to process **more tokens** at once  
✅ **Lowered `temperature`** for **more stable responses**  

---

## 🎯 **Project Features**  
✅ **User Registration & Login (JWT Auth)**  
✅ **Generate AI Blogs (LLaMA 2 Model)**  
✅ **Save Generated Blogs to MySQL**  
✅ **View Saved Blogs in Sidebar**  
✅ **Clean & Minimal UI**  

---

## 🤝 **Contributing**  
Feel free to **fork**, **improve**, and **submit pull requests**! 🚀  

---

## 📞 **Contact**  
📧 **Email:** `snehakamatam28@example.com`  
🌐 **GitHub:** [github.com/sneha2835](https://github.com/sneha2835)  

---

## 📌 **Create `.gitignore`**  
To avoid pushing unnecessary files, create a **`.gitignore`** file:  

venv/
__pycache__/
*.pyc
.env
models/llama-2-7b-chat.Q4_K_M.gguf


---

## 📌 **Final Steps to Push Code to GitHub**  

### **1️⃣ Initialize Git repository (if not already)**

git init


### **2️⃣ Add all files to Git tracking**

git add .


### **3️⃣ Commit with a meaningful message**

git commit -m "Initial commit: Added full project with AI model"


### **4️⃣ Link to your GitHub repository**

git remote add origin https://github.com/sneha2835/AI_Blog_Generation.git


### **5️⃣ Push code to GitHub**

git branch -M main
git push -u origin main


---

## **✅ Final Checklist Before Pushing to GitHub**
🔲 **All project files are present**  
🔲 **Database setup instructions are correct**  
🔲 **Git ignore file is added (`.gitignore`)**  
🔲 **Project runs successfully before pushing**  
