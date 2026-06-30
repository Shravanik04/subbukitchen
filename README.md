# 🍛 Subbu Kitchen — Pure Veg South Indian Masala Powders Website

> Homemade South Indian pure vegetarian spice blends and masala powders from **Subbu Kitchen**, Rajarajeshwhari Nagar, Bangalore.

---

## 📌 About

This is a **menu showcase and order-redirect website** for Subbu Kitchen. Customers can:

- Browse our collection of fresh, homemade masala powders
- Get redirected to WhatsApp, Swiggy, or **Ownly by Rapido** to place their order
- View delivery platform options and contact details

The website does **not** process payments — it redirects customers to the appropriate ordering platform.

---

## 🍽️ Menu Items

We offer authentic, home-style spice powders prepared fresh with zero preservatives:

- **Sambar Powder**: Classic South Indian aromatic blend of coriander, cumin, dry chillies, and roasted lentils.
- **Rasam Powder**: Warm, peppery, and comforting spice mix with cumin and coriander.
- **Chilli Powder**: Pure, vibrant red chilli powder made from premium hand-picked dried red chillies.
- **Puliyogare Powder**: Tangy and spicy tamarind rice blend with hand-roasted spices and peanuts.
- **Bisibelebath Powder**: Traditional Karnataka-style comfort blend with spices, lentils, and dry coconut (copra).
- **Vangibath Powder**: Aromatic spiced rice mix infused with rich notes of cinnamon, cloves, and coriander.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Backend | Python 3 · Flask |
| Database | SQLite |
| Fonts | Google Fonts (Outfit, Playfair Display) |

---

## 📁 Project Structure

```
subbus-kitchen/
│
├── app.py                  # Flask backend (serving sk/ templates and static)
├── requirements.txt        # Python dependencies
├── Procfile                # For Render / Railway deployment
│
├── sk/                     # Main application directory
│   ├── app.py              # Flask app copy
│   ├── templates/
│   │   ├── index.html      # Homepage — menu, platforms, why us
│   │   └── success.html    # Success page
│   └── static/
│       ├── css/
│       │   └── style.css   # Custom styles & animations
│       └── images/
│           └── south_indian/
│               ├── logo.jpeg         # Logo image
│               ├── samabr.png        # Sambar Powder image
│               ├── rasam.png         # Rasam Powder image
│               ├── chilli.png        # Chilli Powder image
│               ├── puliyogare.png    # Puliyogare Powder image
│               ├── bisibelebath.png  # Bisibelebath Powder image
│               └── vangibath.png     # Vangibath Powder image
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

## 📞 Contact

**Subbu Kitchen**
- 📍 Rajarajeshwhari Nagar, Bangalore
- 📞 WhatsApp / Call: [8123987160](https://wa.me/918123987160)
- 🟠 Swiggy: Search "Subbu Kitchen RR Nagar"
- 🛵 Ownly by Rapido: Search "Subbu Kitchen" in the app

---

## 📄 License

This project is private and built exclusively for **Subbu Kitchen**.
Not licensed for redistribution or reuse.
