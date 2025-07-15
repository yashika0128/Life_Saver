# ❤️ LifeSaver - Connect. Donate. Save Lives.

**LifeSaver** is a modern blood donation web platform built with **Django**, **Bootstrap 5**, and animated UI elements. It bridges the gap between **donors** and **receivers**, ensuring safe, easy, and efficient access to blood when it’s needed most.

> 💡 Designed for impact. Developed with love. Built in the AI era.

---

## 🌟 Features

- 🔥 **Stunning Landing Page** with animated backgrounds, glowing buttons & smooth scroll navigation
- 🩸 **Donor & Receiver Registration** forms with urgency levels, blood group filters & location-based suggestions
- 🎉 **Animated Submission Feedback** with confetti/hearts and interactive animal icons
- 📋 **Live Donor List** with Edit and Delete (CRUD) operations
- 🗂️ **Community Support** section with a discussion forum (coming soon)
- 📱 **Fully Responsive UI** — optimized for mobile and desktop
- 🔒 CSRF Protected Django Forms
- ✅ Realtime feedback & toast notifications using JavaScript
- 📍 Future-ready: Google Maps API integration, login system, and donor tracking

---

## 🛠️ Tech Stack

| Layer       | Tools Used                                |
|-------------|--------------------------------------------|
| Frontend    | HTML5, CSS3, Bootstrap 5, Font Awesome     |
| Animations  | Custom CSS Animations, JavaScript          |
| Backend     | Django (Python)                            |
| Database    | SQLite3                                     |
| Dev Tools   | Git, GitHub, VS Code                       |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yashika0128/LifeSaver.git
cd LifeSaver
```
### 2. Set up the virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Run the development server
```bash
python manage.py runserver
```
---

## 🧩 Folder Structure
<pre>
Life_Saver/
├── lifesaver_project/        # Django Project Settings
├── lifesaver_app/            # Core app for donors, receivers
│   ├── templates/lifesaver_app/
│   │   ├── index.html
│   │   ├── donor_form.html
│   │   ├── receiver_form.html
│   │   ├── donor_list.html
│   │   └── ...
├── static/                   # Static assets (css/js/images/screenshots)
├── db.sqlite3                # SQLite DB
├── manage.py
└── README.md
</pre>

---

## 🤝 Support & Contribution

 Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Let’s collaborate and save lives together.

---
## Every drop counts. Thank you for being a LifeSaver. ❤️
