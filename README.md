# 🍛 Subbu's Kitchen — Pure Veg South Indian Food Website

> Homemade South Indian pure vegetarian food ordering website for **Subbu's Kitchen**, Rajarajeshwhari Nagar, Bangalore.

---

## 📌 About

This is a **menu showcase and order-redirect website** for Subbu's Kitchen. Customers can:

- Browse the daily fresh menu
- Get redirected to WhatsApp, Swiggy, or **Ownly by Rapido** to place their order
- View delivery platform options and contact details

The website does **not** process payments — it redirects customers to the appropriate ordering platform.

---

## 🍽️ Menu Items

| Item | Price | Includes |
|------|-------|---------|
| Subbu's Chapati Box | ₹95 | 3 Chapati, 1 Palyam, 1 Curry, Curd, Pickle |
| Subbu's Normal Meals | ₹115 | 2 Chapati, Palyam, Curry, Rice, Sambar, Pickle, Curd |
| Subbu's Meals (Full Thali) | ₹135 | 2 Chapati, Palyam, Curry, Rice, Sambar, Rasam, Salad, Pickle, Curd |

> 🎁 FREE Sweet on orders of 2+ Normal Meals or Subbu's Meals

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Backend | Python 3 · Flask |
| Database | SQLite |
| Map | Leaflet.js + OpenStreetMap |
| Fonts | Google Fonts (Playfair Display, Lato) |
| Deployment | PythonAnywhere / Render / Railway |

---

## 📁 Project Structure

```
subbus-kitchen/
│
├── app.py                  # Flask backend — routes & DB logic
├── requirements.txt        # Python dependencies
├── Procfile                # For Render / Railway deployment
│
├── templates/
│   ├── index.html          # Homepage — menu, platforms, why us
│   ├── order.html          # Order form (internal use / reference)
│   └── success.html        # Order confirmation page
│
├── static/
│   ├── css/
│   │   └── style.css       # All styles & animations
│   ├── js/
│   │   ├── main.js         # Scroll reveal & nav animations
│   │   └── map.js          # Leaflet delivery map
│   └── images/
│       └── south_indian/
│           ├── logo.jpeg         # Subbu's Kitchen logo
│           ├── chapati_box.jpeg  # Chapati Box food photo
│           ├── normal_meals.jpeg # Normal Meals food photo
│           └── thali.jpeg        # Subbu's Meals food photo
│
└── database/
    └── schema.sql          # SQLite table definitions
```

---

## 🚀 Running Locally

### 1. Clone or extract the project

```bash
cd subbus-kitchen
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

### 4. Open in browser

```
http://localhost:5000
```

---

## ☁️ Deployment

### Option A — PythonAnywhere (Easiest, Recommended)

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Go to **Files** → upload the project ZIP → extract it
3. Go to **Web** → Add new web app → Manual config → Python 3.11
4. Set source directory to `/home/<yourusername>/subbus-kitchen`
5. Edit the WSGI config file — replace contents with:
   ```python
   import sys
   sys.path.insert(0, '/home/<yourusername>/subbus-kitchen')
   from app import app as application
   ```
6. Hit **Reload** — your site is live at `yourusername.pythonanywhere.com`

---

### Option B — Render (Free tier)

1. Push project to GitHub
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Deploy → live at `yourapp.onrender.com`

---

### Option C — Railway

1. Push project to GitHub
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Set start command: `gunicorn app:app`
4. Gets a live URL instantly

---

## 📦 Before Deploying — Important

Add `gunicorn` to `requirements.txt`:
```
flask==3.0.0
gunicorn
```

Add `init_db()` call before `if __name__ == '__main__':` in `app.py` so the database initialises on every server start:
```python
init_db()   # ← add this line

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
```

---

## 📞 Contact

**Subbu's Kitchen**
- 📍 Rajarajeshwhari Nagar, Bangalore
- 📞 WhatsApp / Call: [8123987160](https://wa.me/918123987160)
- 🟠 Swiggy: Search "Subbu's Kitchen RR Nagar"
- 🛵 Ownly by Rapido: Search "Subbu's Kitchen" in the app

---

## 📄 License

This project is private and built exclusively for **Subbu's Kitchen**.
Not licensed for redistribution or reuse.
