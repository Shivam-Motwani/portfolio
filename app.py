from flask import Flask, render_template, request, flash, redirect, url_for, send_file
from flask_mail import Mail, Message
import json
import csv
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Flask-Mail configuration (optional - for contact form)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)

def load_projects():
    """Load projects from JSON file"""
    try:
        with open('data/projects.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/')
def home():
    """Home page with hero section"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page with bio and skills"""
    return render_template('about.html')

@app.route('/projects')
def projects():
    """Projects page with portfolio showcase"""
    projects_data = load_projects()
    return render_template('projects.html', projects=projects_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with form"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Save to CSV for local testing
        save_contact_to_csv(name, email, message)
        
        # Optionally send email (uncomment if configured)
        # send_contact_email(name, email, message)
        
        flash('Thank you for your message! I\'ll get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/download-resume')
def download_resume():
    """Download resume file"""
    try:
        # Look for the new resume filename first
        resume_filename = 'Shivam_Motwani_Resume.pdf'
        resume_path = os.path.join(os.path.dirname(__file__), 'static', 'files', resume_filename)
        
        # If new resume doesn't exist, fallback to old filename
        if not os.path.exists(resume_path):
            resume_filename = 'resume.pdf'
            resume_path = os.path.join(os.path.dirname(__file__), 'static', 'files', resume_filename)
        
        # Alternative path construction for production environments
        if not os.path.exists(resume_path):
            resume_path = os.path.join(app.static_folder, 'files', resume_filename)
        
        # Final check if file exists
        if not os.path.exists(resume_path):
            flash('Resume file is currently unavailable. Please contact me directly.', 'error')
            return redirect(url_for('contact'))
        
        # Send file with proper headers for download
        return send_file(
            resume_path,
            as_attachment=True,
            download_name='Shivam_Motwani_Resume.pdf',
            mimetype='application/pdf'
        )
        
    except Exception as e:
        app.logger.error(f"Resume download error: {str(e)}")
        flash('Unable to download resume at this time. Please try again later.', 'error')
        return redirect(url_for('contact'))

def save_contact_to_csv(name, email, message):
    """Save contact form data to CSV file"""
    csv_file = 'data/contacts.csv'
    file_exists = os.path.isfile(csv_file)
    
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Date', 'Name', 'Email', 'Message'])
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), name, email, message])

def send_contact_email(name, email, message):
    """Send contact form data via email (optional)"""
    try:
        msg = Message(
            subject=f'Portfolio Contact Form - {name}',
            recipients=[app.config['MAIL_USERNAME']],
            body=f'''
            New contact form submission:
            
            Name: {name}
            Email: {email}
            Message: {message}
            
            Sent from your portfolio website.
            '''
        )
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == '__main__':
    # Use debug=True for local development only
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode)
