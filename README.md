# 🍦 Harry Ice Cream

A modern and responsive **ice cream shop web application** built with **Python and Django**. Harry Ice Cream showcases handcrafted ice creams, sorbets, and gelato flavours through a clean product catalogue with a responsive Bootstrap-based interface.

The project demonstrates Django fundamentals including **URL routing, views, templates, static files, forms, models, database integration, and CRUD operations**.

---

## 🚀 Features

* 🍨 **Artisan Ice Cream Showcase**
  Display a curated collection of handcrafted ice creams, sorbets, and gelato.

* 🎠 **Hero Section / Carousel**
  Attractive homepage carousel highlighting featured and seasonal products.

* 🛍️ **Product Catalogue**
  Responsive card-based layout for displaying ice cream flavours with images, descriptions, and pricing/details.

* 🔍 **Product Details**
  Users can view detailed information about individual menu items.

* 📝 **Menu Management**
  Django-powered functionality for adding, updating, and managing menu items.

* 📱 **Responsive Design**
  Mobile-friendly interface using **Bootstrap 5** and responsive HTML/CSS.

* 🗄️ **Database Integration**
  Product and contact information can be stored and managed using Django models.

* 📩 **Contact Form**
  Visitors can submit their name, email, and message through the website.

* 🔧 **Django Admin Panel**
  Admin users can manage products and other database records through Django's built-in administration interface.

---

## 🛠️ Tech Stack

### Backend

* 🐍 Python
* 🌐 Django

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5

### Database

* SQLite

### Development Tools

* Git
* GitHub
* VS Code / PyCharm
* Django Development Server

---

## 📂 Project Structure

```text
harry-ice-cream/
│
├── home/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── services.html
│   │   └── contact.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── harry_ice_cream/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

> The exact structure may vary depending on your Django project configuration.

---

## 🍨 Menu Highlights

| Flavour                         | Description                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------ |
| 🍫 **Belgian Dark Chocolate**   | Rich dark chocolate ice cream with roasted nuts and chocolate drizzle.         |
| 🍦 **Madagascar Vanilla Bean**  | Classic sweet cream ice cream made with whole vanilla beans and waffle crunch. |
| 🥭 **Alphonso Mango Sorbet**    | Refreshing fruit sorbet made with ripe seasonal Alphonso mangoes.              |
| 💚 **Roasted Pistachio Gelato** | Traditional gelato infused with roasted pistachios and aromatic cardamom.      |
| 🧂 **Salted Caramel Swirl**     | Creamy caramel ice cream combined with crunchy buttery toffee pieces.          |

---

## ⚙️ Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/harry-ice-cream.git
```

### 2. Navigate to the Project

```bash
cd harry-ice-cream
```

### 3. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet:

```bash
pip install django
```

---

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create a Superuser

To access the Django administration panel:

```bash
python manage.py createsuperuser
```

Enter your:

```text
Username
Email
Password
```

---

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open the website in your browser:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

---

## 🗃️ Database

This project uses **SQLite** during development.

Django models are used to store and manage application data.

Example model structure:

```python
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
```

Django migrations are used to create and update database tables.

---

## 🔄 Application Flow

```text
User
  │
  ▼
Django URL
  │
  ▼
Django View
  │
  ├──► Template
  │       │
  │       ▼
  │    HTML + CSS + Bootstrap
  │
  └──► Model
          │
          ▼
       SQLite Database
```

---

## Link


## 📚 Django Concepts Demonstrated

This project helped demonstrate practical understanding of:

* Django project and app structure
* URL routing
* Django views
* Django templates
* Template inheritance
* HTML forms
* POST requests
* Django models
* SQLite database
* Django ORM
* CRUD operations
* Django Admin
* Static files
* Bootstrap integration
* Responsive web design
* Migrations
* Virtual environments

---

## 🔮 Future Improvements

The project can be extended with:

* 🛒 Shopping cart functionality
* 👤 User registration and login
* 💳 Online payment integration
* ⭐ Product reviews and ratings
* 🔎 Product search and filtering
* 🏷️ Categories and flavour filters
* 📦 Order management
* 📧 Email notifications
* 🖼️ Image upload through Django Admin
* 🚀 Deployment using a cloud platform
* 🔐 Authentication and role-based access

---

## 🎯 Learning Objectives

The main objective of this project was to build a practical Django web application while learning how the **frontend, backend, database, and Django framework work together**.

It provides hands-on experience with building dynamic websites, handling user input, storing information in a database, and managing application data through Django Admin.

---

## 👨‍💻 Author

**Sandip Yadav**

🎓 MCA Student
💻 Aspiring Software Developer

### Connect With Me

* GitHub: `https://github.com/your-username`
* LinkedIn: `https://linkedin.com/in/sandip4career/`

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for **learning and portfolio purposes**.

© 2026 Harry Ice Cream
