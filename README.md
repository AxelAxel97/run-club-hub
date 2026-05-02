# Run Club Hub

Run Club Hub is a Django web application built for a running club community. It allows users to view, create, update, and delete running event records through a web interface, while also providing additional pages for discussion and login. The project demonstrates relational database use, CRUD functionality, structured navigation, and responsive layout design.

## Project Purpose

The purpose of Run Club Hub is to give a running club a simple platform to manage upcoming events and provide a central place for club members to navigate important pages. It provides value by allowing event information to be stored in a database and updated dynamically through the application.

## Features

- Homepage with shared navigation bar
- Events page displaying event records from the database
- Full CRUD functionality for event records
- Discussion page
- Login page
- Shared `base.html` template for consistent layout
- Django admin panel for record management
- Custom CSS styling
- Bootstrap-based page structure

## CRUD Functionality

Users can:
- **Create** a new event
- **Read** and view all existing events
- **Update** existing event details
- **Delete** existing events

## Data Model

The project currently uses a Django model for event records, storing information such as:
- title
- date
- time
- location
- description

These records are stored in the project database and displayed dynamically in the frontend templates.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Backend language |
| Django 5.x | Web framework |
| PostgreSQL | Production database (Heroku) |
| SQLite | Local development database |
| Bootstrap 5 | Responsive layout, cards, badges, and utility classes |
| HTML5 / CSS3 | Templates and custom styles |
| Unicode Emoji | Visual icons throughout the UI (no library required) |
| Font Awesome 6 | Social media icons in footer |
| WhiteNoise | Static file serving in production |
| Gunicorn | Production WSGI server |
| Heroku | Cloud deployment platform |
| Git / GitHub | Version control |


## Project Structure

- `club/` - Django app containing models, views, URLs, forms, and templates
- `runclubhub/` - project settings and main URL configuration
- `templates/` - shared templates including `base.html`
- `static/css/` - custom stylesheet
- `TESTING.md` - manual testing documentation
- `README.md` - project overview and setup instructions

## Deployment

The live site is deployed on Heroku and can be accessed here:

**Live site:** https://run-club-hub-4c7ff48afff2.herokuapp.com/

### How to deploy

1. Create a Heroku account at https://heroku.com
2. Install the Heroku CLI with `brew install heroku`
3. Log in with `heroku login`
4. Create the app with `heroku create`
5. Add Postgres with `heroku addons:create heroku-postgresql:essential-0`
6. Set config vars: `SECRET_KEY`, `DEBUG`
7. Push code with `git push heroku main`
8. Run migrations with `heroku run python manage.py migrate`

### Local development

1. Clone the repository
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the server: `python3 manage.py runserver`
6. Access locally at: `http://127.0.0.1:8000/`

































