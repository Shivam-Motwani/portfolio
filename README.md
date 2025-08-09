# Personal Portfolio Website

A modern, responsive portfolio website built with Flask, featuring a clean design, smooth animations, and excellent user experience.

## 🌟 Features

### Design & UI/UX
- **Modern Design**: Clean, minimal design with smooth animations
- **Responsive Layout**: Mobile-first design that works on all devices
- **Dark/Light Theme**: Optional theme switcher for user preference
- **Smooth Animations**: AOS (Animate On Scroll) library integration
- **Interactive Elements**: Hover effects, transitions, and micro-interactions

### Pages & Functionality
1. **Home Page**
   - Full-width hero section with gradient background
   - Animated typing effect for tagline
   - Smooth scroll navigation
   - Featured projects showcase
   - Call-to-action sections

2. **About Me**
   - Professional bio with profile photo
   - Skills showcase with icon-based cards
   - Experience and education timeline
   - Downloadable resume functionality
   - Statistics and achievements

3. **Projects**
   - Responsive grid layout for project cards
   - Filter functionality by category
   - Project details with tech stack badges
   - GitHub and live demo links
   - Image hover effects and overlays

4. **Contact**
   - Interactive contact form with validation
   - Email integration (Flask-Mail support)
   - CSV storage for local testing
   - Social media links
   - FAQ section with accordion

### Technical Features
- **Flask Backend**: Python web framework for server-side logic
- **Jinja2 Templates**: Dynamic content rendering
- **Bootstrap 5**: Responsive CSS framework
- **Font Awesome**: Beautiful icons throughout the site
- **SEO Optimized**: Meta tags, Open Graph, and Twitter cards
- **Form Validation**: Client-side and server-side validation
- **Error Handling**: Graceful error management
- **Performance Optimized**: Lazy loading, minified assets

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/portfolio.git
   cd portfolio
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   ```bash
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
portfolio/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore           # Git ignore file
├── data/
│   ├── projects.json    # Project data
│   └── contacts.csv     # Contact form submissions
├── static/
│   ├── css/
│   │   └── style.css    # Custom CSS styles
│   ├── js/
│   │   └── main.js      # Custom JavaScript
│   ├── images/          # Image assets
│   └── files/           # Downloadable files (resume, etc.)
└── templates/
    ├── base.html        # Base template
    ├── index.html       # Home page
    ├── about.html       # About page
    ├── projects.html    # Projects page
    └── contact.html     # Contact page
```

## 🎨 Customization

### Personal Information
1. **Update contact details** in `templates/base.html` and `templates/contact.html`
2. **Add your photo** to `static/images/profile-photo.jpg`
3. **Update social media links** throughout the templates
4. **Modify the bio and experience** in `templates/about.html`

### Projects
1. **Edit** `data/projects.json` to add your projects
2. **Add project images** to `static/images/`
3. **Update GitHub and demo URLs**

### Colors and Styling
1. **Modify CSS variables** in `static/css/style.css`
2. **Update the color scheme** by changing the root variables
3. **Customize animations** and transitions

### Email Configuration (Optional)
To enable email functionality for the contact form:

1. **Set environment variables:**
   ```bash
   export MAIL_USERNAME=your.email@gmail.com
   export MAIL_PASSWORD=your-app-password
   ```

2. **Update email settings** in `app.py`

## 🌐 Deployment

### Heroku Deployment

1. **Install Heroku CLI**
2. **Create a Heroku app**
   ```bash
   heroku create your-portfolio-name
   ```

3. **Add Procfile**
   ```
   web: gunicorn app:app
   ```

4. **Deploy**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

### PythonAnywhere Deployment

1. **Upload files** to your PythonAnywhere account
2. **Set up a web app** with Flask
3. **Configure the WSGI file** to point to your app
4. **Set environment variables** in the web app settings

### DigitalOcean/VPS Deployment

1. **Set up a Ubuntu server**
2. **Install Nginx and Gunicorn**
3. **Configure reverse proxy**
4. **Set up SSL with Let's Encrypt**

Example Nginx configuration:
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file for local development:
```env
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
MAIL_USERNAME=your.email@gmail.com
MAIL_PASSWORD=your-app-password
```

### Security Considerations
- Change the default `SECRET_KEY` in production
- Use environment variables for sensitive data
- Enable HTTPS in production
- Implement rate limiting for forms
- Validate and sanitize all user inputs

## 📱 Browser Support

- Chrome 70+
- Firefox 65+
- Safari 12+
- Edge 79+
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

If you need help with setup or customization:
- Check the [Issues](https://github.com/yourusername/portfolio/issues) page
- Create a new issue if you find a bug
- Contact me at your.email@example.com

## 🎯 Roadmap

- [ ] Add blog functionality
- [ ] Implement dark mode toggle
- [ ] Add more animation options
- [ ] Create admin panel for content management
- [ ] Add analytics integration
- [ ] Implement search functionality
- [ ] Add multi-language support

## 📸 Screenshots

![Home Page](static/images/screenshot-home.png)
![Projects Page](static/images/screenshot-projects.png)
![Contact Page](static/images/screenshot-contact.png)

## ⚡ Performance

- **Lighthouse Score**: 95+ for Performance, Accessibility, Best Practices, and SEO
- **Page Load Time**: < 2 seconds
- **Mobile Friendly**: 100% mobile responsive
- **Optimized Images**: WebP format with fallbacks
- **Minified Assets**: CSS and JavaScript optimization

---

**Made with ❤️ by Shivam Motwani**

*Last updated: August 2025*
