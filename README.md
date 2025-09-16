# Rental Alerts SaaS

A Python SaaS MVP that scrapes rental property listings and displays them in a simple dashboard.  

---

## **Features**

- Backend powered by **Flask**
- Scraper placeholder function to simulate rental data
- Frontend HTML page to display dashboard
- Ready for future integration: database models, CSV/JSON export, email alerts
- Clean folder structure:
```
rental-alerts-saas/
├── backend/
│
│ ├──
│ ├── models.py
│ ├── utils.py
│ └── requirements.txt
├── frontend/
│ ├── index.html
│ └── static/
├── data/
├── README.md
└── .gitignore
```
---

## **Getting Started**

### 1. Clone the repository

```bash
git clone https://github.com/GarrettOlitsky/rental-alerts-saas.git
cd rental-alerts-saas
```
### 2. Create a virtual environment (optional but recommended
python -m venv env
.\env\Scripts\activate  # Windows
source env/bin/activate # macOS/Linux
### 3. Install dependencies
pip install -r backend/requirements.txt
### 4. Run Flask backend
python backend/app.py
### 5. Open frontend

Go to http://127.0.0.1:5000/ in your browser

You should see the Rental Alerts Dashboard placeholder page
## 💡 How it Works

User signs up and sets rental preferences (location, budget).

Scraper runs (currently placeholder) to gather listings.

Listings are saved to CSV/DB for user reference.

Frontend displays listings in a simple dashboard.

Future plans include email/SMS notifications and user subscription management.

## 🛠️ Tech Stack

Backend / API: Flask

Frontend: HTML + CSS + JS (placeholder, can upgrade to React/Tailwind)

Scraping: Python (requests + BeautifulSoup, future: Playwright/Scrapy)

Database: SQLite (future: PostgreSQL)

Hosting / Deployment: Local / GitHub Pages for frontend, Heroku/Railway/Render for backend

Email Alerts: Placeholder (future: SendGrid / Mailgun)

## 📈 Future Enhancements

Connect scraper to live sites like Craigslist/Zillow

Database integration with SQLAlchemy and PostgreSQL

User authentication & subscription plans

Email/SMS alerts for new rental listings

Advanced frontend dashboard with filtering, search, and sorting

Automated daily scraping using Celery + Redis

Deploy full SaaS to cloud with CI/CD

## 🔒 License

This project is licensed under the MIT License.
