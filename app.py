import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "change_this_secret_for_prod")

app.config.update(
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com"),
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587)),
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "True") == "True",
    MAIL_USERNAME = os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD"),
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", os.getenv("MAIL_USERNAME"))
)

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name','').strip()
        email = request.form.get('email','').strip()
        company = request.form.get('company','').strip()
        message = request.form.get('message','').strip()

        if not name or not email or not message:
            flash('Please complete all required fields (Name, Email, Message).', 'danger')
            return redirect(url_for('contact'))

        subject = f"SkyForge Contact: {name}"
        body = f"""New contact form submission on SkyForge

Name: {name}
Email: {email}
Company: {company}
Message:
{message}
"""
        try:
            msg = Message(subject=subject, body=body, recipients=[os.getenv('RECEIVER_EMAIL', os.getenv('MAIL_USERNAME'))])
            mail.send(msg)
            flash('Thanks — your message was sent. We will reply soon.', 'success')
        except Exception as e:
            print('Mail error:', e)
            flash('Sorry — there was a problem sending your message. Please try again later.', 'danger')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=os.getenv('FLASK_DEBUG','False')=='True')
