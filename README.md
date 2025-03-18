# Vendor and Shop Management System

# Project Description

This is a fully functional Django REST framework-based Vendor and Shop Management System with:
- Vendor Registration & Authentication (JWT)
- Shop Management (CRUD)
- Public API for Nearby Shop Search
- Secure Token-Based Access

# Installation & Setup Guide
1. Clone the Repository
Run the following command to clone the repository:
git clone https://github.com/YOUR_GITHUB_USERNAME/vendor-shop-management.git
cd vendor-shop-management
2. Create a Virtual Environment
For Linux/macOS:
python -m venv venv
source venv/bin/activate
For Windows:
venv\Scripts\activate
3. Install Required Dependencies
pip install -r requirements.txt
4. Apply Database Migrations
python manage.py makemigrations vendor
python manage.py migrate
5. Create a Superuser (Admin Panel)
python manage.py createsuperuser
6. Run the Development Server
python manage.py runserver

Access the API at: http://127.0.0.1:8000/api/
Admin Panel: http://127.0.0.1:8000/admin/

# API Endpoints
Method	Endpoint	Description
POST	/api/register/	Register a new vendor

POST	/api/token/	Obtain JWT token

POST	/api/token/refresh/	Refresh JWT token

GET	/api/shops/	List all vendor's shops

POST	/api/shops/	Create a new shop

GET	/api/shops/<id>/	Retrieve a specific shop

PUT	/api/shops/<id>/	Update shop details

DELETE	/api/shops/<id>/	Delete a shop

GET	/api/nearby-shops/?lat=<latitude>&lon=<longitude>&radius=<km>	Search nearby shops

# Project Structure
vendor-shop-management/
│── vendor_shop/
│   ├── settings.py
│   ├── urls.py
│── vendor/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── urls.py
│── manage.py
│── requirements.txt
│── README.md

# Upload Project to GitHub
1. Initialize Git Repository
git init
git add .
git commit -m "Initial commit - Vendor Shop Management System"
2. Create a New GitHub Repository
Go to GitHub and create a new repository named vendor-shop-management, then copy the repository URL.
3. Push Code to GitHub
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/vendor-shop-management.git
git branch -M main
git push -u origin main
Contributing
Pull requests are welcome. For major changes, open an issue first and update tests as needed.
