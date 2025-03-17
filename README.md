# 📝 Django BlogSite

A simple blog website.


## 🚀 Features

- List all blog posts
- View single post detail
- Create, edit, and delete posts (CRUD)
- User registration and login/logout
- Admin panel for managing content
- Authentication-based access (only logged-in users can create/edit posts)


## 🔧 Prerequisites

Before running this project, make sure you have **Python** installed.


## 📂 Project Setup

### 1. Clone the Repository
git clone 'repository_name' 
cd blogsite

### 2. Create a Virtual Environment
First, create a virtual environment to isolate project dependencies:

python -m venv venv


### 3. Activate the Environment

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

### 4. Install Dependencies from requirements.txt
Once the virtual environment is activated, install all necessary dependencies listed in requirements.txt:

pip install -r requirements.txt
Note: The requirements.txt file contains all the necessary libraries for the project. Make sure to install them before running the project.


## Running the Development Server

### 1. Apply migrations to set up the database:
python manage.py migrate

### 2. Create a superuser for the admin panel:
python manage.py createsuperuser

### 3. Start the development server:
python manage.py runserver
You can now access the site at http://127.0.0.1:8000/.
