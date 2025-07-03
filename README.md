# 🌿 PackGreen

**PackGreen** is a fully functional e-commerce website developed using **Django** that promotes eco-friendly and sustainable packaging solutions. It offers a clean, responsive interface for users to explore a variety of green packaging products while supporting a sustainability-driven mission.

---

## 🌟 Features

- 🛍️ **Product Listing**: Showcase sustainable packaging products with images, categories, and descriptions.
- 🔐 **User Authentication**: Includes user **Login**, **Signup**, and **Logout**.
- 📸 **Interactive Carousel**: Highlights key messages about eco-conscious packaging.
- 📦 **Dynamic Product Cards**: Responsive cards for displaying product details.
- 📬 **Contact Page**: A contact form to enable user communication.
- ⚠️ **Custom Alerts**: Dynamic alerts for warnings and messages.
- 🧾 **Admin Panel**: Manage products and users through Django Admin.

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Templating**: Django Template Language (DTL)
- **Database**: SQLite (default) – can be replaced with PostgreSQL/MySQL
- **Media & Static Files**: Managed with Django static/media configuration

---

## 🧩 File Structure Overview

- `templates/test1/home.html` – Homepage with product listing and carousel
- `templates/test1/navbar.html` – Reusable navigation bar
- `templates/test1/footer.html` – Footer section
- `templates/test1/products.html` – Products Page with all the products listed with their description
- `templates/test1/contact.html` – Contact Us Page with the contact details listed and a message box to leave any comlaint or feedback.
- `static/test1/` – Stores images
- `media/` – Stores uploaded product images
- `models.py` – Product model containing name, description, category, image, and ID
- `views.py` – Handles routing and context for templates

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mugdh04/PackGreen.git
cd PackGreen
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv\Scripts\activate  # On Mac: venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```
Visit your app at: http://127.0.0.1:8000/

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change or improve.

---

## 🌱 Let’s build a greener future.
