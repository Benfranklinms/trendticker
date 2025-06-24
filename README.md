# 📉 TrendTicker

TrendTicker is a full-stack web application that allows users to track Flipkart product prices. Users can enter a product URL, set a target price, and receive email alerts when the product drops below the desired amount. Live product previews are also shown before tracking begins.

---

## 🚀 Features

- 🔍 Live product preview with current price and image
- 📬 Email notification when the product hits the target price
- ✅ Clean and responsive UI using React & Tailwind CSS
- 🔧 Backend built with Flask and BeautifulSoup for web scraping

---

## 🖥️ Tech Stack

| Frontend      | Backend         | Other Tools         |
|---------------|------------------|---------------------|
| React (Vite)  | Flask (Python)   | SMTP   |
| Axios         | BeautifulSoup    | MySQL     |
| Tailwind CSS  | Flask Blueprint  | React Toastify      |

---

## 📷 Preview

![Preview](https://via.placeholder.com/700x400?text=App+Preview+Here)

---

## 📦 Installation & Setup

### 🔧 Backend Setup (Flask)

```bash
cd server
python -m venv venv
source venv/bin/activate      # For Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
````

### 🌐 Frontend Setup (React + Vite)

```bash
cd client
npm install
npm run dev
```

> Ensure both the server and client are running on different ports (default: Flask on 5000, Vite on 5173).

---

## ✅ Usage

1. Paste a Flipkart **product URL** (not a search URL).
2. Enter your **target price** and **email**.
3. Click **"Track Now"**.
4. You'll receive a mail when price drops below your target.

---

## ⚠️ Note

* Use only valid **product page URLs** like:
  `https://www.flipkart.com/apple-iphone-15-blue-128-gb/p/itm12345...`
* Do **not** use search result URLs like:
  `https://www.flipkart.com/search?q=iphone`

---

## 🛠️ Folder Structure

```
trendticker/
│
├── client/          # React Frontend
│   └── App.jsx
│
├── server/          # Flask Backend
│   ├── app.py
│   ├── controllers/
│   ├── utils/
│   └── config/
│
├── README.md
└── requirements.txt
