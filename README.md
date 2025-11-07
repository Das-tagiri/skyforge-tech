# SkyForge Tech — Flask + Bootstrap 5

Professional tech-startup landing site built with Bootstrap 5 (frontend) and Flask backend for contact form.
The backend is configured to send emails via Gmail SMTP (Flask-Mail). Use a Gmail App Password (create in Google Account -> Security -> App passwords).

## Quick start (local)
1. Copy `.env.example` to `.env` and update values:
   - MAIL_USERNAME (your Gmail)
   - MAIL_PASSWORD (your Gmail app password)
   - RECEIVER_EMAIL (where messages should be delivered)

2. Create virtualenv and install:
   ```
   python -m venv venv
   venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```

3. Run:
   ```
   python app.py
   ```

4. Open http://127.0.0.1:5000

## Deploy
- Deploy backend on Render / Railway / Heroku. Use Procfile (web: gunicorn app:app) and set env vars on the platform.

## Notes
- Do not commit `.env` to GitHub.
- Replace placeholder images in `static/images/` with real assets for production.
