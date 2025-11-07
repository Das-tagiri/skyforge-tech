# SkyForge Tech — Flask + Bootstrap 5

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![GitHub Repo Size](https://img.shields.io/github/repo-size/Das-tagiri/skyforge-tech)
![Last Commit](https://img.shields.io/github/last-commit/Das-tagiri/skyforge-tech)
![Issues](https://img.shields.io/github/issues/Das-tagiri/skyforge-tech)
![Forks](https://img.shields.io/github/forks/Das-tagiri/skyforge-tech)
![Stars](https://img.shields.io/github/stars/Das-tagiri/skyforge-tech)
![Contributors](https://img.shields.io/github/contributors/Das-tagiri/skyforge-tech)

![Landing Page Screenshot](https://github.com/Das-tagiri/skyforge-tech/blob/main/static/images/screenshort.png)

Professional tech-startup landing site built with **Bootstrap 5** (frontend) and **Flask** backend for the contact form.
The backend is configured to send emails via **Gmail SMTP** (Flask-Mail). Use a Gmail App Password (create in Google Account → Security → App passwords).

---

## Table of Contents

* [Features](#features)
* [Quick Start](#quick-start)
* [Deployment](#deployment)
* [Screenshot](#screenshot)
* [Live Preview](#live-preview)
* [Notes](#notes)
* [Author](#author)

---

## Features

* Fully responsive landing page using Bootstrap 5
* Flask backend for contact form
* Email notifications via Gmail SMTP
* Easy to deploy on Render / Railway / Heroku
* Simple structure for adding more pages or sections

---

## Quick Start (Local)

1. Copy `.env.example` to `.env` and update values:

```env
MAIL_USERNAME=your_gmail@example.com
MAIL_PASSWORD=your_gmail_app_password
RECEIVER_EMAIL=receiver_email@example.com
```

2. Create a virtual environment and activate:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate   # Linux / Mac
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run locally:

```bash
python app.py
```

5. Open in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Deployment

* Deploy https://skyforge-tech.onrender.com/
* Use **Procfile**: `web: gunicorn app:app`
* Set environment variables (`MAIL_USERNAME`, `MAIL_PASSWORD`, `RECEIVER_EMAIL`) on the platform

---

## Screenshot

![Landing Page Screenshot](static/images/screenshot.png)

> Replace this placeholder with your actual landing page screenshot

---

## Live Preview

[View Live Site](https://your-app-url.onrender.com)

> Replace with your actual deployed URL

---

## Notes

* **Do not commit `.env`** to GitHub
* Replace placeholder images in `static/images/` with real assets for production
* Contact form requires a proper Gmail App Password to work

---

## Author

**Kaga Dastagiri**
[GitHub](https://github.com/Das-tagiri) | [LinkedIn](https://www.linkedin.com/in/your-linkedin-profile)
